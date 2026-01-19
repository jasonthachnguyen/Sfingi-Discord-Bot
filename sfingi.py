import random
import math

class Sfingi:
    """
    The Sfingi class is an object to track and manage information about Sfingi including
    his hunger, affection and hyigene stats. It also provides text for when you interact
    with him.
    """
    def __init__(self):
        self.hunger = 100.0
        self.affection = 100.0
        self.hygiene = 100.0
        self.recoverAmt = 100.0
        self.afterFeedText = [
            "Sfingi is feeling nice and full!",
            "Even though his belly is ready to burst, he wants more food...",
            "Sfingi looks up at you with his fat little belly.",
            "Sfingi walks away with his belly bouncing around."
        ]
        self.afterPetText = [
            "Sfingi purrs as you softly brush your him against him.",
            "As you pet Sfingi, you feel his belly jiggle...",
            "While petting Sfingi, he slowly walks away...",
            "Sfingi is happy with you!"
        ]
        self.afterWashText = [
            "Sfingi tries to run away from the bath but to no avail...",
            "Stinky kitty...",
            "While getting washed, Sfingi thinks about his next meal.",
            "After being threatened to be tossed out the window, Sfingi gave up resisting."
        ]
        self.hungerStatusText = [
            "Sfingi is as full as a cat of his size can get!",
            "Sfingi is content for a fat cat.",
            "Sfingi is feeling a little peckish",
            "Sfingi is starving! NOOOOO!"
        ]
        self.hygieneStatusText = [
            "Sfingi is as clean as a fiddle!",
            "Sfingi is clean enough to not smell.",
            "Sfingi is a little stinky...",
            "Sfingi REEKS!!!!!"
        ]
        self.affectionStatusText = [
            "Sfingi feels loved and appreciated.",
            "Sfingi is okay but wouldn't mind more affection.",
            "Sfingi is starting to feel a bit lonely.",
            "Sfingi is meowing and whining for your affection."
        ]
        self.thanksText = [
            "thanks big dawg, ppreciate it", 
            "merow", 
            "meoww", 
            "purr", 
            "REORRRW", 
            "MEEEEEEOWWWWWWW"]

    #RESET METHODS
    def resetHunger(self):
        self.hunger = self.recoverAmt

    def resetAffection(self):
        self.affection = self.recoverAmt

    def resetHygiene(self):
        self.hygiene = self.recoverAmt

    #DECREASE METHODS
    def decreaseHunger(self):
        self.hunger = max(0, self.hunger - 1) 

    def decreaseAffection(self):
        self.affection = max(0, self.affection - 1) 

    def decreaseHygiene(self):
        self.hygiene = max(0, self.hygiene - 1) 

    #ACCESSORS
    def getNeedsText(self, need, statusTextList):
        """
        Returns the respective text from the list of hunger status texts based on the current hunger.

        :param self: The object itself
        :param need: Any of the defined needs of Sfingi
        :param statusTextList: A list with all of the text for the status
        """
        #Divide 100 by the length of the text list to get the dividend which we then divide the hunger by to get the right index.
        derivedIndex = math.ceil(need / (self.recoverAmt/len(statusTextList))) - 1
        statusTextListReversed = list(reversed(statusTextList))
        return statusTextListReversed[derivedIndex]
    
    def getAfterFeedText(self):
        return self.randomizeSound(self.afterFeedText)
    
    def getAfterPetText(self):
        return self.randomizeSound(self.afterPetText)
    
    def getAfterWashText(self):
        return self.randomizeSound(self.afterWashText)
    
    def getStatus(self):
        hungerText = self.getNeedsText(self.hunger, self.hungerStatusText)
        affectionText = self.getNeedsText(self.affection, self.affectionStatusText)
        hygieneText = self.getNeedsText(self.hygiene, self.hygieneStatusText)
        return f"{hungerText}\n{affectionText}\n{hygieneText}"
    
    def getThanksText(self, specificText = -1):
        """
        Returns a specific element of the thanks text list - set to return a random element by default.
        
        :param self: The object itself
        :param specificText: Used if a specific index of thanksText List needs to be used
        """
        return self.randomizeSound(self.thanksText) if specificText == -1 else self.thanksText[specificText]
    
    def getHungerValue(self):
        return self.hunger
    
    def getAffectionValue(self):
        return self.affection
    
    def getHygieneValue(self):
        return self.hygiene

    #UTILITY
    def randomizeSound(self, textList):
        #Returns a randomized sound when a list of sounds
        sound = textList[random.randrange(len(textList))]
        return sound