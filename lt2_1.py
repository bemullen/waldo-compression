# lt2_1.py
# author = brooke mullen

import sys

class Waldo():

	def __init__(self, file):
		self.message = ''
		self.file = file
		self.index = 0 # our seek
		self.waldo = 'waldo'
		self.block = 50000
		self.add = 0

	def finder(self):
		
		f = open(self.file)
		while True:
			self.message = f.read(self.block)
			if (self.message == ""):
				f.close()
				break
			leng = len(self.message)
			while (self.index < leng):
				k = self.message.find(self.waldo, self.index)
				if(k!=-1):
					x = k + self.add
					print("Found Waldo @ " + str(x))
					self.index = x + 1
				if(k==-1):
					break
			self.index = 0
			self.add += self.block
			self.add -= 4
			f.seek(self.add)

first_arg = sys.argv[1]
#first_arg = 'test1.txt'
#first_arg = 'lt2_2.txt'
			
def main(thefile=first_arg):
	where_is_waldo = Waldo(thefile)
	where_is_waldo.finder()

if __name__ == "__main__":
    main()
# waldo-compression
