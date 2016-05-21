# Design a modular program that asks the user to enter a distance in kilometers, and then converts that distance to miles. The conversion formula is as follows: miles = kilometers x 0.6214

def main():
    kilometers = float(input("Please enter a distance in kilometers to be converted to miles: "))
    convert_to_kilo(kilometers)
    
def convert_to_kilo(user_kilometers):
    """
    convert_to_kilo accepts exaclty one value (user_kilometers), converts it to miles and then prints the result.
    """
    miles = (user_kilometers * 0.6214)
    print(miles, "miles")
    
main()