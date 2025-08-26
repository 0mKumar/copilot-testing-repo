#!/usr/bin/env python3
"""
Demo script that runs the exact commands from the problem statement.
This demonstrates the CLI functionality with the provided command sequence.
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from cli import CopilotCLI


def main():
    """Run the exact command sequence from the problem statement."""
    
    # Exact commands from the problem statement
    problem_statement_commands = [
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
    
    print("=" * 60)
    print("COPILOT TESTING REPOSITORY CLI DEMO")
    print("Running commands from problem statement...")
    print("=" * 60)
    
    cli = CopilotCLI()
    cli.run_batch(problem_statement_commands)
    
    print("\n" + "=" * 60)
    print("Demo completed! All commands executed successfully.")
    print("=" * 60)


if __name__ == "__main__":
    main()