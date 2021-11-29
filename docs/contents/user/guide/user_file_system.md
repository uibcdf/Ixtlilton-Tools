# File system

## The Ixtlilton's file system

Before reading about your user file system, have a look to [the description of the Ixtlilton's
file system](../../about/file_system.md). Only knowing the volumes structure in Ixtlilton you will understand the logic behind your user file
system.

## The user file system

As user, you have three directories with different usage. The main features of these three
directories are summarized in the following table:

| Directory | Usage | In Mounted Point | Quotas |
|-----------|-------|-----------------|--------|
| /home/username | Local binaries, scripts, user setting files, environments, github repos, **not heavy files**  | /home  | None yet  |
| /work/username  | Data from projects and heavy stuff  | /DATA | None |
| /scratch/username  | Temporary data requiring fast reading/writing | /HOTDATA | None yet |

### Home

Your user has a main home directory: '/home/username'. Once you have accessed to Ixtlilton with
your user account, type:

```bash
echo $HOME
```

The environment variable `HOME` defines de path of your main directory. You can always go to your home with any of the following two commands:

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

#### The user local directory

Your local directory '\$HOME/local' is nothing but the symbolic link to the directory '\$HOME/.local'
created by default by the Linux OS for every user. This symbolic link is for you to notice the
place where you must locate your scripts to be invokable from anywhere in your terminal, your
libraries, etc. The directory '\$HOME/.local' is a hidden directory. 

Try to see what's in your local directory:

```bash
ls $HOME/local
```

##### The '\$HOME/local/bin' directory

There is a bin directory for your user. This is the place to put your local binaries or your
scripts with executable rights. Any file with executable rights in this directory will be invokable by you at any time. You can check [the section of the documentation for users
regarding your environment variables](environment_variables.md) and try:

```bash
echo $PATH
```

As you can see, the path '\$HOME/opt/bin' is in the output. As it was said above, your user looks
for binaries there in addition to the common directories defined by the system for every user.

##### The '\$HOME/local/etc' directory

Usually, in the unix file system, the etc directory is interpreted as the place to store host-specific system configuration files used by the local binaries.
Use this directory at your own convenience since its content only affects your user.

##### The '\$HOME/local/opt' directory

In a unix file system, the opt directory is where third party application software packages are placed (self-contained software which function has nothing to see with the OS and/or self-contained software developed by a third party). Is this directory really necessary for you? Maybe not... You can install software locally in your home directory the way you prefer. But, if you want to make use
of the [Lmod environment modules manager installed in Ixtlilton](environment_modules.md) we suggest you to place the compiled
version of the software in a directory inside '\$HOME/opt/apps', the source code in '\$HOME/opt/src',
and the corresponding modulefiles in '\$HOME/opt/modulefiles'. You can find further details about
this implementation in the subsection ["Your own environment modules"](environment_modules.md#your-own-environment-modules).

Check the value of your environment variables `MODULEPATH`:

```bash
echo $MODULEPATH
```

##### The '\$HOME/local/include' directory

You can place here local C header files if you compile your own C code. Check that this directory
is included in your environment variable `INCLUDE`:

```bash
echo $INCLUDE
```

##### The '\$HOME/local/lib', '\$HOME/local/lib32', and '\$HOME/local/lib64' directories

Your user has three directories, emulating the same structure a unix SO has, to store local
libraries. These three directories are included in the `LIBRARY_PATH` and `LD_LIBRARY_PATH`
environment variables of your user:

```bash
echo $LIBRARY_PATH
```

```bash
echo $LD_LIBRARY_PATH
```

##### The '\$HOME/local/man' directory

A unix system has a man directory where the documentation of binaries are stored in the proper
format to be printed out by the command `man`. Try for instance:

```bash
man ls
```

If you need to include man files for your binaries or third party software installed locally, the
directory '\$HOME/local/man' is the place. Check your environment variable `MANPATH`:

```bash
echo $MANPATH
```

##### The '\$HOME/local/share' directory

The '\$HOME/local/share' directory architecture-independent shareable text files: user setting files
and so on used by the software installed locally by you or in the OS by the administrator. Do not
remove information in your '$HOME/local/share' unless you know what you are doing.

##### The '\$HOME/local/src' directory

Your '\$HOME/local/src' is the place where you should keep the source code and packages locally
installed and tracked by the Lmod environment modules manager.

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
HDDs are used to build big volumes, and their expansion is affordable without expensive costs. There
will be, then, no quotas or limits regarding the user work directory. It is true that this space is shared
with other users, but as soon as DATA needs more room available new HDDs will be added.

**Your work directory should store heavy stuff of your project, data which is not going to be frequently readed or
shared with other users. Keep it there what you want as long as you need it. Once a project is finished, the corresponding data
should be moved to the archived version of the project to be stored in the volume COLD\_STORAGE\_ROOM.**

### Scratch

Your user has a scratch directory:

```
echo $SCRATCH
```

There is an alias to go to your scratch directory easy:

```
cds
```

Your scratch directory is placed in the HOT\_DATA volume. HOT\_DATA is a 460 Gbs SSD drive where
there are only two directories: '/HOT\_DATA/scratch' and '/HOT\_DATA/projects'. The directory
'/HOT\_DATA/scratch' is the place where all users have their own scratch directory. And
'/HOT\_DATA/projects' is a single directory where shared and frequently readed data is
temporary stored accessible to all users working in a common project (your user has no read/write rigths by default, ask to the administrators if you need it). Thereby again, the volume is limited and there is no space limit in your scratch directory, but as soon as we have problems of coexistence rigid quotas will be imposed.

**Your scratch directory should be used not to store stuff for a long time, you have your work
directory for that purpose, but to dump those files which need a fast reading/writing access
memory during a short term period.**

## Directories from the global file system the user should know

There are some directories in the Ixtlilton's file system the user should know. At certain point,
although only the administrators have by default writing rights, every use would need to access to
them. Any new user has no, by default, writing rights to these directories. They will be granted
by the administrators if the user and the case warrant.

| Directory | Usage | In Mounted Point |
|-----------|-------|-----------------|
| /DATA/projects | Shared data from projects | /DATA |
| /DATA/backups | Backups directory  | /DATA |
| /HOTDATA/projects | Temporary shared data from projects with fast reading/writing access | /HOTDATA |
| /HOTDATA/TempDATA  | Temp directory with fast reading/writing access | /HOTDATA |
| /ColdStorageRoom/archive  | Archive where old and sleeping projects are stored compressed | /NFS/NAS |
| /ColdStorageRoom/backups  | Mirror from /DATA/Backups | /NFS/NAS |

The user can find further information about these directories in [the description of the Ixtlilton's
file system](../../about/file_system.md).

