# Populates a user profile with inputted informatino
# Elizabeth Goulborn
# 28.09.2025

def populate(user_bank, profile):
	""" This function asks the user questions to populate their
	profile with information about themselves"""
	print("\n\n~~User information needed.~~")
	full_name = input("\nEnter full name: ")
	age = str(input("\nEnter age: "))
	location = input("\nEnter city of residence: ")
	activity = input("\nEnter current activity (to keep other users in the loop!): ")
	
	user_bank[profile] = {
        "full_name": full_name,
        "age": age,
        "location": location,
        "activity": activity
        }
