# File system

## The Ixtlilton's file system

The following sections describe the file system mounted in the master node of Ixtlilton.
Below, in the section '', the file system of every slave node is described. Users should also know
about how a slave node is configured, but their interaction with them will be done only through the
jobs submitted to the SLURM workload manager.

This is the table summarizing the global file system:

| Mounted Volume | Size | Type |
| -------------- | ---- | ---- |
| / | 223 Gb | SSD |
| /home | 465.8 Gb | SSD |
| /HOT_DATA | 465.8 Gb | SSD |
| /DATA | 8.2 Tb | Raid 5 HDD |
| /COLD_STORAGE_ROOM | 11 Tb | Raid 5 HDD |


### ROOT

### HOME

There is an 466 Gbs SSD drive with a unique volume hosting the directory `/home`.
This place stores the home directory of every user. The writing/reading speed is fast, but the
memory limited here. In a first moment there will be no space quotas applied to each home
directory, but there will be be quotas if needed.

Users know that their own work directory must be used to store their scripts, docs, module environments, conda environments, github repos, small software and temporary light files for analysis

### DATA

DATA is a virtual raid 5 volume built with HDDs drives. This kind of drives have a slow
reading/writing speed, but this memory is cheap. Today this volume adds up to 8.2 Tbs, but will be
increased as soon as there is no room left to play its role.

Two directories are found in DATA: `/DATA/work` and `/DATA/projects` 

#### Work

The directory `/DATA/work` stores the work directory of every user. Users know that this folder is
used to store heavy, not shared with other users, and not frequently read data or files during a
long term period. Once the project is finished all these files and data will be moved to the
COLD_STORAGE_ROOM for its indefinite storage.

#### Projects

There is in DATA a directory, `/DATA/projects`, where heavy and not frequently read data should
be stored. These files, or data, have to be organised in folders with names evoking each project.
And every user participating in the project must have rights to use it. Files here have to be
accessible for every coworker to avoid duplicity of files. 

Users should not make multiple copies of what it is stored here, if not necessary. All users
analysing a common file should do it from here, not from their own copy. And, if fast access is
needed to the data, there is specific shared directory to temporary keep an accessible copy to every coworker
as well: `HOT_DATA/projects`.

### HOT_DATA

HOT_DATA is a 465.8 Gb SSD drive. Reading and writting access is fast, but this kind of memory is
expensive and it should not be used to store data *sine die*. By contrast, this volume gives us the
chance to have a place where those actual files are placed to enjoy a high speed access. Two
directories are found in HOT_DATA: `/HOT_DATA/scratch` and `/HOT_DATA/projects`. There are no
quotas yet, but since room is limited, there will be space limit rules if necessary.

#### Scratch

The directory `/HOT_DATA/scratch` hosts the scratch directory of every single user. It is reported
in the user guide sections that this directory has to be used as a sandbox to put temporary working
files, heavy if it is needed, not accessible or shared with other users, to enjoy fast reading
access to them. In other supercomputers or cluster, there is a space limit in each scratch
directory and in addition a life-time limit is also imposed. Files with a life longer than 30 days
are automatically removed, for example. By now, no similar rules are defined, yet.

Users know the function of their own scracth directory since it is reported in the section ''.

#### Projects

Those heavy files belonging to a project, such as recent md trajectories, which have to be
accessible to more than a user, and need to be repeteadly read, have to be temporary placed in
`/HOT_DATA/projects`. These files have to be organised in directories with a name related with each
project, to ensure a quick identification by anyone.

Again, there is now no need to fix a limite in space, but it will be done as soon as problems arise.
Because of that, users must remove the files when high speed access is not longer needed.

### COLD_STORAGE_ROOM

There is an external NAS attached to Ixtlilton. The volume COLD_STORAGE_ROOM is nowadays settled
there, in a virtual raid 5 of HDDs adding up to 11 Tb.

The main function of this volume is to keep backups and old projects safe during an undefined period
of time. That's the reason why the volume is off the master node. High speed access is not a
pririoty, but safety.

In the near future, this has to be in a larger raid volume, in an exclusive node. Not in a NAS. 

Two directories are split the volume: `/COLD_STORAGE_ROOM/archive` and `/COLD_STORAGE_ROOM/backups`.

#### Archive

The directory `/COLD_STORAGE_ROOM/archive`, as its own name suggests, stores old projects. These
projects must be placed here well documented and compressed. They should be easily recovered in
case spin-off projects are opened in the future.

#### Backups

This directory keeps automatic backups of important files and data. The backups policy is not
defined yet.

## Sharing projects data

Two directories, in volumes DATA and HOT_DATA, are defined to share heavy files belonging to a
project which should be accessible to any coworker: `/DATA/projects` and `/HOT_DATA/projects`.

The main idea behind this two directories is avoiding multiple copies of the same file. Imagine,
for instance, thereis 150 Gb of trajectories analized simultaneously by three users. There is no
need for every coworker to keep their own copy of the data. That would occupy 300 extra Gb needlessly. To keep this clear and simple, both former directories will store a single copy with all rights granted.

Two things make `/DATA/projects` and `/HOT_DATA/projects` different:

- `/DATA/projects` is in a slow access volume with not size limit virtually.
- `/HOT_DATA/projects` is in a high speed access volume with a small size, less than 500 Gb shared
  among projects and scratch directories of users.

## Finished projects

Once a project is finished a good documenting job has to be done. The whole project, with all data
(compressed), has to be kept for the future. And every aspect of the project, every result, must be easily
reproducible with all what is included in the package. As if it were a time capsule.

Finished projects have to be stored in `/COLD_STORAGE_ROOM/archive`.

## A slave node file system.

### Local

### Imported by NFS

## The user file system

The description of the user file system can be found in the section ['Instructions for users: File
system'](../user/user_file_system.md).


