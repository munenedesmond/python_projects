"""
Context
Given 2 elevators (named "left" and "right") in a building with 3 floors (numbered 0 to 2), write a function elevator accepting 3 arguments (in order)
Task
Given 2 elevators (named "left" and "right") in a building with 3 floors (numbered 0 to 2), write a function elevator accepting 3 arguments (in order):
1. left - The current floor of the left elevator
2. right - The current floor of the right elevator
3. call - The called floor, i.e. the floor you want to reach
It should return the name of the elevator closest to the called floor ("left"/"right").
In the case where both elevators are equally distant from the called floor, choose the elevator to the right.
You can assume that the inputs will always be valid integers between 0-2.
Examples:
elevator(0, 1, 0); // => "left" 
elevator(0, 1, 1); // => "right" 
elevator(0, 1, 2); // => "right" 
elevator(0, 0, 0); // => "right" 
elevator(0, 2, 1); // => "right"

"""

# elevator function
def elevator(left, right, call):
    if call == right == left:
        print("right")
    elif call == left:
        print("left")
    elif call < right - left > call:
        print("right")
    else:
        print("right")


elevator(0, 1, 0)
elevator(0, 1, 1)
elevator(0, 1, 2)
elevator(0, 0, 0)
elevator(0, 2, 1)
elevator(2, 1, 1)

#Output 
'''
left
right
right
right
right
right
'''
