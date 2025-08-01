# Random Password Generator

A Python script that generates secure, customizable passwords using cryptographic-strength randomness.

## Features

- Generates passwords with customizable length (default: 12 chars)
- Includes uppercase, lowercase, numbers, and special characters
- Uses cryptographically secure secrets module (not random)
- Simple CLI interface (easy to extend to GUI)

## Quick Start

```bash
python password_generator.py
```

## Customization

Modify the generate_password() function to:

```bash
# Generate a 16-character password without special chars
print(generate_password(length=16, use_special_chars=False))
```

## How It Works

- Character Pool: Combines ASCII letters, digits, and punctuation
- Secure Selection: Uses secrets.choice() for cryptographically strong randomness
- Flexibility: Parameters control length and character sets

## Future Improvements

- Add GUI interface (Tkinter)
- Implement password strength meter
- Add copy-to-clipboard functionality
- Save password history (encrypted)

## Dependencies

None required (uses Python's built-in secrets and string modules)
