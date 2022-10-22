from lib2to3.pytree import LeafPattern
from game.word import Word
from game.jumper import Jumper
from game.check import Check

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        word (Word): The word to be guessed.
        check (Check): Check if the word is in the alphabet, if it was already chosen and updates the hidden word.
        jumper (Jumper): The game's jumper.
        hidden_word_display (string): Display of the hidden word.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._word = Word()
        self._check = Check()
        self._jumper = Jumper()
        self.hidden_word_display = ''
        self._is_playing = True

    def start_game(self):
        """Starts the game by displaying the hidden word and by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        self.guess_word = self._word.generate_word()
        self.hidden_word = self._word.generate_hidden_word()
        for i in range(len(self.hidden_word)):
            self.hidden_word_display += ' _ '
        print(self.hidden_word_display)
        self._jumper.display_jumper()
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """Gets the guess of the user.

        Args:
            self (Director): An instance of Director.
        """
        self.letter = input('\nGuess a letter [a-z]: ')
        
    def _do_updates(self):
        """Checks the validity of the guess, updates the jumper or the hidden word.

        Args:
            self (Director): An instance of Director.
        """
        check_alphabet = self._check.check_alphabet(self.letter)
        check_choices = self._check.check_choices(self.letter)
        if check_alphabet:
            if check_choices:
                if self.letter not in self.guess_word:
                    self._jumper.update_jumper(self.letter)
                else:
                    self._check.check_letter(self.hidden_word, self.letter, self.guess_word)
            
        
    def _do_outputs(self):
        """Shows the results of the game, displays the hidden word and jumper again.

        Args:
            self (Director): An instance of Director.
        """
        if self.guess_word == self.hidden_word:
            self._is_playing = False
            print('\nYou win!\n')
        elif self._jumper.jumper[0] == '     x':
            print('\nGame over!\n')
            self._is_playing = False
        self.hidden_word_display = ''
        for i in range(len(self.hidden_word)):
            self.hidden_word_display += self.hidden_word[i]
        print(self.hidden_word_display)
        for i in range(len(self._jumper.jumper)):
            print(self._jumper.jumper[i])