# Setting up a new project

First of all the reader should know that, for the sake of simplicity, all actions described here are automatized in
a script introduced in the next subsection.

Lets say we are starting a project on the study of the protein target EBNA1.

The first step step is defining a group on ixtlilton to which all user working on this project will be
associated, a working group. Group ids corresponding to projects will be in the range from 10000 to 11000, and its
name, to be identified at a first glance, should start with the prefix 'wg_':

```bash
su
groupadd wg_EBNA1 -g 10000
```

Next two steps are to make, with the proper rigths and owner, the directories to store the shared
data between members of the working group.

```bash
su
mkdir /HOTDATA/projects/EBNA1
mkdir /DATA/projects/EBNA1
chgrp wg_EBNA1 /HOTDATA/Projects/EBNA1
chgrp wg_EBNA1 /DATA/Projects/EBNA1
chmod a-w /HOTDATA/Projects/EBNA1 
chmod a-w /DATA/Projects/EBNA1
chmod g+rw /HOTDATA/Projects/EBNA1 
chmod g+rw /DATA/Projects/EBNA1
```

This way, both directories have rigths to be written and read by any coworker belonging to the
group `wg_EBNA1`.

Finnally, lets define the members of the group:

```bash
usermod -a -G wg_EBNA1 username1
usermod -a -G wg_EBNA1 username2
```

From now on `username1` and `username2` can store the project data which has to be shared. This
workflow will avoid multiple copies of the same files spared along the coworkers directories.

## A single script to do it for you.

There is a script doing all these commands. Its name is `make_new_project_setup`:

```bash
su
module load cluster_tools
make_new_project_setup -n EBNA1 -u username1 username2
```

The script defines the groupid as the lowest unocupied integer in the range 10000 to 10001.
