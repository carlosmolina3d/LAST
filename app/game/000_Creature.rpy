# Controlled by AI or Player

init python:
    class Creature(object):
        # Tuple of random names
        names = (
        'Katie', 'Lucy', 'Lilly', 'Sara', 'Anna', 'Leah', 'Star', 'Cheryl', 'Tara',
        'Cybele', 'Artemis', 'Lara', 'Amy', 'Kelly', 'Kimberly', 'Kim', 'Maria',
        'Susan', 'Ashley', 'Carly', 'Michelle', 'Candy', 'Danielle', 'Gwen', 'Heather',
        'Ivana', 'Jill', 'Nancy', 'Pearl', 'Queen', 'Rima', 'Ursula', 'Viola',
        'Wendy', 'Xena', 'Zara'
        )

        # Properties

        # Constructor
        def __init__(self):
            self.name = ''
            self.job = ''
            self.character = Character(self.name, image='')

        def setName(self, name):
            # String -> None
            self.name = name

        def getName(self):
            # None -> String
            return self.name

        def setJob(self, job):
            # Job -> None
            self.job = job

        def getJob(self):
            # None -> Job
            return self.job

        def autoNamer(self):
            self.name = renpy.random.choice(self.names)
