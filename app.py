import random
import string
import re
import sys


def get_valid_input(prompt, validation_func, error_message):
    """Function to get valid input based on a validation function."""
    while True:
        user_input = input(prompt).strip()  # Remove leading and trailing whitespace
        if validation_func(user_input):
            return user_input
        else:
            print(error_message)

def is_alpha(input_str):
    """Check if the input contains only alphabetic characters."""
    return input_str.isalpha()

def is_digit(input_str):
    """Check if the input contains only digit characters."""
    return input_str.isdigit()

def get_name():
    """Prompt the user to enter a valid name."""
    return get_valid_input(
        prompt="What is your name:\n",
        validation_func=is_alpha,
        error_message="Please enter only letters. Expected input!"
    )

def get_age():
    """Prompt the user to enter a valid age."""
    return get_valid_input(
        prompt="How old are you:\n",
        validation_func=is_digit,
        error_message="Enter a valid number for your age."
    )

def get_gender():
    """Prompt the user to enter a valid gender."""
    valid_genders = {'man', 'woman', 'male', 'female', 'm', 'f'}
    
    def is_valid_gender(input_str):
        """Check if the gender input is valid."""
        return input_str.lower() in valid_genders

    gender = get_valid_input(
        prompt="Are you a man or a woman?\n",
        validation_func=is_valid_gender,
        error_message="Enter a valid gender (man/woman)."
    )
    
    return 'man' if gender.lower() in {'man', 'male', 'm'} else 'woman'

def main():
    name = get_name()
    print(f"Welcome, {name}!")

    age = get_age()
    print(f"Ok {name}, you are {age} years old!")

    gender = get_gender()
    print(f"Your name is {name}, you are {age} years old, and you are a {gender}. Great!")

    saved_data_list = [name, age, gender]
    print(f"Data saved: {saved_data_list}")

if __name__ == "__main__":
    main()
















    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    main()





















