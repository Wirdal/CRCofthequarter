import os
import generator
"""Holds the "meat" for all the writing, reading, and generating"""


class CRC:
	"""
	Implemented as a way to shorten arguments, and because I thought it 
	was a smart idea at the time. Seems a little dumb now, but I might change it
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
		return("\n" + self.first 
			+ " " + self.last # All have spaces in between
			+ " " +self.lab 
			+ " " + self.quarter 
			+ " " +self.year 
			+ " " + self.num)

	def addCRC(self, filename):
		""" Adds a singular person to the text file. """
		 #Getting the relative path
		dirname = os.path.dirname(__file__)
		# Giving the path to the file that holds that lab
		fileloc = os.path.join(dirname, "labs", filename) 
		with open(fileloc, mode = "a") as file:
			file.write(self.formatString())

	def getLab(self):
		"""Getter for the lab"""
		return self.lab


def text2List(smFile):
	"""Takes a file with CRC info, and writes all info to the corresponding lab sheet"""
	with open(smFile) as file:
		crcs = []
		for line in file:
			# Take off enders
			temp = line.rstrip() 
			# Creates a list with each number
			temp = temp.split(sep = " ") 
			# Create an object with it, and throw it onto the list
			crcs.append(CRC(temp)) 
		# A list of objects, CRCs
		for i in crcs:
			i.addCRC(i.getLab())


def addLab(labname):
	"""Creates text file for lab. Returns true if creation occurred, false if not"""
	exists = checkLab(labname)
	if exists:
		return(False)
	else:
		dirname = os.path.dirname(__file__)
		fileloc = os.path.join(dirname, "labs", labname +".txt")
		with open(fileloc, mode = "x"): # Mode x means to create
			return(True)


def deleteLab(labname):
	"""Opposite of addLab"""
	exists = checkLab(labname)
	if exists:
		dirname = os.path.dirname(__file__)
		fileloc = os.path.join(dirname, "labs", labname +".txt")
		os.remove(fileloc)
		return(True)
	else:
		return(False)


def renameLab(labname, newname):
	"""
	Given a lab, this function renames its textfile, and the selection,
	along with the labs	associated with the CRCs in that file to the new name
	"""
	dirname = os.path.dirname(__file__)
	filelocOld = os.path.join(dirname, "labs", labname +".txt")
	filelocNew = os.path.join(dirname, "labs", newname +".txt")
	try:
		 os.rename(filelocOld, filelocNew)
	except:
		pass


def checkLab(labname):
	""" For internal use, check if a lab exists. True if is, False if not"""
	if labname in getLabs():
		return(True)
	else:
		return(False)


def getLabs():
	""" 
	Returns an array of the labs currently under CLM management
	Labs are held in the local directory as labs.txt
	Should read file names instead
	"""
	dirname = os.listdir("labs\\")
	lablist = []
	for i in dirname:
		lablist.append(i.rstrip(".txt"))
	return(lablist)


def genSheets():
	"""
	Reads the info from the text files, and generates the sheets by
	using tkinter methods. Primarily canvas. Can be changed to 
	change number of CRCs grabbed from the text file.
	Generates all.
	"""
	lablist = os.listdir("labs\\")
	for lab in lablist:
		dirname = os.path.dirname(__file__)
		fileloc = os.path.join(dirname, "labs", lab)
		# Grab the 10 most recent entries for each lab
		# The one at the front of the list will be the first
		# Call the function with those entries
		# It technically grabs the 10 most recent additions to the text file.
		with open(fileloc, mode = "r") as file:
			crclist = []
			for line in reversed(file.readlines()):
				# Change this line if you want a different number of CRCs
					# Start the actual window that will generate
				line = line.rstrip("\n")
				crclist.append(line)
			generator.generator(crclist = crclist[:10])
#genSheets()