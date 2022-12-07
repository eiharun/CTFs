# Notes
RSACTFTOOL? -- P is not prime
					|
					v
https://youtube.com/watch?v=5J4rWJHwLSE&feature=share
```
def calculateHint(self):
	return (self.rsa.p >> self.shift) << self.shift #replaces the last (shift)number of binary values with zero. Essensitally deletes last [shift] number of binary values, and fills them in with zeros.
    So there is 2^256 numbers missing

```
If the last actual value is zero, then no changes happen, but if it was one, it was replaced with a zero
RsaTool told me that the p value was not prime, so the last value was probably a one. 

Can't find a decent way to find the prime value between p and p + 2^256.