let viewportHeight;
const mainWindow = window.parent;
const specMap = document.getElementById("spec-map");
const logo = document.getElementById("logo");
const mobileNav = document.getElementById("mobile-nav");
const hamburgerMenu = document.getElementById("hamburger");
const pseudoBackground = document.getElementById("pseudo-background");

window.addEventListener('message', 
    (event) => {
        if (event.data[0] == "toggleHighContrast") {
            toggleHighContrast()
        }
        if (event.data[0] == "updateViewportHeight") {
            console.log("rec")
            updateViewportHeight(event.data[1])
        }
    }
    )

window.addEventListener('resize', handleResize);

function toggleHighContrast() {
    
    //update font colour of all items in header
    document.querySelector("main").classList.toggle("high-contrast")
}

function handleResize() {
    if (document.querySelector(".big.topic").offsetHeight == 0) {
        return false
    }
    var newHeight = document.querySelector(".big.topic").offsetHeight + "px"
    Array.from(document.querySelectorAll(".small.topic")).forEach(
        topic => {
        topic.style.height = newHeight
    })
    specMap.style.height = newHeight
    if (window.innerWidth > 680) {
        if (mobileNav.classList.contains("display")) {
            mobileNav.classList.remove("display")
            updateiframeHeight("110px")
            mainWindow.postMessage(["hamburgerMenuClosed"],"*")
        }
        hamburgerMenu.classList.remove("selected")
        pseudoBackground.classList.remove("display")
    }
    resetMobileNav()
    mainWindow.postMessage(["updateBodyHeight","initial"],"*")               
}

function resetMobileNav() {

    //get all mobile-dropdowns which have been given a class of .visible and remove this class
    Array.from(document.querySelectorAll(".mobile-dropdown.visible")).forEach(element => {
            element.classList.remove("visible")
        }
        )

    //get all mobile dropdown toggles which have been given a class of .selected and remove this class
    Array.from(document.querySelectorAll(".mobile-dropdown-toggle.selected")).forEach(element => {
            element.classList.remove("selected")
        }
        )
}  

function updateiframeHeight(newHeight) {
    mainWindow.postMessage(["updateiframeHeight",newHeight],"*")
}

function updateViewportHeight(newViewportHeight) {
    viewportHeight = newViewportHeight
}

function requestViewportHeight() {
    mainWindow.postMessage(["requestViewportHeight"],"*")
}

function hamburgerPress() {

    //reset dropdowns and toggles
    resetMobileNav()

    //hamburgerMenu, mobileNav and pseduoBackground are defined as constant at the start of the file
    //toggle the appearance of the hamburger menu icon
    hamburgerMenu.classList.toggle("selected")
    //toggle the visibility of the mobile navigation menu and pseudo-bacgkround
    mobileNav.classList.toggle("display")
    pseudoBackground.classList.toggle("display")


    //if the hamburger menu has just been opened 
    if (hamburgerMenu.classList.contains("selected")) {
        //set the iframe height to fill the entire window
        updateiframeHeight("100vh")  
        //send a message to handle the menu being opened
        mainWindow.postMessage(["hamburgerMenuOpened"],"*")
    }

    //if the mobile navigation menu is now closed
    else {
        //reduce the height of the iframe to 110px (size of unexpanded header)
        //delay reducing the height of the iframe to allow the closing transition animation to occur
        setTimeout(() => updateiframeHeight("110px"),400)
        //send a message to handle the menu being closed
        mainWindow.postMessage(["hamburgerMenuClosed"],"*")
    }
}

function mobileDropdownTogglePress(dropdownNum) {

    //toggle the appearance of the selected dropdown toggle
    document.querySelector(".mobile-dropdown-toggle."+dropdownNum).classList.toggle("selected")

    //toggle the visivility of the selected dropdown
    document.querySelector(".mobile-dropdown."+dropdownNum).classList.toggle("visible")

    //set the new height of the iframe to be either the height of the mobile navigation menu, or the height of the viewport,
    //whichever is larger; this allows the menu to be scrolled down when multiple dropdowns are open and prevents the 
    //background of the parent page showing
    var navHeight = mobileNav.offsetHeight
    var newHeight = Math.max(navHeight,viewportHeight) + "px"
    updateiframeHeight(newHeight)
}

handleResize();updateiframeHeight("110px")
