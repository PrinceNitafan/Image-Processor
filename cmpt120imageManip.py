# CMPT 120 Yet Another Image Processer
# Starter code for cmpt120imageManip.py
# Author(s): Prince Nitafan, Gavin Samra
# Date: December 6th, 2020
# Description: This file contains the image functions

import cmpt120imageProj
import numpy


#This function inverts the colour of the image#
#New RGB values are the differences of 255 (max colour val) and each Red, Green, and Blue values#
def invert(pixel):

   for x in range(len(pixel)):
       for y in range(len(pixel[0])):

           pxl = pixel[x][y]
           r = 255 - pxl[0]
           g = 255 - pxl[1]
           b = 255 - pxl[2]

           pixel[x][y] = [r, g, b]

   return(pixel)


#This horizontally flips the image#
#The width (x) values are flipped#
def flipHorizontal(pixel):

    #this creates a blank canvas for the new RGB values to intergrate in#
    blank = cmpt120imageProj.createBlackImage(len(pixel), len(pixel[0]))

    for x in range(len(pixel)):
        for y in range(len(pixel[0])):

            n = -(x - (len(pixel)-1))
            px1 = pixel[n][y]

            r = px1[0]
            g = px1[1]
            b = px1[2]

            blank[x][y] = [r,g,b]

    return(blank)


#This flips the image vertically#
#The height (y) values are flipped#
def flipVertical(pixel):

    #this creates a blank canvas for the new RGB values to intergrate in#
    blank = cmpt120imageProj.createBlackImage(len(pixel), len(pixel[0]))

    for x in range(len(pixel)):
        for y in range(len(pixel[0])):

            n = -(y - (len(pixel[0]) -1))
            pxl = pixel[x][n]

            r = pxl[0]
            g = pxl[1]
            b = pxl[2]

            blank[x][y] = [r,g,b]

    return(blank)


#This removes the Red channels#
#It turns all Red values to 0#
def removeRed(pixel):
    for x in range(len(pixel)):
        for y in range(len(pixel[0])):
            pxl = pixel[x][y]

            r = pxl[0]
            g = pxl[1]
            b = pxl[2]

            pixel[x][y] = [0, g, b]

    return(pixel)


#This removes the Green Channel#
#It turns all Green values to 0#
def removeGreen(pixel):
    for x in range(len(pixel)):
        for y in range(len(pixel[0])):
            pxl = pixel[x][y]

            r = pxl[0]
            g = pxl[1]
            b = pxl[2]

            pixel[x][y] = [r, 0, b]

    return(pixel)


#This removes the Blue Channel#
#It turns all Blue values to 0#
def removeBlue(pixel):
    for x in range(len(pixel)):
        for y in range(len(pixel[0])):
            pxl = pixel[x][y]

            r = pxl[0]
            g = pxl[1]
            b = pxl[2]

            pixel[x][y] = [r, g, 0]

    return(pixel)


#This turns the image to grayscale#
#It averages out the RGB values through addition of the three values and divsion by 3#
def grayScale(pixel):
    for x in range(len(pixel)):
        for y in range(len(pixel[0])):
            pxl = pixel[x][y]

            r = pxl[0]
            g = pxl[1]
            b = pxl[2]

            gray = (r+g+b)/3

            pixel[x][y] = [gray, gray, gray]

    return(pixel)


#This filters the picture to the sepia form#
#This uses the sepia values to multiply each original RGB values#
def sepiaFilter(pixel):
    for x in range(len(pixel)):
        for y in range(len(pixel[0])):
            pxl = pixel[x][y]

            r = pxl[0]
            g = pxl[1]
            b = pxl[2]

            red = int((r * .393) + (g * .769) + (b * .189))
            green = int((r * .349) + (g * .686) + (b * .168))
            blue = int((r * .272) + (g * .534) + (b * .131))

            if red > 255:
                red = 255
            if blue > 255:
                blue = 255
            if green > 255:
                green = 255

            pixel[x][y] = [red, green, blue]

    return(pixel)


#This decreases the brightness of the image#
#It decreases each RGB value by 10#
def decreaseBrightness(pixel):
    for x in range(len(pixel)):
        for y in range(len(pixel[0])):
            pxl = pixel[x][y]

            r = pxl[0] - 10
            g = pxl[1] - 10
            b = pxl[2] - 10

            if r <= 0:
                r = 0
            if g <= 0:
                g = 0
            if b <= 0:
                b = 0

            pixel[x][y] = [r, g, b]

    return(pixel)


#This increases the brightness of the image#
#It increases each RGB value by 10#
def increaseBrightness(pixel):
    for x in range(len(pixel)):
        for y in range(len(pixel[0])):
            pxl = pixel[x][y]

            r = pxl[0] + 10
            g = pxl[1] + 10
            b = pxl[2] + 10

            if r >= 255:
                r = 255
            if g >= 255:
                g = 255
            if b >= 255:
                b = 255

            pixel[x][y] = [r, g, b]

    return(pixel)


#This rotates the image left#
#It uses an opposite widths and height blank canvas for the image values to be intergrated#
def rotateLeft(pixel):

    #This makes a blank canvas with the opposite widths and heights of the inputted image#
    blankinvert = cmpt120imageProj.createBlackImage(len(pixel[0]),len(pixel))

    for x in range(len(pixel)):
        for y in range(len(pixel[0])):

            pxl = pixel[x][y]

            r = pxl[0]
            g = pxl[1]
            b = pxl[2]

            n = -(x - (len(pixel)-1))
            blankinvert[y][n] = [r,g,b]

    return(blankinvert)


#This rotates the image right#
#It uses an opposite widths and height blank canvas for the image values to be intergrated#
def rotateRight(pixel):

    #This makes a blank canvas with the opposite widths and heights of the inputted image#
    blankinvert = cmpt120imageProj.createBlackImage(len(pixel[0]),len(pixel))

    for x in range(len(pixel)):
        for y in range(len(pixel[0])):

            pxl = pixel[x][y]

            r = pxl[0]
            g = pxl[1]
            b = pxl[2]

            n = -(y - (len(pixel[0])-1))
            blankinvert[n][x] = [r,g,b]

    return(blankinvert)


#This pixelates the image#
#It changes the values in 4x4 pixels (16 pixels) to the an average RGB value of the 16 pixels#
def pixelate(pixel):
    for x in range(3, len(pixel)+1, 4): #This for loop goes in steps of 4 pixels (width)#
        for y in range(3, len(pixel[0])+1, 4): #This for loop goes in steps of 4 (height)#

            #this provides the ending values for x2/y2 for loops#
            x1 = x - 4
            y1 = y - 4

            r = 0
            g = 0
            b = 0

            #This section captures the 16 pixels and averages the RGB values#
            for x2 in range(x, x1, -1):
                for y2 in range(y, y1, -1):

                    pxl = pixel[x2][y2]

                    rp = pxl[0]
                    gp = pxl[1]
                    bp = pxl[2]


                    r = r + rp
                    g = g + gp
                    b = b + bp

            r = r/16
            g = g/16
            b = b/16
            #This section ends here#

            #This section changes 4x4 pixels of the inputed image to the average RGB values#
            for x3 in range(x, x1, -1):
                for y3 in range(y, y1, -1):
                    pixel[x3][y3] = [r,g,b]


    return(pixel)


#This function binarizes the image#
def binarize(pixel):

    #these two are blank canvases for the background and forground of the inputed image#
    blank = cmpt120imageProj.createBlackImage(len(pixel),len(pixel[0]))
    blank2 = cmpt120imageProj.createBlackImage(len(pixel),len(pixel[0]))

    #This section1 grayscales the inputted image#
    if len(pixel) == len(pixel):
        for x in range(len(pixel)):
            for y in range(len(pixel[0])):

                pxl = pixel[x][y]

                r = pxl[0]
                g = pxl[1]
                b = pxl[2]

                ave = (r + g + b)/3

                pixel[x][y] = [ave, ave, ave]
        #Section1 ends here#

        #this is the first threshold variable#
        threshold = 0

        #This section2 averages the first threshold of the grayscale image#
        for x in range(len(pixel)):
            for y in range(len(pixel[0])):

                pxl2 = pixel[x][y]
                r2 = pxl2[0]
                g2 = pxl2[0]
                b2 = pxl2[0]

                ave2 = (r2 + g2 + b2)/3

                threshold = threshold + ave2

        threshold = threshold/(len(pixel)*len(pixel[0]))
        #section2 ends here#

        #this section3 gets the average of each RGB pixel#
        #seperates the grayscale image into the background and foregoround#
        for x in range(len(pixel)):
            for y in range(len(pixel[0])):

                pxl3 = pixel[x][y]

                r3 = pxl3[0]
                g3 = pxl3[1]
                b3 = pxl3[2]

                ave3 = int((r3 + g3 + b3)/3)

                if ave3 < threshold:
                    blank[x][y] = pixel[x][y]
                elif ave3 > threshold:
                    blank2[x][y] = pixel[x][y]
        #section3 ends here#

        #this is the threshold2 variable of the foreground and background#
        threshold2 = 0

        #this section4 calculates the average of the RGB values of the fore/background#
        for x in range(len(pixel)):
            for y in range(len(pixel[0])):

                pxl4 = blank[x][y]
                pxl5 = blank2[x][y]

                r4 = pxl4[0]

                ave4 = (r4 + r4 + r4)/3

                r5 = pxl5[0]

                ave5 = (r5 + r5 + r5)/3

                average = (ave4 + ave5)/2

                threshold2 = threshold2 + average

        threshold2 = threshold2/(len(pixel)*len(pixel[0]))
        #section4 ends here#

        #This section5 turns the image black or white based on threshold2#
        for x in range(len(pixel)):
            for y in range(len(pixel[0])):

                pxl6 = pixel[x][y]

                r6 = pxl6[0]

                if r6 < threshold2:
                    pixel[x][y] = [0,0,0]
                elif r6 > threshold2:
                    pixel[x][y] = [255,255,255]
        #section5 ends here#

        return(pixel)