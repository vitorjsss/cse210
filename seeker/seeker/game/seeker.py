# TODO: Implement the Seeker class as follows...

# 1) Add the class declaration. Use the following class comment.

import random


class Seeker:
    """The person looking for the Hider. 
    
    The responsibility of a Seeker is to keep track of its location and distance travelled.
    
    Attributes:
        location (int): The location of the Seeker (1-1000).
    """

# 2) Create the class constructor. Use the following method comment.
    def __init__(self):
        """Constructs a new Seeker.

        Args:
            self (Seeker): An instance of Seeker.
        """
        self.location = 0
# 3) Create the get_location(self) method. Use the following method comment.
    def get_location(self):
        self.current_location = self.location
        return self.current_location
        
    """Gets the current location.
        
    Returns:
        number: The current location,
    """
        
# 4) Create the move_location(self, location) method. Use the following method comment.
    def move_location(self, location):
        self.location = location
        return self.location
    """Moves to the given location.

    Args:
        self (Seeker): An instance of Seeker.
        location (int): The given location.
    """