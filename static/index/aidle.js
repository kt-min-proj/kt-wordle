window.onload = function () {
  document.querySelector(".aidl_login")
      .addEventListener("click", function () {
        document.querySelector(".aidl_login").style.display = "none"
      })
}


function exampleopen() {
  if (document.querySelector(".example").style.display == "flex") {
    document.querySelector(".example").style.display = "none"
  }
  else {
    document.querySelector(".example").style.display = "flex"
  }
}