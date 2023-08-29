# create a function that takes the RGB values of a colour and converts it to the corresponding HEX value for that colour.
# the function should take 3 arguments, the red value, the green value and the blue value.

"""
Example:
rgbToHex(255, 255, 255) --> "FFFFFF"
rgbToHex(255, 255, 300) --> "FFFFFF"
rgbToHex(0, 0, 0)       --> "000000"
rgbToHex(148, 0, 211)   --> "9400D3"
""" 


def rgbToHex(red, green, blue):
    """this function converts RGB values into HEX values"""

    # we first ask the user for the input
    question1 = int(input('Please enter the RGB values: '))
    question2 = int(input('Please enter the second RGB value: '))
    question3 = int(input('Please enter the third RGB value: '))

    # raise error if the input is different
    if question1 & question2 & question3 < 0 or question1 & question2 & question3 > 255:
        raise Exception('Sorry, you have to enter a valid number')
    
    return f"{question1}, {question2}, {question3}"