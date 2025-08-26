#!/usr/bin/env python3
"""
Simple CLI application for the Copilot Testing Repository Demo.
Handles commands: help, hello world, verify, signin
"""

import sys
import re
from datetime import datetime


class CopilotCLI:
    def __init__(self):
        self.authenticated = False
        self.commands = {
            'help': self.show_help,
            'hello': self.hello_world,
            'verify': self.verify_command,
            'signin': self.signin_command,
            'exit': self.exit_command,
            'quit': self.exit_command,
        }

    def show_help(self, *args):
        """Display available commands and usage information."""
        help_text = """
Copilot Testing Repository CLI - Available Commands:

  help                    Show this help message
  hello world            Display a hello world greeting
  verify <id>:<uuid>     Verify an ID with UUID format
  signin                 Sign in to the system
  exit/quit              Exit the CLI

Examples:
  hello world
  verify 304485:ca56d739-d144-4e84-a7ae-76c8da73214c
  signin

This CLI demonstrates basic command processing for coding agent testing.
        """
        print(help_text.strip())

    def hello_world(self, *args):
        """Display hello world message."""
        print("Hello world! Welcome to the coding agent demonstration repository.")
        print("This is a simple greeting from the Copilot Testing CLI.")

    def verify_command(self, *args):
        """Handle verification command with ID:UUID format."""
        if not args:
            print("Error: verify command requires an argument in format <id>:<uuid>")
            print("Example: verify 304485:ca56d739-d144-4e84-a7ae-76c8da73214c")
            return

        verify_string = ' '.join(args)
        
        # Check if it matches the expected format: number:uuid
        pattern = r'^(\d+):([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})$'
        match = re.match(pattern, verify_string)
        
        if match:
            id_part, uuid_part = match.groups()
            print(f"✓ Verification successful!")
            print(f"  ID: {id_part}")
            print(f"  UUID: {uuid_part}")
            print(f"  Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        else:
            print("✗ Verification failed!")
            print("Expected format: <id>:<uuid>")
            print("Example: 304485:ca56d739-d144-4e84-a7ae-76c8da73214c")

    def signin_command(self, *args):
        """Handle signin command."""
        if self.authenticated:
            print("Already signed in!")
            return
        
        print("Signing in...")
        # Simulate signin process
        self.authenticated = True
        print("✓ Successfully signed in to Copilot Testing Repository CLI")
        print("You now have access to all features.")

    def exit_command(self, *args):
        """Exit the CLI."""
        print("Goodbye! Thanks for using Copilot Testing Repository CLI.")
        sys.exit(0)

    def process_command(self, command_line):
        """Process a single command line."""
        if not command_line.strip():
            return

        parts = command_line.strip().split()
        command = parts[0].lower()
        args = parts[1:]

        # Handle special case for "hello world"
        if command == 'hello' and args and args[0].lower() == 'world':
            self.hello_world()
            return

        if command in self.commands:
            self.commands[command](*args)
        else:
            print(f"Unknown command: {command}")
            print("Type 'help' for available commands.")

    def run_interactive(self):
        """Run the CLI in interactive mode."""
        print("Welcome to Copilot Testing Repository CLI!")
        print("Type 'help' for available commands or 'exit' to quit.")
        
        while True:
            try:
                command = input("\n> ").strip()
                if command:
                    self.process_command(command)
            except KeyboardInterrupt:
                print("\n\nExiting...")
                break
            except EOFError:
                print("\nExiting...")
                break

    def run_batch(self, commands):
        """Run commands from a list (for testing/automation)."""
        for command in commands:
            print(f"> {command}")
            self.process_command(command)


def main():
    """Main entry point."""
    cli = CopilotCLI()
    
    if len(sys.argv) > 1:
        # Run commands from command line arguments
        command = ' '.join(sys.argv[1:])
        cli.process_command(command)
    else:
        # Run in interactive mode
        cli.run_interactive()


if __name__ == "__main__":
    main()