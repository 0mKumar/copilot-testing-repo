#!/usr/bin/env python3
"""
Test script for the Copilot CLI application.
Tests the exact commands from the problem statement.
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from cli import CopilotCLI


def test_problem_statement_commands():
    """Test the exact sequence of commands from the problem statement."""
    
    # Commands from the problem statement
    commands = [
        "help",
        "hello world", 
        "verify 304485:ca56d739-d144-4e84-a7ae-76c8da73214c",
        "signin",
        "help",
        "signin",
        "help",
        "help",
        "help",
        "help",
        "help",
        "help"
    ]
    
    print("Testing Copilot CLI with problem statement commands...")
    print("=" * 60)
    
    cli = CopilotCLI()
    
    for i, command in enumerate(commands, 1):
        print(f"\n[Test {i}] Command: {command}")
        print("-" * 40)
        cli.process_command(command)
    
    print("\n" + "=" * 60)
    print("All problem statement commands have been tested!")


def test_individual_commands():
    """Test individual command functionality."""
    print("\nTesting individual command functionality...")
    print("=" * 60)
    
    cli = CopilotCLI()
    
    # Test cases
    test_cases = [
        ("help", "Should show help message"),
        ("hello world", "Should display hello world greeting"),
        ("verify 123:abc", "Should fail - invalid UUID format"),
        ("verify 304485:ca56d739-d144-4e84-a7ae-76c8da73214c", "Should succeed"),
        ("signin", "Should sign in successfully"),
        ("signin", "Should indicate already signed in"),
        ("unknown_command", "Should show unknown command message"),
    ]
    
    for command, description in test_cases:
        print(f"\nTest: {command}")
        print(f"Expected: {description}")
        print("-" * 40)
        cli.process_command(command)


if __name__ == "__main__":
    # Run tests
    test_problem_statement_commands()
    test_individual_commands()