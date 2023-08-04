document.addEventListener('DOMContentLoaded', () => {
    const sidebar = document.getElementById('sidebar');
    const barContent = document.querySelector('.bar-content');
    const icon = document.getElementById('sidebar-icon');

    // Add click event listener to the icon
    icon.addEventListener('click', () => {
        // Toggle the 'expanded' class on the sidebar
        sidebar.classList.toggle('expanded');

        // Toggle the 'visible' class on the bar-content
        barContent.classList.toggle('visible');

        // Toggle the 'shift' class on the bar-content
        icon.classList.toggle('shift');
    });
});