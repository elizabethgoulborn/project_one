# Create a verification function to check username compatability.
# Elizabeth Goulborn
# 28.09.2025

def verify(user, user_bank):
	"""Defines whether or not a given username can be added to the user bank."""
	verity = True
		
	# If username is already in the name bank, reject.
	if user in user_bank:
		verity = False
		reject_reason = "Username already taken"
		return verity, reject_reason
		
	# If username does not meet rules, reject.
	elif len(user) > 16:
		verity = False
		reject_reason = "Username too long"
		return verity, reject_reason
		
	elif " " in user:
		verity = False
		reject_reason = "Space(s) detected"
		return verity, reject_reason
		
	# If username meets all rules, return True
	else:
		return verity, None
