
# RC4 Encryption Algorithm Implementation #

This project implements the RC4 encryption algorithm, following the steps described below. The implementation includes key scheduling, pseudorandom byte generation, and XOR-based encryption of a given string. The output includes the initial string, pseudorandom bytes, and the encrypted result.

## RC4 Algorithm Overview

1. **S-box Initialization and Scrambling:**
   The S-box is initialized as a list of integers from 0 to 255. The key scheduling algorithm (KSA) scrambles this S-box using the provided key.

2. **Pseudorandom Byte Generation:**
   Once the key is scheduled, the pseudorandom stream generation (PRGA) starts. This produces a stream of pseudorandom bytes from the scrambled S-box.

3. **Encryption:**
   The plaintext is XORed with the pseudorandom byte stream to produce the ciphertext. The same process can be used to decrypt the ciphertext back into the plaintext.

### Steps Performed in the Code

1. **Key Scheduling (KSA):**
   - The S-box (`s`) is initialized to the values 0-255.
   - The key (stored in the `key` variable) is encoded into bytes and repeatedly appended to the `schedule` array until it has at least 256 bytes.
   - The S-box is scrambled using the key bytes by repeatedly swapping elements in the S-box, depending on the key values.

2. **Pseudorandom Byte Stream Generation (PRGA):**
   - After the S-box is scrambled, 256 bytes are generated and discarded from the pseudorandom stream to further randomize the state.
   - Subsequent calls to `randomByte()` will return one pseudorandom byte at a time.

3. **Encryption Process:**
   - The plaintext (stored in the `string` variable) is first converted to a byte array using `.encode('utf-8')`.
   - Each byte in the plaintext is XORed with a byte from the pseudorandom stream to produce the encrypted ciphertext.
   
### How It Works

1. **S-box Initialization:**
   The S-box is initialized with values from 0 to 255:
   ```python
   s = [0, 1, 2, ..., 255]
   ```

2. **Key Scheduling (scramble method):**
   The key (hardcoded as `"cis350"`) is encoded to bytes and used to shuffle the S-box:
   ```python
   key = "cis350"
   scramble(key)
   ```

3. **Discarding 256 Bytes:**
   The pseudorandom stream generates and discards the first 256 bytes as follows:
   ```python
   for i in range(256):
       randomByte()
   ```

4. **Encrypting the String:**
   The plaintext (hardcoded as `"Assignment 2"`) is encrypted by XORing it with bytes from the pseudorandom stream:
   ```python
   string = "Assignment 2"
   encrypted = encrpyt(key, string)
   ```

### Example Output

Given the key `"cis350"` and the string `"Assignment 2"`, the program will output:
1. **Initial string:** (The byte representation of the plaintext)
   ```
   [65, 115, 115, 105, 103, 110, 109, 101, 110, 116, 32, 50]
   ```
2. **Pseudorandom stream:** (The generated pseudorandom byte stream)
   ```
   [63, 149, 233, ...]
   ```
3. **Encrypted bytes:** (Result of XORing the plaintext bytes with the pseudorandom bytes)
   ```
   [126, 6, 154, ...]
   ```

### How to Run

1. Clone the repository.
2. Make sure you have Python installed on your machine.
3. Run the script with Python:
   ```bash
   python rc4.py
   ```

### Future Improvements

- Add support for command-line arguments to accept dynamic keys and messages for encryption.
- Implement decryption to verify that the ciphertext can be restored to its original form.
