const toggleSidebarBtn = document.getElementById('toggle-sidebar-btn');
const sidebar = document.getElementById('sidebar');
const main = document.getElementById('body');

toggleSidebarBtn.addEventListener('click', function() {
  sidebar.classList.toggle('active');
  if (window.innerWidth > 1199) {
    if (sidebar.classList.contains('active')) {
        main.style.marginLeft = '280px';
      } else {
        main.style.marginLeft = '0px';
      }
  }
  
});

// get the radio button group element
var radios = document.getElementsByName('RadioSelectTipe');
var tipe1 = document.querySelectorAll('.tipe1');
var tipe2 = document.querySelectorAll('.tipe2');

for (var i = 0; i < radios.length; i++) {
    radios[i].onchange = function () {
        if (this.value == '1') {
            for (var j = 0; j < tipe1.length; j++) {
                tipe1[j].style.display = "block";
            }
            for (var k = 0; k < tipe2.length; k++) {
                tipe2[k].style.display = "none";
            }
        } else if (this.value == '2') {
            for (var j = 0; j < tipe1.length; j++) {
                tipe1[j].style.display = "none";
            }
            for (var k = 0; k < tipe2.length; k++) {
                tipe2[k].style.display = "block";
            }
        }
    }
}

var radios2 = document.getElementsByName('RadioSelectDayaTorsi');
var daya = document.querySelectorAll('.daya');
var torsi = document.querySelectorAll('.torsi');

for(var i = 0; i < radios.length; i++) {
    radios2[i].onchange = function() {
        if (this.value == 'D') {
            for (var j = 0; j < daya.length; j++) {
                daya[j].style.display = "block";
            }
            for (var k = 0; k < torsi.length; k++) {
                torsi[k].style.display = "none";
            }
        } else if (this.value == 'T') {
            for (var j = 0; j < daya.length; j++) {
                daya[j].style.display = "none";
            }
            for (var k = 0; k < torsi.length; k++) {
                torsi[k].style.display = "block";
            }
        }
    }
}