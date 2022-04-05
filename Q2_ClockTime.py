class clockTime: # 24 hour format

    hours = 0
    minutes = 0
    seconds = 0

    def setHours(self,h): #hour

        self.hours = h

    def setMinutes(self,m): #minutes

        self.minutes=m

    def setSeconds(self,s): #seconds

        self.seconds=s

    def setTime(self,h,m,s): 
        
        self.hours=h
        self.minutes=m
        self.seconds=s

    def showTime(self): #display

        print(self.hours,":",self.minutes,":",self.seconds)

def main():
    # main
    clock = clockTime()

    input_hours= -1
    input_min = -1
    input_seconds = -1

    while input_hours < 0 or input_hours >23:

        input_hours = int(input("Enter in hours: "))

    while input_min < 0 or input_min > 59:

        input_min = int(input("Enter in minutes: "))

    while input_seconds < 0 or input_seconds > 59:

        input_seconds = int(input("Enter in seconds: "))

    clock.setTime(input_hours,input_min,input_seconds)
    clock.showTime()



if __name__ == "__main__":
    main()
