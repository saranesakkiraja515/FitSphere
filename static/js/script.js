    document.addEventListener('DOMContentLoaded', function () {
        // Add hover effect for zooming in on images
        const images = document.querySelectorAll('.card-cover, .img-fluid');

        images.forEach((image) => {
            image.addEventListener('mouseover', function () {
                image.style.transform = 'scale(1.1)'; // Zoom in
                image.style.transition = 'transform 0.3s ease'; // Smooth transition
                image.style.cursor = 'pointer'; // Hand cursor on hover
            });

            image.addEventListener('mouseout', function () {
                image.style.transform = 'scale(1)'; // Reset zoom
                image.style.cursor = 'default'; // Default cursor
            });
        });
    });

