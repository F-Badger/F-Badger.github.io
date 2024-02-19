const headerIframe = document.getElementById("header")
const mainSection = document.querySelector("main")
const footerIframe = document.getElementById("footer")

window.addEventListener('message', 
(event) => {
    var message = event.data[0]
    if (message == "toggleHighContrast") {
        toggleHighContrast()
    }
    else if (message == "updateiframeHeight") {
        headerIframe.style.height = event.data[1]
    }
    else if (message == "hamburgerMenuOpened") {
        setTimeout(() => mainSection.classList.add("hide"),400)
    }
    else if (message == "hamburgerMenuClosed") {
        document.body.style.height = "intial"
        mainSection.classList.remove("hide")
    }
    else if (message == "requestViewportHeight") {
        var viewportHeight = window.innerHeight
        headerIframe.contentWindow.postMessage(["updateViewportHeight",viewportHeight],"*")
    }
}
)

function toggleHighContrast() {

    //update page background background
    document.body.classList.toggle("high-contrast")

    //update font colour of main section and header
    document.querySelector("main").classList.toggle("high-contrast")

    //post message to header iframe to make it enable high contrast
    //the headerIframe is defined as a constant at the start of the file
    headerIframe.contentWindow.postMessage(["toggleHighContrast"], "*")
}

function setFooterPosition() {
    if (document.body.offsetHeight + footerIframe.offsetHeight > window.innerHeight) {
        footerIframe.style.position = "relative"
    }
}

setFooterPosition()