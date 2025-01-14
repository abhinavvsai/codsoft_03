import random
import string

def generate_password(length):
    # Define the characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    
    # Prompt the user to specify the desired length of the password
    while True:
        try:
            length = int(input("Enter the desired length for the password: "))
            if length < 1:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    # Generate the password
    password = generate_password(length)
    
    # Display the generated password
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
