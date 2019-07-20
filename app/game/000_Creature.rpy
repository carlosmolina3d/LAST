# Creature Class

init python:
    class Creature(object):
        '''Controlled by the user or AI.'''

        # Properties
        girlList = []

        # Constructor
        def __init__(self, name='Name', mood='Neutral', stats=None):
            self.name = name
            self.mood = mood
            self.stats = stats


        # Partner methods
        def addMember(self, creature):
            '''creature -> Screen
            Assigns creature to your crew.'''

            # Check to see if you have a partner and if so, terminate that partnership.
            if self.partner != None:
                self.partner.partner = None
                self.partner = otherGirl

            else:
                self.partner = otherGirl

            # Check to see if otherGirl has  a partner and if so, terminate that partnership.
            if otherGirl.partner != None:
                otherGirl.partner.partner = None
                otherGirl.partner = self

            else:
                otherGirl.partner = self
            return renpy.say(avatar, "You have a new partner! %s!" % (otherGirl.name))

        def removePartner(self):
            '''otherGirl -> Screen
            Removes otherGirl from the partnership.'''

            if self.partner == None:
                return renpy.say(avatar, "You don't have a partner.")

            else:
                renpy.say(avatar, "You are no longer partners with %s." % (self.partner.name))
                self.partner.partner = None
                self.partner = None

        # dosent belong in creatures
        # # Currency methods
        # def updateGems(self, factor):
        #     '''Interger -> None
        #     Does addition to the amount of gems you have by factor.'''
        #     self.gems += factor
