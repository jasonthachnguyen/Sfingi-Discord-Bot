import random 
import time

class catTracker():
    def __init__(self):
        self.hunger = 100
        self.boredom = 100
        self.love = 100
        self.grooming = 100
        self.recoverAmt = 100
        self.fullText = [
            "Sfingi is feeling nice and full!",
            "Even though his belly is ready to burst, he wants more food...",
            "Sfingi looks up at you with his fat little belly.",
            "Sfingi walks away with his belly bouncing around."
        ]
        self.sounds = ["thanks big dawg, ppreciate it", "merow", "meoww", "purr", "grrr", "meYOEW"]

    def getStatus(self):
        #Prints out all the information about sfingi
        return f"Sfingi's current stats - hunger: {self.hunger}, boredom: {self.boredom}, love: {self.love}"

    def feed(self):
        #This method allows the discord user to feed Sfingi and add to his hunger and returns a randomized sound
        self.hunger = self.recoverAmt 
        sound = self.randomizeSound() 
        return f'"{sound}" - Sfingi is feeling nice and full.'
    
    def pet(self):
        #This method allows the discord user to pet Sfingi and add to his boredom and love and returns a randomized sound.
        self.love += self.recoverAmt / 2
        self.boredom += self.recoverAmt // 3
        sound = self.randomizeSound()
        print(f"Petting sound is {sound}")
        return sound
    
    def randomizeSound(self):
        #Returns a randomized sound when a list of sounds
        print("Sound has been randomized")
        sound = self.sounds[random.randrange(len(self.sounds))]
        print(f"Sound is hello")
        return sound
    
    
    


