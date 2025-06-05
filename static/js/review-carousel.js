document.addEventListener("DOMContentLoaded", function () {
    const reviews = document.querySelectorAll(".review-item");
    let currentIndex = 0;

    function showCurrentReview() {
        reviews.forEach((review, i) => {
            review.classList.remove("active");
        });

        reviews[currentIndex].classList.add("active");

        currentIndex = (currentIndex + 1) % reviews.length;
    }

    if (reviews.length > 0) {
        showCurrentReview(); // show first one immediately
        setInterval(showCurrentReview, 4000);
    }
});
