#!/usr/bin/env python3
"""
Usage Examples for Message Processor - Coding Agent Demo

This file demonstrates various ways to use the MessageProcessor class
and showcases different coding agent capabilities.
"""

from message_processor import MessageProcessor


def basic_usage_example():
    """Demonstrate basic message processing functionality."""
    print("=== Basic Usage Example ===\n")
    
    processor = MessageProcessor()
    
    # Process individual messages
    messages = [
        "Welcome to the demo!",
        '<emoji id="wave" alt="👋" title="Wave"></emoji>',
        "hello bot",
        "This is a <emoji id=\"heart\" alt=\"❤️\" title=\"Heart\"></emoji> message"
    ]
    
    for msg in messages:
        result = processor.process_message(msg)
        print(f"Input:  {result['original']}")
        print(f"Output: {result['processed']}")
        if 'bot_response' in result:
            print(f"Bot:    {result['bot_response']}")
        print()


def bulk_processing_example():
    """Demonstrate processing multiple messages at once."""
    print("=== Bulk Processing Example ===\n")
    
    processor = MessageProcessor()
    
    bulk_input = """Welcome to our service!
<emoji id="robot" alt="🤖" title="Robot"></emoji> Coding Agent Active
How can I help you today?
hello bot
<emoji id="thumbs_up" alt="👍" title="Thumbs Up"></emoji> Great job!"""
    
    results = processor.process_input(bulk_input)
    
    print("Bulk processing results:")
    for i, result in enumerate(results, 1):
        print(f"{i}. {result['processed']}")
        if 'bot_response' in result:
            print(f"   Bot: {result['bot_response']}")
    print()


def interactive_example():
    """Demonstrate interactive usage with user input."""
    print("=== Interactive Example ===\n")
    
    processor = MessageProcessor()
    
    print("Enter messages to process (empty line to finish):")
    print("Try including emoji elements like: <emoji id=\"smile\" alt=\"🙂\" title=\"Smile\"></emoji>")
    print("Or bot interactions like: hello bot\n")
    
    messages = []
    while True:
        try:
            user_input = input("> ")
            if not user_input.strip():
                break
            messages.append(user_input)
        except (EOFError, KeyboardInterrupt):
            break
    
    if messages:
        print("\nProcessing your messages:")
        for msg in messages:
            result = processor.process_message(msg)
            print(f"You: {result['original']}")
            print(f"Processed: {result['processed']}")
            if 'bot_response' in result:
                print(f"Bot: {result['bot_response']}")
            print()
    else:
        print("No messages entered.")


def emoji_showcase():
    """Showcase all available emoji mappings."""
    print("=== Available Emoji Showcase ===\n")
    
    processor = MessageProcessor()
    
    print("Available emoji IDs and their mappings:")
    for emoji_id, emoji_char in processor.emoji_map.items():
        emoji_element = f'<emoji id="{emoji_id}" alt="{emoji_char}" title="{emoji_id.title()}"></emoji>'
        result = processor.process_message(emoji_element)
        print(f"  {emoji_id}: {emoji_element} → {result['processed']}")
    print()


def main():
    """Run all examples."""
    print("🤖 Message Processor Usage Examples\n")
    print("This demonstrates various coding agent capabilities:")
    print("- Message parsing and processing")
    print("- Emoji element handling")
    print("- Bot interaction detection")
    print("- Structured data output\n")
    
    basic_usage_example()
    bulk_processing_example()
    emoji_showcase()
    
    # Only run interactive example if we're in an interactive terminal
    import sys
    if sys.stdin.isatty():
        interactive_example()
    else:
        print("=== Interactive Example ===")
        print("(Skipped - not in interactive terminal)\n")
    
    print("=== Examples Complete ===")
    print("This showcases how coding agents can create comprehensive,")
    print("well-documented examples that help users understand functionality!")


if __name__ == "__main__":
    main()