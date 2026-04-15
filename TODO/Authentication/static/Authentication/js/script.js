document.addEventListener("DOMContentLoaded", () => {
    const title = document.querySelector(".auth-title");
    const card = document.querySelector(".auth-card");

    // Эффект "живого" градиента
    let angle = 0;

    setInterval(() => {
        angle += 1;
        card.style.boxShadow = `0 0 40px rgba(0, ${150 + Math.sin(angle/10)*50}, 255, 0.2)`;
    }, 50);


    // Анимация фокуса на инпутах
    const inputs = document.querySelectorAll("input");

    inputs.forEach(input => {
        input.addEventListener("focus", () => {
            input.style.transform = "scale(1.02)";
        });

        input.addEventListener("blur", () => {
            input.style.transform = "scale(1)";
        });
    });
});