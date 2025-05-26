def check_case(char):
    if char.isupper():
        return "Uppercase"
    elif char.islower():
        return "Lowercase"
    else:
        return "Neither uppercase nor lowercase"
    
char = input("Enter a single character:")
if len(char) == 1:
    print(f"The character '{char}' is {check_case(char)}.")
else:
    print("Please enter exactly one character.")