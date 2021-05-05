var path = window.location.pathname;
var page = path.split("/").pop().slice(0, -5);
document.getElementById(page).style.color = "rgb(5, 56, 107)";

$(document).ready(function () {
    $(".menu").click(function () {
        this.classList.toggle("change");
        $(".header-main").slideToggle("slow");
    });
});

function slideup() {
    if (screen.width < 800)
        $(".header-main").slideUp();
}