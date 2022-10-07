#!/bin/bash
FILES WITH COMANDS INSIDE
0-current_working_directory --> prints the absolute path name of the current working directory.
1-listit --> display the contents list of your directory.
2-bring_me_home --> changes the working directory to the user's home directory.
3-listfiles --> displays current directory contents in a long format.
4-listmorefiles --> displays current directory contents, including hidden files (starting with .). [LONG FORMAT]
5-listfilesdigitonly --> displays current directory contents [long format, with user and group IDs displayed numericarlly, and hidden files i.e starting with .]
6-firstdirectory --> creates a directory named my_first_directory in the /tmp/ directory.
7-movethatfile --> moves the file betty from /tmp/ to /tmp/my_first_directory.
8-firstdelete --> deletes the file betty.
9-firstdirdeletion --> deletes the directory my_first_directory that is in the /tmp directory.
10-back --> changes the working directory to the previous one.
11-lists --> this is a script that lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the /boot directory (following this order), in long format.
12-file_type --> prints the type of the file named 'iamafile'. the file 'iamafile' will be in the /tmp directory when the script is ran.
13-symbolic_link --> creates a symbolic link to /bin/ls, named __ls__
14-copy_html --> copies all the HTML files fromthe current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory. (consider that all the HTML files have the extension .html
100-lets_move --> moves all files beginning with an uppercase letter to the directory /tmp/u. Assume the /tmp/u directory will exist when the command is ran.
101-clean_emacs --> deletes all files in the current working directory that end with the character ~
 102-tree --> creates the directories welcome/, welcome/to/, and welcome/to/school in the current directory.
103-commas --> this command lists all the files and directories of the current directory, separated by commas (,).Directory names should end with a slash (/), files and directories starting wih a dot (.) should be listed, the listing should be alpha ordered, except for the directories . and .. whhich should be listed at the very beginning. Only digits and letters are used to sort; Digits should come first.
school.mgc --> this creates a magic file 'school.mgc' that can be used with the command file to detect School data files. School data files always contain the string SCHOOL at offset 0.
