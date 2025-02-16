chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.message === "fetchAsinData") {
        console.log("Received ASIN from content script:", request.asin);
        
        fetch("http://127.0.0.1:8000/receive_asin", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ asin: request.asin })
        })
        .then(response => response.json())
        .then(data => {
            console.log("Response from server:", data);
        })
        .catch(error => {
            console.error("Error sending ASIN to server:", error);
        });

        sendResponse({ success: true });
    }
    return true; // Required for async sendResponse
});