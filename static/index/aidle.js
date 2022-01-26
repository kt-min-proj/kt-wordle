function exampleopen() {
  if (document.querySelector(".example").style.display == "flex") {
    document.querySelector(".example").style.display = "none"
  }
  else {
    document.querySelector(".example").style.display = "flex"
  }
}