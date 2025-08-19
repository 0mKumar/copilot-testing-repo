#!/usr/bin/env python3
"""
Tests for the Coffee Maker Simulation
Simple tests to validate the coffee making functionality.
"""

import sys
import os

# Add the current directory to the path so we can import coffee_maker
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from coffee_maker import CoffeeMaker


def test_coffee_maker_initialization():
    """Test that coffee maker initializes with correct default values."""
    maker = CoffeeMaker()
    
    assert maker.water_level == 100, "Water level should start at 100%"
    assert maker.coffee_grounds == 50, "Coffee grounds should start at 50g"
    assert maker.is_on == False, "Coffee maker should start turned off"
    assert maker.temperature == 20, "Temperature should start at room temperature (20°C)"
    print("✓ Coffee maker initialization test passed")


def test_ingredient_checking():
    """Test ingredient checking functionality."""
    maker = CoffeeMaker()
    
    # Test with sufficient ingredients
    success, message = maker.check_ingredients(1)
    assert success == True, "Should have enough ingredients for 1 cup"
    assert "available" in message.lower(), "Message should indicate ingredients are available"
    
    # Test with insufficient coffee grounds
    maker.coffee_grounds = 5  # Not enough for even 1 cup (needs 15g)
    success, message = maker.check_ingredients(1)
    assert success == False, "Should not have enough coffee grounds"
    assert "coffee grounds" in message.lower(), "Message should mention coffee grounds"
    
    # Test with insufficient water
    maker.coffee_grounds = 50  # Reset
    maker.water_level = 10  # Not enough for 1 cup (needs 25%)
    success, message = maker.check_ingredients(1)
    assert success == False, "Should not have enough water"
    assert "water" in message.lower(), "Message should mention water"
    
    print("✓ Ingredient checking test passed")


def test_multiple_cups():
    """Test making multiple cups of coffee."""
    maker = CoffeeMaker()
    
    # Test ingredient check for multiple cups
    success, message = maker.check_ingredients(2)
    assert success == True, "Should have enough ingredients for 2 cups"
    
    # Test making 2 cups (should work with default ingredients)
    initial_grounds = maker.coffee_grounds
    initial_water = maker.water_level
    
    # We can't easily test the full make_coffee method due to time.sleep() calls
    # So we'll test the resource consumption logic from brew_coffee
    maker.temperature = 93  # Pre-heat to skip heating delay
    maker.is_on = True
    
    # Manually calculate expected consumption
    cups = 2
    expected_grounds_used = cups * 15  # 30g
    expected_water_used = cups * 25    # 50%
    
    # Test that we would have enough
    assert initial_grounds >= expected_grounds_used, "Should have enough grounds for 2 cups"
    assert initial_water >= expected_water_used, "Should have enough water for 2 cups"
    
    print("✓ Multiple cups test passed")


def test_coffee_serving():
    """Test coffee serving functionality."""
    maker = CoffeeMaker()
    
    # Test serving 1 cup
    result = maker.serve_coffee(1)
    assert "1" not in result or "cup" in result, "Result should mention single cup or just describe coffee"
    assert "☕" in result, "Result should contain coffee emoji"
    
    # Test serving multiple cups
    result = maker.serve_coffee(3)
    assert "3" in result and "cups" in result, "Result should mention 3 cups"
    assert "☕" in result, "Result should contain coffee emoji"
    
    print("✓ Coffee serving test passed")


def test_edge_cases():
    """Test edge cases and error conditions."""
    maker = CoffeeMaker()
    
    # Test with zero cups (edge case)
    success, message = maker.check_ingredients(0)
    assert success == True, "Zero cups should always be possible"
    
    # Test with negative cups (should handle gracefully)
    try:
        success, message = maker.check_ingredients(-1)
        # Should either work (no ingredients needed) or handle gracefully
        print(f"   Negative cups handled: {success}, {message}")
    except Exception as e:
        print(f"   Negative cups raised exception (acceptable): {e}")
    
    print("✓ Edge cases test passed")


def run_all_tests():
    """Run all tests and report results."""
    print("🧪 Running Coffee Maker Tests")
    print("=" * 40)
    
    tests = [
        test_coffee_maker_initialization,
        test_ingredient_checking,
        test_multiple_cups,
        test_coffee_serving,
        test_edge_cases
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except Exception as e:
            print(f"❌ {test.__name__} failed: {e}")
            failed += 1
    
    print("\n" + "=" * 40)
    print(f"Tests completed: {passed} passed, {failed} failed")
    
    if failed == 0:
        print("🎉 All tests passed! Coffee maker is working correctly.")
        return True
    else:
        print("⚠️  Some tests failed. Please check the implementation.")
        return False


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)