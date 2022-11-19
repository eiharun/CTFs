# Challenge 1

## Pulse Check:

**flag:** *flag{im_alive_and_so_are_the_servers}*

___

# Challenge 2

## EZ Pwn 1:
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
    system(command);                                                   //executes command
}
~~~
Command to access challenge: nc chals.2022.squarectf.com 4100



