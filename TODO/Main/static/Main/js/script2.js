document.addEventListener("DOMContentLoaded", () => {

    const inputs = document.querySelectorAll(
        ".create-form input, .create-form textarea, .create-form select"
    );

    inputs.forEach(input => {
        input.addEventListener("focus", () => {
            input.style.transform = "scale(1.02)";
        });

        input.addEventListener("blur", () => {
            input.style.transform = "scale(1)";
        });
    });

});