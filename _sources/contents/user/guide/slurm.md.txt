# SLURM jobs submission

## Queuing system

## Job files

## What is Slurm?

Slurm is an open-source workload manager and job scheduler for unix HPC (High Performace Computing) clusters. Everything in the
cluster related with the running jobs, the queues and partitions, the scheduling and the resources available at
each moment, is then supervised and managed by Slurm.

## Computing nodes

Let's first see how the universe managed by Slurm is configured. Detailed information about the computing nodes can be printed out with the command:

```
scontrol show nodes
``` 

This former command prints out detailed information about the nodes and its configuration in SLURM.
Let's check for instance 'node04':

```
NodeName=node04 Arch=x86_64 CoresPerSocket=10
   CPUAlloc=0 CPUErr=0 CPUTot=20 CPULoad=0.01
   AvailableFeatures=(null)
   ActiveFeatures=(null)
   Gres=gpu:GTX1080Ti:3
   NodeAddr=192.168.0.4 NodeHostName=node04 Version=17.11
   OS=Linux 3.10.0-693.11.6.el7.x86_64 #1 SMP Thu Jan 4 01:06:37 UTC 2018 
   RealMemory=62000 AllocMem=0 FreeMem=63133 Sockets=2 Boards=1
   State=IDLE ThreadsPerCore=1 TmpDisk=0 Weight=1 Owner=N/A MCS_label=N/A
   Partitions=normal,prior 
   BootTime=2021-08-18T12:11:04 SlurmdStartTime=2021-11-30T23:48:19
   CfgTRES=cpu=20,mem=62000M,billing=20
   AllocTRES=
   CapWatts=n/a
   CurrentWatts=0 LowestJoules=0 ConsumedJoules=0
   ExtSensorsJoules=n/s ExtSensorsWatts=0 ExtSensorsTemp=n/s
```

As we can see, there is information about the hardware found in 'node04' as the number of GPUs, the
RAM memory, or the number of cpu cores. But also the name of the Slurm partitions this node belongs
to (normal and prior, in this case).

If you want to print out a more schematic info, try:

```
sinfo -N -l
```

The output is a list not only about nodes. A line per node and partition is shown. But not all
partitions, only the partitions each user have access. For instance, a regular member of the UIBCDF
will see something like:

```
Wed Dec  1 18:22:37 2021
NODELIST   NODES PARTITION       STATE CPUS    S:C:T MEMORY TMP_DISK WEIGHT AVAIL_FE REASON              
ixtlilton      1    tests*        idle   20   2:10:1  62000        0      1   (null) none                
node01         1    normal        idle   20   2:10:1  62000        0      1   (null) none                
node02         1    normal        idle   20   2:10:1  62000        0      1   (null) none                
node03         1    normal        idle   20   2:10:1  50000        0      1   (null) none                
node04         1    normal        idle   20   2:10:1  62000        0      1   (null) none                
```

A guest user will see something like:

```
Wed Dec  1 18:27:51 2021
NODELIST   NODES PARTITION       STATE CPUS    S:C:T MEMORY TMP_DISK WEIGHT AVAIL_FE REASON              
node01         1    guests        idle   20   2:10:1  62000        0      1   (null) none                
node02         1    guests        idle   20   2:10:1  62000        0      1   (null) none                
node03         1    guests        idle   20   2:10:1  50000        0      1   (null) none                
node04         1    guests        idle   20   2:10:1  62000        0      1   (null) none                
```

Having a look to the description of Ixtlilton's hardware is useful to understand the resources
managed by Slurm. Have a look to the sections [Main node]('../../about/main_node.md') and [Secondary nodes]('../../about/secondary_nodes.md') from this online documentation.


## Partitions

Slurm works with sets of nodes or partitions. Each partition can be confiture with special settings and
rights for different users. And each partition has its own jobs queue. Before giving more details on this, lets
see the partitions defined in Ixtlilton:

```bash
scontrol show partitions
```

The output looks like something similar depending on the user profile:

```
PartitionName=tests
   AllowGroups=uibcdf AllowAccounts=ALL AllowQos=ALL
   AllocNodes=ALL Default=YES QoS=N/A
   DefaultTime=NONE DisableRootJobs=NO ExclusiveUser=NO GraceTime=0 Hidden=NO
   MaxNodes=UNLIMITED MaxTime=03:00:00 MinNodes=1 LLN=NO MaxCPUsPerNode=UNLIMITED
   Nodes=ixtlilton
   PriorityJobFactor=10000 PriorityTier=1 RootOnly=NO ReqResv=NO OverSubscribe=NO
   OverTimeLimit=NONE PreemptMode=OFF
   State=UP TotalCPUs=20 TotalNodes=1 SelectTypeParameters=NONE
   DefMemPerNode=UNLIMITED MaxMemPerNode=UNLIMITED

PartitionName=normal
   AllowGroups=uibcdf AllowAccounts=ALL AllowQos=ALL
   AllocNodes=ALL Default=NO QoS=N/A
   DefaultTime=NONE DisableRootJobs=NO ExclusiveUser=NO GraceTime=0 Hidden=NO
   MaxNodes=UNLIMITED MaxTime=1-00:00:00 MinNodes=1 LLN=NO MaxCPUsPerNode=UNLIMITED
   Nodes=node01,node02,node03,node04
   PriorityJobFactor=5000 PriorityTier=1 RootOnly=NO ReqResv=NO OverSubscribe=NO
   OverTimeLimit=NONE PreemptMode=OFF
   State=UP TotalCPUs=80 TotalNodes=4 SelectTypeParameters=NONE
   DefMemPerNode=UNLIMITED MaxMemPerNode=UNLIMITED

PartitionName=prior
   AllowGroups=uibcdf_prior AllowAccounts=ALL AllowQos=ALL
   AllocNodes=ALL Default=NO QoS=N/A
   DefaultTime=NONE DisableRootJobs=NO ExclusiveUser=NO GraceTime=0 Hidden=NO
   MaxNodes=UNLIMITED MaxTime=UNLIMITED MinNodes=1 LLN=NO MaxCPUsPerNode=UNLIMITED
   Nodes=ixtlilton,node01,node02,node03,node04
   PriorityJobFactor=65000 PriorityTier=65000 RootOnly=NO ReqResv=NO OverSubscribe=NO
   OverTimeLimit=NONE PreemptMode=OFF
   State=UP TotalCPUs=100 TotalNodes=5 SelectTypeParameters=NONE
   DefMemPerNode=UNLIMITED MaxMemPerNode=UNLIMITED
```

If you want a more summarized list:

```bash
sinfo
```

Which shows something like:

```
PARTITION AVAIL  TIMELIMIT  NODES  STATE NODELIST
tests*       up    3:00:00      1   idle ixtlilton
normal       up 1-00:00:00      4   idle node[01-04]
prior        up   infinite      5   idle ixtlilton,node[01-04]
```

Then, each partition has its own settings. For example, each partition has a walltime limit. As such, the partition named 'normal' will run jobs
with a maximum duration of 24 real hours. Once the walltime has been reached, Slurm will kill the process if this is still running.

Let's show here a table describing the main features of each partition:

| Name | Nodes | Wall time | Priority |Description | Allow Groups |
| ---- | ----- | --------- | ----------- | ----- | ------ |
| tests | ixtlilton | 3 hours | High | Tests and short jobs | uibcdf |
| normal | nodes[01-04] | 24 hours | Normal | Normal jobs | uibcdf |
| guests | nodes[01-04] | 24 hours | Low | Collaboration jobs | guests |
| prior  | ixtlilton and nodes[01-04]| Infinity | Top | High priority jobs| uibcdf\_prior |

### 'tests' partition

This partition, composed by a single node (ixtlilton), is dedicated to run short jobs and tests. Only runs with a 3 hours walltime will be accepted. And jobs
will have a high priority in the queues in this resources would be shared among different
partitions.

All UIBCDF members have access to this partition.

### 'normal' partition

This partition, composed by all secondary nodes, is dedicated to run regular jobs. This does not
mean that regular jobs are going to be run without limits. In order to give chance to everybody in
the queue, jobs here have a 24 hours walltime. So, if you need to run a 10 days simulation, save a
checkpoint every 23 hours and 50 minutes, stop your simulation and restart it as a new job
submission to the queue till your simulation is finished. In case the queue is empty, your
simulation will run as if it where only an interrupted job.

All UIBCDF members have access to this partition, and jobs in this queue have a normal priority.

### 'guests' partition

This is the partition to be used by the external collaborators. All secondary nodes are available
in this partition and the same time limitation from the 'normal' partition applies here: a 24 hours
walltime. Jobs submitted to this partition have low priority.

Only guests members will have access to this partition.

### 'prior' partition

This partition is "the top priority" partition. All nodes and resources are included in this queue.
And jobs submitted to 'prior' will have high priority in the queue and no time limit. By default
no UIBCDF member can use this partition but the principal researchers. If you need, under special
circunstances, access to the 'prior' partition, the right to use it will be given temporarily by
the administrators with the approval of all principal researchers.

## The job queues

To display all jobs in all queues type in the terminal:

```bash
squeue
```

If you only want to display the jobs submitted, for instance, to the 'normal' partition:

```bash
squeue -p normal
```

Use the flag '-u' jobs submitted by a specific user have to be printed out:

```
squeue -u username
```

If a more detailed info is needed from all jobs, do:

```
scontrol show jobs
```

### The job status in the queue

Every job submitted to Slurm have a status (ST) reporting its state.

#### Pending (PD)
A job can be in PD (pending) if it still waiting to be started. Usually, this state lasts as long
as there is room available in the partition to be executed, and there no other jobs before in the queue.

#### Running (R)
A job is in R if it is already running. This state will last until the end of the submitted process
or until the partition's walltime. Whatever happens first.

#### Completed (CG)
A job is in CG if it is already completing.

## Submitting a job

A regular submission is done by means of a file, a submission bash script to slurm. This script
contains all settings and commands necessary for Slurm to execute the job. And to easily
identify these files, the extension \*.slurm will be used to name them.

Before giving details about the submission instructions, let's submitt our first job. This first
experience will give you more insight than any introduction paragraph.

### Your first job submitted to Ixtlilton

Let's suppose that we have a task to be executed in Ixtlilton. To make this first experience
simple, this task will not entail complicated algorithms... our task is taking a 30 seconds nap.
Write a bash script named 'napping' with the following lines:

```bash
#!/bin/bash
echo "Going to sleep in" $HOSTNAME
sleep 30s
echo "Done"
```

Make the script executable:

```bash
chmod +x napping
```

And run it locally:

```bash
./napping
```

The terminal will go to sleep during 30 seconds. The environment variable HOSTNAME will tell us
that the process is runing in the node ixtlilton -obvious, we run it there-.

Now let's submit this task to Slurm. Let's run this job in the first resources available in the
'normal' partition found by Slurm for us. Write the following Slurm submission bash script in a new
file named 'nap\_submission.slurm':

```bash
#!/bin/bash
#SBATCH -p normal     # partition (queue)
#SBATCH -N 1          # number of nodes
#SBATCH -n 1          # number of cores
#SBATCH -t 0-1:00     # time (D-HH:MM)
#SBATCH -o slurm.out  # STDOUT
#SBATCH -e slurm.err  # STDERR
./napping
```

This is probably the first time you see the Slurm instructions in a submission bash script. Some
details will be given in the next subsection about them. At this point it is enough guessing that
our 'nap\_submission.slurm' script is asking to Slurm for a single CPU core in a single node of the
'normal' partition to run our script 'napping' with a 1 hour walltime. The standard output will be
written in a file named 'slurm.out' and the standard error will be dumped in a file named
'slurm.err'. And finally, it is time to submit it:

```bash
sbatch nap_submission.slurm
```

Now, quickly, run this command:

```
squeue -p normal -u $USER
```

If the job is already running, you will get something like:

```
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
              2919    normal nap_subm    diego  R       0:16      1 node01
```

This former command shows us that our job as the job id 2919 and it has been running in node01 for
16 seconds already.

If you want more details about the resources required, the status, etc. Or if the submission had
errors and the job is stuck in queue, the following command can be useful:

```
scontrol show jobs
```

You will find all jobs there. Find yours:

```
JobId=2918 JobName=nap_submission.slurm
   UserId=diego(2001) GroupId=diego(2001) MCS_label=N/A
   Priority=4294901759 Nice=0 Account=(null) QOS=(null)
   JobState=RUNNING Reason=None Dependency=(null)
   Requeue=1 Restarts=0 BatchFlag=1 Reboot=0 ExitCode=0:0
   RunTime=00:00:11 TimeLimit=01:00:00 TimeMin=N/A
   SubmitTime=2021-12-01T21:06:22 EligibleTime=2021-12-01T21:06:22
   StartTime=2021-12-01T21:06:23 EndTime=2021-12-01T22:06:23 Deadline=N/A
   PreemptTime=None SuspendTime=None SecsPreSuspend=0
   LastSchedEval=2021-12-01T21:06:23
   Partition=normal AllocNode:Sid=ixtlilton:13609
   ReqNodeList=(null) ExcNodeList=(null)
   NodeList=node01
   BatchHost=node01
   NumNodes=1 NumCPUs=1 NumTasks=1 CPUs/Task=1 ReqB:S:C:T=0:0:*:*
   TRES=cpu=1,node=1,billing=1
   Socks/Node=* NtasksPerN:B:S:C=0:0:*:* CoreSpec=*
   MinCPUsNode=1 MinMemoryNode=0 MinTmpDiskNode=0
   Features=(null) DelayBoot=00:00:00
   Gres=(null) Reservation=(null)
   OverSubscribe=OK Contiguous=0 Licenses=(null) Network=(null)
   Command=/home/diego/tests_slurm/test_napping/nap_submission.slurm
   WorkDir=/home/diego/tests_slurm/test_napping
   StdErr=/home/diego/tests_slurm/test_napping/slurm.err
   StdIn=/dev/null
   StdOut=/home/diego/tests_slurm/test_napping/slurm.out
   Power=
```

Finnally, once the job is finished, check the content of the resulting files 'slurm.out' and
'slurm.err'.

```bash
cat slurm.out 
>Going to sleep in node01
>Done
```

### Slurm submission instructions

Examples of these files will be stored in github in order to share submission instructions in ixtlilton or any other cluster used by the UIBCDF members.

In addition to the templates, in the following sections some useful variables and instructions are described.

Once the bash script is ready, the command to submit it is:

## Managing you submitted job

xx
