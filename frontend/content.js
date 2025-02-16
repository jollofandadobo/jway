function extractASIN() {
    let match = document.URL.match(/\/dp\/([A-Z0-9]{10})|\/gp\/product\/([A-Z0-9]{10})/);
    return match ? (match[1] || match[2]) : null;
}

let asin = extractASIN();
if (asin) {
    // Send the ASIN to the background script
    chrome.runtime.sendMessage({ asin: asin });
}