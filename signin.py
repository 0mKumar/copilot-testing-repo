#!/usr/bin/env python3
"""
Simple signin module with hello greeting functionality
"""


def signin(username):
    """
    Sign in a user and return a greeting message
    
    Args:
        username (str): The username to sign in
        
    Returns:
        str: A hello greeting message
    """
    if not username or not username.strip():
        return "Error: Username cannot be empty"
    
    return f"Hello, {username}! You have successfully signed in."


def main():
    """Main function to run the signin process"""
    print("=== Signin System ===")
    username = input("Enter your username: ")
    message = signin(username)
    print(message)


if __name__ == "__main__":
    main()
