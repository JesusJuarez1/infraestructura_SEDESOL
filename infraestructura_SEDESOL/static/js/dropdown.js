document.addEventListener('DOMContentLoaded', function() {
    var userDropdown = document.getElementById('userDropdown');
    var adminButton = document.getElementById('adminButton');
    var logoutButton = document.getElementById('logoutButton');
    var arrow = document.querySelector('.arrow');
    
    if (userDropdown && adminButton && logoutButton && arrow) {
        userDropdown.addEventListener('click', function() {
            var isOpen = arrow.innerHTML === '▼'; // Verifica si la flecha hacia abajo está presente
            arrow.innerHTML = isOpen ? '▲' : '▼'; // Cambia la flecha hacia arriba o hacia abajo
        });
        userDropdown.addEventListener('click', function() {
            var adminButtonDisplay = window.getComputedStyle(adminButton).getPropertyValue('display');
            var logoutButtonDisplay = window.getComputedStyle(logoutButton).getPropertyValue('display');
            
            adminButton.style.display = adminButtonDisplay === 'none' ? 'block' : 'none';
            logoutButton.style.display = logoutButtonDisplay === 'none' ? 'block' : 'none';
        });
    }
});
