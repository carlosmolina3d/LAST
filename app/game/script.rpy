# The 7th saga
# FTL

label start:
    # Init objects in 000_Objects.rpy first
    # Multiple random starts
    # pick a Random start() from an array

    # Ask if they want to play story mode or make a custom crew


    #########################################
    # Tests
    #########################################

    'This is the pre start testing.'

    # '[will only get attributes. Not run functions]'

    # Need to name the Characters. Can't autoname them in init.
    $ test.autoNamer()

    # speakers name, grabbing a variable
    '[test.name]' 'My name is [test.name]'

    # speakers name using a method
    '[test.name]' 'My name is method [test.getName]'





    #########################################
    # Works!!!!
    #########################################

    menu():
        'Do you want to play story mode, or generate your own crew members?'

        'Story Mode':
            jump storyMode

        'Free Mode':
            jump freeMode

    label freeMode:
        'Not yet implemented!!!'
        return

    label storyMode:
        # test out simple paths
        # menus can take arguments
        menu():
            'What path do you want to take'

            'Pilot' : # can also take arguments before the :
                $ job = 'Pilot'
            'Machine':
                $ job = 'Machine'

    label Pilot:
        'This is the [job] entry point.'
        jump chapterOne

    label Machine:
        'This is the [job] entry point.'
        jump chapterOne

    jump expression job

    # Make your own custom crew -> Names, jobs, maybe pics

    # Chapter One after intro path
    label chapterOne:
        $ friend = renpy.random.choice(names)
        'So your a [job]. That is good news. We really need one right now.'
        'You should talk to [friend].'

    # SCREEN TESTS -------------------------------->

    # a screen(a, b) can take parameters, and use them below
    screen crewScreen:
        # replaces other screens with the same tag.
        tag shipOptions
        # prevents the user from interacting with displayables below it, except for the default keymap
        modal True
        # adds bg image
        add 'images/crewMenu.png'

        # Need to align text to menus maybe as children?

        bar:
            value 10 range 24

        text "Map" xalign .5 yalign 0.05

        vbox:
            xalign .5 yalign .95

            text 'Crew Members' xalign .5
            hbox:
                spacing 150
                text '[crew[1]]'
                text '[crew[2]]'
                text '[crew[3]]'
                text '[crew[4]]'
                text '[crew[5]]'
                text '[crew[6]]'


        # Keeps it children side by side
        hbox:
            xalign .5 yalign .17
            spacing 170
            text "Crew" xalign .1 yalign 0.17
            text "Cargo" xalign .2 yalign 0.17
            text "Upgrades" xalign .3 yalign 0.17
            text "Quest" xalign .7 yalign 0.17
            text "Log" xalign .8 yalign 0.17

    # calls a screen

    call screen crewScreen


    # This ends the game.

    return
