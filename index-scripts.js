window.addEventListener('message', 
(event) => {

    //check if the message is "toggleHighContrast", as the message event will have multiple uses
    if (event.data == "toggleHighContrast") {

        //call the function to handle toggling high contrast
        toggleHighContrast()
    }
}
)
function toggleHighContrast() {

    //update page background background
    document.body.classList.toggle("high-contrast")

    //update font colour of main section and header
    document.querySelector("main").classList.toggle("high-contrast")
    document.querySelector("header").classList.toggle("high-contrast")
}