//select all of the topicHeader checkboxes
const topicHeadersCheckboxes = document.querySelectorAll('.topicHeader input[type="checkbox"]')

topicHeadersCheckboxes.forEach(function(topicCheckbox) {

    //add an event listener to each topicHeader checkbox for if they are changed
    topicCheckbox.addEventListener('change', function() {

        //get the closest checkboxContainer to the topicHeader checkbox
        //this checkboxContainer will contain the checkboxes for the subtopics of the topicHeader 
        var checkboxContainer = this.closest('.checkboxContainer');

        //get all the checkboxes for the subtopics
        var subtopicCheckboxes = checkboxContainer.querySelectorAll('input[type="checkbox"]:not(.topicHeader input[type="checkbox"])');
        
        //update the state of each subtopic checkbox to match the topicHeader checkbox
        subtopicCheckboxes.forEach(function(subtopicCheckbox) {
            subtopicCheckbox.checked = topicCheckbox.checked;
        })
    })
})

function generateQuestions() {

    //get all the checkboxes for the subtopics (and convert to an array)
    var subtopicCheckboxes = Array.from(document.querySelectorAll('input[type="checkbox"]:not(.topicHeader input[type="checkbox"])'));

    //check if no checkboxes have been selected
    if (subtopicCheckboxes.every((checkbox) => !(checkbox.checked))) {
        alert("At least one topic must be selected") //raise an alert
        return //empty return to exit function
    }

    //use array methods to get the checkboxes which have been checkd
    var checkedCheckboxes = subtopicCheckboxes
    .filter((checkbox) => checkbox.checked) //filter list to include only checkboxes that are checked
    .map((checkbox) => checkbox.name) //map each selected checkbox so that the list only includes the names give to the checkboxes

}