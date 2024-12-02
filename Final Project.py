import re
# Step 1: Define User class
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
# Step 2: Define UserList class
class UserList:
    def __init__(self, filename):
        self.filename = filename
        self.userlist = []
        self.read_user_file()
    def read_user_file(self):
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    username, password = line.strip().split(',')
                    self.userlist.append(User(username, password))
        except FileNotFoundError:
            print(f"File {self.filename} not found. Starting with an empty list.")
    def write_user_file(self):
        with open(self.filename, 'w') as file:
            for user in self.userlist:
                file.write(f"{user.username},{user.password}\n")
        print("Changes Saved")
    def display_user_list(self):
        print(f"{'Username':<15} {'Password':<15}")
        print("-" * 30)
        for user in self.userlist:
            print(f"{user.username:<15} {user.password:<15}")
    def find_username(self, username):
        for index, user in enumerate(self.userlist):
            if user.username == username:
                return index
        return -1
    def change_password(self, username, password):
        index = self.find_username(username)
        if index != -1:
            self.userlist[index].password = password
            print("Password Changed")
        else:
            print("Username Not Found")
    def add_user(self, username, password):
        if self.find_username(username) != -1:
            print("Username Already Exists")
        else:
            self.userlist.append(User(username, password))
            print("User Added")
    def delete_user(self, username):
        index = self.find_username(username)
        if index != -1:
            del self.userlist[index]
            print("User Deleted")
        else:
            print("Username Not Found")
    def strength(self, password):
        score = 0
        if len(password) >= 8:
            score += 1
        if re.search(r'[A-Z]', password):
            score += 1
        if re.search(r'[a-z]', password):
            score += 1
        if re.search(r'\d', password):
            score += 1
        # Corrected regex for special characters
        if re.search(r'[~!@#$%^&*()_+\-|={}[\]:;<>?]', password):
            score += 1
        return score
# Step 3: Main Program Logic
def main():
    filename = 'user_data.txt'
    user_list = UserList(filename)
    while True:
        print("\nMenu:")
        print("1) Add a New User")
        print("2) Delete an Existing User")
        print("3) Change Password on an Existing User")
        print("4) Display All Users")
        print("5) Save Changes to File")
        print("6) Quit")
        selection = input("Enter Selection: ")
        if selection == '1':
            username = input("Enter Username: ")
            if user_list.find_username(username) != -1:
                print("Username Already Exists")
                continue
            while True:
                password = input("Enter Password: ")
                password_strength = user_list.strength(password)
                if password_strength < 5:
                    print(f"This password is weak - {password_strength}")
                else:
                    user_list.add_user(username, password)
                    break
        elif selection == '2':
            username = input("Enter Username: ")
            user_list.delete_user(username)
        elif selection == '3':
            username = input("Enter Username: ")
            if user_list.find_username(username) == -1:
                print("Username Not Found")
                continue
            while True:
                password = input("Enter New Password: ")
                password_strength = user_list.strength(password)
                if password_strength < 5:
                    print(f"This password is weak - {password_strength}")
                else:
                    user_list.change_password(username, password)
                    break
        elif selection == '4':
            user_list.display_user_list()
        elif selection == '5':
            user_list.write_user_file()
        elif selection == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid Selection")
if __name__ == "__main__":
    main()