let high_contrast = false
window.addEventListener('message', 
(event) => {
    if (event.data[0] == "toggleHighContrast") {
        toggleHighContrast()
        var headeriframe = document.getElementById('header');
        headeriframe.contentWindow.postMessage(["toggleHighContrast"], "*")
    }
    else if (event.data[0] == "updateiframeHeight") {
        var headeriframe = document.getElementById('header');
        headeriframe.style.height = event.data[1]
    }
    else if (event.data[0] == "updateBodyHeight") {
        document.body.style.height = event.data[1]
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