import time, os

class workCounter(object):

	##
	#
	# Local variable
	#
	##
	date = False;
	filePath = "./data/"
	fileExtension = ".txt"
	fileDest = False

	fileArrival = "arrival"
	f = False
	timeSpent = 0

	debug = False

	##
	#	Constructor
	##
	def __init__(self, debug = 0):
		self.date = time.strftime("%Y_%m_%d")
		# Enabling debugging
		self.debug = True if debug == 1 else False
		return

	##
	# Responsible for running whole app
	##
	def run(self):
		if (self.date == False):
			return

		self.createFile()
		self.work() # this  puts everything on hold. because of infinite loop
		return

	##
	# Creates both files, current date file and populates arrival txt.
	##
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

	##
	# Does all the hard work
	##
	def work(self):
		# Debug additional features
		i = False
		if(self.debug):
			i = 1

		while(1 if self.debug == True else i < 10):
			time.sleep(1 if self.debug else 60) # if debug sleep = 1, otherwise sleep correctly 60 secs
			self.timeSpent += 1 # add 1 minute

			if (self.debug):
				print(self.timeSpent)

			# opens file, rewrites it with current minutes
			# and closes file,
			# waits another 60 seconds
			self.f = open(self.fileDest, "w")
			self.f.truncate()
			self.f.write(str(self.timeSpent))
			self.f.close()

			if(self.debug):
				i += 1

v = workCounter()
v.run()