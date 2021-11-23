'''
RobinHood
Context
A hero is on his way to the castle to complete his mission. However, he's been told that the castle is surrounded with a couple of powerful dragons! each dragon takes 2 bullets to be defeated, our hero has no idea how many
Task
A hero is on his way to the castle to complete his mission. However, he's been told that the castle is surrounded with a couple of powerful dragons! each dragon takes 2 bullets to be defeated, our hero has no idea how many bullets he should carry.
Assuming he's gonna grab a specific given number of bullets and move forward to fight another specific given number of dragons, will he survive?
Return True if yes, False otherwise :).


'''
#Code 

# survival function
def survival(dragons, bullets):
    # each dragon requires two thus bullets have to be twice the No of dragons
    if bullets >= (2 * dragons):
        print(True)
    else:
        print(False)


survival(5, 10)
survival(10, 5)

#Output

True
False
