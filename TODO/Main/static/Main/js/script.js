document.addEventListener("DOMContentLoaded", () => {

    const cards = document.querySelectorAll(".card");

    cards.forEach((card, index) => {
        card.style.opacity = "0";
        card.style.transform = "translateY(15px)";

        setTimeout(() => {
            card.style.transition = "all 0.4s ease";
            card.style.opacity = "1";
            card.style.transform = "translateY(0)";
        }, index * 80);
    });

});
document.addEventListener("DOMContentLoaded", () => {

    const dropdowns = document.querySelectorAll(".dropdown");

    dropdowns.forEach(drop => {
        const btn = drop.querySelector(".dropdown-toggle");

        btn.addEventListener("click", (e) => {
            e.stopPropagation();

            // закрыть другие
            document.querySelectorAll(".dropdown").forEach(d => {
                if (d !== drop) d.classList.remove("active");
            });

            drop.classList.toggle("active");
        });
    });

    // клик вне — закрыть
    document.addEventListener("click", () => {
        document.querySelectorAll(".dropdown").forEach(d => {
            d.classList.remove("active");
        });
    });

});