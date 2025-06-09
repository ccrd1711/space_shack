document.addEventListener("DOMContentLoaded", function () {
    const burger = document.getElementById("burger");
    const navList = document.querySelector("header nav ul");

    burger.addEventListener("click", function () {
        navList.classList.toggle("active");
    });
});
