const toggleSidebarBtn = document.getElementById('toggle-sidebar-btn');
const sidebar = document.getElementById('sidebar');
const main = document.getElementById('main');

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