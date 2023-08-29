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
    red = int(input('Please enter the RGB values: '))
    green = int(input('Please enter the second RGB value: '))
    blue = int(input('Please enter the third RGB value: '))

    # raise error if the input is different
    if red & blue & green < 0 or red & blue & green > 255:
        raise Exception('Sorry, you have to enter a valid number')
    
    RGB = f"{red}, {green}, {blue}"

    # to return the right hexadecimal values, we have to use the following formula in 'return ...'
    """
    Given RGB values, where all three are 0-255 (0, 0, 0 being black and 255, 255, 255 being white),
    use the equation: R/16 = x + y/16. G/16 = x' + y'/16. B/16 = x" + y"/16.
    """
    return RGB//16 =  x + y//16