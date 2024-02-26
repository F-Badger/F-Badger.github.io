const footerIframe = document.getElementById("footer")
const headerIframe = document.getElementById("header")

window.addEventListener("resize", handleResize)

window.addEventListener("message", 
(event) => {
    var message = event.data[0]
    if (message == "toggleHighContrast") {
        toggleHighContrast()
    }
})

function handleResize() {
    setFooterPosition()
}

function setFooterPosition() {
    if (document.body.offsetHeight + footerIframe.offsetHeight > window.innerHeight) {
        footerIframe.style.position = "relative"
    }
    else {
        footerIframe.style.position = "absolute"
    }
}

function toggleHighContrast() {
    document.body.classList.toggle("high-contrast")
    document.querySelector("main").classList.toggle("high-contrast")
    headerIframe.contentWindow.postMessage(["toggleHighContrast"], "*")
}

handleResize()