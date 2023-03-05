def circle_area(diameter = 3):
    '''A function that calculates the area of a circle given the diameter'''
    pi = 3.14159 # approximate
    
    # TODO:
    # Create a variable called 'radius' equal to half the diameter
    # Create a variable called 'area', using the formula for the area of a circle: pi times the radius squared
    # Be sure to return the 'area'

    # YOUR CODE HERE
    radius = diameter/2
    area = pi*radius*radius

    
    print(area)
def main():
    circle_area(10)
main()