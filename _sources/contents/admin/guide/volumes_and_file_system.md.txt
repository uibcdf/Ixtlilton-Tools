# Volumes and File System

## Volumes

### Master Node

#### Root and Home Volume

Principal SSD with three partitions: /, Swap memory and Home

NAME   MAJ:MIN RM   SIZE RO TYPE  MOUNTPOINT\
sda      8:0    0 223.6G  0 disk  \
├─sda1   8:1    0   100G  0 part  /\
├─sda2   8:2    0     8G  0 part  [SWAP]\
└─sda3   8:3    0   115G  0 part  /home


##### Root / Partition

This partition has the main root directory with the software and system. It is 100 Gb big but it should occupy the whole volume once a new SSD is bought to host the Home partition.

##### Home Partition

This partition holds the main home directory of users. This should be a fast access directory to submitt jobs and run fast jobs and analysis. There are two main directories per user: a "home" and a "scratch" directory.

> TODO: This partition should be in a 1 or 2 Tb SSD alone. This new SSD should host the users directory "home" and "scratch" without quotes at the beginning.

###### Main users home directory

```
/home
```

Quotes are not needed yet. The principal "home" directory should be used to store scripts and small files (not raw data).

###### Users scratch directory

```
/home/scratch
```

Quotes are not needed yet. The "scratch" directory should be fast access directory to store temporary data urged to be written and read frequently.


#### DATA Volume

Raid 5 Volume with 4x 2.7 Tb hard drives. It results with a 8.2 Tb virtual volume:

NAME   MAJ:MIN RM   SIZE RO TYPE  MOUNTPOINT
sdb      8:16   0   2.7T  0 disk  \
└─md0    9:0    0   8.2T  0 raid5 /DATA \
sdc      8:32   0   2.7T  0 disk  \
└─md0    9:0    0   8.2T  0 raid5 /DATA \
sdd      8:48   0   2.7T  0 disk  \
└─md0    9:0    0   8.2T  0 raid5 /DATA \
sde      8:64   0   2.7T  0 disk  \
└─md0    9:0    0   8.2T  0 raid5 /DATA 


To check the sanity of the volume:

```
mdadm -D /dev/md0
```

Or checking the file:

```
less /proc/mdstat
```

The file `/etc/mdadm.conf` was written with the partitition details after the volume configuration. It was created this way:

```
mdadm --detail --scan >> /etc/mdadm.conf
```

A daemon can be initilize to monitor every now and then the status of the volume. Errors should be communicated by email:

```
mdadm –monitor –mail=root@localhost –delay=1800 /dev/md2
```

##### Projects directory

```
/DATA/projects
```

This is a shared directory with the raw data available for every member of a project. Groups should probably defined according to projects, not really sure about this.

##### Work directory

```
/DATA/work
```

This directory has work directory per user. The access is not so fast as scratch so it should store the main work files not really urged of write/read speed. 

### Storage Node

At the moment the storage node is a NAS. This NAS is now located with with the ip 192.168.0.203.
A raid 5 with 4 x 4Tb Hard Drives makes a volume of 11.89 Tb.

Two directories are defined in its single volume Volume_1 to be NFS shared:

```
nfs://192.168.0.203/nfs/archive
nfs://192.168.0.203/nfs/backups
```

Administration with a browser is possible with:

|                 |           |
| Device username | uibcdf    |
| Password        | adm1n4147 |

Remote ssh conection is also available with:

|          |           |
| User     | root      |
| Password | adm1n4147 |


#### Cold Storage Room

In the master node the following directory hosts both mount points for "archive" and "backups".

```
/ColdStorageRoom
```

###### Archive

This directory storages the projects already finished. Raw data, scripts,
documentation and papers should be included compressed to be kept archived.

```
/ColdStorageRoom/archive
```


###### Backups

Backups of files of the SSD volumes are automatically storage here. Every user
should find here compressed files corresponding to its "home" in Ixtlilton and
directories included in the backup list per user. In addition, a backup of the
master and nodes system should also be kept here to make recovery processes
faster.

```
/ColdStorageRoom/backups
```


### Slave GPUs Nodes (Nodo01 and Nodo02)

#### LocalDATA Volume

Raid 0 Volume with 2x 2.7 Tb hard drives. It results with a 5.5T Tb virtual volume:

NAME   MAJ:MIN RM   SIZE RO TYPE  MOUNTPOINT
sdb      8:16   0   2.7T  0 disk  
└─md0    9:0    0   5.5T  0 raid0 /LocalDATA
sdc      8:32   0   2.7T  0 disk  
└─md0    9:0    0   5.5T  0 raid0 /LocalDATA

#### TempDATA Volume

SSD 166 Gb partition dedicated to temporal fast read and write tasks.

NAME   MAJ:MIN RM   SIZE RO TYPE  MOUNTPOINT
└─sda5   8:5    0 166.6G  0 part  /TempDATA

#### NFS imported Volumes

Volumes /opt, /home and /DATA are imported from the master node.

'''
home      --fstype=nfs,nfsvers=3,tcp,rsize=8192,wsize=8192,hard,intr,timeo=600,rw  172.17.253.253:/home
opt      --fstype=nfs,nfsvers=3,tcp,rsize=8192,wsize=8192,hard,intr,timeo=600,rw  172.17.253.253:/opt
DATA      --fstype=nfs,nfsvers=3,tcp,rsize=8192,wsize=8192,hard,intr,timeo=600,rw  172.17.253.253:/DATA
'''

The three of them are mounted on /NFS and linked to /home, /opt and /DATA.


### Slave CPUs Nodes (Nodo03 y Nodo04)

1 x 2.7 Tb hard drives.

NAME   MAJ:MIN RM   SIZE RO TYPE  MOUNTPOINT
sdb      8:0    0   2.7T  0 disk /LocalDATA

#### TempDATA Volume

SSD 166 Gb partition dedicated to temporal fast read and write tasks.

NAME   MAJ:MIN RM   SIZE RO TYPE  MOUNTPOINT
└─sda5   8:5    0 166.6G  0 part  /TempDATA

#### NFS imported Volumes

Volumes /opt, /home and /DATA are imported from the master node.

'''
home      --fstype=nfs,nfsvers=3,tcp,rsize=8192,wsize=8192,hard,intr,timeo=600,rw  172.17.253.253:/home
opt      --fstype=nfs,nfsvers=3,tcp,rsize=8192,wsize=8192,hard,intr,timeo=600,rw  172.17.253.253:/opt
DATA      --fstype=nfs,nfsvers=3,tcp,rsize=8192,wsize=8192,hard,intr,timeo=600,rw  172.17.253.253:/DATA
'''

The three of them are mounted on /NFS and linked to /home, /opt and /DATA.


## File System

### Admin File System


#### Admin

##### Tools

With a github repo in https://github.com/uibcdf/Ixtlilton

```
/root/Admin/Tools
```

#### Hardware

Not in the github repo. Probably this repo should be in Admin excluding unnecesary files

```
/root/Admin/Hardware
```

##### Benchmarks

To be written

###### Tools

To be written

###### Results

To be written

<aside class="notice">

TODO: this way to write color boxes does not work.

</aside>


### Users File System

Each user has three directories. No quotes are needed at the moment.

| Directory          | Description                                                        | Space                | Backedup |
| ---                | ---                                                                | ---                  | ---      |
| /home/user         | Main home dir with scripts, software and light files (fast access) | No Limit Yet (~10Gb) | Yes      |
| /scratch/user | Temporary data files frequently read and written (fast access)     | No Limit Yet (~50Gb) | No       |
| /work/user    | Main working dir (slow access)                                     | No Limit             | No       |

#### User Home

This directory should store permanent scripts and temporary user software. This directory has fast access. Raw data should not be kept here, This directory is placed in a small ssd unit.

Quote: This directory has no limit yet but as a rule of thumb every user should occupy not more than 10Gb.
Backedup: Yes

```
/home/user
```

#### Scratch

This directory should be used as a box to store temporary data files frequently read and written. It has fast access but it is placed in a small ssd unit. At the moment has no quotes. 

Quote: This directory has no limit yet but as a rule of thumb every user should occupy not more than 50Gb (500Gb in the future).
Backedup: No

```
/scratch/user
```

#### Work

This directory should be used as the main working directory. It has a slow access but not room limit. 

Quote: This directory has no limit.
Backedup: No

```
/DATA/work/user
```

### Shared File System

Three common directories are shared with different purpose: "Projects" and "ColdStorageRoom/archive", "ColdStorageRoom/backups"

#### Projects

This is a shared directory with the raw data available for every member of a
project. Groups should probably be defined according to projects, not really sure
about this.

```
/Data/projects
```

#### Archive

This directory storages the projects already finished. Raw data, scripts,
documentation and papers should be included compressed to be kept archived.

```
/ColdStorageRoom/archive
```

#### Backups

Backups of files in the SSD volumes are automatically storage here. Every user
should find here compressed files corresponding to its "home" in Ixtlilton and
directories included in the backup list per user.

```
/ColdStorageRoom/backups
```


