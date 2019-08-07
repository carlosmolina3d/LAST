# Globals in renpy
# Need to make classes. This is a test only.

init python:
    crew = {1:None, 2:None, 3:None, 4:None, 5:None, 6:None}

    # For each name in the tuple, define var = Character("Name", other values), then add it characters tuple.
    # names = ('Katie', 'Lucy', 'Lilly', 'Sara', 'Anna', 'Leah')
    # characters = ()
    #
    # job = 'Jobless'

    test = Creature()
    test.setName(renpy.random.choice(test.names))

    
