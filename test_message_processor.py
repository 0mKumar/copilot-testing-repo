#!/usr/bin/env python3
"""
Test suite for the Message Processor - Coding Agent Demo

This demonstrates how coding agents can create comprehensive test cases
to validate functionality and ensure code quality.
"""

import unittest
from message_processor import MessageProcessor


class TestMessageProcessor(unittest.TestCase):
    """Test cases for the MessageProcessor class."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.processor = MessageProcessor()
    
    def test_simple_message_processing(self):
        """Test processing of simple text messages."""
        result = self.processor.process_message("Hello world")
        
        self.assertEqual(result['original'], "Hello world")
        self.assertEqual(result['processed'], "Hello world")
        self.assertEqual(result['word_count'], 2)
        self.assertFalse(result['has_emoji'])
        self.assertFalse(result['is_bot_interaction'])
    
    def test_emoji_parsing(self):
        """Test emoji element parsing and conversion."""
        input_text = '<emoji id="smile" alt="🙂" title="Smile"></emoji>'
        result = self.processor.process_message(input_text)
        
        self.assertEqual(result['processed'], '🙂')
        self.assertTrue(result['has_emoji'])
        
    def test_unknown_emoji(self):
        """Test handling of unknown emoji IDs."""
        input_text = '<emoji id="unknown" alt="?" title="Unknown"></emoji>'
        result = self.processor.process_message(input_text)
        
        self.assertEqual(result['processed'], ':unknown:')
        self.assertTrue(result['has_emoji'])
    
    def test_bot_interaction_detection(self):
        """Test detection of bot interactions."""
        test_cases = [
            ("hello bot", True),
            ("Hello Bot", True),
            ("ask the bot", True),
            ("regular message", False),
        ]
        
        for message, expected in test_cases:
            with self.subTest(message=message):
                result = self.processor.process_message(message)
                self.assertEqual(result['is_bot_interaction'], expected)
    
    def test_bot_response_generation(self):
        """Test bot response generation."""
        response = self.processor.generate_bot_response("hello bot")
        self.assertIn("Hello!", response)
        self.assertIn("👋", response)
        
        response = self.processor.generate_bot_response("talk to bot")
        self.assertIn("Bot here!", response)
        self.assertIn("🤖", response)
    
    def test_multiple_message_processing(self):
        """Test processing multiple messages."""
        input_text = """Message one
<emoji id="heart" alt="❤️" title="Heart"></emoji>
hello bot"""
        
        results = self.processor.process_input(input_text)
        
        self.assertEqual(len(results), 3)
        self.assertEqual(results[0]['processed'], "Message one")
        self.assertEqual(results[1]['processed'], "❤️")
        self.assertTrue(results[2]['is_bot_interaction'])
        self.assertIn('bot_response', results[2])
    
    def test_empty_input_handling(self):
        """Test handling of empty or whitespace-only input."""
        results = self.processor.process_input("   \n  \n  ")
        self.assertEqual(len(results), 0)
    
    def test_emoji_map(self):
        """Test that emoji mapping works for known emojis."""
        known_emojis = ['smile', 'heart', 'thumbs_up', 'wave', 'robot']
        
        for emoji_id in known_emojis:
            input_text = f'<emoji id="{emoji_id}" alt="test" title="test"></emoji>'
            result = self.processor.process_message(input_text)
            
            # Should not contain the original emoji_id wrapped in colons
            self.assertNotEqual(result['processed'], f':{emoji_id}:')
            # Should contain an actual emoji character
            self.assertTrue(len(result['processed']) > 0)


def run_tests():
    """Run the test suite and display results."""
    print("=== Running Message Processor Tests ===\n")
    
    # Create test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMessageProcessor)
    
    # Run tests with verbose output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print(f"\n=== Test Summary ===")
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    if result.wasSuccessful():
        print("✅ All tests passed!")
    else:
        print("❌ Some tests failed.")
        
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tests()
    exit(0 if success else 1)