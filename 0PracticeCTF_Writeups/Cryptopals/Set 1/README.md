# Set 1

## Convert hex to base64

String: `49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d`

From Hex: `I'm killing your brain like a poisonous mushroom`

To Base 64: `SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t`

## Fixed XOR

String: `1c0111001f010100061a024b53535009181c`

XOR with: `686974207468652062756c6c277320657965` Using [XOR_Program.py](XOR_Program.py)

Result: `746865206b696420646f6e277420706c6179`

## Single-byte XOR cipher

Hex encoded string: `1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736`
\... has been XOR'd against a single character. Find the key, decrypt the message.
`Note: after some research, I found that this is also how the ceaser cipher works, where the XOR key is the value it is shifted by`
[Single-byte_XOR_cipher_decoder.py](Single-byte_XOR_cipher_decoder.py) Brute force XOR using 2 hex characters, i.e. 8 bits (one byte) which is commonly used to encode plaintext. Ex `'a' = 61 in hex`

Result = `Cooking MC's like a pound of bacon`

## Detect single-character XOR
