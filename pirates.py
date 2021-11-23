"""
Context
Ahoy matey!
You are a leader of a small pirate crew. And you have a plan. With the help of OOP you wish to make a pretty efficient system to identify ships with a heavy booty on board.
Task
Ahoy matey!
You are a leader of a small pirate crew. And you have a plan. With the help of OOP you wish to make a pretty efficient system to identify ships with a heavy booty on board.
Unfortunately for you, people weigh a lot this days, so how do you know if a ship if full of gold and not people?
You begin with writing a generic Ship class:
class Ship: def __init__(self, draft, crew): self. Draft = draft self. Crew = crew
Every time your spies see a new ship enter the dock, they will create a new ship object based on their observations:
● draft - an estimate of the ship's weight based on how low it is in the water
● crew - the count of crew on board
Titanic = Ship (15, 10)
Taking into account that an average crew member on board adds 1.5 units to the draft, a ship that has a draft of more than 20 without crew is considered worthy to loot. Any ship weighing that much must have a lot of booty!
Add the method Is_worth_it to decide if the ship is worthy to loot. For example:
Titanic.is_worth_it()
> False


"""
#Code 

# ship class
class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew

    # is_worth_it method
    def is_worth_it(self):
        if self.draft - (self.crew * 1.5) >= 20:
            print(True)
        elif self.draft - (self.crew * 1.5) < 20:
            print(False)


Titanic = Ship(15, 10)
Premium = Ship(20, 0)

Titanic.is_worth_it()
Premium.is_worth_it()

#Output

False
True
