document.addEventListener('DOMContentLoaded', function () {
    // Animasi Menu Sidebar Script
    const toggleSidebarBtn = document.getElementById('toggle-sidebar-btn');
    const sidebar = document.getElementById('sidebar');
    const body = document.getElementById('body');
  
    toggleSidebarBtn.addEventListener('click', function () {
      sidebar.classList.toggle('active');
      if (window.innerWidth > 1080) {
        if (sidebar.classList.contains('active')) {
          body.style.marginLeft = '280px';
        } else {
          body.style.marginLeft = '0px';
        }
      }
    });
  
    // Highlight menu aktif Script
    const navLinks = document.querySelectorAll('.sidebar-nav .nav-link');
    navLinks.forEach((navLink) => {
      navLink.addEventListener('click', () => {
        navLinks.forEach((link) => link.classList.remove('active'));
        navLink.classList.add('active');
      });
    });
  
    // Pilihan Radio Script
    let radios = document.getElementsByName('RadioSelectTipe');
    let tipe1 = document.querySelectorAll('.tipe1');
    let tipe2 = document.querySelectorAll('.tipe2');
    let notipe = document.querySelectorAll('.notipe');
    let radios2 = document.getElementsByName('RadioSelectDayaTorsi');
    let daya = document.querySelectorAll('.daya');
    let torsi = document.querySelectorAll('.torsi');
    // Fungsi Tipe untuk menampilkan dan menyembunyikan konten
    function updateContent() {
        for (let i = 0; i < radios.length; i++) {
            if (radios[i].checked) {
                if (radios[i].value == '1') {
                    for (let j = 0; j < tipe1.length; j++) {
                        tipe1[j].style.display = "block";
                    }
                    for (let k = 0; k < tipe2.length; k++) {
                        tipe2[k].style.display = "none";
                    }
                    for (let l = 0; l < notipe.length; l++) {
                        notipe[l].style.display = "block";
                    }
                } else if (radios[i].value == '2') {
                    for (let j = 0; j < tipe1.length; j++) {
                        tipe1[j].style.display = "none";
                    }
                    for (let k = 0; k < tipe2.length; k++) {
                        tipe2[k].style.display = "block";
                    }
                    for (let l = 0; l < notipe.length; l++) {
                        notipe[l].style.display = "block";
                    }
                }
            }
        }
    }
    // Fungsi Daya Torsi untuk menampilkan dan menyembunyikan konten
    function updateContent2() {
        for (let i = 0; i < radios2.length; i++) {
            if (radios2[i].checked) {
                if (radios2[i].value == 'D') {
                    for (let j = 0; j < daya.length; j++) {
                        daya[j].style.display = "block";
                    }
                    for (let k = 0; k < torsi.length; k++) {
                        torsi[k].style.display = "none";
                    }
                } else if (radios2[i].value == 'T') {
                    for (let j = 0; j < daya.length; j++) {
                        daya[j].style.display = "none";
                    }
                    for (let k = 0; k < torsi.length; k++) {
                        torsi[k].style.display = "block";
                    }
                }
            }
        }
    }

    for (let j = 0; j < tipe1.length; j++) {
        tipe1[j].style.display = "none";
    }
    for (let k = 0; k < tipe2.length; k++) {
        tipe2[k].style.display = "none";
    }
    for (let l = 0; l < notipe.length; l++) {
        notipe[l].style.display = "none";
    }
    for (let j = 0; j < torsi.length; j++) {
        torsi[j].style.display = "none";
    }
    for (let k = 0; k < daya.length; k++) {
        daya[k].style.display = "none";
    }

    for (let i = 0; i < radios.length; i++) {
        radios[i].onchange = updateContent;
    }
    for (let i = 0; i < radios2.length; i++) {
        radios2[i].onchange = updateContent2;
    }

    // Panggil Fungsi saat halaman di load
    window.onload = function() {
        updateContent();
        updateContent2();
    };
    


    // Script Lainnya disini
  });