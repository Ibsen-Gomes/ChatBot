function sendMessage() {
    let userMessage = document.getElementById("userInput").value;
    let messagesDiv = document.getElementById("messages");

    if (userMessage.trim() !== "") {
        messagesDiv.innerHTML += `<div><b>Você:</b> ${userMessage}</div>`;
        
        fetch("/get_response", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: userMessage })
        })
        .then(response => response.json())
        .then(data => {
            messagesDiv.innerHTML += `<div><b>Bot:</b> ${data.response}</div>`;
        });

        document.getElementById("userInput").value = "";
    }
}
