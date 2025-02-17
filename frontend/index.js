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
    landingButton.addEventListener('click', async function () {
        if (isAmazonPage(currentURL)) {
            // TODO: fetch product info and return dictionary
            // with title, image, and ai summary
            /* const myProduct = {
                title: "",
                image: "",
                summary: ""
            }; */
            
            // localStorage.setItem("myProduct", JSON.stringify(myProduct));
            goToProductPage(); // TODO: remove once fetch is implemented
            // render(insights);  // TODO: uncomment once fetch is implemented
        } else {
            window.open('https://www.amazon.ca', '_blank');
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