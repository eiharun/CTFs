# Challenge 1

## Pulse Check:

**flag:** *flag{im_alive_and_so_are_the_servers}*

___

# Challenge 2

## EZ pwn 1:
Source Code (With my comments):
~~~
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main()
{
    char command[16];                                               //length of command
    char way_too_small_input_buf[8];                                //length of input = 8 characters
    strcpy(command, "ls");
    
    puts("Hi! would you like me to ls the current directory?");
    read(0, way_too_small_input_buf, 24);                           //reads your input with a buffer size of 8, and max size of 24 characters
    if (!strcmp(way_too_small_input_buf, "no\n")) {                 //checks if you said no, otherwise, runs the ls command
        puts("Oh, ok :(");
        exit(0);
    }
    puts("Ok, here ya go!\n");
    system(command);                                                //executes command
}
~~~
#### Step 0
Command to access challenge: nc chals.2022.squarectf.com 4100

#### Step 1
![image](https://user-images.githubusercontent.com/92404926/202836226-ba85e828-c316-427f-9dfa-b402cb98095c.png)
>Saying yes will show us the files in the current directory

#### Step 2
The following code is our exploit
~~~
read(0, way_too_small_input_buf, 24);   //reads your input with a buffer size of 8, and max size of 24 characters
~~~
>The buffer size is 8, so if we input characters above this threshold we can override/overwrite the __ls__ command
>
>We can test this:

![image](https://user-images.githubusercontent.com/92404926/202836546-db868915-baca-44ea-97a3-74d16fce43a3.png)
>Once we pass the 8 character buffer size, we can overwrite the __ls__ command and input our own command.
>In this case, I used __whoami__, we can see the user is ***pwnable_user***

#### Step 3
We can use this to peek into the folders in the directory

![image](https://user-images.githubusercontent.com/92404926/202836728-056602ed-a73b-480a-ab9b-b339440e7b21.png)
>We have a problem, the length of the folder *the_flag_is_in_here* exceeds the length allowed by the code below
~~~
read(0, way_too_small_input_buf, 24);
~~~
>The max length allowed is 24 characters| 8 (buffer) + 19 (length of folder = 27 > 24 (allowd # of chars)
>We also look at the *ez-pwn-1* folder to see if that contains anything interesting.... nope

#### Step 4
At this point, I am thinking of ways to shorten my command to that I can peek into the folder containing the flag
We can take a guess that inside the folder there is a text document titled flag.txt, but I want to be thourough with my investigation

After some reasearch I found this command: __cd */__ and thought maybe it can be used with **ls**. *Spoiler:* It does. (ls */)
###### You learn something new everyday

### What does __*/__ do?
(*) is a global pattern or commonly called a wildcard [^1].
I like to think about it as a loop: It loops through all the directories in your working directory.
When used in combination with __ls__ it effectively lists all the files in the working directory.

[^1]: https://www.tecmint.com/use-wildcards-to-match-filenames-in-linux/

![image](https://user-images.githubusercontent.com/92404926/202837350-e3c0387d-4346-4a08-af0d-b0334d05a3fc.png)
>Using __ls */__ along with the 8 char buffer

##### Update: You can also just use (ls *) and it will list all the files in your working directory and will also tell you what folder they are in. Awesome!

>![image](https://user-images.githubusercontent.com/92404926/202837389-4e9abe53-de37-44cd-8885-30bafa7b5289.png)
>
>_ez-pwn-1_ has no files, but _the_flag_is_in_here_ has one! [Flag.txt]

#### Step 5
How to we read the file?
Simple enough

![image](https://user-images.githubusercontent.com/92404926/202837487-087880ee-c555-44d2-ad86-ddaf922acd45.png)
>We use the command **cat */flag.txt**
>(*) gives us a global file list, (/) allows us to select one of the many files

**flag:** *flag{congrats_youve_exploited_a_memory_corruption_vulnerability}*
___

# Challenge 3

## EZ pwn 2
