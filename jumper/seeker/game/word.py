import random

class Word:
    """A class that generates the random Word.
    
    The responsibility of the class Word is to generates the random word that will be guessed.
    """
     
    def __init__(self):
        """Constructs a new Seeker.

        Args:
            self (Seeker): An instance of Seeker.
        """
        self.word = []
        self.hidden_word = []

    def generate_word(self):
        """Generates the word according to a list.

        Args: 
            self (TerminalService): An instance of TerminalService.
            prompt (string): The prompt to display on the terminal.

        Returns:
            string: The user's input as text.
        """
        words = ["apple", "banana", "city", "secular", "robot", "Ireland", "ant", "mars", "low", "sports", "car", "tree", "wolf", "sheep", "perpendicular", "cake", "meal"]
        self.random_word = random.randint(words) #generates random word from the list
        self.word = list(self.random_word)
        return self.word #return random word
    
    def generate_hidden_word(self):
        for i in range(len(self.word)):
            self.hidden_word.append(' _ ')