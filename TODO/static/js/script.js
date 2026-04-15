// Плавное появление элементов
document.addEventListener("DOMContentLoaded", () => {
    const elements = document.querySelectorAll(".card");

    elements.forEach((el, index) => {
        el.style.animationDelay = `${index * 0.1}s`;
        el.classList.add("fade-in");
    });
});


// Кнопка эффект "нажатия"
document.addEventListener("click", (e) => {
    if (e.target.classList.contains("btn")) {
        e.target.style.transform = "scale(0.95)";

        setTimeout(() => {
            e.target.style.transform = "scale(1)";
        }, 100);
    }
});