

from operator import truediv


class Check:
    """Checks the validity of the user's guess. 
    
    The responsibility of Check is to validate the user's guess and, update the hidden word with the correct guessed letter.
    
    Attributes:
        self (Check): An instance of Check.
        alphabet (list[string]): A list containing the alphabet.
        choices (list[string]): A list containing the letters already chosen by the user.
    """

    def __init__(self):
        """Constructs the alphabet and th choices list.
        
        Args:
            self (Check): An instance of Check.
        """
        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.choices = []

    def check_alphabet(self, letter):
        """Checks if the letter chosen is in the alphabet.
        
        Args:
            self (Check): An instance of Check.
            letter (string): The letter chosen by the user.
        
        Returns:
            boolean: If the letter is in the alphabet or not.
        """
        if letter not in self.alphabet:
            print('Invalid entry! Type one letter [a-z]')
            return False
        else:
            return True
    
    def check_choices(self, letter):
        """Checks if the letter was already chosen.
        
        Args:
            self (Check): An instance of Check.
            letter (string): The letter chosen by the user.
        
        Returns:
            boolean: If the letter was already chosen or not.
        """
        if letter not in self.choices:
            self.choices.append(letter)
            return True
        else:
            print('You already typed this letter! Try another.')
            return False

    def check_letter(self, hidden_word,letter, word):
        """Checks if the letter is in the word.
        
        Args:
            self (Check): An instance of Check.
            hidden_word (list[string]): The hidden word divided in a list.
            letter (string): The letter chosen by the user.
            word (list[string]): The word divided in a list.
        
        """
        letter = letter.lower()
        for i in range(0, len(word)):
            if letter == word[i]:
                self.update_hidden_word(hidden_word, i, letter)                 
        
    def update_hidden_word(self, hidden_word, letter_number, letter):
        """Updates the hidden word with the letter chosen.
        
        Args:
            self (Check): An instance of Check.
            hidden_word (list[string]): The hidden word divided in a list.
            letter_number (int): The index of the letter in the word's list to be substituted.
            letter (string): The letter chosen by the user.
        
        """
        hidden_word[letter_number] = letter
        return hidden_word