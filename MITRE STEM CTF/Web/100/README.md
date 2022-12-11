# Web 100
## Description 
They told me make it easy, so I did.
http://44.197.231.105:3020

![Web](ScreenShots/10-18-11.png)

So, we have an input. What does the site do?
Whenever I see an input in a web-app, the first thing I always do command execution
![ls](ScreenShots/10-19-32.png)

Looks like that doesn't work...
What else works?

![inp](ScreenShots/10-20-13.png)

For some reason saved inputs show up. One is a XSS input, which actually works!

![alert](ScreenShots/10-20-54.png)

I looked through the web a bit more and found a cookie!

![Cookie](ScreenShots/10-21-28.png)

We can use XSS to print the cookie's value
```<script>alert(document.cookie)</script>```

![CookieValue](ScreenShots/10-22-05.png)

But it doesn't look easily readable (where are the brackets?), luckily google has a feature

![flagcookie](ScreenShots/10-23-44.png)

If we click that button...

![flagcookie2](ScreenShots/10-24-04.png)

Flag: `MCA{e442d224e08167c18a4e30744ddf35816bd88aa9}`