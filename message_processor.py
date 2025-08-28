#!/usr/bin/env python3
"""
Message Processor - Coding Agent Demo

This script demonstrates how a coding agent can process different types of content:
- Text messages
- Emoji elements (XML-like format)
- Bot interactions

This serves as a practical example for the copilot-testing-repo demonstration platform.
"""

import re
import sys
from typing import List, Dict, Any


class MessageProcessor:
    """
    A simple message processor that handles text messages, emoji elements, and bot interactions.
    """
    
    def __init__(self):
        self.emoji_map = {
            'smile': '🙂',
            'heart': '❤️',
            'thumbs_up': '👍',
            'wave': '👋',
            'robot': '🤖'
        }
    
    def parse_emoji(self, text: str) -> str:
        """
        Parse emoji elements in the format: <emoji id="smile" alt="🙂" title="Smile"></emoji>
        and replace them with actual emoji characters.
        """
        emoji_pattern = r'<emoji\s+id="([^"]+)"[^>]*></emoji>'
        
        def replace_emoji(match):
            emoji_id = match.group(1)
            return self.emoji_map.get(emoji_id, f':{emoji_id}:')
        
        return re.sub(emoji_pattern, replace_emoji, text)
    
    def process_message(self, message: str) -> Dict[str, Any]:
        """
        Process a single message and return structured information about it.
        """
        original = message.strip()
        processed = self.parse_emoji(original)
        
        # Check if this is a bot interaction
        is_bot_interaction = 'bot' in original.lower()
        
        return {
            'original': original,
            'processed': processed,
            'is_bot_interaction': is_bot_interaction,
            'has_emoji': '<emoji' in original,
            'word_count': len(original.split())
        }
    
    def generate_bot_response(self, message: str) -> str:
        """
        Generate an appropriate bot response for bot interactions.
        """
        message_lower = message.lower()
        
        if 'hello bot' in message_lower:
            return "Hello! 👋 I'm a coding agent demo bot. How can I help you today?"
        elif 'bot' in message_lower:
            return "🤖 Bot here! I'm ready to assist with your coding agent demonstrations."
        else:
            return "Message processed successfully! ✅"
    
    def process_input(self, input_text: str) -> List[Dict[str, Any]]:
        """
        Process multiple lines of input and return results for each message.
        """
        lines = input_text.strip().split('\n')
        results = []
        
        for line in lines:
            if line.strip():  # Skip empty lines
                message_data = self.process_message(line)
                
                # Add bot response if it's a bot interaction
                if message_data['is_bot_interaction']:
                    message_data['bot_response'] = self.generate_bot_response(line)
                
                results.append(message_data)
        
        return results


def main():
    """
    Main function demonstrating the message processor with the given problem statement input.
    """
    processor = MessageProcessor()
    
    # Test input from the problem statement
    test_input = """Some message
Another one
And another one
<emoji id="smile" alt="🙂" title="Smile"></emoji>
hello bot"""
    
    print("=== Coding Agent Message Processor Demo ===\n")
    print("Input:")
    print(test_input)
    print("\n" + "="*50 + "\n")
    
    results = processor.process_input(test_input)
    
    print("Processing Results:")
    for i, result in enumerate(results, 1):
        print(f"\nMessage {i}:")
        print(f"  Original: {result['original']}")
        print(f"  Processed: {result['processed']}")
        print(f"  Word Count: {result['word_count']}")
        print(f"  Has Emoji: {result['has_emoji']}")
        print(f"  Bot Interaction: {result['is_bot_interaction']}")
        
        if 'bot_response' in result:
            print(f"  Bot Response: {result['bot_response']}")
    
    print("\n" + "="*50)
    print("Demo completed! This shows how coding agents can:")
    print("✅ Parse and process different message formats")
    print("✅ Handle emoji elements and convert them to actual emojis")
    print("✅ Detect and respond to bot interactions")
    print("✅ Provide structured output with metadata")


if __name__ == "__main__":
    main()