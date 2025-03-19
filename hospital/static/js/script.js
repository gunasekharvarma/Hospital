async function staffLogin(username, password) {
    try {
        const response = await fetch("http://127.0.0.1:8000/accounts/login/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ username, password })
        });

        const data = await response.json();

        if (response.ok) {
            console.log("Login successful:", data);
            localStorage.setItem("staffToken", data.token);
            document.getElementById("loginMessage").innerText = "Login successful!";

        } else {
            console.error("Login failed:", data);
            document.getElementById("loginMessage").innerText = "Login failed. Check credentials.";
        }
    } catch (error) {
        console.error("Error:", error);
    }
}

document.getElementById("loginForm").addEventListener("submit", function (event) {
    event.preventDefault();
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    staffLogin(username, password);
});