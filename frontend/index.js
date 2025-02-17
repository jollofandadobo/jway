// import { extractASIN } from './content.js';

function extractASIN(url) {
    let match = url.match(/\/dp\/([A-Z0-9]{10})|\/gp\/product\/([A-Z0-9]{10})/);
    return match ? (match[1] || match[2]) : null;
}

const landingPage = document.querySelector('.landing-page');
const productPage = document.querySelector('.product-page');

const landingButton = document.querySelector('.landing--button');
const productButton = document.querySelector('.product--button');

const productTitle = document.querySelector('.product--title');
const productImage = document.querySelector('.product--image');
const productSummary = document.querySelector('.summary').querySelector('p');

const exitButton = document.querySelector('.exit-bttn');

const productFromLocalStorage = JSON.parse(localStorage.getItem("myProduct"));

function isAmazonPage(url) {
    return url.includes("https://www.amazon");
}

function updateButton(url) {
    if (isAmazonPage(url)) {
        landingButton.textContent = 'Generate insights';
        landingButton.style.backgroundColor = 'var(--green)';
        landingButton.style.color = 'var(--green-dark)';
    } else {
        landingButton.textContent = 'Go to Amazon';
        landingButton.style.backgroundColor = 'var(--yellow)';
        landingButton.style.color = 'var(--yellow-dark)';
    }
}

function goToProductPage() {
    landingPage.style.display = 'none';
    productPage.style.display = 'flex';
}

function goToLandingPage() {    
    landingPage.style.display = 'flex';
    productPage.style.display = 'none';
}

if (productFromLocalStorage) {
    render(productFromLocalStorage);
} else {
    goToLandingPage();
}

chrome.tabs.query({active: true, currentWindow: true}, function(tabs) { 
    const currentURL = tabs[0].url;
    updateButton(currentURL);
    const asin = extractASIN(currentURL);
    landingButton.addEventListener('click', async function () {
        // console.error("Button clicked");
        if (isAmazonPage(currentURL)) {
            chrome.runtime.onMessage.addListener((request) => {
                if (request.message === "asinDataReceived") {  
                    console.error(request.data)                 
                    localStorage.setItem("myProduct", JSON.stringify(request.data));
                    render(request.data); // Required for async sendResponse
                }
            });
        } else {
            window.open('https://www.amazon.ca', '_blank');
        }
    });
    productButton.addEventListener('click', async function () {
        if (isAmazonPage(currentURL)) {
            if (asin) {
                try {
                    const response = await fetch(`http://127.0.0.1:8000/api/rainforest/${encodeURIComponent(asin)}`);
                    const data = await response.json();
                    if (data) {
                        localStorage.setItem("myProduct", JSON.stringify(data));
                        render(data);
                    }
                } catch (error) {
                    console.error("Error fetching product info:", error);
                }
            }
        }
    });
});

exitButton.addEventListener('click', () => {
    window.close();
});
    
function render({title, image, summary}) {
    goToProductPage();
    productTitle.textContent = title;
    productImage.src = image;
    productSummary.textContent = summary;
}

/* 
https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts
https://developer.chrome.com/docs/extensions/reference/api/tabs
*/

// TODO: SAVE ANY NEW INSIGHTS INTO THING