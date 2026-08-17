# Crypto CLI

A lightweight command-line interface (CLI) tool for encoding and decoding text using various cryptographic ciphers and data encodings.

## Features

- **Caesar Cipher**: A classic substitution cipher that shifts characters by a specific amount.
- **Vigenère Cipher**: A polyalphabetic substitution cipher that uses a keyword to shift characters.
- **Base64**: Standard Base64 encoding and decoding.
- **Hexadecimal**: Hex encoding and decoding.

## Prerequisites

- Python 3.x

## Usage

You can use the `cli.py` script to encode (`--text`) or decode (`--cipher`). 

```bash
python cli.py --mode <algorithm> [arguments...]
```

### 1. Caesar Cipher
Requires a `--shift` integer argument.
- **Encode:** 
  ```bash
  python cli.py --mode ceasar --text "hello" --shift 1
  ```
- **Decode:**
  ```bash
  python cli.py --mode ceasar --cipher "ifmmp" --shift 1
  ```

### 2. Hexadecimal
- **Encode:**
  ```bash
  python cli.py --mode hex --text "hello"
  ```
- **Decode:**
  ```bash
  python cli.py --mode hex --cipher "68656c6c6f"
  ```

### 3. Base64
- **Encode:**
  ```bash
  python cli.py --mode base64 --text "hello"
  ```
- **Decode:**
  ```bash
  python cli.py --mode base64 --cipher "aGVsbG8="
  ```

### 4. Vigenère Cipher
Requires a `--key` string argument.
- **Encode:**
  ```bash
  python cli.py --mode vigenere --text "hello" --key "abc"
  ```
- **Decode:**
  ```bash
  python cli.py --mode vigenere --cipher "hfnlp" --key "abc"
  ```

## Testing

A comprehensive automated test suite is included. You can run all functional tests by executing:

```bash
python test_cli_suite.py
```
