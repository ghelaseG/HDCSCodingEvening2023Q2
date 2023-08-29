# create a function that takes the RGB values of a colour and converts it to the corresponding HEX value for that colour.
# the function should take 3 arguments, the red value, the green value and the blue value. 


def rgbToHex(red, green, blue):
    """this function converts RGB values into HEX values"""
    question1 = input('Please enter the the RGB values: ')
    question2 = input('Please enter the second RGB value: ')
    question3 = input('Please enter the third RGB value: ')
    if question1 & question2 & question3 < 0 or question1 & question2 & question3 > 1000:
        raise Exception('Sorry, you have to enter a valid number')