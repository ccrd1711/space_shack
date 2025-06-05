document.addEventListener("DOMContentLoaded", function () {
    const reviews = document.querySelectorAll(".review-item");
    let currentIndex = 0;
    const visibleCount = 1;
    const intervalTime = 10000;

    function showCurrentReview() {
        reviews.forEach((review) => {
            review.classList.remove("active");
        });

        for (let i = 0; i < visibleCount; i++) {
            const indexToShow = (currentIndex + i) % reviews.length;
            reviews[indexToShow].classList.add("active");
        }

        currentIndex = (currentIndex + visibleCount) % reviews.length;
    }

    if (reviews.length > 0) {
        showCurrentReview();
        setInterval(showCurrentReview, intervalTime);
    }
});
