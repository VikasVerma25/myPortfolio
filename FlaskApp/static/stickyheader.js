var path = window.location.pathname;
var page = path.split("/").pop().slice(0,-5);
document.getElementById(page).style.borderBottom = "0.2vw solid rgb(7, 80, 153)";

window.onscroll = function() {myFunction()};
    
    var header = document.getElementById("myHeader");
    var sticky = header.offsetTop;
    
    function myFunction() {
      if (window.pageYOffset > sticky) {
        header.classList.add("sticky");
      } else {
        header.classList.remove("sticky");
      }
}