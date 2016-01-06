import time, datetime, os

class stats(object):

	filePath = os.path.dirname(__file__) + "/data/"

	def __init__(self):
		print("[W] Stats module initialized")
		return

	def printMenu(self):
		print("")
		print("[W] Choose from any option below")
		print("")
		print("[W] 1 - Show arrivals")
		print("[W] 9 - Print menu")
		print("[W] 0 - Quit")
		print("")
		return

	def loop(self):
		self.printMenu()
		x = int(input("Input number: "))
		while(x != 0):
			if(x == 1):
				self.printArrivals()
			elif(x == 9):
				self.printMenu()
			else:
				print("[W] Did nothing")

			x = int(input("Input number: "))

	def printArrivals(self):
		print("[W] Arrivals printed")
		return

