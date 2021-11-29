# Shell aliases

There are some aliases already defined for your dot file '.bash\_aliases':

```bash
less ~/.bash_aliases
```

## To navigate

To go to your home directory:

```bash
alias cdh="cd $HOME"
```

To go to your scratch directory:

```bash
alias cds="cd $SCRATCH"
```

To go to your work directory:

```bash
alias cdw="cd $WORK"
```

## To safely remove files

Removing files can be something dangerous some times. The command `rm *` is the nightmare of every
Linux user. That's way having aliases to avoid misstyping the character \* when we execute `rm` can
save your day. 

To safely remove backup files:

```bash
alias purge_backups='rm *~'
```

To safely remove Python compiled bytecode files:

```bash
alias purge_python='rm *.pyc'
```

To safely remove gromacs \#files:

```bash
alias purge_gromacs='rm \#*'
```

To safely remove any of the above mentioned files:

```bash
alias purge='rm *~ \#* *.pyc'
```

## To work with SLURM

Sometimes the command `squeue` has a default format with not enough information. Try the following
alias you alread have in your dot file '.bash\_aliases':

```bash
alias squeuel='squeue --format="%.18i %24j %.8u %.12T %.12M %.12l %.6D %.12P %R"'
```


```{tip}
Have a look to the section of this user guide name 'Dot files and
directories'. You might want to define some other environment variables.
```

