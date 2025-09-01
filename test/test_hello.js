/**
 * Simple test file for Hello World examples
 * This demonstrates basic testing concepts for coding agents
 */

const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');

// Simple test framework
class SimpleTest {
    constructor() {
        this.tests = [];
        this.passed = 0;
        this.failed = 0;
    }

    test(name, fn) {
        this.tests.push({ name, fn });
    }

    async run() {
        console.log('Running Hello World Tests...\n');
        
        for (const test of this.tests) {
            try {
                await test.fn();
                console.log(`✓ ${test.name}`);
                this.passed++;
            } catch (error) {
                console.log(`✗ ${test.name}: ${error.message}`);
                this.failed++;
            }
        }
        
        console.log(`\nResults: ${this.passed} passed, ${this.failed} failed`);
        return this.failed === 0;
    }
}

// Helper function to run command and capture output
function runCommand(command, args = []) {
    return new Promise((resolve, reject) => {
        const parentDir = path.join(__dirname, '..');
        const process = spawn(command, args, { cwd: parentDir });
        let stdout = '';
        let stderr = '';
        
        process.stdout.on('data', (data) => {
            stdout += data.toString();
        });
        
        process.stderr.on('data', (data) => {
            stderr += data.toString();
        });
        
        process.on('close', (code) => {
            if (code === 0) {
                resolve(stdout);
            } else {
                reject(new Error(stderr || `Process exited with code ${code}`));
            }
        });
    });
}

// Test suite
const tester = new SimpleTest();

tester.test('Python Hello World exists and runs', async () => {
    const output = await runCommand('python3', ['hello.py']);
    if (!output.includes('Hello, World!')) {
        throw new Error('Python script did not output expected greeting');
    }
    if (!output.includes('Welcome to the Copilot Testing Repository!')) {
        throw new Error('Python script did not output expected welcome message');
    }
});

tester.test('JavaScript Hello World exists and runs', async () => {
    const output = await runCommand('node', ['hello.js']);
    if (!output.includes('Hello, World!')) {
        throw new Error('JavaScript script did not output expected greeting');
    }
    if (!output.includes('Welcome to the Copilot Testing Repository!')) {
        throw new Error('JavaScript script did not output expected welcome message');
    }
});

tester.test('Java Hello World compiles and runs', async () => {
    // Compile
    await runCommand('javac', ['Hello.java']);
    
    // Run
    const output = await runCommand('java', ['Hello']);
    if (!output.includes('Hello, World!')) {
        throw new Error('Java program did not output expected greeting');
    }
    if (!output.includes('Welcome to the Copilot Testing Repository!')) {
        throw new Error('Java program did not output expected welcome message');
    }
});

tester.test('HTML Hello World file exists', async () => {
    const htmlPath = path.join(__dirname, '..', 'hello.html');
    if (!fs.existsSync(htmlPath)) {
        throw new Error('HTML file does not exist');
    }
    
    const content = fs.readFileSync(htmlPath, 'utf8');
    if (!content.includes('Hello, World!')) {
        throw new Error('HTML file does not contain expected greeting');
    }
    if (!content.includes('Welcome to the Copilot Testing Repository!')) {
        throw new Error('HTML file does not contain expected welcome message');
    }
});

// Run tests
if (require.main === module) {
    tester.run().then(success => {
        process.exit(success ? 0 : 1);
    });
}

module.exports = { SimpleTest, runCommand };