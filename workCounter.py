import time, os

class workCounter(object):

	##
	#
	# Local variable
	#
	##
	date = -1;
	filePath = "./data/"
	fileExtension = ".txt"
	fileDest = False

	fileArrival = "arrival"
	f = False
	timeSpent = 0

	debug = False

	def __init__(self, debug = 0):
		self.date = time.strftime("%Y_%m_%d")
		# Enabling debugging
		self.debug = True if debug == 1 else False
		return

	def run(self):
		if (self.date == -1):
			return

		self.createFile()
		self.work()
		return

	def createFile(self):
		# Assuming date is correct
		self.fileDest = self.filePath + self.date + self.fileExtension;

		# Creating arrival document
		# Must be created first, to check if arrival already exists in system
		fileArrivalDest = self.filePath + self.fileArrival + self.fileExtension;
		if(os.path.exists(fileArrivalDest)):
			# everything is ok, that's the way it should be..
			if not (os.path.exists(self.fileDest)):
				# if not exists, add line with arrival
				self.f = open(fileArrivalDest, "a+")
				self.f.write(self.date + " " + time.strftime("%H:%M") + "\n")
				self.f.close()
		else:
			# create file if there is no
			self.f = open(fileArrivalDest, "w")
			self.f.write(self.date + " " + time.strftime("%H:%M") + "\n")
			self.f.close()

		self.f = False

		# Creating time counting document
		if (os.path.exists(self.fileDest)):
			self.f = open(self.fileDest, "r")
			try:
				self.timeSpent = int(self.f.readline().rstrip())
			except Exception:
				self.timeSpent = 0
		else:
			self.f = open(self.fileDest, "w")
		self.f.close()

		self.f = False

		return

	def work(self):
		# Debug
		i = False
		if(self.debug):
			i = 1

		while(1 if self.debug == True else i < 10):
			time.sleep(1 if self.debug else 60) # if debug sleep = 1, otherwise sleep correctly 60 secs
			self.timeSpent += 1 # add 1 minute
			if (self.debug):
				print(self.timeSpent)
			self.f = open(self.fileDest, "w")
			self.f.truncate()
			self.f.write(str(self.timeSpent))
			self.f.close()

			if(self.debug):
				i += 1

v = workCounter()
v.run()