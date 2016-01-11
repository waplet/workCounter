import time, datetime, os

class workCounter(object):

	##
	#
	# Local variable
	#
	##
	date = False;
	filePath = os.path.dirname(__file__) + "/data/"
	fileExtension = ".txt"
	fileDest = False

	fileArrival = "arrival"
	f = False
	timeSpent = 0
	timeSpentStart = 0
	dateStart = False;

	debug = False

	##
	#	Constructor
	##
	def __init__(self, debug = 0):
		self.date = time.strftime("%Y_%m_%d")
		self.dateStart = datetime.datetime.now()
		# Enabling debugging
		self.debug = True if debug == 1 else False

		print("[W] Work counter has been initiated")
		return

	##
	# Responsible for running whole app
	##
	def run(self):
		if (self.date == False):
			return

		print("[W] Work counter has been run")
		self.createFile()
		self.work() # this  puts everything on hold. because of infinite loop
		return

	##
	# Creates both files, current date file and populates arrival txt.
	##
	def createFile(self):
		# Assuming date is correct
		currentDate = datetime.datetime.now()

		self.fileDest = self.filePath + currentDate.strftime("%Y_%m") + "/" + self.date + self.fileExtension;

		# Creating arrival document
		# Must be created first, to check if arrival already exists in system
		fileArrivalDest = self.filePath + self.fileArrival + "_" + str(currentDate.year) + "_" + currentDate.strftime("%m") + self.fileExtension

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
				self.timeSpentStart  = self.timeSpent
			except Exception:
				self.timeSpent = 0
			print("[W] You have already arrived today")
		else:
			if(not os.path.exists(os.path.dirname(self.fileDest))):
				os.makedirs(os.path.dirname(self.fileDest))
			self.f = open(self.fileDest, "w")
			print("[W] Arrival at %s " % time.strftime("%Y-%m-%d %H:%M"))
		self.f.close()

		self.f = False


		print("[W] Files has been created")
		return

	##
	# Does all the hard work
	##
	def work(self):
		# Debug additional features
		i = False
		if(self.debug):
			i = 1

		while(1 if self.debug == False else i < 10):
			time.sleep(1 if self.debug else 60) # if debug sleep = 1, otherwise sleep correctly 60 secs

			if (self.debug):
				print(self.timeSpent)

			# recalculate time after hours
			if(self.timeSpent % 60 == 0):
				if(self.dateStart):
					diff = datetime.datetime.now() - self.dateStart
					diffSeconds = int(diff.total_seconds())
					diffMinutes = diffSeconds / 60

					if(self.debug):
						self.timeSpent = self.timeSpentStart + diffSeconds
					else:
						self.timeSpent = self.timeSpentStart + diffMinutes

			# opens file, rewrites it with current minutes
			# and closes file,
			# waits another 60 seconds
			self.timeSpent += 1 # add 1 minute
			self.f = open(self.fileDest, "w")
			self.f.truncate()
			self.f.write(str(self.timeSpent))
			self.f.close()

			print("[W] [%s] %d hours %d minutes have been spent today totally" % (time.strftime("%Y-%m-%d %H:%M"), int(self.timeSpent / 60), self.timeSpent % 60) )

			if(self.debug):
				i += 1

	# # not used by now
	# def monthdelta(self, date, delta):
	# 	m, y = (date.month+delta) % 12, date.year + ((date.month)+delta-1) // 12
	# 	if not m: m = 12
	# 	d = min(date.day, [31,29 if y%4==0 and not y%400==0 else 28,31,30,31,30,31,31,30,31,30,31][m-1])
	#     	return date.replace(day=d,month=m, year=y)