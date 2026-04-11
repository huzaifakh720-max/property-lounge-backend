// =============================
// PROPERTY LOUNGE SCRIPT
// =============================


// Wait for page load
document.addEventListener("DOMContentLoaded", function () {

    // =============================
    // PROPERTY CARD ANIMATION
    // =============================

    let cards = document.querySelectorAll(".property-card");

    cards.forEach((card, i) => {
        setTimeout(() => {
            card.classList.add("show");
        }, i * 200);
    });


    // =============================
    // SCROLL ANIMATION
    // =============================

    const sections = document.querySelectorAll(
        ".featured, .video-tour, .why-us, .cta"
    );

    window.addEventListener("scroll", () => {

        sections.forEach(section => {

            const position = section.getBoundingClientRect().top;
            const screenHeight = window.innerHeight;

            if (position < screenHeight - 100) {
                section.classList.add("show");
            }

        });

    });



    // =============================
    // MOBILE MENU
    // =============================

    const menuBtn = document.querySelector(".menu-toggle");
    const nav = document.querySelector("nav");

    if (menuBtn) {

        menuBtn.addEventListener("click", () => {
            nav.classList.toggle("active");
        });

    }



    // =============================
    // IMAGE ZOOM EFFECT
    // =============================

    const images = document.querySelectorAll(".property-card img");

    images.forEach(img => {

        img.addEventListener("mouseenter", () => {
            img.style.transform = "scale(1.05)";
        });

        img.addEventListener("mouseleave", () => {
            img.style.transform = "scale(1)";
        });

    });



    // =============================
    // SMOOTH BUTTON HOVER
    // =============================

    const buttons = document.querySelectorAll(".view-btn, .cta-btn");

    buttons.forEach(btn => {

        btn.addEventListener("mouseenter", () => {
            btn.style.transform = "scale(1.05)";
        });

        btn.addEventListener("mouseleave", () => {
            btn.style.transform = "scale(1)";
        });

    });



    // =============================
    // HERO TEXT FADE
    // =============================

    const heroTitle = document.querySelector(".hero h1");
    const heroText = document.querySelector(".hero p");

    if (heroTitle) {
        heroTitle.style.opacity = "0";
        heroTitle.style.transform = "translateY(-30px)";

        setTimeout(() => {
            heroTitle.style.transition = "1s";
            heroTitle.style.opacity = "1";
            heroTitle.style.transform = "translateY(0)";
        }, 300);
    }

    if (heroText) {
        heroText.style.opacity = "0";

        setTimeout(() => {
            heroText.style.transition = "1.5s";
            heroText.style.opacity = "1";
        }, 700);
    }


});