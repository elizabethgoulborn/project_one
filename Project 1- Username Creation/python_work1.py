# Practicing how python works: Unique profile creation
# Elizabeth Goulborn
# 24.09.2025

# Initialise name bank dictionary to store username and other info
# about the user
# Desired user information: username, full name, age, city of residence
user_bank = {}

# Import functions
from verify import verify
from populate import populate

# Begin main loop to act upon username verification
loop = True
cont_loop = True
while loop == True:
	
	# Invite username input
	username = input("""\n~~Welcome, new user. Please create a username below.~~
~~Usernames must not exceed 16 characters, and must not include spaces.~~\n\n\nEnter username here: """)
	
	# Check verity status of username 
	verity, reject_reason = verify(username, user_bank)

	# If username is invalid, prompt user for another username.
	if verity == False:
		print("\nUsername rejected for reason: " + reject_reason + "\nPlease enter another username.\n")
		
	# If username is valid, exit loop.
	else:
		user_bank[username] = {}
		print("\n\nWelcome, " + username + "!\nYour username has been added to the database.")
		
		# Implement continuation/exit
		while cont_loop == True:
			cont = input("\nWould you like to add another user? (Y/N)\nEnter response here: ")
			if cont not in ["Y", "N"]:
				print("\nInvalid input. Please try again (Y/N): ")
			elif cont == "Y":
				break
			elif cont == "N":
				cont_loop = False
				loop = False

# Print confirmation message	
print("\n\n\n~~New profile generated: " + username + "~~")

# Update chosen user profile with personal info
for user in user_bank:
	user = {}
	
profile = input("\n\nEnter username to edit profile: ")

# If given username exists, allow profile customisation
if profile in user_bank:
	populate(user_bank, profile)
	print("\n\n~~Profile updated~~")
	print(f"Current user: {user_bank[profile]}")
	
# Reject profiles that do not exist
else:
	print("\n~~User not found in database.~~")
	
