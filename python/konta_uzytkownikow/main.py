import logging

LOG_FILE = "user_manager.log"

logging.basicConfig(filename=LOG_FILE,
                    filemode='a',
                    format='%(asctime)s,%(msecs)03d %(name)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG)

logger = logging.getLogger("User_Manager")

class User:
    '''User Class: has username, email and role'''
    def __init__(self, username: str, email: str, role: str):
        self.username = username
        self.email = email
        self.role = role
        logging.debug("Added new user")

    def __str__(self):
        return self.username

class UserManager:
    '''Usermanager Class: Holds all users inside of an array and lets you manage them'''
    def __init__(self):
        self.users = []
        logging.debug("Initiated new user manager")

    def add_user(self, username: str, email: str, role: str):
        '''Adds a new user with username, email and role to an array'''
        newUser = User(username,email,role)
        self.users.append(newUser)
        logging.debug("Appended a new user to UserManager")

    def delete_user(self, username: str):
        '''Deletes an user from provided username'''
        for user in self.users:
            if user.username == username:
                self.users.remove(user)
                print(f'{user} deleted')
                logging.debug(f"Deleted user {user} from manager")
                return
        print(f"ERROR: Couldn't find {username} in users")
        logging.debug(f"Couldn't delete user {user} from manager, reason: doesn't exist")

    def display_users(self):
        '''Displays all users in the user manager'''
        print("Wyświetlanie wszystkich użytkowników:")
        for user in self.users:
            print(f'  - {user}')


if __name__ == "__main__":
        
    logger.info("Program started")

    userManager = UserManager()
    userManager.add_user("uzytkownik1", "test@test.test", "role")
    userManager.add_user("uzytkownik2", "test@test.test", "role")
    userManager.add_user("uzytkownik", "test@test.test", "role")
    userManager.add_user("noob", "test@test.test", "role")
    userManager.display_users()
    userManager.delete_user("noob")
    userManager.display_users()