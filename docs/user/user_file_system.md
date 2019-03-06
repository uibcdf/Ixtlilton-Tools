# File system

## The global file system

Before reading about your user file system, have a look to [the description of the global
file](../about(file_system.md)
system. Only knowing the volumes structure in Ixtlilton you will understand why you have three directories:
home, work and scratch.

## Your user file system

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
writing processes than a HDD drive. But watch the use you give to your home. This SSD drive is hosting exclusively all
users home directories. Thereby, the space for your home directory is limited and shared with the other users. At this point there is no space limit for each home directory. It is supposed that the rational use of our home directories avoids taking any action regarding quotas, yet.

Your home should store scripts, docs, module environments, conda environments, github repos, small
software and temporary not heavy files for analysis.

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

Your work directory should store heavy stuff of your project which is not going to be frequently readed or
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
