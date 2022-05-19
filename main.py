# CMPT 120 Yet Another Image Processer
# Starter code for main.py
# Author(s): Prince Nirafan, Gavin Samra
# Date: Decmeber 6, 2020
# Description: This file controls the user interface of the image processor

import cmpt120imageProj
import cmpt120imageManip
import tkinter.filedialog
import pygame
pygame.init()

# list of system options
system = [
            "Q: Quit",
            "O: Open Image",
            "S: Save Current Image",
            "R: Reload Image"
         ]

# list of basic operation options
basic = [
          "1: Invert",
          "2: Flip Horizontal",
          "3: Flip Vertical",
          "4: Switch to Intermeidate Functions",
          "5: Switch to Advanced Functions"
         ]

# list of intermediate operation options
intermediate = [
                  "1: Remove Red Channel",
                  "2: Remove Green Channel",
                  "3: Remove Blue Channel",
                  "4: Convert to Grayscale",
                  "5: Apply Sepia Filter",
                  "6: Decrease Brigtness",
                  "7: Increase Brightness",
                  "8: Switch to Basic Functions",
                  "9: Switch to Advanced Functions"
                 ]

# list of advanced operation options
advanced = [
                "1: Rotate Left",
                "2: Rotate Right",
                "3: Pixelate",
                "4: Binarize",
                "5: Switch to Basic Functions",
                "6: Switch to Intermediate Functions"
             ]

# a helper function that generates a list of strings to be displayed in the interface
def generateMenu(state):
    """
    Input:  state - a dictionary containing the state values of the application
    Returns: a list of strings, each element represets a line in the interface
    """
    menuString = ["Welcome to CMPT 120 Image Processer!"]
    menuString.append("") # an empty line
    menuString.append("Choose the following options:")
    menuString.append("") # an empty line
    menuString += system
    menuString.append("") # an empty line

    # build the list differently depending on the mode attribute
    if state["mode"] == "basic":
        menuString.append("--Basic Mode--")
        menuString += basic
        menuString.append("")
        menuString.append("Enter your choice (Q/O/S/R or 1-5)")
    elif state["mode"] == "intermediate":
        menuString.append("--Intermediate Mode--")
        menuString += intermediate
        menuString.append("")
        menuString.append("Enter your choice (Q/O/S/R or 1-9)")
    elif state["mode"] == "advanced":
        menuString.append("--Advanced Mode--")
        menuString += advanced
        menuString.append("")
        menuString.append("Enter your choice (Q/O/S/R or 1-6)")
    else:
        menuString.append("Error: Unknown mode!")

    return menuString

#a helper function that returns the result image as a result of the operation chosen by the user
#it also updates the state values when necessary (e.g, the mode attribute if the user switches mode)
def handleUserInput(state, img):
    """
        Input:  state - a dictionary containing the state values of the application
                img - the 2d array of RGB values to be operated on
        Returns: the 2d array of RGB vales of the result image of an operation chosen by the user
    """
    userInput = state["lastUserInput"].upper()

    #this section1 is the open, save, and reload system#
    if userInput.isalpha(): # check if the input is an alphabet
        print("Log: Doing system functionalities " + userInput)

        if userInput == "O":
            tkinter.Tk().withdraw()
            openFilename = tkinter.filedialog.askopenfilename()
            print("Log: Open Image " + openFilename) #Informs the user of the function#
            hd = "Opened Image: " #Image header; similar styled to other functions#
            pic = openFilename.split("/") #This get's the name of the photo#
            nam = len(pic)
            pn = pic[nam-1]
            state["name"] = pn #saves the name of the image to the dictionary#
            img = cmpt120imageProj.getImage(openFilename)
            cmpt120imageProj.showInterface(img, hd + pn, generateMenu(appStateValues))
            state["lastOpenFilename"] = openFilename

        elif userInput == "S":
            tkinter.Tk().withdraw()
            saveFilename = tkinter.filedialog.asksaveasfilename()
            print("Log: Saving Image " + saveFilename)
            hd = "Saved Image: "
            pic = saveFilename.split("/") #This saves the name of the photo#
            nam = len(pic)
            pn = pic[nam-1]
            state["name"] = pn
            cmpt120imageProj.saveImage(img, pn)
            cmpt120imageProj.showInterface(img, hd + pn, generateMenu(appStateValues))

        elif userInput == "R":
            img = cmpt120imageProj.getImage(state["lastOpenFilename"])
            rel = state["lastOpenFilename"]
            print("Log: Reloading Image " + rel)
            hd = "Reloaded: "
            pic = state["lastOpenFilename"].split("/") #This get's the name of the photo#
            nam = len(pic)
            pn = pic[nam-1]
            cmpt120imageProj.showInterface(img, hd + pn, generateMenu(appStateValues))

        else:
            print("Log: Unrecognized user input: " + userInput )
    #section1 ends here#


    #this section2 is the basic functions#
    elif userInput.isdigit() and state["mode"] == "basic": #a digit for manipulation options
        print("Log: Doing manipulation functionalities " + userInput)
        if userInput == "1": #inverts the image#
            print("Log: Performing 1: Invert")
            hd = "Inverted: "
            pn = state["name"] #name of the image#
            inverted = cmpt120imageManip.invert(img)
            cmpt120imageProj.showInterface(inverted, hd + pn, generateMenu(appStateValues))
            img = inverted #this makes the img be modified; similarily coded on other functions#

        elif userInput == "2": #flips the image horizontally#
            print("Log: Performing 2: Flip Horizontal")
            hd = "Flipped Horizontally: "
            pn = state["name"]
            flipH = cmpt120imageManip.flipHorizontal(img)
            cmpt120imageProj.showInterface(flipH, hd + pn, generateMenu(appStateValues))
            img = flipH

        elif userInput == "3": #flips the image vertically#
            print("Log: Performing 3: Flip Vertical")
            hd = "Flipped Vertically: "
            pn = state["name"]
            flipV = cmpt120imageManip.flipVertical(img)
            cmpt120imageProj.showInterface(flipV, hd + pn, generateMenu(appStateValues))
            img = flipV

        elif userInput == "4":
            print("Log: Performing 4: Switching to Intermediate Functions")
            hd = "Intermediate Fucntions: "
            pn = state["name"]
            state["mode"] = "intermediate"
            cmpt120imageProj.showInterface(img, hd + pn, generateMenu(appStateValues))

        elif userInput == "5":
            print("Log: Performing 5: Switching to Advanced Functions")
            hd = "Advanced Fucntions: "
            pn = state["name"]
            state["mode"] = "advanced"
            cmpt120imageProj.showInterface(img, hd + pn, generateMenu(appStateValues))

        else:
            print("Log: Unrecognized user input: " + userInput )
    #section2 ends here#



    #this section3 is the intermediate functions#
    elif userInput.isdigit() and state["mode"] == "intermediate":
        print("Log: Doing manipulation functionalities " + userInput)
        if userInput == "1":
            print("Log: Performing 1: Removing Red Channel")
            hd = "Removed Red Channel: "
            pn = state["name"]
            remr = cmpt120imageManip.removeRed(img)
            cmpt120imageProj.showInterface(remr, hd + pn, generateMenu(appStateValues))
            img = remr

        elif userInput == "2":
            print("Log: Performing 2: Removing Green Channel")
            hd = "Removed Green Channel: "
            pn = state["name"]
            remg = cmpt120imageManip.removeGreen(img)
            cmpt120imageProj.showInterface(remg, hd + pn, generateMenu(appStateValues))
            img = remg

        elif userInput == "3":
            print("Log: Performing 3: Remove Blue Channel")
            hd = "Remove Blue Channel: "
            pn = state["name"]
            remb = cmpt120imageManip.removeBlue(img)
            cmpt120imageProj.showInterface(remb, hd + pn, generateMenu(appStateValues))
            img = remb

        elif userInput == "4":
            print("Log: Performing 4: Grayscale")
            hd = "Grayscale: "
            pn = state["name"]
            gray = cmpt120imageManip.grayScale(img)
            cmpt120imageProj.showInterface(gray, hd + pn, generateMenu(appStateValues))
            img = gray

        elif userInput == "5":
            print("Log: Performing 5: Sepia Filter")
            hd = "Sepia Filter: "
            pn = state["name"]
            sepia = cmpt120imageManip.sepiaFilter(img)
            cmpt120imageProj.showInterface(sepia, hd + pn, generateMenu(appStateValues))
            img = sepia

        elif userInput == "6":
            print("Log: Performing 6: Decrease Brightness")
            hd = "Decrease Brightness: "
            pn = state["name"]
            decbr = cmpt120imageManip.decreaseBrightness(img)
            cmpt120imageProj.showInterface(decbr, hd + pn, generateMenu(appStateValues))
            img = decbr

        elif userInput == "7":
            print("Log: Performing 7: Increase Brightness")
            hd = "Increase Brightness: "
            pn = state["name"]
            incbr = cmpt120imageManip.increaseBrightness(img)
            cmpt120imageProj.showInterface(incbr, hd + pn, generateMenu(appStateValues))
            img = incbr

        elif userInput == "8":
            print("Log: Performing 8: Switching to Basic Functions")
            hd = "Basic Fucntions: "
            pn = state["name"]
            state["mode"] = "basic"
            cmpt120imageProj.showInterface(img, hd + pn, generateMenu(appStateValues))

        elif userInput == "9":
            print("Log: Performing 9: Switching to Advanced Functions")
            hd = "Advanced Fucntions: "
            pn = state["name"]
            state["mode"] = "advanced"
            cmpt120imageProj.showInterface(img, hd + pn, generateMenu(appStateValues))

        else:
            print("Log: Unrecognized user input: " + userInput )
    #section3 ends here#



    #this section4 is the advanced functions#
    elif userInput.isdigit() and state["mode"] == "advanced":
        if userInput == "1":
            print("Log: Performing 1: Rotate Left")
            hd = "Rotate Left: "
            pn = state["name"]
            rotateL = cmpt120imageManip.rotateLeft(img)
            cmpt120imageProj.showInterface(rotateL, hd + pn, generateMenu(appStateValues))
            img = rotateL

        elif userInput == "2":
            print("Log: Performing 2: Rotate Right")
            hd = "Rotate Right: "
            pn = state["name"]
            rotateR = cmpt120imageManip.rotateRight(img)
            cmpt120imageProj.showInterface(rotateR, hd + pn, generateMenu(appStateValues))
            img = rotateR

        elif userInput == "3":
            print("Log: Performing 3: Pixelate")
            hd = "Pixelate: "
            pn = state["name"]
            pixl = cmpt120imageManip.pixelate(img)
            cmpt120imageProj.showInterface(pixl, hd + pn, generateMenu(appStateValues))
            img = pixl

        elif userInput == "4":
            print("Log: Performing 4: Binarize")
            hd = "Binarize: "
            pn = state["name"]
            bina = cmpt120imageManip.binarize(img)
            cmpt120imageProj.showInterface(bina, hd + pn, generateMenu(appStateValues))
            img = bina

        elif userInput == "5":
            print("Log: Performing 5: Switching to Basic Functions")
            hd = "Basic Fucntions: "
            pn = state["name"]
            state["mode"] = "basic"
            cmpt120imageProj.showInterface(img, hd + pn, generateMenu(appStateValues))

        elif userInput == "6":
            print("Log: Performing 6: Switching to Intermediate Functions")
            hd = "Intermediate Fucntions: "
            pn = state["name"]
            state["mode"] = "intermediate"
            cmpt120imageProj.showInterface(img, hd + pn, generateMenu(appStateValues))

        else:
            print("Log: Unrecognized user input: " + userInput )
    #section4 ends here#

    return img

# use a dictionary to remember several state values of the application
appStateValues = {
                    "mode": "basic",
                    "lastOpenFilename": "",
                    "lastSaveFilename": "",
                    "lastUserInput": "",
                    "name": ""
                 }

currentImg = cmpt120imageProj.createBlackImage(600, 400) # create a default 600 x 400 black image
cmpt120imageProj.showInterface(currentImg, "No Image", generateMenu(appStateValues))

# ***this is the event-loop of the application. Keep the remainder of the code unmodified***
keepRunning = True
# a while-loop getting events from pygame
while keepRunning:
    ### use the pygame event handling system ###
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            appStateValues["lastUserInput"] = pygame.key.name(event.key)
            # prepare to quit the loop if user inputs "q" or "Q"
            if appStateValues["lastUserInput"].upper() == "Q":
                keepRunning = False
            # otherwise let the helper function handle the input
            else:
                currentImg = handleUserInput(appStateValues, currentImg)
        elif event.type == pygame.QUIT:#another way to quit the program is to click the close botton
            keepRunning = False

# shutdown everything from the pygame package
pygame.quit()

print("Log: Program Quit")