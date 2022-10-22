

class Check:
    """The person looking for the Hider. 
    
    The responsibility of a Seeker is to keep track of its location and distance travelled.
    
    Attributes:
        location (int): The location of the Seeker (1-1000).
    """

    def check_letter(self, hidden_word,letter, word, choices):
        letter = letter.lower()
        if letter not in choices:    
            for i in range(0, len(word)):
                if letter == word[i]:
                    self.update_hidden_word(hidden_word, i, letter)
        else:
            print('You already typed this letter! Try another.')
                        

    """Gets the current location.
        
    Returns:
        number: The current location,
    """
        
    def update_hidden_word(self, hidden_word, letter_number, letter, choices):
        """Updates the hidden word with the letter given, if it is part of the word.

        Args:
        self (Seeker): An instance of Seeker.
        location (int): The given location.
        """
        if hidden_word[letter_number] == letter:
            print('You already typed this letter! Try another.')
        else:
            hidden_word[letter_number] = letter
            choices.append(letter)
            return hidden_word