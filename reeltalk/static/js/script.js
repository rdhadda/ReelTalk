document.addEventListener('DOMContentLoaded', function() {
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);

    
    let tooltip = document.querySelectorAll('.tooltipped');
    M.Tooltip.init(tooltip);
    
  });