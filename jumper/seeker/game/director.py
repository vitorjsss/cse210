from game.word import Word
from game.jumper import Jumper
from game.check import Check

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        hider (Hider): The game's hider.
        is_playing (boolean): Whether or not to keep playing.
        seeker (Seeker): The game's seeker.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._word = Word()
        self._check = Check()
        self._jumper = Jumper()
        self.guess_word = self._word.generate_word()
        self.hidden_word = self._word.generate_hidden_word()
        hidden_word_display = ''
        for i in range(len(self.hidden_word)):
            hidden_word_display += ' _ '
        print(hidden_word_display)
        self._jumper.display_jumper()
       
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """

        Args:
            self (Director): An instance of Director.
        """
        self.letter = input('\nGuess a letter [a-z]: ')
        
    def _do_updates(self):
        """Updates the jumper.

        Args:
            self (Director): An instance of Director.
        """
        if self.letter not in self.guess_word:
            self._jumper.update_jumper()
        else:
            self._check.check_letter(self.hidden_word, self.letter, self.guess_word)
        
    def _do_outputs(self):
        """Provides a hint for the seeker to use.

        Args:
            self (Director): An instance of Director.
        """
        if self.guess_word == self.hidden_word:
            self._is_playing = False
        elif self._jumper.jumper[0] == '     X':
            print('\nGame over!')
            self._is_playing = False
        else:
            print(self.hidden_word)
            print(self._jumper.jumper)