# Environment variables and shell aliases

## Environment variables

Some environment variables were modified at the moment of creating your user to modify its
behaviour. Some other variables described here are unix default environment variables. Knowing them
makes the interaction with your Ixtlilton user easier.

As you probably already know, you can print out in the terminal all your user environment variables
with:

```bash
export
```

### User file system variables

There are some variables you should know to be used as shortcuts of directories. This can make your
bash scripting lighter. Execute in your terminal the following commands to see these variables:

```bash
echo $USER
```

```bash
echo $HOME
```

```bash
echo $WORK
```

```bash
echo $SCRATCH
```

```bash
echo $DATA
```

```bash
echo $HOTDATA
```

### Path variable

Your Path variable includes now your '$HOME/user/bin' directory. Try in your terminal:

```bash
echo $PATH
```

Binnaries and executable files placed in this directory will be invokable by you in your terminal
at any place and moment.

### Library variables

If you need to include libraries locally in your user to be called by compilers, e.g., make use of
your directories `$HOME/user/lib`, `$HOME/user/lib32`, and `$HOME/user/lib64`. They are already in
your environment variables usually referred with this purpose:

```bash
echo $LIBRARY_PATH
```

and

```bash
echo $LD_LIBRARY_PATH
```

### Environment modulefiles

The environment modules will manage the work with applications software locally installed in your
user. As you saw in [the despcription of your user file system](user_file_system.md), there is
place to where Lmod will look for your modulefiles: `$HOME/opt/modulefiles`. The way to communicate
this to Lmod is including this path in your MODULEPATH environment variable:

```bash
echo $MODULEPATH
```

## Shell aliases

There are some aliases already defined for your user:

```bash
# go to your home directory
cdh
```

```bash
# go to your scratch directory
cds
```

```bash
# go to your work directory
cdw
```

