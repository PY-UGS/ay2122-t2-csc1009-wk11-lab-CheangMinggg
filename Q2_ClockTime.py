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

    while True:
        try:
            h = int(input("Enter hours in 24h format (value 0-23): "))
            if h >= 0 and h <= 23:  #  make sure in the correct 24hr format for hours (0-23)
                break
            print("Incorrect Format!")
        except Exception as e:
            print(e)

    while True:
        try:
            m = int(input("Enter minutes in 24h format (value 0-59): ")) 
            if m >= 0 and m <= 59:  # make sure in the correct 24hr format for minutes (0-59)
                break
            print("Incorrect Format!")
        except Exception as e:
            print(e)

    while True:
        try:
            s = int(input("Enter seconds in 24h format (value 0-59): "))
            if s >= 0 and s <= 59:  #  make sure in the correct 24hr format for seconds (0-59)
                break
            print("Incorrect Format!")
        except Exception as e:
            print(e)


    clock.setTime(h, m, s)
    clock.showTime()

if __name__ == "__main__":
    main()