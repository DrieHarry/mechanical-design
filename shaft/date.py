import datetime

def get_date():
    months = {
        1: "Januari",
        2: "Februari",
        3: "Maret",
        4: "April",
        5: "Mei",
        6: "Juni",
        7: "Juli",
        8: "Agustus",
        9: "September",
        10: "Oktober",
        11: "November",
        12: "Desember",
    }
    date = datetime.datetime.now()
    month = months[date.month]
    return f"{date.day} {month} {date.year}"