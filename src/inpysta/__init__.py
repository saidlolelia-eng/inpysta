"""
This project library is not to be claimed as your own. To use it, add credit
and acknowledgement of PySta. This library, as it is open-source, should be credited.

C 2026 inPySta Dev.

_ inPySta Dev. Studio

How To Use

    1. Open any Python file
    2. In the terminal, run: 'pip install inpysta'
    3. In your code, add: 'from inpysta import MockEngineMain'
    4. add: 'Engine = MockEngineMain("MyEngine") # you can name it whatever
    5. Now, run anything you want.
    
COMMANDS BASED OFF OF v1.0.2

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
Since this is still v1.0.2, no posts have been added. Maybe in v5.0.0, we'll have posts.

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

# Authored by "Elia Jebreen" 
# NOTE Thanks for using inPySta

_version = "Beta v1.0.2" # MAIN VERSION OF inPySta

class NotAValidUser(Exception): ... # Errors if someone is not a user
class AlreadyFollowed(Exception): ... # Errors if someone is already followed
class NoInfoProvided(Exception): ... # If no info is provided

def _NotAValidUser(user: str=None): raise NotAValidUser(f"Not a valid user: {user}")
def _AlreadyFollowed(): raise AlreadyFollowed()
def _NoInfoProvided(message): raise NoInfoProvided(message)

users = [] # Simulate all users

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
        self.followersCount = 0 # How many follow this user
        
        self.follows = [] # people the USER follows
        self.followsCount = 0
        self.parentalUsername = parentalUsername
        
        self.notAdult = True if userage < 18 else False
        if self.notAdult:
            print(f"You might want to set up a parental username for {self.username}")
            
        users.append(self)
               
        def _follow(self, usernameFollowing: str): # Follow this user
            """Follow someone"""
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
                
                # Update current user's following list
                self.follows.append(target_clean)
                self.followsCount += 1
                
                # Update the target user's followers list
                target_user.followers.append(self.username.lower())
                target_user.followersCount += 1
            else:
                _NotAValidUser(usernameFollowing)
                return

            
    def _unfollow(self, usernameUnfollowing: str): # Unfollow this user
        """Unfollow someone"""
        
        if usernameUnfollowing.lower() in self.followers:
            self.followers.remove(usernameUnfollowing.lower())
            self.followersCount -= 1
        else:
            print(f"{usernameUnfollowing} is not in {self.username}'s followers")
            return
        
    def __repr__(self):
        """Tells Python exactly how to print this object in lists and consoles."""
        return f"'{self.username}'"

class MockEngineMain:
    def __init__(self, engine):
        self.engine = "Mock Engine" if engine is None else engine
        
    @staticmethod
    def CreateUser(username:str, userage: int | str, parentalUser=None):
        """
        Create a new user and store it
        """
        
        if username.lower() in [i.username.lower() for i in users]:
            print(f"Registration Error: Username '{username}' is already taken.")
            return None

        if username is None or userage is None:
            _NoInfoProvided("Username or userage was not provided.")
            return
            
        try:
            NewUser = UserProfileAccount(username, userage, parentalUser)
            return NewUser
        except Exception as e:
            __error__ = type(e).__name__
            print(f"Something went wrong: {__error__}")
        
    @staticmethod
    def DeleteUser(user:UserProfileAccount):
        """
        Remove a user from the database
        """
        
        if not user in users:
            _NoInfoProvided("Username to delete was not provided.")
            return
        
        try:
            users.remove(user)
        except Exception as e:
            __error__ = type(e).__name__
            print(f"Something went wrong: {__error__}")
        
    @staticmethod
    def ViewUsers() -> list:
        """
        View all the users in the database
        """
        print(users)
        return users
    
    @staticmethod
    def PrintInfo(username):
        """
        Prints info about the provided username
        """
        
        if username is None:
            _NoInfoProvided("Username not provided")
        
        if username.lower() not in [i.username.lower() for i in users]:
            _NotAValidUser(username)
            return

        
        for i in users:
            if i.username == username:
                print("**********************************")
                print(f"Info about '{i.username}':")
                print("**********************************")
                print(f"    Username: {i.username}")
                print(f"    Age: {i.userage}")
                print(f"    Parental User: {f'Enabled (\'{i.parentalUsername}\')' if i.parentalUsername else 'Disabled'}")
                print()
                print(f"    Followers: {i.followers}")
                print(f"    Follow Count: {i.followersCount}")
                print(f"    Following: {i.follows}")
                print(f"    Following Count: {i.followsCount}")
                print("***********************************************")
                
    @staticmethod
    def EditInfo(username: str):
        """
        Edit info about a user. Provide username.
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
            
def main(): # Won't run if you're using the library
    """
    Testing the engine.
    """

    engine = MockEngineMain("Engine") # Create the main engine (you can have 2+ engines!)
    
    engine.CreateUser("test", 19) # Create a user named test with age 19
    engine.CreateUser("admin", 5) # Create a user named admin with age 5
    engine.ViewUsers() # view all users
    engine.PrintInfo("admin") # Print the info of admin
    engine.PrintInfo("test") # Print info of test
    engine.SetParentalUser("admin") # Set a parent for admin (test)
    engine.PrintInfo("admin") # print info about admin
    
if __name__ == "__main__":
    main()
else:
    print(f"Running PySta {_version}")