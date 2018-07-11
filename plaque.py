#The file is ordered by First-last-lab-quarter-year, where the lines are spaces, which will be the delimiterss
#A class, meant to handle the data taken from the text file.
import os
"""Holds the "meat" for all the writing, reading, and generating"""


class CRC:
	"""
	Holds the information in an array, from 0 to 4; first, last, lab, quarter,
	year

	Implemented as a way to shorten arguements
	"""

	def __init__(self, crclist):
		self.first= crclist[0]
		self.last = crclist[1]
		self.lab = crclist[2]
		self.quarter = crclist[3]
		self.year = crclist[4]
		self.num = crclist[5]

	def formatString(self):
		""" Formats the string to be written"""
		return("\n" + self.first + " " + self.last + " " +self.lab + " " 
			+ self.quarter + " " +self.year + " " + self.num)

	def addCRC(self, filename):
		""" Adds a singular person to the text file. """
		dirname = os.path.dirname(__file__) #Getting the relative path
		# Giving the path to the file that holds that lab
		fileloc = os.path.join(dirname, "labs/" + filename) 
		with open(fileloc, mode = "a") as file:
			file.write(self.formatString())


def text2List(smFile):
	""" Takes the text file and gives it in a list """
	with open(smFile) as file:
		# https://docs.python.org/3/library/stdtypes.html#str.splitlines
		# https://docs.python.org/3/library/functions.html?highlight=open#open
		crcs = []
		for line in file:
			# Take off enders
			temp = line.rstrip() 
			# Creates a list with each number
			temp = temp.split(sep= " ") 
			# Create an object with it, and throw it onto the list
			crcs.append(CRC(temp)) 
		# A list of objects, CRCs
		return(crcs) 


def addLab(labname):
	"""Creates text file for lab. Returns true if creation occured, false if not"""
	exists = checkLab(labname)
	if exists:
		return(False)
	else:
		dirname = os.path.dirname(__file__)
		fileloc = os.path.join(dirname, "labs/" + labname +".txt")
		with open(fileloc, mode = "x"):
			return(True)
def removeLab(labname):
	"""Oppopsite of addLab."""

def renameLab(labname, newname):
	"""
	Given a lab, this function renames its textfile, and the selection,
	along with the labs	associated with the CRCs in that file to the new name
	"""
	dirname = os.path.dirname(__file__)
	fileloc = os.path.join(dirname, "labs/" + labname)
	# os.rename(labname, newname, src_dir_fd =  fileloc, dst_dir_fd = fileloc)	
def checkLab(labname):
	""" For internal use, check if a lab exists. True if it is, False if not"""
	if labname in getLabs():
		return(True)
	else:
		return(False)
def getLabs(file = "labs.txt"):
	""" 
	Returns an array of the labs currently under CLM management
	Labs are held in the local directory as labs.txt
	Should read file names instead
	"""
	dirname = os.path.dirname(__file__)
	file = os.path.join(dirname, file)
	lst = [] 
	with open(file) as file:
		for line in file:
			temp = line.rstrip()
			lst.append(temp)
	return(lst)

def genSheets():
	"""
	Code for how we will take information out of the text file, and create a sheet for each lab.
	Needs to take each lab in the list shown in the en3+try boxes, and then go through an organize all the entries in the text file.
	Might make a helper function, to organize by labs, or by quarter and year. 
	Either way, the value should be valid

	In the end, we should be taking a file. That file will hold all the information we need
	Start by grabbing all seperate lab groups, sort those based on year, then quarter.
	Afterwards, give that list to whatever is used to generate the pictures themselves.
	Might just tag everything else in it's own seperate file
	"""
	
	#for lab in labs:

	pass
print("Printing starts here")