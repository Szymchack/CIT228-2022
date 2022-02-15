from user import User

class Admin(User):

    def __init__(self, first_name, last_name, email, username, location, password):
        super().__init__(first_name, last_name, email, username, location, password)
        self.privileges = []

    def show_privileges(self):
        print("\nPrivileges:")
        for privilege in self.privileges:
            print(f"-{privilege}")

cathyann = Admin('cathyann', 'szymchack', 'c_szymchack@example.com', 'cat', 'the beach', 'really')
cathyann.describe_user()

cathyann.privileges.show_privileges()

print("\nAdding privileges...")
cathyann_privileges = [
    'can reset passwords',
    'can mediate discussions',
    'can boot you outta account']

