document.addEventListener('DOMContentLoaded', function() {
    const mobileMenuButton = document.querySelector('.mobile-menu-button');
    const mainNav = document.querySelector('.main-nav');
    
    mobileMenuButton.addEventListener('click', function() {
        mainNav.classList.toggle('active');
        
        // Animate the hamburger icon
        this.classList.toggle('open');
    });
});