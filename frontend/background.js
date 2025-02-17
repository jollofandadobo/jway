chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.message === "fetchAsinData") {
        console.log("Received ASIN from content script:", request.asin);

        const url = `http://127.0.0.1:8000/api/rainforest/${encodeURIComponent(request.asin)}`;

        fetch(url, {
            method: "GET",
            headers: {
                "Content-Type": "application/json"
            }
        })
        .then(response => response.json())
        .then(data => {
            console.log("Response from server:", data);
            sendResponse({ success: true, data }); // Send response back to content script

            // Replace it with a message from back end
            chrome.runtime.sendMessage({
                message: "asinDataReceived",
                data: "Place holder sumaryyy for now"
            })
        })
        .catch(error => {
            console.error("Error fetching ASIN data:", error);
            sendResponse({ success: false, error: error.message });

            // Replace it with a message from back end
            chrome.runtime.sendMessage({
                message: "asinDataError",
                data: "Data could not be recaived"
            })
        });

        return true; // Required for async sendResponse
    }
});
