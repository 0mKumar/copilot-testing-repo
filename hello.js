/**
 * Simple Hello World example in JavaScript
 * This demonstrates basic JavaScript syntax and console output
 */

function main() {
    console.log("Hello, World!");
    console.log("Welcome to the Copilot Testing Repository!");
    
    // Demonstrate basic variables and template literals
    const name = "Coding Agent";
    const message = `Greetings from ${name}!`;
    console.log(message);
}

// Run the main function
main();

// Export for potential module usage
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { main };
}