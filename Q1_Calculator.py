class Calculator:
    input1 = 0
    input2 = 0

    def __init__(self,input1,input2):
        self.input1 = input1
        self.input2 = input2
    
    def adder(self): # addition method
        return self.input1+self.input2
    
    def subtracter(self): # substraction method
        return self.input1-self.input2
    
    def multiplier(self): # multiplication method
        return self.input1*self.input2

    def divider(self):     # division method
        return self.input1/self.input2
       
    def clear(self):  # clear 
        self.input1 = 0
        self.input2 = 0


def main(): # main
    num1 = int(input("Key in number 1: "))
    num2 = int(input("Key in number 2: "))

    cal = Calculator(num1,num2)

    print("Addition: ",cal.adder())
    print("Subtraction:",cal.subtracter())
    print("Mutliplication: ",cal.multiplier())
    print("Division:",cal.divider())
    
    cal.clear()

if __name__ == "__main__":
    main()