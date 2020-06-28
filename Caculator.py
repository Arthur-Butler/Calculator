#importing system utils to use to exit program
import sys
#Declaring class to be called in GUI function later
class Calculator:
    #Constructor initialising instances
    def __init__(self,Input,ValueArray):
        self.Input=Input
        self.ValueArray=ValueArray
    #functions used to calculate    
    def multiplication(self):
       result=1
       for i in range(len(self.ValueArray)):
            result=result*int(self.ValueArray[i])
       print("Answer: "+str(result))
    
    def subtraction(self):
        result=int(self.ValueArray[0])+int(self.ValueArray[0])
        for i in range(len(self.ValueArray)):
            result=result-int(self.ValueArray[i])
        print("Answer: "+str(result))
    
    def addition(self):
        result=int()
        for i in range(len(self.ValueArray)):
            result=result+int(self.ValueArray[i])
        print("Answer: "+str(result))
    
    def division(self):
        result=int(self.ValueArray[0])*int(self.ValueArray[0])
        for i in range(len(self.ValueArray)):
            result=result/int(self.ValueArray[i])
        print("Answer: "+str(result))
def Clear():
    Option=input("If error, type 'Clear' to restart or 'Next' to continue")
    if Option[0]=="C" or Option[0]=="c":
        GUI()
#GUI function
def GUI():
    #Choice between functions
    User_input=input("Choose function. Choose between multiplication, addition, subtraction and division:")
    Clear()
    #Input asking how many values the user would like to process
    NoNumbers=int(input("Enter number of values to be processed:"))
    Clear()
    #Array containing user values
    ValueContainer=[]
    for i in range(NoNumbers):
        Value=input("Enter required value as integer:")
        ValueContainer.append(Value)
    x=Calculator(User_input, ValueContainer)
    #If statement used to carry bout users choice and call corresponding function from function class
    if User_input[0]=="m" or User_input[0]=="M":
        x.multiplication()
    if User_input[0]=="s" or User_input[0]=="S":
        x.subtraction()
    if User_input[0]=="a" or User_input[0]=="A":
        x.addition()
    if User_input[0]=="d" or User_input[0]=="D":
        x.division()
    #Option to either exit or start again
    Option=input("Type 'Next' to proceed and 'Exit' to close")
    if Option[0]=="N" or Option[0]=="n":
        GUI()
    else:
        sys.exit()
#Printing greeting
print("Welcome to Calculator!")
#Option to either exit or start again
Option=input("Type 'Next' to proceed and 'Exit' to close")
if Option[0]=="N" or Option[0]=="n":
    GUI()
else:
    sys.exit()
