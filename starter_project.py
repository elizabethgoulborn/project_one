# First python project: basic "social media" creation
# Elizabeth Goulborn
# 28.09.2025

# 1. Import functions needed/ initalisation
from verify import verify
from populate import populate
from view_profile import view_profile

# Initialising userbank/user dictionaries
import json
import os

filename = "user_bank.json"

if os.path.exists(filename):
	with open(filename, "r") as f:
		user_bank = json.load(f)
else:
	user_bank = {}

# 2. Prompt user to either sign in or create a new account 
# until a valid username is entered
user_truth = True
while user_truth:
	profile = input("\n\nWelcome! Please enter your username to sign in.\
\nTo create a new account, enter 'new account'\n\nENTER HERE: ")

# 2.1 Create a new account
# Begin main loop to act upon username verification
	if profile.strip() == "new account":
		loop = True
		while loop:
	
			# 2.1.1 Invite username input
			username = input("""\n~~Welcome, new user. Please create a username below.~~
~~Usernames must not exceed 16 characters, and must not include spaces.~~\n\n\nEnter username here: """)
	
			# 2.1.2 Check verity status of username 
			verity, reject_reason = verify(username, user_bank)

			# 2.1.3 If username is invalid, prompt user for another username.
			if verity == False:
				print("\nUSERNAME REJECTED FOR REASON: " + reject_reason + "\nPlease enter another username.\n")
		
			# 2.1.4 If username is valid, exit loop.
			else:
				user_bank[username] = {}
				with open(filename, "w") as f:
					json.dump(user_bank,f)
				print("\n\nWelcome, " + username + "!\nYour username has been added to the database.")
				profile = username
				loop = False
				
			
	# 2.2 Sign in
	elif profile in user_bank:
		
		# 2.2.1 If given username exit loop to continue with interaction
		user_truth = False
		active = True
		while active:
			activity = input("\n\nWelcome, " + profile + ". What would you like to do?\
\nEnter 1 to view your profile\nEnter 2 to edit your profile\
\nEnter 3 to view another user's profile\nEnter 4 to sign out\nENTER: ")

			if activity == "1":
				# 2.2.1.1 View profile
				view_profile(user_bank,profile)
	
			elif activity == "2":
				# 2.2.1.2 Edit profile
				populate(user_bank, profile)		
				with open(filename, "w") as f:
					json.dump(user_bank,f)		
				print("\n\n~~Profile updated~~")
				print(f"Current user: {user_bank[profile]}")
	
			elif activity == "3":
				# 2.2.1.3 View another user's profile
				view = input("\n\nPlease enter the username of the profile you want to view.\
\nENTER HERE: ")
				view_profile(user_bank,view)
	
			elif activity == "4":
				# 2.2.1.4 Sign out
				print("\n\n~~SIGNED OUT~~")
				active = False
	
			else:
				# 2.2.1.5 Reject any invalid input
				print("\n\n~~INVALID RESPONSE~~")
	
	else:
		# 2.2.2 Reject profiles that do not exist
		print("\n~~USER NOT FOUND~~")













