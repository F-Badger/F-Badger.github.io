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

const sectionUsedRadios = document.getElementsByName("sectionsUsed")
const learnSectionQuestions = document.getElementById("learnQuestions")
const practiceSectionQuestions = document.getElementById("practiceQuestions")

sectionUsedRadios.forEach(function(radio) {
    radio.addEventListener("change", function() {
        if (this.value == "learn") {
            learnSectionQuestions.classList.remove("hidden")
            practiceSectionQuestions.classList.add("hidden")
        }
        else if (this.value == "practice") {
            learnSectionQuestions.classList.add("hidden")
            practiceSectionQuestions.classList.remove("hidden")
        }
        else {
            learnSectionQuestions.classList.remove("hidden")
            practiceSectionQuestions.classList.remove("hidden")
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