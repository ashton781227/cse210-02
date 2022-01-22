from game.hilo import Card

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        is_playing (boolean): Whether or not the game is being played.
        points (int): The score for the game.
        round (int): The round the game is in.
        lastvalue (int): The last value of the card
    """
    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        
        self.is_playing = True
        self.points = 300
        self.round = 0
        self.lastvalue = 10
    
        

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.play_game()

        print("Thank you for playing!")
        print("Play again soon!")

    def play_game(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """
        
        if self.round > 0:
            keep_playing = input("Play again? [y/n]")
            print()
            self.is_playing = (keep_playing == "y")

        self.round += 1

        if not self.is_playing:
            return 

        card = Card()
        print(f'The card is: {self.lastvalue}')
        guess = input("Higher or Lower? [h/l] ")
        card.face(guess, self.lastvalue)
        self.lastvalue = card.lastvalue
        self.points += card.points

        print(f'Next card was: {card.value}')
        print(f'Your score is: {self.points}')
        

        self.is_playing == (self.points > 0)
       
