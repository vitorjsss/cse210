class Jumper:
    """The jumper is the character with the parachutes representing the player.
    
    The responsibility of Jumper is to display the jumper, and updates the parachute.
    
    Attributes:
        _jumper (list[str]): The drawing of the jumper.
    """

    def __init__(self):
        """Constructs a new Jumper.

        Args:
            self (Jumper): An instance of Jumper.
        """
        self._jumper = ['    ___', '   /___\\', '   \\   /', '    \\ /', '     O', '   / | \\', '    / \\', '', '^^^^^^^^^^^^']
    
    def display_jumper(self):
        """Displays the jumper.

        Args:
            self (Jumper): An instance of Jumper.
        """
        for i in range(len(self._jumper)):
            print(self._jumper[i])

    def update_jumper(self):
        """Updates the parachute of the jumper.

        Args:
            self (Jumper): An instance of Jumper.
        
        """
        if self._jumper[0] == '    \\ /':
            del self._jumper[0]
            self._jumper[0] = '     x'
        else:
            del self._jumper[0]