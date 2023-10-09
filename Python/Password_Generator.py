import string 
import random

if __name__ == "___main___":
    LOWERCASE_LETTER = string.ascii_lowercase
    UPPERCASE_LETTER = string.ascii_uppercase
    DIGITS = string.digits
    SPECIAL_CHAR = string.punctuation
    
    password_length = 12
    arr = []
    arr.extend(list(LOWERCASE_LETTER))
    arr.extend(list(UPPERCASE_LETTER))
    arr.extend(list(DIGITS))
    arr.extend(list(SPECIAL_CHAR))
    
    print("The generated : ")
    print("".join(random.sample(arr,password_length)))
