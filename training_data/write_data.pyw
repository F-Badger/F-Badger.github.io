import tkinter as tk
import json

#filename of JSONL file with training data
fileName = "check_self_contained_training_data.jsonl"

#open jsonl training data file
theFile = open(fileName,"a")

#set window
window = tk.Tk()

#set window title, size and background colour
window.title("Enter Training Data") 
window.geometry("500x250") 
window.configure(bg='#C3DFE0') 

#stop window being resized or made fullscreen (as it is not designed for that)
window.resizable(False, False) 
window.attributes('-fullscreen', False) 

#display label and input box for the example prompt
promptLabel = tk.Label(
    window, 
    text="Example Prompt:", #label text
    bg="#C3DFE0" #label background colour (same as parent window)
    )
promptEntry = tk.Text(
    window,
    height = 4 #text box has height of 4 lines
    )
promptLabel.pack(
    pady = 10 #label has 10px of vertical padding
)
promptEntry.pack(
    padx = 10 #text box has 10px of horizontal padding
    )

#display label and input box for the ideal output
idealOutputLabel = tk.Label(
    window, 
    text="Ideal Output:", #label text
    bg="#C3DFE0" #label backgound colour (same as parent window)
    ) 
idealOutputEntry = tk.Text(
    window,
    height = 3 #text box has height of 3 lines
    )
idealOutputLabel.pack(
    pady = 10 #label has 10px of vertical padding
)
idealOutputEntry.pack(
    padx = 10 #text box has 10px of horizontal padding
    )

#write the inputs to the training file when submit button pressed
def submit_entry():

    #get the inputs from the window and remove whitespace
    examplePrompt = promptEntry.get("1.0",tk.END).strip()
    idealOutput = idealOutputEntry.get("1.0",tk.END).strip()

    #show an error window if either input is blank
    if examplePrompt == "" or idealOutput == "": #check if either input is blank

        #set new error window
        errWindow = tk.Tk()

        #set error window title, size and background colour
        errWindow.title("Error")
        errWindow.geometry("200x70")
        errWindow.configure(bg="#F5846C")

        #stop window being resized or made fullscreen
        errWindow.resizable(False, False)
        errWindow.attributes('-fullscreen', False)

        #display error message on error window
        errLabel = tk.Label(
            errWindow,
            text = "Input Boxes cannot be empty", #error message
            bg="#F5846C" #background colour (same as parent window)
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
    
    #remove line seperators from inputs, if any
    examplePrompt = examplePrompt.replace("\n"," ")
    idealOutput = idealOutput.replace("\n"," ")

    #format the data to be added to the training file
    data = {
            "messages": [
                {"role": "system", "content": "Determine if the following question is self-contained."},
                {"role": "user", "content": examplePrompt},
                {"role": "assistant", "content": idealOutput}
                ]
            }
    
    json.dump(data,theFile) #write object to training file  
    theFile.write("\n") #add a new line character (necessary for JSONL format)

    clear_window() #clear the input boxes

#clear all input boxes
def clear_window():
    promptEntry.delete(1.0,tk.END)
    idealOutputEntry.delete(1.0,tk.END)
    
#display button for submitting inputs
submitButton = tk.Button(
    window,
    text="Submit", #button text
    command=submit_entry, #call the submit_entry() function on button press
    width = 8, #button has a width of 8 characters
    )
submitButton.pack(
                  side=tk.LEFT, #position button on left of window
                  padx = 10, #10px of horizontal padding
                  pady = 10 #10px of vertical padding
                  )

#display button for clearing inputs 
clearButton = tk.Button(
    text="Clear", #button text
    command=clear_window, #call the clear_window() function on button press
    width = 8 #button has a width of 8 characters
    )
clearButton.pack(
                  side=tk.LEFT, #position button on left of window
                  padx = 8, #8px of horizontal padding
                  pady = 10, #10px of vertical padding
                  )

window.mainloop() #listen for events
