#!/bin/bash
# Test script for all hello world programs
# Validates that each implementation outputs the expected "Hello, World!" message

set -e  # Exit on any error

echo "Testing Hello World implementations..."
echo "======================================"

failed_tests=0
total_tests=0

# Function to run a test
run_test() {
    local test_name="$1"
    local command="$2"
    local expected="Hello, World!"
    
    echo -n "Testing $test_name... "
    total_tests=$((total_tests + 1))
    
    if output=$(eval "$command" 2>&1) && [ "$output" = "$expected" ]; then
        echo "✅ PASS"
    else
        echo "❌ FAIL"
        echo "  Expected: '$expected'"
        echo "  Got: '$output'"
        failed_tests=$((failed_tests + 1))
    fi
}

# Test Python
run_test "Python" "python3 hello_world.py"

# Test JavaScript (Node.js)
run_test "JavaScript" "node hello_world.js"

# Test Java
run_test "Java" "javac HelloWorld.java && java HelloWorld"

# Test Bash
run_test "Bash" "./hello_world.sh"

# Test C
run_test "C" "gcc hello_world.c -o hello_world_c && ./hello_world_c"

echo ""
echo "======================================"
echo "Test Summary:"
echo "  Total tests: $total_tests"
echo "  Passed: $((total_tests - failed_tests))"
echo "  Failed: $failed_tests"

if [ $failed_tests -eq 0 ]; then
    echo "🎉 All tests passed!"
    exit 0
else
    echo "💥 Some tests failed!"
    exit 1
fi