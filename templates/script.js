document.getElementById("appointmentForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent default form submission

    // Get form data
    const formData = new FormData(event.target);
    const day = formData.get("day");
    const slot = formData.get("slot");

    // Simulate AJAX request to Flask backend
    fetch('/book_slot', {
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(data => {
        // Update message div with response from Flask
        const messageDiv = document.getElementById("message");
        messageDiv.textContent = data;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
