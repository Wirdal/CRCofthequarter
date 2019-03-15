from tkinter import *
from tkinter import ttk
import labs
"""This section holds the GUI code. It will execute commands help in labs.py"""


class plaqueApp:

	def __init__(self, master):
		""" 
		The layout is as follows, and a reference picture can be found at mockup.png
		
		Four frames
			1. For the addition of a singular CRC
			2. For the addition of a list of CRC's
			3. For lab specific operations
			4. For generating sheets
		"""

		# Making the titlebar, and forcing un-resizabliltiy
		master.title("CRC of the Quarter")
		master.resizable(False, False)

		# FIRST FRAME

		self.frame_addCRC = ttk.Frame(master)
		self.frame_addCRC.grid(row = 0)

		# Labels

		ttk.Label(self.frame_addCRC, text = "ADD CRC"
			).grid(row = 0, column = 2, pady = 10 , columnspan = 2, sticky = "n")

		ttk.Label(self.frame_addCRC, text = "First"
			).grid(row = 1, column = 0,  padx = 10)

		ttk.Label(self.frame_addCRC, text = "Last"
			).grid(row = 1, column = 1,  padx = 10)

		ttk.Label(self.frame_addCRC, text = "Lab"
			).grid(row = 1, column = 2,  padx = 10)

		ttk.Label(self.frame_addCRC, text = "Quarter"
			).grid(row = 1, column = 3,  padx = 10)

		ttk.Label(self.frame_addCRC, text = "Year"
			).grid(row = 1, column = 4,  padx = 10)
			
		ttk.Label(self.frame_addCRC, text = "ITLM Number"
			).grid(row = 1, column = 5,  padx = 10)

		# Textboxes

		self.entry_first = ttk.Entry(self.frame_addCRC, width = 15)

		self.entry_last = ttk.Entry(self.frame_addCRC, width = 15)

		self.entry_lab = ttk.Combobox(self.frame_addCRC, width = 12, 
			values = labs.getLabs(), postcommand = self.labUpdate)

		self.entry_quarter = ttk.Combobox(self.frame_addCRC, width = 12, 
			values = ("Spring", "Fall", "Winter"))

		self.entry_year = ttk.Entry(self.frame_addCRC, width = 15)

		self.entry_num = ttk.Entry(self.frame_addCRC, width = 15)

		# Submit Button

		ttk.Button(self.frame_addCRC, text = "Submit", command = self.submit1
			).grid(row = 3, column= 2, pady = 3, columnspan = 2, sticky = "n")

		# Placement

		# This needs to be done separately,
		# or else the variable will hold a none type, which would not
		# allow us to access its field.
		self.entry_first.grid(row = 2, column = 0,  padx = 10)

		self.entry_last.grid(row = 2, column = 1,  padx = 10)

		self.entry_lab.grid(row = 2, column = 2,  padx = 10 , pady =10)

		self.entry_quarter.grid(row = 2, column = 3,  padx = 10)

		self.entry_year.grid(row = 2, column = 4,  padx = 10)

		self.entry_num.grid(row = 2, column = 5, padx = 10)

		# SECOND FRAME
	
		self.frame_addList = ttk.Frame(master)
		self.frame_addList.grid(row = 1)

		# Labels

		ttk.Label(self.frame_addList, text = "ADD FROM LIST"
			).grid(row = 0, column = 0, pady = 5 , sticky = "ns")

		ttk.Label(self.frame_addList, 
			text = "Filename. Must be a text file. Include extension"
			).grid(row = 1, column = 0, sticky = "s")

		# Textbox

		self.entry_filename = ttk.Entry(self.frame_addList, width = 30)

		# Placement

		self.entry_filename.grid(row = 2, column = 0, columnspan = 5)

		ttk.Button(self.frame_addList, command = self.submit2, text = "Submit"
		).grid(row = 3, column= 0, pady = 10)

		# THIRD FRAME
	
		self.frame_editLabs = ttk.Frame(master)
		self.frame_editLabs.grid(row = 2)

		# Labels
	
		ttk.Label(self.frame_editLabs, text = "Add Lab"
			).grid(row = 0, column = 0, padx = 6)

		ttk.Label(self.frame_editLabs, text = "Delete Lab"
			).grid(row = 0, column = 1, padx = 6)

		ttk.Label(self.frame_editLabs, text = "Rename Lab (To -> From)"
			).grid(row = 0, column = 2, padx = 6)

		# Textboxes

		self.entry_addLab = ttk.Entry(self.frame_editLabs, width = 15)

		self.entry_deleteLab = ttk.Combobox(self.frame_editLabs, width = 12, 
			values = labs.getLabs(), postcommand = self.labUpdate)

		self.entry_renameLab1 = ttk.Combobox(self.frame_editLabs, width = 12, 
			values = labs.getLabs(), postcommand = self.labUpdate)

		self.entry_renameLab2 = ttk.Entry(self.frame_editLabs, width = 15)

		# Placement

		self.entry_addLab.grid(row = 1, column = 0, padx = 10)

		self.entry_deleteLab.grid(row = 1, column = 1, padx = 10)

		self.entry_renameLab1.grid(row = 1, column = 2, padx = 10, pady = 5)
		
		self.entry_renameLab2.grid(row = 2, column = 2, padx = 10, pady = 5)

		# Buttons

		ttk.Button(self.frame_editLabs, text = "Add Lab", command = self.addLab
			).grid(row = 3, column= 0, pady = 5)

		ttk.Button(self.frame_editLabs, text = "Delete Lab", command = self.deleteLab
			).grid(row = 3, column= 1, pady = 5)

		ttk.Button(self.frame_editLabs, text = "Rename Lab", command = self.renameLab
			).grid(row = 3, column= 2, pady = 5)


		# FOURTH FRAME

		self.frame_genSheets = ttk.Frame(master)
		self.frame_genSheets.grid(row = 3)

		# Button

		ttk.Button(self.frame_genSheets, text = "Generate Sheets", 
			command = labs.genSheets
			).grid(row = 0, column= 0, pady = 20)

		#TODO Add box that displays the exact values for a certain text file
		# Possibly display a preview?

	def submit1(self):
		"""Method for the first button, akin to adding a single CRC"""
		# Grabbing all the info from the boxes
		first = self.entry_first.get()
		last = self.entry_last.get()
		lab = self.entry_lab.get()
		quarter = self.entry_quarter.get()
		year = self.entry_year.get()
		num = self.entry_num.get()
		crc = labs.CRC([first, last, lab, quarter, year, num])
		# Check if non-name fields are valid.
		if self.checkvalidsubmit1():
			lab = lab + ".txt" #Add the extension for courtesy
			# We need to do the check for more than one word per first/last here.
			# Well, we don't need to check, we can just replace all instances of
			first = first.replace(" ", "/")
			last = last.replace(" ", "/")
			# Generator will take care of removing them
			crc.addCRC(lab) #Write to that file
			self.entry_first.delete(0, "end")
			self.entry_last.delete(0, "end")
			self.entry_lab.delete(0, "end")
			self.entry_quarter.delete(0, "end")
			self.entry_year.delete(0, "end")
			self.entry_num.delete(0, "end")

	def submit2(self):
		"""Given a list, will add each entry in that list"""
		# Grab the info from the textbox
		filename = self.entry_filename.get()
		labs.text2List(filename)
		self.entry_filename.delete(0, "end")
	
	def addLab(self):
		"""Clears the entry box, then calls the lab function"""
		labname = self.entry_addLab.get()
		labs.addLab(labname)
		self.entry_addLab.delete(0, "end")
		self.entry_lab.delete(0, "end")


	def deleteLab(self):
		"""Clears the entry box, then calls the lab function"""
		labname = self.entry_deleteLab.get()
		if self.validlab(delete = True):
			labs.deleteLab(labname)
			self.entry_deleteLab.delete(0, "end")
			self.entry_lab.delete(0, "end")
		else:
			self.entry_deleteLab.delete(0, "end")
			self.entry_deleteLab.insert(0, "Invalid Lab")
	
	def renameLab(self):
		"""Clears the entry box, then calls the lab function"""
		oldname = self.entry_renameLab1.get()
		newname = self.entry_renameLab2.get()
		if self.validlab(rename = True):
			labs.renameLab(oldname, newname)
			self.entry_renameLab1.delete(0, "end")
			self.entry_renameLab2.delete(0, "end")
			self.entry_lab.delete(0, "end")
		else:
			self.entry_renameLab1.delete(0, "end")
			self.entry_renameLab1.insert(0, "Invalid Lab")
	
	def validlab(self, rename = False, delete = False, add = False):
		""" Will check if the labs in the add,remove, and rename are legal"""
		add = self.entry_addLab.get()
		delete = self.entry_deleteLab.get()
		rename = self.entry_renameLab1.get()
		valid = True
		lab = labs.getLabs()
		if add:
			if add not in lab:
				valid = False
		if delete:
			if delete not in lab:
				valid = False
		if rename:
			if rename not in lab:
				valid = False
		return(valid)

	def checkvalidsubmit1(self):
		"""
		Checks to see if the Lab, Quarter, and year are valid answers.
		If not, it replaces the field with a notice saying such.
		"""
		lab = self.entry_lab.get()
		quarter = self.entry_quarter.get()
		year = self.entry_year.get()
		num = self.entry_num.get()
		valid = True
		# Check the lab
		if lab not in labs.getLabs():
			self.entry_lab.set("Invalid Lab")
			valid = False
		# Check the quarter
		if quarter not in ("Fall", "Spring", "Winter"):
			self.entry_quarter.set("Invalid Quarter")
			valid = False
		# Check the year
		try:   
			int(year)
		except ValueError:
			self.entry_year.delete(0 , END)
			#Entry boxes themselves don't have the set() method. So we use insert
			self.entry_year.insert(0, "Invalid Year") 
			valid = False
		# Check the ITLM number
		try:
			int(num)
		except ValueError:
			self.entry_num.delete(0 , END)
			self.entry_num.insert(0, "Invalid Number")
			valid = False
		return(valid)

	def labUpdate(self):
		val = labs.getLabs()
		self.entry_lab["values"] = val
		self.entry_renameLab1["values"] = val
		self.entry_deleteLab["values"] = val


def main():
	root = Tk()
	plaqueApp(root)
	root.mainloop()

if __name__ == "__main__" :
	main()