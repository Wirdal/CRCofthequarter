import os
from PIL import Image, ImageDraw, ImageFont
""" Holds the code for actual plaque generation"""
path = "Z:\\staffpics" #Make sure to mount to the Z: drive.

#load in fonts
#Font size 22 in Word --> 61 here. 2.77272727273 conversion factor.
fnt_FuturaUCDavisBold = ImageFont.truetype('fonts\\FuturaUCDavis-Bold.ttf', 61)
fnt_FuturaUCDavisLight = ImageFont.truetype('fonts\\FuturaUCDavis-Light.ttf', 61)
fnt_BerkeleyUCDavisBold = ImageFont.truetype('fonts\\BerkeleyUCDavis-Bold.ttf', 133)
fnt_BerkeleyUCDavisBold_smallcaps = ImageFont.truetype('fonts\\BerkeleyUCDavis-Bold.ttf', 108)
fnt_BerkeleyUCDavisMedium = ImageFont.truetype('fonts\\BerkeleyUCDavis-Medium.ttf', 50)
fnt_BerkeleyUCDavisMedium_italics_24pt = ImageFont.truetype('fonts\\BerkeleyUCDavis-MediumIt.ttf', 72)
fnt_BerkeleyUCDavisMedium_italics_12pt = ImageFont.truetype('fonts\\BerkeleyUCDavis-MediumIt.ttf', 34)
# These are for the lower 9 names
#fnt_FuturaUCDavisBoldsm = ImageFont.truetype('fonts\\FuturaUCDavis-Bold.ttf', 28)
#fnt_FuturaUCDavisBoldsm_long = ImageFont.truetype('fonts\\FuturaUCDavis-Bold.ttf', 24)
fnt_FuturaUCDavisMedium = ImageFont.truetype('fonts\\FuturaUCDavis-Medium.ttf', 32) #30
fnt_FuturaUCDavisMedium_long = ImageFont.truetype('fonts\\FuturaUCDavis-Medium.ttf', 28)
fnt_FuturaUCDavisLightsm = ImageFont.truetype('fonts\\FuturaUCDavis-Light.ttf', 32)

def backtrack(year, itlm):
    """
    Will try and find a picture with the given specifications,
    up to four years back, otherwise gives a default.
    Returns the Image object.
    """
    try:
        img = Image.open(os.path.join(path, year, "itlm" + itlm +".jpg"))
    except IOError:
        try:
            year = str(int(year) - 1) 
            img = Image.open(os.path.join(path, year, "itlm" + itlm +".jpg"))
        except IOError:
            try:
                year = str(int(year) - 1) 
                img = Image.open(os.path.join(path, year, "itlm" + itlm +".jpg"))
            except IOError:
                try:
                    year = str(int(year) - 1) 
                    img = Image.open(os.path.join(path, year, "itlm" + itlm +".jpg"))
                except IOError:
                    img = Image.open("default.jpg")
    return(img)

def generator(crclist, baseImage = "temp.jpg"):
    """ 
    A script, takes the list of CRCs, and generates an employee of 
    the month sheet out of it. Designed to be modular based on the 
    background image
    """

    def checkLength(name):
        """
        Takes a the name of the crc and checks if the horizontal pixel size is too long.
        Changes the font size if it is.
        """
        textsize = t.textsize(text = name, font = fnt_FuturaUCDavisMedium)
        #Instead of characters, use horizontal pixel dimension. Measured from third column to end of line.
        if textsize[0] < 252:
            return fnt_FuturaUCDavisMedium
        else:
            return fnt_FuturaUCDavisMedium_long
    
    # Path starts with year
    # Then goes to itlmXXX.jpg, where XXX is the itlm number. they should all be unique
    base = Image.open(baseImage).convert("RGBA")
    txt = Image.new("RGBA", base.size, (255,255,255,0))
    # If the base directory ever moves, this can be changed
    
    # A layer holding all the text. Will be compoosited over base later
    # We do this for each picture individually, to save memory
    t = ImageDraw.Draw(txt)


    # First image
    first = crclist[0].split(sep = " ")
    # Grab the picture, based on year, and ITLM number
    # Need to go back through previous years.
    # If the file doesnt exist in the current year directory
    # We need to go back a year
    # Do this for ~ 4 years, so 4 loops

    # Size for first image is 485x 628
    imgFirst = backtrack(first[4], first[5])
    imgFirst = imgFirst.resize((485, 628)).convert("RGBA")
    # Add it to the base picture
    base.alpha_composite(imgFirst, (315, 320))
    # Free up memory
    del imgFirst
    # Name
    t.text((882, 485), text = first[0] + " " + first[1], font = fnt_FuturaUCDavisBold, fill = (0,0,0,255))
    # Quarter and year
    t.text((882, 565), text = first[3] + " " + first[4], font = fnt_FuturaUCDavisLight, fill = (0,0,0,255))

    # Second Image
    second = crclist[1].split(sep = " ")
    imgSecond = backtrack(second[4], second[5])
    # Size for second and all others is 64 x 81
    imgSecond = imgSecond.resize((64,81)).convert("RGBA")
    # Placement is 294x1495
    base.alpha_composite(imgSecond, (294, 1495))
    # Free up memory
    del imgSecond
    # TODO Add text
    name = second[0] + " " + second[1]
    t.text((371, 1495), text = second[0] + " " + second[1], font = checkLength(name), fill = (0,0,0,255))
    t.text((371, 1542), text = second[3] + " " + second[4], font = fnt_FuturaUCDavisLightsm , fill = (0,0,0,255))

    # Third Image
    third = crclist[2].split(sep = " ")
    imgThird = backtrack(third[4], third[5])
    imgThird = imgThird.resize((64,81)).convert("RGBA")
    # Placement is 694x1495
    base.alpha_composite(imgThird, (694,1495))
    del imgThird
    # TODO add text
    name = third[0] + " " + third[1]
    t.text((771, 1495), text = third[0] + " " + third[1], font = checkLength(name), fill = (0,0,0,255))
    t.text((771, 1542), text = third[3] + " " + third[4], font = fnt_FuturaUCDavisLightsm, fill = (0,0,0,255))

    # Fourth Image
    fourth = crclist[3].split(sep = " ")
    imgFourth = backtrack(fourth[4], fourth[5])
    imgFourth = imgFourth.resize((64, 81)).convert("RGBA")
    # Placement is 1094x1495
    base.alpha_composite(imgFourth, (1094,1495))
    del imgFourth
    # TODO add text
    name =  fourth[0] + " " + fourth[1]
    t.text((1171, 1495), text = fourth[0] + " " + fourth[1], font = checkLength(name), fill = (0,0,0,255))
    t.text((1171, 1542), text = fourth[3] + " " + fourth[4], font = fnt_FuturaUCDavisLightsm, fill = (0,0,0,255))



#Why is the fifth image use "eighth"?
    # Fifth Image
    eighth = crclist[4].split(sep = " ")
    imgFifth = backtrack(eighth[4], eighth[5])
    imgFifth = imgFifth.resize((64,81)).convert("RGBA")
    # Placement is 294x1605
    base.alpha_composite(imgFifth, (294,1605))
    del imgFifth
    # TODO add text
    name = eighth[0] + " " + eighth[1]
    t.text((371, 1605), text = eighth[0] + " " + eighth[1], font = checkLength(name), fill = (0,0,0,255))
    t.text((371, 1652), text = eighth[3] + " " + eighth[4], font = fnt_FuturaUCDavisLightsm, fill = (0,0,0,255))






    # Sixth Image
    sixth = crclist[5].split(sep = " ")
    imgSixth = backtrack(sixth[4], sixth[5])
    imgSixth = imgSixth.resize((64,81)).convert("RGBA")
    # Placement is 694x1605
    base.alpha_composite(imgSixth,(694,1605))
    del imgSixth
    #TODO add text
    name = sixth[0] + " " + sixth[1]
    t.text((771, 1605), text = sixth[0] + " " + sixth[1], font = checkLength(name), fill = (0,0,0,255))
    t.text((771, 1652), text = sixth[3] + " " + sixth[4], font = fnt_FuturaUCDavisLightsm, fill = (0,0,0,255))

    # Seventh Image
    seventh = crclist[6].split(sep = " ")
    imgSeventh = backtrack(seventh[4], seventh[5])
    imgSeventh = imgSeventh.resize((64,81)).convert("RGBA")
    # Placement is 1094x1605
    base.alpha_composite(imgSeventh, (1094,1605))
    del imgSeventh
    #TODO add text
    name =  seventh[0] + " " + seventh[1]
    t.text((1171, 1605), text = seventh[0] + " " + seventh[1], font = checkLength(name), fill = (0,0,0,255))
    t.text((1171, 1652), text = seventh[3] + " " + seventh[4], font = fnt_FuturaUCDavisLightsm, fill = (0,0,0,255))

    # Eighth Image
    eighth = crclist[7].split(sep = " ")
    imgEighth = backtrack(eighth[4], eighth[5])
    imgEighth = imgEighth.resize((64,81)).convert("RGBA")
    # Placement is 294 x 1715
    base.alpha_composite(imgEighth, (294,1715))
    del imgEighth
    #TODO add text
    name = eighth[0] + " " + eighth[1]
    t.text((371, 1715), text = eighth[0] + " " + eighth[1], font = checkLength(name), fill = (0,0,0,255))
    t.text((371, 1762), text = eighth[3] + " " + eighth[4], font = fnt_FuturaUCDavisLightsm, fill = (0,0,0,255))

    # Ninth Image
    ninth = crclist[8].split(sep = " ")
    imgNinth = backtrack(ninth[4], ninth[5])
    imgNinth = imgNinth.resize((64,81)).convert("RGBA")
    # Placement is 694x1715
    base.alpha_composite(imgNinth, (694,1715))
    del imgNinth
    #TODO add text
    name = ninth[0] + " " + ninth[1]
    t.text((771, 1715), text = ninth[0] + " " + ninth[1], font = checkLength(name), fill = (0,0,0,255))
    t.text((771, 1762), text = ninth[3] + " " + ninth[4], font = fnt_FuturaUCDavisLightsm, fill = (0,0,0,255))

    # Tenth Image
    tenth = crclist[9].split(sep = " ")
    imgTenth = backtrack(tenth[4], tenth[5])
    imgTenth = imgTenth.resize((64,81)).convert("RGBA")
    # Placement is 694x1715
    base.alpha_composite(imgTenth, (1095,1715))
    del imgTenth
    #TODO add text
    name =  tenth[0] + " " + tenth[1]
    t.text((1171, 1715), text = tenth[0] + " " + tenth[1], font = checkLength(name), fill = (0,0,0,255))
    t.text((1171, 1762), text = tenth[3] + " " + tenth[4], font = fnt_FuturaUCDavisLightsm, fill = (0,0,0,255))

    # Now that all the pictures are layered, we can layer the text.

    labname = first[2]
    quarter = first[3]
    year = first[4]

    # Text placement is below
    # Cases will be implemented for the lab grop and title. 
    # Names are consant, unchanging parameters.

    #Title placement
    if labname == "HWS":
        # Then place the hardware support text
        t.text((285, 1030), text = "H", font = fnt_BerkeleyUCDavisBold, fill = (0,0,0,255))
        t.text((380, 1052), text = "ARDWARE", font = fnt_BerkeleyUCDavisBold_smallcaps, fill = (0,0,0,255))
        t.text((931, 1030), text = "S", font = fnt_BerkeleyUCDavisBold, fill = (0,0,0,255))
        t.text((1003, 1052), text ="UPPORT", font = fnt_BerkeleyUCDavisBold_smallcaps, fill = (0,0,0,255))
        t.text((571, 1142), text = "E", font = fnt_BerkeleyUCDavisBold, fill = (0,0,0,255))
        t.text((648, 1164), text = "MPLOYEE", font = fnt_BerkeleyUCDavisBold_smallcaps, fill = (0,0,0,255))
        textsize = t.textsize(text = labname.replace('-', '/').upper(), font = fnt_BerkeleyUCDavisMedium)
        t.text(((853 - ((textsize[0])/2)), (1398 - ((textsize[1])/2))), text = labname.replace('-', '/').upper(), font = fnt_BerkeleyUCDavisMedium, fill = (0,0,0,255))
    elif labname == "Admin":
        t.text((405, 1030), text = "A", font = fnt_BerkeleyUCDavisBold, fill = (0,0,0,255))
        t.text((496, 1052), text = "DMIN", font = fnt_BerkeleyUCDavisBold_smallcaps, fill = (0,0,0,255))
        t.text((809, 1030), text = "S", font = fnt_BerkeleyUCDavisBold, fill = (0,0,0,255))
        t.text((879, 1052), text = "UPPORT", font = fnt_BerkeleyUCDavisBold_smallcaps, fill = (0,0,0,255))
        t.text((570, 1142), text = "E", font = fnt_BerkeleyUCDavisBold, fill = (0,0,0,255))
        t.text((647, 1164), text = "MPLOYEE", font = fnt_BerkeleyUCDavisBold_smallcaps, fill = (0,0,0,255))
        textsize = t.textsize(text = labname.replace('-', '/').upper(), font = fnt_BerkeleyUCDavisMedium)
        t.text(((853 - ((textsize[0])/2)), (1398 - ((textsize[1])/2))), text = labname.replace('-', '/').upper(), font = fnt_BerkeleyUCDavisMedium, fill = (0,0,0,255))
    else: #CRC
        t.text((370, 1030), text = "C", font = fnt_BerkeleyUCDavisBold, fill = (0,0,0,255))
        t.text((459, 1052), text = "OMPUTER", font = fnt_BerkeleyUCDavisBold_smallcaps, fill = (0,0,0,255))
        t.text((996, 1030), text = "R", font = fnt_BerkeleyUCDavisBold, fill = (0,0,0,255))
        t.text((1078, 1052), text = "OOM", font = fnt_BerkeleyUCDavisBold_smallcaps, fill = (0,0,0,255))
        t.text((484, 1142), text = "C", font = fnt_BerkeleyUCDavisBold, fill = (0,0,0,255))
        t.text((573, 1164), text = "ONSULTANT", font = fnt_BerkeleyUCDavisBold_smallcaps, fill = (0,0,0,255))
        textsize = t.textsize(text = labname.replace('-', '/').upper(), font = fnt_BerkeleyUCDavisMedium)
        t.text(((853 - ((textsize[0])/2)), (1398 - ((textsize[1])/2))), text = labname.replace('-', '/').upper(), font = fnt_BerkeleyUCDavisMedium, fill = (0,0,0,255))
    
    #accent left
    accent = Image.open("accent.png").convert("RGBA") #accent.png is 65x23 pixels.
    textsize = t.textsize(text = labname.replace('-','/').upper(), font = fnt_BerkeleyUCDavisMedium)
    x = int((853 - ((textsize[0])/2))-65-10) #Beginning of placement of labname minus 65+10 pixels.
    y = int(1381 + ((textsize[1])/4))
    base.alpha_composite(accent, (x, y))
    #accent right
    accent = accent.transpose(Image.FLIP_LEFT_RIGHT)
    x = int((853 + ((textsize[0])/2))+10)
    base.alpha_composite(accent, (x, y))
    del accent
    
    #Border lines for CRC history
    t.line([(276, 1460), (1423, 1460)], fill = (0,0,0,255), width = 2)
    t.line([(276, 1831), (1423, 1831)], fill = (0,0,0,255), width = 2)

    #extra text for "of the quarter" and "Computer Lab Management\n IET-Academic Technology Services".
    #"Of The Quarter": top left of 'f' crossbar.
    t.text((651, 1281), text = "of the Quarter", font = fnt_BerkeleyUCDavisMedium_italics_24pt, fill = (0,0,0,255))
    #"Computer Lab Management": tip of top of 'C'.
    t.text((663, 1848), text = "Computer Lab Management", font = fnt_BerkeleyUCDavisMedium_italics_12pt, fill = (0,0,0,255))
    #"IET-Academic Technology Services": Top-left of 'I'.
    t.text((615, 1884), text = "IET-Academic Technology Services", font = fnt_BerkeleyUCDavisMedium_italics_12pt, fill = (0,0,0,255))
    
    base = Image.alpha_composite(base, txt)
    base = base.crop((58, 101, 1631, 2099))
    #print margin in Paint settings (portrait): 
        #left: .31
        #right: .31
        #top: .47
        #bottom: .47 in
    labname = os.path.join("finished", labname)
    base.save(labname + ".png", format="PNG")

    #DONE WOOO