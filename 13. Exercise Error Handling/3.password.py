class PasswordTooShortError(Exception):
    pass

class PasswordTooCommonError(Exception):
    pass

class PasswordNoSpecialCharactersError(Exception):
    pass

class PasswordContainsSpacesError(Exception):
    pass

def common_not(pwd, spec):
    only_digits = pwd.isdigit()
    only_letters = pwd.isalpha()
    only_special_chars = all(ch in spec for ch in pwd)
    return only_digits or only_letters or only_special_chars

PWD_LEN = 8
CHARS_PWD = [ "@", "*", "&", "%"]

while True:
    password = input()
    if password == "Done":
        break
    
    if len(password) < PWD_LEN:
        raise PasswordTooShortError("Password must contain at least 8 characters")
    
    if common_not(password, CHARS_PWD):
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")
    
    if not any(ch in CHARS_PWD for ch in password):
        raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")
    
    if " " in password:
        raise PasswordContainsSpacesError("Password must not contain empty spaces")
    
    print("Password is valid")
    
    
    