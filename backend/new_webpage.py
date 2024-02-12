import tkinter as tk

#set window
window = tk.Tk()

#set window title, size and background colour
window.title("Create New Webpage")
window.configure(bg='#C3DFE0') 

#create frame for title entry section
titleFrame = tk.Frame(window, bg="#C3DFE0")

titleLabel = tk.Label(
    titleFrame, 
    text="Title:", #label text
    bg="#C3DFE0" #label background colour (same as frame)
    )
titleEntry = tk.Entry(
    titleFrame,
    width=100  #entry box has width of 100 characters
    )
titleLabel.pack(
    side=tk.LEFT,  #align label on left of frame
    padx = 10 #label has 10px of horizontal padding
)
titleEntry.pack(
    side=tk.LEFT,  #align entry box on left of frame on same line as label
    padx = 10 #entry has 10px of horizontal padding
    )

titleFrame.pack(
    anchor=tk.NW,  #position title entry frame in top left of window
    pady=15,  #frame has 15px of vertical padding
)


#create frame for section entry
newSectionFrame = tk.Frame(window, bg="#FFC8DD")


#create frame for section title entry
newSectionTitleFrame = tk.Frame(newSectionFrame, bg="#FFC8DD")

newSectionTitleLabel = tk.Label(
    newSectionTitleFrame, 
    text="New Section:",  #label text
    bg="#FFC8DD"  #label background colour (same as frame)
    )
newSectionTitleEntry = tk.Entry(
    newSectionTitleFrame,
    width=60  #entry box has width of 60 characters
    )
newSectionTitleLabel.pack(
    side=tk.LEFT,  #align label on left of frame

    #10px of padding
    padx = 10,
    pady = 10,
    )
newSectionTitleEntry.pack(
    side=tk.LEFT,  #align entry box on left of frame on same line as label

    #10px of padding
    padx = 10,
    pady = 10,
    )

newSectionTitleFrame.pack()


#create frame for content options selection
contentOptionsFrame = tk.Frame(newSectionFrame, bg="#FFC8DD")

newSectionContentOptionsLabel = tk.Label(
    contentOptionsFrame,
    text="Select a Content Option:", #label text
    bg="#FFC8DD" #label background colour (same as frame)
)

newSectionContentOptionsLabel.pack(
    side = tk.LEFT,  #position label on left of frame

    #10px of padding
    padx = 10,
    pady = 10,
)


#create frame for content options buttons
contentOptionsButtonsFrame = tk.Frame(contentOptionsFrame, bg="#FFC8DD")

contentOptionParagraph = tk.Button(
    contentOptionsButtonsFrame,
    text = "Paragraph", #button text
    width = 12,  #button has width 12 
)

contentOptionBulletPoints = tk.Button(
    contentOptionsButtonsFrame,
    text = "Bullet Points", #button text
    width = 12,  #button has width 12 
)

contentOptionTable = tk.Button(
    contentOptionsButtonsFrame,
    text = "Table", #button text
    width = 12,  #button has width 12
)

contentOptionParagraph.pack(
    side = tk.LEFT,

    #10px of padding
    padx = 10,
    pady = 10, 
)

contentOptionBulletPoints.pack(
    side = tk.LEFT,

    #10px of padding
    padx = 10,
    pady = 10, 
)

contentOptionTable.pack(
    side = tk.LEFT,

    #10px of padding
    padx = 10,
    pady = 10, 
)

contentOptionsButtonsFrame.pack ()

contentOptionsFrame.pack()

addSectionButton = tk.Button(
    newSectionFrame,
    text = "Add Section", #button text
    width = 12,  #button has width 12
)

addSectionButton.pack(
    side=tk.LEFT,

    #10px of padding
    padx = 10,
    pady = 10, 
)

newSectionFrame.pack(
    anchor="nw",  #position title entry frame in top left of window, below title entry frame

    padx = 20,  #20px of horizontal padding to slightly indent frame 
    pady = 10,  #10px of vertical padding
)

createPageButton = tk.Button(
    window,
    text = "Create Webpage", #button text
    width = 15,  #button has width 15
)

createPageButton.pack(
    side=tk.LEFT,

    #10px of padding
    padx = 10,
    pady = 10, 
)

window.mainloop()  #listen for events