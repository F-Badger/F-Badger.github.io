let viewportHeight;
const mainWindow = window.parent;
const specMapNav = document.getElementById("spec-map");
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
    
    //changes are only needed if the window has been resized to a width greater than the small screen breakpoint (680px)
    if (window.innerWidth > 680) {

        //get the height of the first topic header (1.1.1) as this will always be the biggest topic header (as it has the longest name)
        var newHeight = document.querySelector(".first.topic").offsetHeight + "px"

        //set the height of all the other topic header and the specification map header to the same size as the first topic header
        //this ensures all dropdowns are shown at the same height, and that all headers are lined up with each other
        Array.from(document.querySelectorAll(".other.topic")).forEach(
        topic => {
            topic.style.height = newHeight
        })
        specMapNav.style.height = newHeight

        //if the mobile hamburger menu was open when the window to resized beyond the small screen breakpoint (so should no longer show)
        if (hamburgerMenu.classList.contains("selected")) {

            //return all elements of the hamburger menu to their default, unopened state
            hamburgerMenu.classList.remove("selected")
            mobileNav.classList.remove("display")
            pseudoBackground.classList.remove("display")
            resetMobileNav()  

            //send message to main window to reduce the size of the iframe (it would previously have been the entire screen)
            updateiframeHeight("110px")

            //send message to main window to run the procedures that would run normally to handle the hamburger menu closing
            mainWindow.postMessage(["hamburgerMenuClosed"],"*")
        }
    }     
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
    //send message to parent window to update height of iframe to newHeight
    mainWindow.postMessage(["updateiframeHeight",newHeight],"*")
}

function updateViewportHeight(newViewportHeight) {
    viewportHeight = newViewportHeight
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
