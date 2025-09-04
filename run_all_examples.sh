#!/bin/bash
# Run all hello world examples
# This script demonstrates how coding agents can create automation tools

echo "=== Running Hello World Examples ==="
echo

echo "Python:"
python3 hello.py
echo

echo "JavaScript (Node.js):"
node hello.js
echo

echo "Go:"
go run hello.go
echo

echo "Java:"
javac Hello.java && java Hello
echo

echo "=== All examples completed! ==="