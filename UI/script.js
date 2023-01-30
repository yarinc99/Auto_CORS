// Onclick of the button

    function myFunction() {
        // Get the checkbox
        var checkBox = document.getElementById("Site");
        // Get the output text
        var text = document.getElementById("texta");
      
        // If the checkbox is checked, display the output text
        if (checkBox.checked == true){
          text.style.display = "block";
        } else {
          text.style.display = "none";
        }
      }
      document.getElementById("start").onclick = function () {
    function getFormData() {
        var formData = {};
        formData["request"] = document.getElementById("request-input").value;
        formData["site"] = document.getElementById("texta").value;
        formData["csrf"] = document.getElementById("csrf").checked;
        formData["auth"] = !document.getElementById("Auth").checked;
        formData["server"] = document.getElementById("server").checked;
        return formData;
    }
    
    document.querySelector("form").addEventListener("submit", function(e) {
        e.preventDefault();
        var formData = getFormData();
        eel.start_script(formData)();
    });
    eel.expose(update_request_output);
    function update_request_output(request) {
    document.getElementById("request-output").style.display = "none";
    document.getElementById("requesttext").innerHTML = request;
    document.getElementById("after").style.display = "block";
}
document.getElementById("copy-button").addEventListener("click", function() {
  var text = document.getElementById("requesttext").innerHTML;
  navigator.clipboard.writeText(text).then(()=>{
      this.innerHTML = "Copied!"
  })
});
document.getElementById("reset").onclick = function () {
        document.getElementById("request-input").value = "";
        document.getElementById("texta").value = "";
        document.getElementById("Site").checked = false;
        document.getElementById("server").checked = false;
        document.getElementById("csrf").checked = false;
        document.getElementById("Auth").checked = false;
        document.getElementById("request-output").style.display = "block";
        document.getElementById("requesttext").innerHTML = "";
        document.getElementById("after").style.display = "none";
        document.getElementById("error").style.display = "none";

}
}
eel.expose(error);
function error(massage) {
document.getElementById("error").style.display = "block";
document.getElementById("error").innerHTML = massage;
}