# SLURM

## Using Slurm

Diplaying compute nodes:
```
scontrol show nodes
``` 

To display the job queue:
```
scontrol show jobs
```

```
scontrol show daemons
salloc
sinfo
squeue
smap
sview
scontrol show config
sstat
sreport
```

### Submitting a job

To easily identify the submission bash scripts to slurm, the extension *.slu will be used.
Examples of these files will be stored in github in order to share submission instructions in ixtlilton or any other cluster used by the UIBCDF members.

In addition to the templates, in the following sections some useful variables and instructions are described.

Once the bash script is ready, the command to submit it is:

```bash
sbatch script_run.slu
```

### Script submission instructions (*.slu)

