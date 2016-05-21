# Design a modular program that asks the user to enter a distance in kilometers, and then converts that distance to miles. The conversion formula is as follows: Miles = kilometers x 0.6214
 

def userinput():
    kilometers = int(input("Please enter a distance in kilometers: "))
    return kilometers
    
def convert(kilometers):
    conv_to_miles = kilometers * 0.6214
    
def result(kilometers):
    print(kilometers + "is" + miles)
    
userinput()
convert()
result()