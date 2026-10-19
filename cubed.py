# Kentavious Mack, Use this as a file to practice code you cannot understand
#Find the volume of cube

#Purpose: Finding the volume of cube
# @param Sidelength the length of a side of a cube
# @return volumeOfCube the function will calculate the volume based on the sidelength provided and return the cube volume

def cubeVolume(sideLength) :
    volume = sideLength ** 3
    return volume

#Purpose: This is the main function. The code will start from here.
# @param None
# @return None

def main() :
    sideLength = int(input("Enter the side length of cube: "))
    result = cubeVolume(sideLength)
    print(result)

main()