import time, datetime, os, sys

class stats(object):

    filePath = os.path.dirname(__file__) + "/data/"
    extension = ".txt"

    def __init__(self):
        print("[W] Stats module initialized")
        return

    def minutesToString(self, minutes = 0):
        return str(int(minutes / 60)) + " hours " + str(int(minutes % 60)) + " minutes"

    def lastDayOfMonth(self, any_day = False):
        if(any_day == False):
            any_day = datetime.datetime.now()

        next_month = any_day.replace(day=28) + datetime.timedelta(days=4)  # this will never fail
        return next_month - datetime.timedelta(days=next_month.day)

    def printMenu(self):
        print("")
        print("[W] Choose from any option below")
        print("")
        print("[W] 1 - Show arrivals [Current]")
        print("[W] 2 - Worktime [Current]")
        print("[W] 3 - Show arrivals [Pick a month]")
        print("[W] 4 - Worktime [Pick a month]")
        print("[W] 9 - Print menu")
        print("[W] 0 - Quit")
        print("")
        return

    def loop(self):
        self.printMenu()
        try:
            x = int(self.ipt("Input number: "))
        except ValueError:
            x = 9

        while(x != 0):
            if(x == 1):
                self.printArrivals()
            elif(x == 2):
                self.printMonthWorktime()
            elif(x == 3):
                self.printArrivalsChosen()
            elif(x == 4):
                self.printMonthWorktimeChosen()
            elif(x == 9):
                self.printMenu()
            else:
                print("[W] Did nothing")

            try:
                x = int(self.ipt("Input number: "))
            except ValueError:
                x = 9

    def printArrivals(self, yearMonthString = False):
        if(yearMonthString == False):
            yearMonthString = datetime.datetime.now().strftime("%Y_%m")

        destination = self.filePath + "arrivals/arrival_" + yearMonthString + self.extension

        if(not os.path.exists(destination)):
            print("[W] No data present for month %s" % str(yearMonthString))
            return

        f = open(destination)
        for line in f:
            print ("%s" % str(line).rstrip())

        print("[W] Arrivals printed")
        return

    def printMonthWorktime(self, yearMonthString = False):

        if(yearMonthString == False):
            yearMonthString = datetime.datetime.now().strftime("%Y_%m")

        destination = self.filePath + yearMonthString
        if(not os.path.exists(destination)):
            print("[W] No data present for month %s" % str(yearMonthString))
            return

        worktimeDays = {}

        day = 1
        for i in range(1, int(self.lastDayOfMonth().day) + 1):
            day = "{0:02d}".format(i)
            worktimeDays[yearMonthString + "_" + day] = 0


        f = False
        worktime = 0
        totalWorktime = 0
        for file in sorted(os.listdir(destination)):
            if file.endswith(".txt"):
                f = open(destination + "/" + file, "r")
                worktime = int(f.readline().rstrip())
                # print(str(file).replace(".txt", ""))
                # print(str(worktime))
                worktimeDays[str(file).replace(".txt", "")] = worktime
                totalWorktime += worktime
                f.close()
                # print(file)

        print("[W] Printing worktime for date: %s " % yearMonthString )

        hourMinutes = ""
        minutes = 0
        day = ""
        for key in sorted(worktimeDays):
            minutes = worktimeDays[key]
            hourMinutes = self.minutesToString(minutes)
            day = str(key).replace(str(yearMonthString) + "_", "")
            if(minutes == 0):
                print("%s: [ 0 ] Not arrived" % day)
            else:
                print ("%s: [ %d ] %s" % (day,minutes / 60, hourMinutes))

        print("[W] [ %d ] Total worktime this month: %s" % (totalWorktime / 60, self.minutesToString(totalWorktime)))

    def printArrivalsChosen(self):
        # date = str(raw_input("Input date (YYYY_MM): "))
        date = str(self.ipt("Input date (YYYY_MM):")).strip()
        self.printArrivals(date)
        return

    def printMonthWorktimeChosen(self):
        date = str(self.ipt("Input date (YYYY_MM):")).strip()
        self.printMonthWorktime(date)
        return

    def ipt(self, pretext = ""):
        print(pretext)
        return sys.stdin.readline()
