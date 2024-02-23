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

        //hide the content of the main part of the page
        //mainSection is defined as a constant at the start of the file
        //delay this to only hide the content after the transistion animation to show the menu has finished
        setTimeout(() => mainSection.classList.add("hide"),400)
    }

    else if (message == "hamburgerMenuClosed") {

        //reset the height of the body (the height of the body increases due to the mobile navigation menu)
        document.body.style.height = "intial"

        //re-display the content of the main part of the page
        mainSection.classList.remove("hide")
    }
}
)

window.addEventListener("resize", handleResize)

function handleResize() {
    setFooterPosition()
    headerIframe.contentWindow.postMessage(["updateViewportHeight",window.innerHeight],"*")
}

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

    //check if the combined height of the footer and document body is more than the height of the window
    //the footerIframe is defined as a constant at the start of the file
    if (document.body.offsetHeight + footerIframe.offsetHeight > window.innerHeight) {

        //set position of the footer iframe to relative
        footerIframe.style.position = "relative"
    }
    else {
        //set the position of the footer iframe to absolute
        footerIframe.style.position = "absolute"
    }
}

setTimeout(() => handleResize(),100)

