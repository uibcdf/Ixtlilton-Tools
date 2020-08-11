# Slurm

## What is Slurm?

Slurm is an open-source workload manager and job scheduler for unix HPC clusters. Everything in the
cluster related with the running jobs, the queues and partitions, the scheduling and the resources available at
each moment, is then supervised and managed by Slurm.

## Computing nodes

Detailed information about the computing nodes can be printed out with the command:

```
scontrol show nodes
``` 

or

```
sinfo -N -l
```

Having a look to the description of Ixtlilton's hardware is useful to understand the resources
managed by slurm. Here is a brief description of the nodes as slurm knows them:

| Name | IP  | CPUs | Threads | Memory | GPUs |
| ---  | --- | ---- | ------  | ------ | ---- |
| ixtlilton | 192.168.0.100 | 20 | 20 | 62000 | GTX1080 (2x)
| node01    | 192.168.0.1   | 20 | 20 | 62000 | GTX1080Ti (3x)
| node02    | 192.168.0.2   | 20 | 20 | 62000 | GTX1080 (2x), GTX1080Ti (1x)
| node03    | 192.168.0.3   | 20 | 20 | 50000 | GTX1080Ti (3x)
| node04    | 192.168.0.4   | 20 | 20 | 62000 | GTX1080Ti (3x)


## Partitions

Slurm works with sets of nodes or partitions of the cluster resources with special settings and
rights. This partitions can be defined also as job queues. Before giving more details on this, lets
see the partitions defined in Ixtlilton:

```bash
sinfo
```

For UIBCDF lab members there are four partitions or job queues.

| Name | Nodes | Wall time | Priority |Description |
| ---- | ----- | --------- | ----------- |
| tests | ixtlilton | 6 hours | High |Tests and short runs |
| gpus  | ixtlilton and nodes[01-04]| 7 days | Normal |Partition with all gpus for gpu jobs|
| gpus_prior  | ixtlilton and nodes[01-04]| Infinity | Top | Partition with all gpus for high priority gpu jobs|
| normal | nodes[01-04] | 7 days | Normal |Partition for standard molecular dynamics simulations |
| prior | nodes[01-04] | Infinity | Top | Partition for standard molecular dynamics simulations |


For UIBCDF guests there is only a partition.

| Name | Nodes | Wall time | Priority | Description |
| ---- | ----- | --------- | ----------- | -------- |
| guests | node02 | 1 day  | Low | Queue for invited guests with projects out of the lab interest |

## The job queue

To display all jobs in the queue:

```bash
squeue
```

If only your jobs have to be printed out:

```
squeue -u $USER
```

The lab guests will have access only to the jobqueue and info regarding the partition 'guests'.

## Jobs

To display all jobs with detailed info:

```
scontrol show jobs
```


## Submitting a job

To easily identify the submission bash scripts to slurm, the extension *.slu will be used.
Examples of these files will be stored in github in order to share submission instructions in ixtlilton or any other cluster used by the UIBCDF members.

In addition to the templates, in the following sections some useful variables and instructions are described.

Once the bash script is ready, the command to submit it is:

```bash
sbatch script_run.slu
```

### Script submission instructions (*.slu)

