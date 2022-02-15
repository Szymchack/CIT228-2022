from user import User
from admin import Admin
from privileges import Privileges

cathyann = Admin('cathyann', 'szymchack', 'c_szymchack@example.com', 'cat', 'the beach', 'really')
cathyann.describe_user()

cathyann.privileges.show_privileges()

lelia = User('lelia', 'borgen', 'leelee@borg.com', 'lab61820', 'Micronesia', 'rujoking')
lelia.describe_user()
lelia.greet_user()

kelli = User('kelli', 'borgen', 'bear@borg.com', 'angelbaby1', 'neitherlands', 'ecktoo')
kelli.describe_user()
kelli.greet_user()

cain = User('cain', 'szymchack', 'monkey@borg.com', 'myBoy', 'michigan', 'monkey')
cain.describe_user()
cain.greet_user()

print("--------------------9-5--------------------")

cain.increment_login_attempts()
cain.increment_login_attempts()
cain.increment_login_attempts()
print("Your number of login attempst: " + str(cain.login_attempts))
cain.reset_login_attempts()
print("We are resetting login attempts: " + str(cain.login_attempts))