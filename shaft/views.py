from django.shortcuts import render


from .forms import *
from .models import *
from .perhitungan import tipe1, tipe2, get_recap
from .date import get_date


import io
from django.http import FileResponse
from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.pyplot as plt
 

date = get_date()
# VIEWS FUNCTION
def input(request):
    return render(request, "shaft/input.html", {
        "form": MyForm(),
        "date": date,
    })

def output(request):
    form = MyForm(request.POST)
    if not form.is_valid():
        return render(request, "shaft/input.html", {
            "form": form,
            "date": date,
        })
    
    # Pilihan tipe 1 atau tipe 2
    RadioTipe = request.POST['RadioSelectTipe']

    if RadioTipe == "1":
        results = tipe1(request)
        recaps = get_recap(request)

        return render(request, "shaft/output.html", {
            "results": results,
            "recaps": recaps,
            "date": date,
        })

    if RadioTipe == "2":
        results = tipe2(request)
        recaps = get_recap(request)

        return render(request, "shaft/output.html", {
            "results": results,
            "recaps": recaps,
            "date": date,
        })


def about(request):
    return render(request, "shaft/about.html", {
        "date": date,
    })


def generate_shaft_image(request):
    # Ambil Input
    d1 = float(request.GET.get("D1"))
    d2 = float(request.GET.get("D2"))
    d3 = float(request.GET.get("D3"))
    d4 = float(request.GET.get("D4")) if request.GET.get("D4") else None
    AB = float(request.GET.get("AB"))
    BC = float(request.GET.get("BC"))
    CD = float(request.GET.get("CD")) if request.GET.get("CD") else None
    rectangle_length = 18 + (d2/5)

    # Create the figure and draw the shaft
    screen_width = 15  # Set your screen width in inches
    screen_height = 7  # Set your screen height in inches
    fig, ax = plt.subplots(figsize=(screen_width, screen_height))

    # Create a list of sections with their respective start points and diameters
    sections = [(0, d1), (AB, d2), (AB + BC, d3)]
    if d4:
        sections.append((AB + BC + CD, d4))

    # Draw vertical lines for each section
    for i, (x, d) in enumerate(sections):
        ax.plot([x, x], [-d/2, d/2], 'k', linewidth=1.5)

    # Draw horizontal lines connecting sections
    for i in range(len(sections) - 1):
        x, d = sections[i]
        next_x, next_d = sections[i + 1]
        ax.plot([x, next_x], [-d/2, -d/2], 'k', linewidth=1.5)
        ax.plot([x, next_x], [d/2, d/2], 'k', linewidth=1.5)

        # Connect sections with different diameters
        if d != next_d:
            ax.plot([next_x, next_x], [-d/2, -next_d/2], 'k', linewidth=1.5)
            ax.plot([next_x, next_x], [d/2, next_d/2], 'k', linewidth=1.5)

    # Draw a rectangle for the last section
    if d4:
        rect_x = sections[-1][0]
        rect_y = -d4/2
        ax.add_patch(plt.Rectangle((rect_x, rect_y), rectangle_length, d4, linewidth=1.5, edgecolor='k', facecolor='none'))
    if not d4:
        rect_x = sections[-1][0]
        rect_y = -d3/2
        ax.add_patch(plt.Rectangle((rect_x, rect_y), rectangle_length, d3, linewidth=1.5, edgecolor='k', facecolor='none'))

    # Draw the dot-dash centerline
    if d4:
        total_length = sum([AB, BC, CD]) + len(sections) + rectangle_length
        ax.plot([-4, total_length + 0.5], [0, 0], 'k-.', linewidth=0.8)
    if not d4:
        total_length = sum([AB, BC]) + len(sections) + rectangle_length
        ax.plot([-4, total_length + 0.5], [0, 0], 'k-.', linewidth=0.8)

    # Add annotations with arrows for diameters and lengths
    # Diameter annotations
    def annotate_diameter(x, d, label_offset=-12, arrow_offset=9, arrow_radius=7):
        ax.annotate(f'⌀ {d}', (x - label_offset, d / 2 + arrow_offset), fontsize=12, ha='center', va='center')
        ax.annotate('', (x, d / 2), (x + arrow_radius, d / 2 + arrow_radius), arrowprops=dict(arrowstyle='->'))

    # Annotate diameters for sections
    annotate_diameter(sections[0][0], d1)
    annotate_diameter(sections[1][0], d2)
    if d4:
        annotate_diameter(sections[2][0], d3)
        annotate_diameter(sections[3][0] + rectangle_length, d4)
    if not d4:
        annotate_diameter(sections[2][0] + rectangle_length, d3)

    # Length
    # AB
    ax.annotate('', (0, -d2/2 - 20), (AB, -d2/2 - 20), arrowprops=dict(arrowstyle='<->'))
    ax.annotate(f'{AB}', (AB/2, -d2/2 - 23), fontsize=12, ha='center', va='center')
    ax.plot([0, 0], [-d1/2 - 5, -d2/2 - 20], 'k:', linewidth=0.6)

    # BC
    ax.annotate('', (AB, -d2/2 - 20), (AB + BC, -d2/2 - 20), arrowprops=dict(arrowstyle='<->'))
    ax.annotate(f'{BC}', (AB + BC/2, -d2/2 - 23), fontsize=12, ha='center', va='center')
    ax.plot([AB, AB], [-d2/2 - 5, -d2/2 - 20], 'k:', linewidth=0.6)
    ax.plot([AB + BC, AB + BC], [-d2/2 - 5, -d2/2 - 20], 'k:', linewidth=0.6)

    # CD
    if d4:
        ax.annotate('', (AB + BC, -d2/2 - 20), (AB + BC + CD, -d2/2 - 20), arrowprops=dict(arrowstyle='<->'))
        ax.annotate(f'{CD}', (AB + BC + CD/2, -d2/2 - 23), fontsize=12, ha='center', va='center')
        ax.plot([AB + BC + CD, AB + BC + CD], [-d3/2 - 5, -d2/2 - 20], 'k:', linewidth=0.6)


    # Set the aspect ratio, limits, and remove ticks and labels
    ax.set_aspect('equal')
    ax.set_xlim([-4, total_length + 10])
    if d4:
        ax.set_ylim([-max(d1, d2, d3, d4) / 2 - 24, max(d1, d2, d3, d4) / 2 + 11])
    if not d4:
        ax.set_ylim([-max(d1, d2, d3) / 2 - 24, max(d1, d2, d3) / 2 + 11])
    ax.set_xticks([])
    ax.set_yticks([])
    ax.axis('off')

    # Save the figure to a temporary buffer and return it as a file response
    buf = io.BytesIO()
    canvas = FigureCanvasAgg(fig)
    canvas.print_png(buf)
    buf.seek(0)
    response = FileResponse(buf, content_type='image/png')
    response['Content-Disposition'] = 'inline; filename="shaft.png"'
    return response