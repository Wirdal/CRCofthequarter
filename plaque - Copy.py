#Start by opening the file. r is for reading only
#The file is ordered by First-last-lab-quarter-year, where the lines are spaces, which will be the delimiterss

#A class, meant to handle the data taken from the text file.
class CRC:
    def __init__(self, first, last, lab, quarter, year):
        self._first = first
        self._last = last
        self._lab = lab
        self._quarter = quarter
        self._year = year

    def construct(filename):
        with open(filename) as file:
            for line in file :
                continue
            
#with open('test.txt') as file:
    #https://docs.python.org/3/library/stdtypes.html#str.splitlines
    #https://docs.python.org/3/library/functions.html?highlight=open#open
    #Will end with a newline character. We can shave this off by force, or find a built in fn.
    #print(file.readline().split(sep=' '))


    
#Ignore the following, Joseph is still learning python.
imageFile = 'Chloe_Parini_SCC_Fall_2017.jpg'
def listFromName(filename):
    """Takes filename, cuts off file extension, and separates each word to a list."""
    removedExtension = filename.split('.')
    del removedExtension[1]
    return(removedExtension[0].split('_')) 

