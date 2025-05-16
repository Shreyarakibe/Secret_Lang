# Secret_Lang
# Secret Language Converter

A Python program that encodes and decodes messages using a custom cipher algorithm.

## How It Works
- **Encoding Rules**:
  - For words with 3+ letters: Moves first letter to end and wraps with "abc" prefix/"xyz" suffix
  - For shorter words: Reverses the word
- **Decoding**: Reverses the encoding process to retrieve original message

## Features
- Simple text-based encoding/decoding
- Preserves word boundaries during conversion
- Handles both short and long words differently
