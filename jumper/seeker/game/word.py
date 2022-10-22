import random

class Word:
    """A class that generates the random Word.
    
    The responsibility of the Word is to generates the random word that will be guessed.
    
    Attributes:
        _word (list[int])
        _hidden_word (list[int])
        _random_word: (str)
        _word: (list[str])
    
    """
     
    def __init__(self):
        """Constructs a new word and hidden word.

        Args:
            self (Word): An instance of Word.
        """
        self._word = []
        self._hidden_word = []

    def generate_word(self):
        """Selects a random word from a list.

        Args: 
            self (Word): An instance of Word.

        Returns:
            list: The random word as a list of letters.
        """
        words = ["apple", "banana", "city", "secular", "robot", "Ireland", "ant", "mars", "low", "sports", "car", "tree", "wolf", "sheep", "perpendicular", "cake", "meal"]
        self._random_word = random.choice(words)
        self._word = list(self._random_word)
        return self._word
    
    def generate_hidden_word(self):
        """Selects the hidden word based on the word.

        Args: 
            self (Word): An instance of Word.

        Returns:
            list: The hidden word as a list.
        """
        for i in range(len(self._word)):
            self._hidden_word.append(' _ ')
        return self._hidden_word