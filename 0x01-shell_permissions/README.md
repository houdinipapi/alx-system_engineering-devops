#!/bin/bash
0. su betty -- Creates a script that switches the current user to the user betty
1. whoami or id -un -- Writes a script that prints the effective username of the current user
2. groups or id -nG --> Writes a script that prints all the groups the current user is part of
3. sudo chown betty hello --> Writes a script that changes the owner of the file hello to the user betty
4. touch hello --> Creates an empty file called hello
5. chmod u+x hello --> This adds execute permission to the owner of the file hell
6. chmod ug+x,o+r hello --> This script adds execute permissions to the owner and the group owner, and read permission to other users, to the file hello
7. chmod ugo+x hello --> This adds execution permission to the owner, the group owner and the other users, to the file hello
8. chmod 007 hello --> This script sets the permission to the file hello as follows [owner: no permission at all] [Group: no permission at all] [other users: all the permissions]
9. chmod 753 hello --> this script sets the mode of the file hello to this: -rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello
10. chmod --reference=olleh hello --> this sets the mode of the file hello the same as olleh's mode.
11. chmod a+x */ --> this script adds execute permission to all subdirectories of the current directory for the owner, the group owner owner and all other users. the regular files should not be changed
12. mkdir -m 751 my_dir --> This creates a directory called my_dir with permissions 751 in the working directory
13. chgrp school hello --> this changes the group owner to school for the file hello
14. chown vincent:staff * --> This changes the owner to vincent and the group owner to staff for all the files and directories in the working directory
15. chown -h vincent:staff _hello --> this changes the owner and the group owner of _hello to vincent and staff respectively
16. chown --from=guillaume betty hello --> this changes the owner of the file hello to betty only if it is owned by the user guillaume
17. telnet towel.blinkenlights.nl --> this script will play the StarWars IV episode in the terminal
