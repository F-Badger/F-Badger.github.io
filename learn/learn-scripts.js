let highContrast = false
const headerIframe = document.getElementById("header")
const mainSection = document.querySelector("main")
const footerIframe = document.getElementById("footer")

window.addEventListener('message', 
(event) => {
    var message = event.data[0]
    if (message == "toggleHighContrast") {
        toggleHighContrast()
        headerIframe.contentWindow.postMessage(["toggleHighContrast"], "*")
    }
    else if (message == "updateiframeHeight") {
        headerIframe.style.height = event.data[1]
    }
    else if (message == "hamburgerMenuOpened") {
        setTimeout(() => mainSection.classList.add("hide"),400)
    }
    else if (message == "hamburgerMenuClosed") {
        document.body.style.height = event.data[1]
        mainSection.classList.remove("hide")
    }
    else if (message == "requestViewportHeight") {
        var viewportHeight = window.innerHeight
        headerIframe.contentWindow.postMessage(["updateViewportHeight",viewportHeight],"*")
    }
}
)

function toggleHighContrast() {
    if (highContrast) {
        Array.from(document.querySelectorAll(".high-contrast")).forEach (
            element => {
                element.classList.remove("high-contrast");
                element.classList.add("default")
            }
        )
        highContrast = false
    }
    else {
        Array.from(document.querySelectorAll(".default")).forEach (
            element => {
                element.classList.remove("default");
                element.classList.add("high-contrast")
            }
        )
        highContrast = true
    }
}

function setFooterPosition() {
    if (document.body.offsetHeight + footerIframe.offsetHeight > window.innerHeight) {
        footerIframe.style.position = "relative"
    }
}

setFooterPosition()