""" Practice creating a Class called 'Profile'. """

# definition
class Profile: 

    username: str
    private: bool

    def __init__(self, username_input: str):
        """Creates new profile."""
        self.username = username_input
        self.private = True
        # it will return self
    
    def tweet(self, msg: str) -> None:
        """If Profile is not private, print message."""
        if self.private is False:  # if not self.private
            print(self.msg)

# instantiation 
user1: Profile = Profile("110_rulez")  # __init__
user1.private = False
user1.tweet("OOP is cool!")