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
    requestViewportHeight()
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
        if (hamburgerMenu.classList.contains("selected")) {
            hamburgerMenu.classList.remove("selected")
        }
        pseudoBackground.classList.remove("enabled")
    }
    resetMobileNav()
    mainWindow.postMessage(["updateBodyHeight","initial"],"*")               
}

function resetMobileNav() {
    Array.from(document.querySelectorAll(".mobile-dropdown.visible")).forEach(element => {
            element.classList.remove("visible")
        }
        )
    Array.from(document.querySelectorAll(".mobile-dropdown-toggle.selected")).forEach(element => {
            element.classList.remove("selected")
        }
        )
}  

function updateiframeHeight(newHeight) {
    mainWindow.postMessage(["updateiframeHeight",newHeight],"*")
}
function requestViewportHeight() {
    mainWindow.postMessage(["requestViewportHeight"],"*")
}
function updateViewportHeight(newViewportHeight) {
    viewportHeight = newViewportHeight
}

function hamburgerPress() {
    resetMobileNav()
    hamburgerMenu.classList.toggle("selected")
    mobileNav.classList.toggle("display")
    pseudoBackground.classList.toggle("enabled")
    if (mobileNav.classList.contains("display")) {
        updateiframeHeight("100vh")  
    }
    else {
        setTimeout(() => updateiframeHeight("110px"),400)
    }
    if (hamburgerMenu.classList.contains("selected")) {
        mainWindow.postMessage(["hamburgerMenuOpened"],"*")
    }
    if (!(hamburgerMenu.classList.contains("selected"))) {
        mainWindow.postMessage(["hamburgerMenuClosed"],"*")
    }         
}

function mobileDropdownTogglePress(dropdownNum) {
    mobileNav.classList.toggle("noMinHeight")
    document.querySelector(".mobile-dropdown-toggle."+dropdownNum).classList.toggle("selected")
    document.querySelector(".mobile-dropdown."+dropdownNum).classList.toggle("visible")
    var navHeight = mobileNav.offsetHeight
    var newHeight = Math.max(navHeight,viewportHeight) + "px"
    updateiframeHeight(newHeight)
    mainWindow.postMessage(["updateBodyHeight",newHeight],"*")
}

handleResize();updateiframeHeight("110px")