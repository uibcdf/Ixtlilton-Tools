# File system

## The Ixtlilton's file system

Before reading about your user file system, have a look to [the description of the Ixtlilton's
file system](../../about/file_system.md). Only knowing the volumes structure in Ixtlilton you will understand the logic behind your user file
system.

## The user file system

As user, you have three directories with different usage.

### Home

Your user has a main home directory:

```bash
echo $HOME
```

You can always go to your home directory with any of the following two commands:

```bash
cd
```

```bash
cdh
```

Your home directory is placed in a 500 Gb SSD drive. An SSD drive has a faster reading and
writing than a HDD drive. But watch the use you give to your home. This SSD drive is hosting exclusively all
users home directories. Thereby, the space for your home directory is limited and shared with the other users. At this point there is no space limit for each home directory. It is supposed that the rational use of our home directories avoids taking any action regarding quotas, yet.

**Your home should store scripts, docs, module environments, conda environments, github repos, small
software and temporary not heavy files for analysis.**

Thus, your home has already some directories:

### Your bin directory

There is a bin directory for your user:

```bash
ls $HOME/bin
```

This directory reproduces the structure usually found in a unix system to place binnaries,
libraries, header or other included files, etc. By default some of your environment variables
already include these paths. Try for instance:

```bash
echo $PATH
```

As you can see, the path '/home/$USER/opt/bin' is in the output. This means that any file with
executable rights in this directory will be invokable by you at any time. You can check [the section of the documentation for users
regarding your environment variables](environment_variables.md)


### Your opt directory

Usually, in the unix file system, the opt directory is interpreted as the place where third party
application software packages are placed (self-contained software which function has nothing to see with the OS and/or self-contained software developed by a third party).

```bash
ls $HOME/opt
```

You can install software locally in your home directory the way you prefer. But, if you want to make use
of the [Lmod environment modules manager installed in Ixtlilton](environment_modules.md) we suggest you place the compiled
version of the software in a directory inside `$HOME/opt/apps`, the source code in `SHOME/opt/src`,
and the corresponding modulefiles in `$HOME/opt/modulefiles`. You can find further details about
this implementation in the subsection ["Your own environment modules"](environment_modules.md#your-own-environment-modules).

### Work

Your user has work directory:

```bash
echo $WORK
```

You can always go to your work directory with the following command:

```bash
cdw
```

Your work directory is placed in the volume DATA. DATA is a 8.2 Tbs raid 5 virtual volume built
with HDDs drives. HDDs are slower than SDDs, but HDDs memory is much cheaper. Thats the reason why
HDDs are used to build big volumes, and their expansion is affordable witout expensive costs. There
will be, then, no quotas or limits regarding work or DATA. It is true that this space is shared
with other users, but as soon as DATA needs more room available new HDDs will be added.

Your work directory should store heavy stuff of your project, data which is not going to be frequently readed or
shared with other users. Keep it there as long as you need. Once the project is finished, this data
should be moved to the quenched version of the project to be stored in the volume
COLD_STORAGE_ROOM.

### Scratch

Your user has a scratch directory:

```
echo $SCRATCH
```

There is an alias to go to your scratch directory easy:

```
cds
```

Your scratch directory is placed in the HOT_DATA volume. HOT_DATA is a 460 Gbs SSD drive where
there are only two directories: `/HOT_DATA/scratch` and `HOT_DATA/projects`. The directory
`/HOT_DATA/scratch` is the place where all users have their own scratch directory. And
`HOT_DATA/projects` is a single directory where shared and frequently readed data is
temporary stored. Thereby again, the volume is limited and there is no space limit in your scratch
directory, but as soon as we have problems of coexistence rigid quotas will be imposed.

Your scratch directory should be used not to store stuff for a long time, you have your work
directory for that purpose, but to dump those files which need a fast reading/writting access
memory during a short term period.
