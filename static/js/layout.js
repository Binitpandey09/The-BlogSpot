// Wait for the document to be fully loaded
document.addEventListener("DOMContentLoaded", function() {
    
    // Find the toggle button and the main layout container
    const toggleButton = document.getElementById('sidebar-toggle-btn');
    const mainLayout = document.getElementById('main-layout');

    // Add a click event listener to the button
    if (toggleButton && mainLayout) {
        toggleButton.addEventListener('click', () => {
            // Toggle the 'sidebar-collapsed' class on the main layout
            mainLayout.classList.toggle('sidebar-collapsed');
        });
    }
});