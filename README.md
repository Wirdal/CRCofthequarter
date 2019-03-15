# CRC of the Quarter Plaque Generator
## Purpose

To create, based off of a list of user given information, the CRC of the quarter plaque. 
---
### Installation
This project was written in Python 3.6. Future iterations of this language may change things significantly. We cannot plan for this, so for best results, run it in Python 3. In addition, the PIP version is 10.0.1, while the Pillow version is XXX.

1. Have Python installed.
2. Make sure pip is updated
3. Have pillow installed

That is pretty much it.

---
### Basic Usage
There is some small preliminary work that needs to be done, so the program can locate the files properly.

1. Mount `\\cold-app2\App2_htdocs`s with `ADS\itlmXXX` as the _Z_ drive
2. Run `gui.py` by double clicking, or running the command `python gui.py` in the command line
3. Enter the information of all CRCs who were selected as the CRC of the quarter by entering their information in the topmost boxes, and pressing submit for each on. If the information was valid, each box should blank out. If not, the boxes with invalid data will delete the information in them, and display "Invalid Lab/quarter/whatever
4. When all is done, click on the "Generate Sheets" button. This will create the images in the directory where the program is located
5. Enjoy our hard work

### Advanced usage
The program was designed for the future of CLM, which includes the addition and deletion of labs as well as the renaming of them. The fields should be self explanatory, but we will explain for our sake.

- The "Add from list" button and textbox allow the user to give a filename, with the .txt extension, and the program will take all information from that file and properly sort, then write the CRCs in that file to their respective location.

* Add lab allows the user to define a new lab name, and after creation, allow CRCs to be created to that lab.

* Remove lab does the opposite, given an existent lab, it will remove the text file, and not allow creation to that lab anymore.

* Rename lab takes an existing lab from user selection, and renames it to the users specification. If the file does not exist, or the "destination" lab already exists, this function will not do anything.

---

## Developer/Maintenance information
For those unfortunate souls who have to rewrite this program in the future, whether it breaks from python updates or user error, this section is for you.

### Organization
This program had a small amount of pre-planning before development started. Files are logically split up into four parts.

- `plaque` handles file I/O. From formatting what to write to the renaming of labs. It takes parameters from `gui` and hands information to `generator`.

- `gui` handles the front end. It also deals with validating user input. It passes information from its fields to `plaque`.

- `generator` handles image and text layering for the final output. It gets all of its information from `plaque`.

- `labs/` Holds the text files, those text files hold the CRC for a selected quarter and year.

    - The text files hold the information in a sensitive way.

        - First name - last name - Lab group - Quarter - Year - ITLM#
    
    - In the case an individual has two or more words per name, we simply replace them with a "/" in the text file, which then is replaced with a space in the generated sheet. This trick is done because we treat each line as a list, and adding a space would add another element to our list, which would throw our indexing off.

- `fonts/` holds the fonts we use.

So, in a sense, the GUI acts as the frontend, the plaque handles middleman tasks, and generator deals with the final product. Extensive commenting accompanies this project, and with a very basic idea it should not be hard to understand.

### Troubleshooting
Chances are, you could be here because a sheet came out improperly, or not at all. This section is for outlining possible problems and the developers way to fix them

> CRC has the wrong picture!

1. The wrong ITLM number was typed in. Go to their lab's text file and change it by hand.
2. While rare, it is possible that the directory in which we grab the picture from has changed the name of the file. Go to `Z:\\staffpics` after mounting the drive and try to find the correct picture, and correct the naming mistakes.
3. Other than this, the file type could have changed. A find and replace will have to be done in `generator`

> I am getting an error saying `Z:\\staffpics\\somelocation` does not exist!

1. Make sure you have mounted the drive, and make sure it is mounted as the Z drive. In a pinch, you can rename the `path` variable at the top of `generator` to suit your needs.

> I hate your program!

1. I hate you.

##### Authors
Joseph Mussano & Chase Maguire, Summer of 2018.