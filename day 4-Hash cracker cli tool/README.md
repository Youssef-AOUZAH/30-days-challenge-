# Hash Cracker CLI Tool

A simple and fast command-line interface tool to crack various types of cryptographic hashes using a dictionary attack. 

## Supported Hashes
The tool can automatically detect and crack the following hash algorithms:
- **MD5**
- **SHA-1**
- **SHA-256**
- **SHA-512**

## Included Example
The directory includes an example dictionary list called `testList.txt` containing a few sample words (including "hello") to help you test the tool immediately.

## Usage

You can run the tool from your terminal by providing the target hash and the path to your dictionary list.

### 1. Auto-Detect Hash Type
If you don't know the hash type, you can omit it. The tool will automatically detect the algorithm based on the hash length and characters.
```bash
python cli.py <hash> --path <path_to_wordlist>
```

### 2. Specifying the Hash Type
If you already know the hash algorithm, you can speed up the process or bypass auto-detection by using the `--type` flag.
```bash
python cli.py <hash> --type <md5|sha1|sha256|sha512> --path <path_to_wordlist>
```

### 3. Example Run
Here is a complete terminal command using the included `testList.txt` to crack a SHA-256 hash (the hash for "hello"):

```bash
python cli.py 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824 --type sha256 --path testList.txt
```

**Expected Output:**
```
Hash Cracker v1.2
Cracking...
A word producing this hash is: hello
```
