"""
This project library is not to be claimed as your own. To use it, add credit
and acknowledgement of inPySta. This library, as it is open-source, should be credited.

C 2026 inPySta Dev.

_ inPySta Dev. Studio

How To Use

    1. Open any Python file
    2. In the terminal, run: 'pip install inpysta'
    3. In your code, add: 'from inpysta import MockEngineMain'
    4. add: 'Engine = MockEngineMain("MyEngine") # you can name it whatever
    5. Now, run anything you want.
    
COMMANDS BASED OFF OF v1.0.3

CreateUser(username, userage)   Creates a user with credentials.
DeleteUser(username)            Deletes a user

myUser = CreateUser(...)        Stores your user
myUser._follow(follower)        {follower} will follow myUser
myUser._unfollow(unfollower)    {unfollower} will unfollow myUser

EditInfo(username)              Will ask you to edit either username, or userage
SetParentalUser(username)       Sets a parental user for {username} based on your input
ViewUsers()                     Returns a list of all the usernames
PrintInfo(username)             Prints info (e.g. Username, userage..) about the provided username


What is inPysta?
inPySta is a Python library that simulates Instagram. You can follow, unfollow and much more.
Since this is still v1.0.3, no posts have been added. Maybe in v5.0.0, we'll have posts.

inPySta is just a project, made for fun. Not professional. Just a project you'd make at 3.00 AM, for
no absolutely no reason. Here's some test code:

from pysta import MockEngineMain

engine = MockEngineMain("myEngine")
myUser = engine.CreateUser("myUser")

This starts an engine, called myEngine. Then it creates a user called myUser, and
saves it to the database.

You can check the database by running:

engine.ViewUsers() <- this returns a list of users

or

print(engine.ViewUsers())

"""

# Authored by "Elijah J." 
# NOTE Thanks for using inPySta

_version = "v1.0.3" # MAIN VERSION OF inPySta

class NotAValidUser(Exception): ... # Errors if someone is not a user
class AlreadyFollowed(Exception): ... # Errors if someone is already followed
class NoInfoProvided(Exception): ... # If no info is provided

def _NotAValidUser(user: str=None): raise NotAValidUser(f"Not a valid user: {user}")
def _AlreadyFollowed(): raise AlreadyFollowed()
def _NoInfoProvided(message): raise NoInfoProvided(message)

users = {} # Simulate all users

class UserProfileAccount: # Create the main User class
    """
    Create an account here
    """
    
    def __init__(self, username, userage, parentalUsername=None): # Never store passwords
        global users
        
        self.username = username # Store username
        
        try:
            self.userage = int(userage)
        except ValueError:
            raise TypeError("Userage must be a valid integer or integer string.")

        self.followers = [] # Who follows this user
        self.followersCount = len(self.followers) # How many follow this user
        
        self.follows = [] # people the USER follows
        self.followsCount = len(self.follows)
        self.parentalUsername = parentalUsername
        
        self.notAdult = True if self.userage < 18 else False
        if self.notAdult:
            print(f"You might want to set up a parental username for {self.username}")
            
        users[self.username.lower()] = self
               
    def _follow(self, usernameFollowing: str): # Follow this user
        """Make this user follow the username provided"""
        target_clean = usernameFollowing.strip().lower()
            
        # Find the actual target user object in the database
        target_user = None
        for u in users:
            if u.username.lower() == target_clean:
                target_user = u
                break
                    
        if target_user: 
            if target_clean in self.follows:
                _AlreadyFollowed()
                return
                
            # Update current user's following list (YOU follow THEM)
            self.follows.append(target_clean)
            self.followsCount += 1
                
            # Update the target user's followers list (THEY gain YOU)
            target_user.followers.append(self.username.lower())
            target_user.followersCount += 1

    def _unfollow(self, usernameUnfollowing: str): # Unfollow this user
        """Make this user stop following {usernameUnfollowing}"""
        target_clean = usernameUnfollowing.strip().lower()
        
        if target_clean in self.follows:
            # You stop following them
            self.follows.remove(target_clean)
            self.followsCount -= 1
            
            # Find them in the database to remove you from their followers
            for u in users:
                if u.username.lower() == target_clean:
                    if self.username.lower() in u.followers:
                        u.followers.remove(self.username.lower())
                        u.followersCount -= 1
                    break
        else:
            print(f"You are not following {usernameUnfollowing}")
            return
        
    def __repr__(self):
        """Tells Python exactly how to print this object in lists and consoles."""
        return f"'{self.username}'"

class MockEngineMain:
    """
    The main engine. Set a title
    """
    def __init__(self, title: str):
        self.engine = "Mock Engine" if title is None else title
        
    @staticmethod
    def CreateUser(username:str, userage: int | str, parentalUser=None):
        """
        Create a new user and store it
        
        Args:
            username (str): The desired handle. Case-insensitive and must be unique.
            userage (int): The age of the user. Automatically triggers parental warnings if under 18.

        Returns:
            UserProfileAccount: The instantiated user object if successful, None otherwise.

        Raises:
            NoInfoProvided: If username or userage parameters are missing.
        """
        
        if username.lower() in users:
            print(f"Registration Error: Username '{username}' is already taken.")
            return None

        if username is None or userage is None:
            _NoInfoProvided("Username or userage was not provided.")
            return
            
        try:
            NewUser = UserProfileAccount(username, userage, parentalUser)
            return NewUser
        except Exception as e:
            print(f"Something went wrong: {type(e).__name__}")
        
    @staticmethod
    def DeleteUser(user: UserProfileAccount):
        """
        Remove a user from the database
        
        Args:
            user (UserProfileAccount): The desired account to delete
            
        Raises:
            NoInfoProvided if no user was given
            
        """
        
        if not user or user.username.lower() not in users:
            _NoInfoProvided("Valid user to delete was not provided.")
            return
        
        try:
            del users[user.username.lower()]
        except Exception as e:
            print(f"Something went wrong: {type(e).__name__}")
        
    @staticmethod
    def ViewUsers() -> list:
        """
        View all the usernames in the database
        
        Returns:
            users: The main database holding all users
        """
        all_users = list(users.values())
        print(all_users)
        return all_users
    
    @staticmethod
    def PrintInfo(username: str):
        """
        Prints info about the provided username
        
        Args:
            username (str): The username to get info about
            
        Raises:
            NoInfoProvided if the username was not given
            
        Returns:
            info: A string of info, just like the one printed
        
        """
        if username is None:
            _NoInfoProvided("Username not provided")
            return
        
        user = users.get(username.lower())
        if not user:
            _NotAValidUser(username)
            return
        
        info = f"""
            Username: {user.username}")
            Age: {user.userage}")
            Parental User: {f'Enabled (\'{user.parentalUsername}\')' if user.parentalUsername else 'Disabled'}")

            Followers: {user.followers}")
            Follow Count: {user.followersCount}")
            Following: {user.follows}")
            Following Count: {user.followsCount}")
        """
        

        print("**********************************")
        print(f"Info about '{user.username}':")
        print("**********************************")
        print(f"    Username: {user.username}")
        print(f"    Age: {user.userage}")
        print(f"    Parental User: {f'Enabled (\'{user.parentalUsername}\')' if user.parentalUsername else 'Disabled'}")
        print()
        print(f"    Followers: {user.followers}")
        print(f"    Follow Count: {user.followersCount}")
        print(f"    Following: {user.follows}")
        print(f"    Following Count: {user.followsCount}")
        print("***********************************************")
        
        return info
        
    @staticmethod
    def EditInfo(username: str):
        """
        Edit info about a user. Provide username.
        
        Args:
            username (str): The user's username desired to edit info about
            
        Raises:
            NoInfoProvided if no username was given
            
        Will ask for input!
        """

        if username is None:
            _NoInfoProvided("Username was not provided")
            return
        username = username.lower()
        
        for i in users:
            if i.username.lower() == username:
                user = i
                break
            else:
                user = None
                
        if user is None:
            _NotAValidUser(username)
            return
        
        usersP = ["username", "user", "name", "id"]
        agesP = ["age"]
        
        toEdit = input("What would you like to edit? (e.g. username, age) ").lower()
        
        if toEdit in usersP:
            changeTo = input(f"Change username ({user.username}) to: ")
            user.username = changeTo
        elif toEdit in agesP:
            changeTo = input(f"Change age ({user.userage}) to: ")
            user.userage = int(changeTo)
        else:
            print("Invalid option: Choose either username or age")
            return
        
    @staticmethod
    def SetParentalUser(username: str):
        """
        Set a parental user for users under 18
        
        Args:
            username (str): The user's username you want to set a parent for
        
        Will ask for input!
        """
        
        if username is None:
            _NoInfoProvided("Username was not provided")
            return
        username = username.lower()
                
        for i in users:
            if i.username.lower() == username:
                user = i
                break
            else:
                user = None
                        
        if user is None:
            _NotAValidUser(username)
            return
        
        if user.notAdult:
            parentalUsername = input(f"Enter a username to set as a parent for '{username}': ")
            for i in users:
                if i.username.lower() == parentalUsername.lower():
                    user.parentalUsername = parentalUsername
                    print(f"Set {parentalUsername} as a parent for {username}")
                    break
                else:
                    _NotAValidUser(parentalUsername)
    
if __name__ == "__main__":
    print(f"Running inPySta {_version} as main")
else:
    print(f"Running inPySta {_version}")