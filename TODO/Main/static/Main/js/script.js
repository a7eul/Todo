document.addEventListener("DOMContentLoaded", () => {

    // Анимация появления карточек
    const cards = document.querySelectorAll(".card");

    cards.forEach((card, index) => {
        card.style.opacity = "0";
        card.style.transform = "translateY(10px)";

        setTimeout(() => {
            card.style.transition = "0.4s";
            card.style.opacity = "1";
            card.style.transform = "translateY(0)";
        }, index * 100);
    });

    // Hover glow для задач
    const tasks = document.querySelectorAll(".task-card");

    tasks.forEach(task => {
        task.addEventListener("mouseenter", () => {
            task.style.boxShadow = "0 0 20px rgba(0,150,255,0.3)";
        });

        task.addEventListener("mouseleave", () => {
            task.style.boxShadow = "";
        });
    });

});