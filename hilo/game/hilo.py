import random

class Card:
    """A card with a number from 1 to 13.

    The responsibility of Card is to keep track of the number on the card and calculate the points for 
    it.
   
    Attributes:
        value (int): The number on the card.
        points (int): The number of points the guess is worth.
        lastvalue (int): The last value of the card drawn
    """

    def __init__(self):
        """Constructs a new instance of Card with a value and points attribute.

        Args:
            self (card): An instance of Card.
        """
        self.value = 0
        self.points = 0
        self.lastvalue = 0

    def face(self, guess, lastvalue):
        """Generates a new random value and calculates the points.
        
        Args:
            self (Card): An instance of Card.
            guess: The guess from the user.
            lastvalue: The last value of the card drawn
        """

        
        self.value = random.randint(1, 13)
        if guess == "l":
            if self.value < lastvalue:
                self.points = 100
                self.lastvalue = self.value
                
            else:
                self.points = -75 
                self.lastvalue = self.value
                
        if guess == "h":
            if self.value > lastvalue:
                self.points = 100
                self.lastvalue = self.value
                
            else: 
                self.points = -75 
                self.lastvalue = self.value
                
