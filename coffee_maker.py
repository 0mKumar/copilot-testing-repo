#!/usr/bin/env python3
"""
Coffee Maker Simulation
A simple program to simulate the process of making a cup of coffee.
"""

import time
import random
from typing import Dict, Tuple


class CoffeeMaker:
    """A simple coffee maker simulation class."""
    
    def __init__(self):
        """Initialize the coffee maker with default settings."""
        self.water_level = 100  # percentage
        self.coffee_grounds = 50  # grams available
        self.is_on = False
        self.temperature = 20  # Celsius, room temperature
        
    def check_ingredients(self, cups: int = 1) -> Tuple[bool, str]:
        """
        Check if we have enough ingredients to make coffee.
        
        Args:
            cups: Number of cups to make
            
        Returns:
            Tuple of (success, message)
        """
        water_needed = cups * 250  # 250ml per cup
        grounds_needed = cups * 15  # 15g per cup
        
        if self.water_level < water_needed / 10:  # Convert to percentage
            return False, f"Not enough water! Need {water_needed}ml, have {self.water_level * 10}ml"
        
        if self.coffee_grounds < grounds_needed:
            return False, f"Not enough coffee grounds! Need {grounds_needed}g, have {self.coffee_grounds}g"
            
        return True, "All ingredients available"
    
    def heat_water(self) -> None:
        """Heat water to optimal brewing temperature."""
        print("🔥 Heating water...")
        target_temp = 93  # Optimal brewing temperature
        
        while self.temperature < target_temp:
            time.sleep(0.1)  # Simulate heating time
            self.temperature += random.randint(5, 10)
            if self.temperature <= target_temp:
                print(f"   Temperature: {self.temperature}°C")
        
        self.temperature = target_temp
        print(f"✓ Water heated to optimal temperature: {self.temperature}°C")
    
    def brew_coffee(self, cups: int = 1) -> None:
        """
        Simulate the coffee brewing process.
        
        Args:
            cups: Number of cups to brew
        """
        grounds_used = cups * 15
        water_used = cups * 25  # 25% of water level per cup
        
        print(f"☕ Brewing {cups} cup(s) of coffee...")
        print(f"   Using {grounds_used}g of coffee grounds")
        print(f"   Using {water_used * 10}ml of water")
        
        # Simulate brewing time
        brew_time = cups * 3  # 3 seconds per cup for simulation
        for i in range(brew_time):
            time.sleep(0.5)
            print("   .", end="", flush=True)
        print()
        
        # Update resources
        self.coffee_grounds -= grounds_used
        self.water_level -= water_used
        
        print(f"✓ Coffee brewing complete!")
        print(f"   Remaining coffee grounds: {self.coffee_grounds}g")
        print(f"   Remaining water: {self.water_level}%")
    
    def serve_coffee(self, cups: int = 1) -> str:
        """
        Serve the freshly brewed coffee.
        
        Args:
            cups: Number of cups to serve
            
        Returns:
            A nice message about the served coffee
        """
        coffee_types = [
            "aromatic Colombian blend",
            "rich French roast", 
            "smooth medium roast",
            "bold dark roast",
            "delicate light roast"
        ]
        
        coffee_type = random.choice(coffee_types)
        
        print(f"🍃 Serving {cups} cup(s) of {coffee_type}")
        
        if cups == 1:
            return f"☕ Here's your perfect cup of {coffee_type}! Enjoy!"
        else:
            return f"☕ Here are your {cups} cups of {coffee_type}! Enjoy!"
    
    def make_coffee(self, cups: int = 1) -> str:
        """
        Complete coffee making process.
        
        Args:
            cups: Number of cups to make
            
        Returns:
            Final message about the coffee
        """
        print(f"🚀 Starting coffee maker to prepare {cups} cup(s)...")
        
        # Turn on coffee maker
        if not self.is_on:
            print("   Turning on coffee maker...")
            self.is_on = True
            time.sleep(0.5)
        
        # Check ingredients
        print("📋 Checking ingredients...")
        success, message = self.check_ingredients(cups)
        if not success:
            return f"❌ Cannot make coffee: {message}"
        
        print(f"✓ {message}")
        
        # Heat water
        self.heat_water()
        
        # Brew coffee
        self.brew_coffee(cups)
        
        # Serve coffee
        result = self.serve_coffee(cups)
        
        print("✨ Coffee making process complete!")
        return result


def main():
    """Main function to demonstrate the coffee maker."""
    print("☕ Welcome to the Coffee Maker Simulator!")
    print("=" * 50)
    
    # Create coffee maker
    coffee_maker = CoffeeMaker()
    
    try:
        # Make a single cup of coffee
        result = coffee_maker.make_coffee(1)
        print("\n" + result)
        
        print("\n" + "=" * 50)
        print("Thanks for using the Coffee Maker Simulator!")
        
    except KeyboardInterrupt:
        print("\n☕ Coffee making cancelled. Come back when you need caffeine!")
    except Exception as e:
        print(f"\n❌ Error making coffee: {e}")


if __name__ == "__main__":
    main()