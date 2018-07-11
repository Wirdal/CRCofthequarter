from tkinter import *
from tkinter import ttk
import plaque
"""This section holds the GUI code. It will execute commands help in plaque.py"""


class plaqueApp:
	""" 
	The layout is as follows, and a reference picture can be found at mockup.png
	
	Three frames
		1. For the addition of a singular CRC
		2. For the addition of a list of CRC's
		3. For generation of sheets
	"""

	def __init__(self, master):
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
			values = ("Admin", "HWS", "SciLab", "SCC", 
				"Sheilds", "MU", "Wellman", "Olson", "Hutchinson" ))
		self.entry_quarter = ttk.Combobox(self.frame_addCRC, width = 12, 
			values = ("Spring", "Summer", "Fall", "Winter"))
		self.entry_year = ttk.Entry(self.frame_addCRC, width = 15)
		self.entry_num = ttk.Entry(self.frame_addCRC, width = 15)
		# Submit Button
		self.button_submit1 = ttk.Button(self.frame_addCRC, text = "Submit", 
			command = self.submit1
			).grid(row = 3, column= 2, pady = 3, columnspan = 2, sticky = "n")
		# Placement
		# This needs to be done seperatly,
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
		self.button_submit2 = ttk.Button(self.frame_addList,
		command = self.submit2, text = "Submit"
		).grid(row = 3, column= 0, pady = 10)

		# THIRD FRAME
		self.frame_genSheets = ttk.Frame(master)
		self.frame_genSheets.grid(row = 3)
		# Button
		self.button_gensheets = ttk.Button(self.frame_genSheets, 
		text = "Generate Sheets", command = plaque.genSheets()
		).grid(row = 0, column= 0, pady = 20)

		# FOURTH FRAME
		self.frame_editLabs = ttk.Frame(master)
		self.frame_editLabs.grid(row = 2)
		# Labels
		ttk.Label(self.frame_editLabs, text = "Add Lab"
			).grid(row = 0, column = 0, padx = 10)
		ttk.Label(self.frame_editLabs, text = "Delete Lab"
			).grid(row = 0, column = 1, padx = 10)
		ttk.Label(self.frame_editLabs, text = "Rename Lab (To -> From)"
			).grid(row = 0, column = 2, padx = 10)
		# Textboxes
		self.entry_addLab = ttk.Entry(self.frame_editLabs, width = 15)
		self.entry_deleteLab = ttk.Entry(self.frame_editLabs, width = 15)
		self.entry_renameLab1 = ttk.Entry(self.frame_editLabs, width =15)
		self.entry_renameLab2 = ttk.Entry(self.frame_editLabs, width = 15)
		# Placement
		self.entry_addLab.grid(row = 1, column = 0, padx = 10)
		self.entry_deleteLab.grid(row = 1, column = 1, padx = 10)
		self.entry_renameLab1.grid(row = 1, column = 2, padx = 10, pady = 5)
		self.entry_renameLab2.grid(row = 2, column = 2, padx = 10, pady = 5)
		# Buttons
		self.button_addLab = ttk.Button(self.frame_editLabs, text = "Add Lab", 
			command = plaque.addLab(self.entry_addLab.get())
			).grid(row = 3, column= 0, pady = 5)
		self.button_deleteLab = ttk.Button(self.frame_editLabs, text = "Delete Lab", 
			command = plaque.removeLab(self.entry_deleteLab.get())
			).grid(row = 3, column= 1, pady = 5)
		self.button_renameLab = ttk.Button(self.frame_editLabs, text = "Rename Lab", 
			command = plaque.renameLab(self.entry_renameLab1.get(), self.entry_renameLab2.get())
			).grid(row = 3, column= 2, pady = 5)
	def submit1(self):
		"""Method for the first button, akin to adding a single CRC"""
		# Grabbing all the info from the boxes
		first = self.entry_first.get()
		last = self.entry_last.get()
		lab = self.entry_lab.get()
		quarter = self.entry_quarter.get()
		year = self.entry_year.get()
		num = self.entry_num.get()
		crc = plaque.CRC([first, last, lab, quarter, year, num])
		# Check if non-name fields are valid.
		if self.checkvalid():
			lab = lab + ".txt" #Add the extension for courtesy
			crc.addCRC(lab) #Write to that file
			self.entry_first.delete(0, "end")
			self.entry_last.delete(0, "end")
			self.entry_lab.delete(0, "end")
			self.entry_quarter.delete(0, "end")
			self.entry_year.delete(0, "end")
			self.entry_num.delete(0, "end")

	def submit2(self):
		"""Given a list, will add each entry in that list"""
		#Grab the info from the textbox
		filename = self.entry_filename.get()
		crcs = plaque.text2List(filename)
		for i in crcs:
			i.addCRC()
		filename = self.entry_filename.delete(0, "end")
		
	def checkvalid(self):
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
		if lab not in ("Admin", "HWS", "SciLab", "SCC", "Shields",
		"MU", "Wellman", "Olson", "Hutchinson" ):
			self.entry_lab.set("Invalid Lab")
			valid = False
		# Check the quarter
		if quarter not in ("Fall", "Spring", "Summer", "Winter"):
			self.entry_quarter.set("Invalid Quarter")
			valid = False
		# Check the year
		try:   
			int(year)
		except ValueError:
			self.entry_year.delete(0 , END)
			self.entry_year.insert(0, "Invalid Year") #Entry boxes themselves don't have the set() method. So we use insert
			valid = False
		# Check the ITLM number
		try:
			int(num)
		except ValueError:
			self.entry_num.delete(0 , END)
			self.entry_num.insert(0, "Invalid Number")
			valid = False
		return(valid)


def main():
	root = Tk()
	boop = plaqueApp(root)
	root.mainloop()

if __name__ == "__main__" :
	main()