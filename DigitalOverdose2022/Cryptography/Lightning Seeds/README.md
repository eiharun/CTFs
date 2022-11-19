# Lightning Seeds
#### Encrypted Flag:* 4fcbac835550403f13c4cc337d8d8da48351921dfb7cd47d33857432c2ee665d821227*

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


