# Lightning Seeds
#### Encrypted Flag: *4fcbac835550403f13c4cc337d8d8da48351921dfb7cd47d33857432c2ee665d821227*

Python Encryption Code
~~~
#!/usr/bin/env python3
import random

with open('flag.txt', 'r') as f:
    flag = f.read()

seed = random.randint(0,999)
random.seed(seed)

encrypted = ''.join(f'{(ord(c) ^ random.randint(0,255)):02x}' for c in flag)

with open('out.txt', 'w') as f:
    f.write(encrypted)
~~~
Encrypted flag is in hexadecimal

Converted: 605532937396836283609633940045509402527329794084873185086104772100925473110624440871

- Specific seed for a range will always producs the same randoom numbers. 
- I only need to bute force the seed that was used to encrypt the flag.

