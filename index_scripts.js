let high_contrast = false
window.addEventListener('message', 
(event) => {
    if (event.data == "toggleHighContrast") {
        toggleHighContrast()
    }
}
)
function toggleHighContrast() {
    if (!high_contrast) {
        document.body.classList.add("high-contrast")
        document.body.classList.remove("default")
        Array.from(document.getElementsByClassName("default-font-colour")).forEach(element => {
            element.classList.remove("default-font-colour");
            element.classList.add("high-contrast-font-colour")
        })
        high_contrast = true
    }
    else {
        document.body.classList.add("default")
        document.body.classList.remove("high-contrast")
        Array.from(document.getElementsByClassName("high-contrast-font-colour")).forEach(element => {
            element.classList.remove("high-contrast-font-colour");
            element.classList.add("default-font-colour")
        });
        high_contrast = false
    }
}