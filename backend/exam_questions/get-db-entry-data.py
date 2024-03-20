import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from writeToDB import writeToDatabase

#initialise variables for paths
questionPath = ""
answerPath = ""

#initialise variables for window height
initialHeight = 600
questionImgHeight = 0
answerImgHeight = 0

#set window
window = tk.Tk()

#set window title, size and background colour
window.title("New Database Entry") 
window.geometry("700x600") 
window.configure(bg='#C3DFE0') 

#stop window being resized or made fullscreen
window.resizable(False, False) 
window.attributes('-fullscreen', False) 

def chooseImage(imageType):

    #open file manager to select an image
    filePath = filedialog.askopenfilename(filetypes=[("Image files", "*.png")])

    if filePath:

        #open selected image file using PIL
        image = Image.open(filePath)

        #set width of the image to be 600px while maintaining aspect ratio
        widthPercent = (600 / float(image.size[0]))
        newHeight = int((float(image.size[1]) * float(widthPercent)))
        image = image.resize((600, newHeight))

        #make image compatiable with tkinter
        image = ImageTk.PhotoImage(image)

        #update the relevant labels and variables depending on if the image is the question or answer
        if imageType == "question":
            #change configuration of label to include the image and change height to fit image
            questionImg.config(image=image, height=newHeight)
            #keep reference to image
            questionImg.image = image
            #need to access global variables
            global questionPath, questionImgHeight 
            #update file path and image height
            questionPath = filePath
            questionImgHeight= newHeight -15 #subtracting 15 prevents the submit button from being stretched too far away

        else:
            answerImg.config(image=image, height=newHeight)
            answerImg.image = image
            global answerPath, answerImgHeight
            answerPath = filePath
            answerImgHeight = newHeight -15
        
        window.geometry(f"700x{initialHeight+questionImgHeight+answerImgHeight}") #update window height to fit images

## CHOOSING IMAGES ## 

#button to choose an image
questionImgButton = tk.Button(
    window, #place button in main window
    text="Choose Question Image", #button text
    command=lambda: chooseImage("question") #call chooseImage function on button press
)
questionImgButton.pack(
    anchor=tk.W, #anchor button to left
    #padding for button
    padx = 50, #50px of horizontal padding
    pady = (25,10), #25px of padding above; 10px below
)

#label to display the image
questionImg = tk.Label(
    window,
    bg="#C3DFE0", #label backgound colour (same as parent window so it is not visible)
)
questionImg.pack()

#button to choose an image
answerImgButton = tk.Button(
    window, 
    text="Choose Answer Image",
    command=lambda: chooseImage("answer")
    )
answerImgButton.pack(
    anchor=tk.W,
    padx = 50,
    pady = (25,10),
)

#label to display the image
answerImg = tk.Label(
    window,
    bg="#C3DFE0" #label backgound colour (same as parent window so it is not visible)
)
answerImg.pack()

def showError():
    #set new error window
        errWindow = tk.Tk()

        #set error window title, size and background colour
        errWindow.title("Error")
        errWindow.geometry("200x70")
        errWindow.configure(bg="#F5846C")

        #stop window being resized or made fullscreen
        errWindow.resizable(False, False)
        errWindow.attributes('-fullscreen',False)

        #display error message on error window
        errLabel = tk.Label(
            errWindow,
            text = "All fields must be completed",  
            bg="#F5846C"
        )
        errLabel.pack(pady=10)

        #close the error window on button press
        def close_window():
            errWindow.destroy()

        #show button to close the error window
        closeButton = tk.Button(
            errWindow,
            text = "Close", #button text
            command = close_window, #call the close_window() function upon button press
        )
        closeButton.pack()

def submitEntry():
    #need to access global variables
    global questionPath, answerPath

    #get all the data
    level = selectedLevel.get()
    year = selectedYear.get()
    paper = selectedPaper.get()
    questionNum = questionNumInput.get().strip() #remove whitespace from start and end, if any
    isExtendedResponse = bool(extendedResponseSelected.get())
    topics = [option for index, option in enumerate(options) if checkboxes[index].get()] #get only the topics which have been selected

    #check if any data is missing
    if (
        questionPath == "" or
        answerPath == "" or
        level == "none" or 
        year == "none" or 
        paper == "none" or 
        questionNum == "" or 
        topics == []
    ):
        showError() #show error popup
        return #empty return to stop any further code from executing
    
    #call function to write to database with appropriate data
    writeToDatabase(year, level, paper, isExtendedResponse, questionNum, questionPath, answerPath, topics)

    #reset all input fields to their original values
    questionPath = ""
    answerPath = ""
    selectedLevel.set("none")
    selectedYear.set("none")
    selectedPaper.set("none")
    questionNumInput.delete(0, tk.END)
    extendedResponseSelected.set(0)
    for checkbox in checkboxes:
         checkbox.set(0)

    #remove images and reset height of image labels and window
    questionImg.config(image=None, height=18)
    answerImg.config(image=None, height=18)
    questionImg.image, answerImg.image = None, None
    global questionImgHeight, answerImgHeight
    questionImgHeight, answerImgHeight = 0, 0
    window.geometry("700x600")

#submit button
submitButton = tk.Button(
    window, 
    text="Submit", 
    command = submitEntry,
)
submitButton.pack(
    side=tk.BOTTOM, #position button at bottom of window
    anchor=tk.W, #anchor button to left
    padx = 50,
    pady = (0,20)
)

## LEFT SECTION ##
# contains options to choose levels and options to choose year

leftSection = tk.Frame(
    window, 
    bg="#C3DFE0"
)
leftSection.pack(
    side=tk.LEFT, #place widget at left side of window and allow other widgets to be placed alongside
    anchor=tk.N, #anchor widget to top of container
    padx=(50,0), 
    pady=25
)

## CHOOSING LEVEL ##

levelLabel = tk.Label(
    leftSection, #place label in leftSection frame
    text="Select the Level:",
    bg="#C3DFE0" 
)
levelLabel.pack(
    anchor=tk.W,
    pady=(0,10),
)

selectedLevel = tk.StringVar(value="none") #hold selected option

asButton = tk.Radiobutton( #radio button used as only one selection should be made for this section
    leftSection,
    text="AS",
    variable=selectedLevel, #link button to variable holding selected option
    value="AS", #button value
    bg="#C3DFE0"
)
asButton.pack(
    anchor=tk.W,
    padx=5,
)

alevelButton = tk.Radiobutton(
    leftSection,
    text="A-Level",
    variable=selectedLevel,
    value="A2",
    bg="#C3DFE0" 
)
alevelButton.pack(
    anchor=tk.W,
    padx=5
)

## CHOOSING YEAR ##

yearLabel = tk.Label(
    leftSection,
    text="Select the Year:",
    bg="#C3DFE0"
)
yearLabel.pack(
    anchor=tk.W,
    pady=(25,10),
)

selectedYear = tk.StringVar(value="none")

specimenButton = tk.Radiobutton(
    leftSection,
    text="Specimen",
    variable=selectedYear,
    value="Specimen", 
    bg="#C3DFE0"
)
specimenButton.pack(
    anchor=tk.W,
    padx=5,
)

button2016 = tk.Radiobutton(
    leftSection,
    text="2016",
    variable=selectedYear,
    value="2016",
    bg="#C3DFE0"
)
button2016.pack(
    anchor=tk.W,
    padx=5,
)

button2017 = tk.Radiobutton(
    leftSection,
    text="2017",
    variable=selectedYear,
    value="2017",
    bg="#C3DFE0"
)
button2017.pack(
    anchor=tk.W,
    padx=5,
)

button2018 = tk.Radiobutton(
    leftSection,
    text="2018",
    variable=selectedYear,
    value="2018",
    bg="#C3DFE0"
)
button2018.pack(
    anchor=tk.W,
    padx=5,
)

button2019 = tk.Radiobutton(
    leftSection,
    text="2019",
    variable=selectedYear,
    value="2019", 
    bg="#C3DFE0"
)
button2019.pack(
    anchor=tk.W,
    padx=5,
)

button2020 = tk.Radiobutton(
    leftSection,
    text="2020",
    variable=selectedYear,
    value="2020",
    bg="#C3DFE0"
)
button2020.pack(
    anchor=tk.W,
    padx=5,
)

button2021 = tk.Radiobutton(
    leftSection,
    text="2021",
    variable=selectedYear,
    value="2021",
    bg="#C3DFE0"
)
button2021.pack(
    anchor=tk.W,
    padx=5,
)

button2022 = tk.Radiobutton(
    leftSection,
    text="2022",
    variable=selectedYear,
    value="2022",
    bg="#C3DFE0"
)
button2022.pack(
    anchor=tk.W,
    padx=5,
)

## RIGHT SECTION ##
# contains checkboxes for topics, input box for question num and option for extended response and paper number

rightSection = tk.Frame(
    window, 
    bg="#C3DFE0"
    )
rightSection.pack(
    side=tk.RIGHT, 
    anchor=tk.N,
    padx=(50,70), 
    pady=25
    )

## INNER SECTIONS ##
# the right section is split into two further sections
# left inner section has the question number input box, extended reponse option and paper option, right has the topic checkboxes

innerLeftSection = tk.Frame(
    rightSection, 
    bg="#C3DFE0"
)
innerLeftSection.pack(
    side=tk.LEFT,
    anchor=tk.N,
)

innerRightSection = tk.Frame(
    rightSection, 
    bg="#C3DFE0"
)
innerRightSection.pack(
    side=tk.RIGHT,
    anchor=tk.N,
    padx=(90,0)
)

## CHOOSING PAPER ##

paperLabel = tk.Label(
    innerLeftSection, 
    text="Select the Paper:",
    bg="#C3DFE0" 
)
paperLabel.pack(
    anchor=tk.W,
    pady=(0,10),
)

selectedPaper = tk.StringVar(value="none")

paper1Button = tk.Radiobutton(
    innerLeftSection,
    text="Paper 1",
    variable=selectedPaper, 
    value="1", 
    bg="#C3DFE0"
)
paper1Button.pack(
    anchor=tk.W,
    padx=5,
)

paper2Button = tk.Radiobutton(
    innerLeftSection,
    text="Paper 2",
    variable=selectedPaper,
    value="2",
    bg="#C3DFE0" 
)
paper2Button.pack(
    anchor=tk.W,
    padx=5
)

## QUESTION NUMBER ##

questionNumLabel = tk.Label(
    innerLeftSection,
    text="Enter the question number:",
    bg="#C3DFE0"
)
questionNumLabel.pack(
    anchor=tk.W,
    pady=(25,0)
)
questionNumInput = tk.Entry(
    innerLeftSection,
)
questionNumInput.pack(
    anchor=tk.W,
    padx=3,
    pady=10,
)

## EXTENDED RESPONSE ## 

#label and checkbox will be side by side, so they are enclosed in a frame together
extendedResponseFrame = tk.Frame(
    innerLeftSection,
    bg="#C3DFE0",
)
extendedResponseFrame.pack(
    anchor=tk.W,
)

extendedResponseLabel = tk.Label(
    extendedResponseFrame,
    text="Extended Response?",
    bg="#C3DFE0"
)
extendedResponseLabel.pack(
    anchor=tk.W,
    side=tk.LEFT,
    pady=15
)

extendedResponseSelected = tk.IntVar()

extendedResponseCheckbox = tk.Checkbutton(
    extendedResponseFrame,
    variable=extendedResponseSelected,
    bg="#C3DFE0",
)
extendedResponseCheckbox.pack(
    side=tk.LEFT,
) 

## CHOOSING TOPICS ##

topicsLabel = tk.Label(
    innerRightSection,
    text="Select the Topics:",
    bg="#C3DFE0"
)
topicsLabel.pack(
    anchor=tk.W,
    pady=(0,10)
)

checkboxes = [] #initialise list of checkboxes - tracks which boxes have been selected (1 is selected, 0 is not selected)

#all of the different topic options which need to be shown
options = ["1.1.1","1.1.2","1.1.3","1.2.1","1.2.2","1.2.3","1.2.4","1.3.1","1.3.2","1.3.3","1.3.4","1.4.1","1.4.2","1.4.3","1.5.1","1.5.2"]

#split checkboxes into two columns for appearance
leftColumn = tk.Frame(
    innerRightSection, 
    bg="#C3DFE0"
    )
leftColumn.pack(
    side=tk.LEFT
    )
rightColumn = tk.Frame(
    innerRightSection, 
    bg="#C3DFE0"
    )
rightColumn.pack(
    side=tk.RIGHT,
    anchor=tk.N
    )

#display the checkboxes
for index, option in enumerate(options): #cycle through all options

    var = tk.IntVar() #variable to track if the checkbutton is selected

    checkbox = tk.Checkbutton( #use checkbutton as multiple selection are possible
        leftColumn if index < 11 else rightColumn, #place checkboxes up to 1.3.4 (index 10) in left column, placing rest in right column
        text=option, #text for checkbutton is the option
        variable=var, #link variable tracking if checkbutton is selected
        bg="#C3DFE0"
    )
    checkbox.pack(
        anchor=tk.W,
    )
    checkboxes.append(var) #add variable tracking if each checkbutton is selected to list tracking which checkboxes have been selected

window.mainloop() #listen for events
