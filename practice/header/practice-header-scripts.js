window.addEventListener("message", 
(event) => {
    var message = event.data[0]
    if (message == "toggleHighContrast") {
        toggleHighContrast()
    }
})

function toggleHighContrast() {
    document.querySelector("main").classList.toggle("high-contrast")
}