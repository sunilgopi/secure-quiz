document.addEventListener("DOMContentLoaded", function() {
    // add event listener for login form submission
    var loginForm = document.getElementById("login-form");
    loginForm.addEventListener("submit", function(event) {
        event.preventDefault();
        var username = document.getElementById("username").value;
        var password = document.getElementById("password").value;
        if (!username || !password) {
            // display error message
            var errorMessage = document.getElementById("error-message");
            errorMessage.innerHTML = "Please enter a username and password";
        } else {
            // send login request to server
            var xhr = new XMLHttpRequest();
            xhr.open("POST", "/login");
            xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
            xhr.onload = function() {
                if (xhr.status === 200) {
                    // redirect to dashboard page
                    window.location.replace("/dashboard");
                } else {
                    // display error message
                    var errorMessage = document.getElementById("error-message");
                    errorMessage.innerHTML = "Invalid username or password";
                }
            };
            xhr.send("username=" + username + "&password=" + password);
        }
    });
});
