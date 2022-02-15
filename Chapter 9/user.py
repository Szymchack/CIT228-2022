class User():
    def __init__ (self, first_name, last_name, email, username, location, password):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.email = email.title()
        self.username = username.title()
        self.location = location.title()
        self.password = password.title()
        self.login_attempts = 0
        
    def describe_user(self):
        print("\n" + self.first_name + " " + self.last_name)
        print("  Email: " + self.email)
        print("  Username: " + self.username)
        print("  Location: " + self.location)
        print("  Password: " + self.password)
    
    def greet_user(self):
        print("\nWelcome back, " + self.first_name + "!")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

