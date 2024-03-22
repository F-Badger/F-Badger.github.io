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

//get the radio buttons for the question about which sections they have used
const sectionUsedRadios = document.getElementsByName("sectionsUsed")

//get the divs containing questions for each section
const learnSectionQuestions = document.getElementById("learnQuestions")
const practiceSectionQuestions = document.getElementById("practiceQuestions")

sectionUsedRadios.forEach(function(radio) {

    radio.addEventListener("change", function() { //add an event listener to each radio that listen for any changes

        //if they have selected that they have only used the learn section
        if (this.value == "learn") {
            learnSectionQuestions.classList.remove("hidden") //show the learn section questions
            practiceSectionQuestions.classList.add("hidden") //hide the practice section questions
        }

        //if they have selected that they have only used the practice section
        else if (this.value == "practice") {
            learnSectionQuestions.classList.add("hidden") //hide the learn section questions
            practiceSectionQuestions.classList.remove("hidden") //show the practice section questions
        }

        //if they have selected that they have used both sections
        else {
            learnSectionQuestions.classList.remove("hidden") //show the learn section questions
            practiceSectionQuestions.classList.remove("hidden") //show the practice section questions
        }
    })
})

const pastQuestionsUsedRadio = document.getElementsByName("usedPastQuestionsSection")
const pastQuestionsQuestions = document.getElementById("pastQuestionsSectionQuestions")

pastQuestionsUsedRadio.forEach(function(radio) {
    radio.addEventListener("change", function() {
        if (this.value == "yes") {
            pastQuestionsQuestions.classList.remove("hidden")
        }
        else {
            pastQuestionsQuestions.classList.add("hidden")
        }
    })
})

const generateQuestionsUsedRadio = document.getElementsByName("usedGenerateQuestionsSection")
const generateQuestionsQuestions = document.getElementById("generateSectionQuestions")

generateQuestionsUsedRadio.forEach(function(radio) {
    radio.addEventListener("change", function() {
        if (this.value == "yes") {
            generateQuestionsQuestions.classList.remove("hidden")
        }
        else {
            generateQuestionsQuestions.classList.add("hidden")
        }
    })
})