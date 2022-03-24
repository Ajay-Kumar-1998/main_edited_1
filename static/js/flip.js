// ==================================  card flip  ==========================

function change() {
  document
    .getElementsByClassName("front")[0]
    .classList.toggle("animationfront");
  document.getElementsByClassName("back")[0].classList.toggle("animationback");
}
