class Jumper:
    """The person hiding from the Seeker.
    
    The responsibility of Hider is to keep track of its location and distance from the seeker.
    
    Attributes:
        _location (int): The location of the hider (1-1000).
        _distance (List[int]): The distance from the seeker.
    """

    def __init__(self):
        """Constructs a new Jumper.

        Args:
            self (jumper): An instance of Jumper.
        """
        self.jumper = ['    ___', '   /___\\', '   \\   /', '    \\ /', '     0', '   / | \\', '    / \\', '', '^^^^^^^^^^^^']
        self.choices = []
    
    def display_jumper(self):
        for i in range(len(self.jumper)):
            print(self.jumper[i])

    def update_jumper(self, letter, alphabet):
        """Gets a hint for the seeker.

        Args:
            self (Hider): An instance of Hider.
        
        Returns:
            string: A hint for the seeker.
        """
        letter = letter.lower()
        if letter in alphabet:
            if self.jumper[0] == '     0':
                self.jumper[0] == '     X'
            else:
                del self.jumper[0]
        else:
            print('Invalid entry! Type one letter [a-z]')