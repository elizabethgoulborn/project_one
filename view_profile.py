# View profile: This function aims to allow a user to view a profile
# Eliza Goulborn
# 29.09.2025

def view_profile(user_bank,profile):
	if profile in user_bank:
		if user_bank[profile] == {}:
			print("\n\n~~User data has not been uploaded.~~")
		else:
			print("\n Here is " + profile + "'s profile:")
			print(user_bank[profile])
	else:
		print("\n~~USER NOT FOUND~~")
	
