def validate_password(password):
  valid_password = True
  minimum_password_length = 6

  # check minimum length
  if (len(password) < minimum_password_length):
    valid_password = False
  
  # check for digit
  if not any(char.isdigit() for char in password):
    valid_password = False
  
  return valid_password