#!/usr/bin/env python3
"""
Coffee Maker Demo
A simple demonstration script showing how to use the coffee maker programmatically.
"""

from coffee_maker import CoffeeMaker


def demo_basic_usage():
    """Demonstrate basic coffee making."""
    print("🎯 DEMO 1: Basic Coffee Making")
    print("-" * 30)
    
    maker = CoffeeMaker()
    result = maker.make_coffee(1)
    print(f"\nResult: {result}")


def demo_multiple_cups():
    """Demonstrate making multiple cups."""
    print("\n🎯 DEMO 2: Making Multiple Cups")
    print("-" * 30)
    
    maker = CoffeeMaker()
    result = maker.make_coffee(2)
    print(f"\nResult: {result}")


def demo_resource_management():
    """Demonstrate resource depletion and error handling."""
    print("\n🎯 DEMO 3: Resource Management")
    print("-" * 30)
    
    maker = CoffeeMaker()
    
    # Deplete coffee grounds
    maker.coffee_grounds = 10  # Not enough for 1 cup
    
    print("Attempting to make coffee with insufficient grounds...")
    result = maker.make_coffee(1)
    print(f"Result: {result}")


def demo_programmatic_coffee_making():
    """Show how to use the coffee maker in other programs."""
    print("\n🎯 DEMO 4: Programmatic Usage")
    print("-" * 30)
    
    maker = CoffeeMaker()
    
    # Check if we can make coffee before trying
    cups_wanted = 1
    can_make, message = maker.check_ingredients(cups_wanted)
    
    if can_make:
        print(f"✅ Can make {cups_wanted} cup(s): {message}")
        result = maker.make_coffee(cups_wanted)
        print(f"Final result: {result}")
    else:
        print(f"❌ Cannot make coffee: {message}")


if __name__ == "__main__":
    print("☕ Coffee Maker Demonstration")
    print("=" * 50)
    print("This script shows different ways to use the coffee maker.\n")
    
    # Run all demonstrations
    demo_basic_usage()
    demo_multiple_cups()
    demo_resource_management()
    demo_programmatic_coffee_making()
    
    print("\n" + "=" * 50)
    print("🎉 Demo complete! Check out coffee_maker.py for the full implementation.")