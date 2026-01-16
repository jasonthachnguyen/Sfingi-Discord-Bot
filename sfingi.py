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
        self.affection = 100
        self.hygiene = 100
        self.recoverAmt = 100
        self.afterFeedText = [
            "Sfingi is feeling nice and full!",
            "Even though his belly is ready to burst, he wants more food...",
            "Sfingi looks up at you with his fat little belly.",
            "Sfingi walks away with his belly bouncing around."
        ]
        self.afterPetText = [
            "Sfingi purrs as you softly brush your him against him.",
            "As you pet Sfingi, you feel his belly jiggle...",
            "While petting Sfingi, he slowly walks away..."
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
            "Sfingi is clean enough to not smell."
            "Sfingi is a little stinky..."
            "Sfingi REEKS!!!!!"
        ]
        self.affection = [
            "Sfingi feels loved and appreciated."
            "Sfingi is okay but wouldn't mind more affection."
            "Sfingi is starting to feel a bit lonely."
            "Sfingi is meowing and whining for your affection."
        ]
        self.thanksText = [
            "thanks big dawg, ppreciate it", 
            "merow", 
            "meoww", 
            "purr", 
            "REORRRW", 
            "MEEEEEEOWWWWWWW"]

    def getStatus():
        pass

    def getNeedsText(self, need, statusTextList):
        """
        Returns the respective text from the list of hunger status texts based on the current hunger.

        :param self: Description
        """
        #Divide 100 by the length of the text list to get the dividend which we then divide the hunger by to get the right index.
        derivedIndex = math.ceil(need / (100/len(statusTextList)))
        return statusTextList[derivedIndex]

    def randomizeSound(self, textList):
        #Returns a randomized sound when a list of sounds
        sound = textList[random.randrange(len(textList))]
        return sound