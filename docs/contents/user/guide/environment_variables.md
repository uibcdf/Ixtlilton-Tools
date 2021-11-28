# Environment variables

The environment variables are variables defined in your shell session by you or the OS with name
and value. They are used by the OS and third applications to define their behaviour depending
on the user choice or setup.

Let's first how to define a shell variable. Type in a terminal:

```bash
ACME_LICENSE_CODE='xdk434%EQ}'
```

And now lets print out the value of our first shell variable:

```bash
echo $ACME_LICENSE_CODE
```

Values can also be integers, float, double or boolean. Let's play a bit bash scripting with different variables:

```bash
TOPYEAR=2020
NOW=`date +'%Y'`
if [[ $NOW -lt TOPYEAR ]]; then WORKS=true; else WORKS=false; fi
if ! $WORKS; then echo "The ACME License expired"; fi
```

Now, if you want that other than your user can access to the value of a variable, you need to turn
the shell variable into an environment variable:

```bash
export ACME_LICENSE_CODE
```

or

```bash
export ACME_LICENSE_CODE='xdk434%EQ}'
```

Finnally, you can print out in the terminal all your user environment variables
with:

```bash
export
```

## Your user

There are three variables keeping information about the sessions user:

```bash
echo $USER
```
```bash
echo $USERNAME
```
```bash
echo $LOGNAME
```

## Where your user is and was

There are a couple of variables useful to drive your user in a script. Try the following:

```
cd ~
cd local
echo $PWD
echo $OLDPWD
```

Now you can guess how the following command knows what was the last place you visited:

```
cd -
echo $PWD
```

## Navigating in your file system

There are some variables you should know to be used as shortcuts of directories. This can make your
bash scripting or your interaction with your terminal lighter.

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

## Path variable

Your Path variable includes the list of directories where your user is going to look for binnaries
and executable scripts:

```bash
echo $PATH
```

You can for instank invoke the command 'ls' at any moment and place because it is located in a
directory included in your 'PATH' environment variable.

```
which ls
```

## Library variables

If you need to include libraries locally in your user to be called by compilers, e.g., make use of
your directories `$HOME/local/lib`, `$HOME/local/lib32`, and `$HOME/local/lib64`. They are already in
your environment variables usually referred with this purpose:

```bash
echo $LIBRARY_PATH
```

and

```bash
echo $LD_LIBRARY_PATH
```

## Environment modulefiles

The environment modules lets you interact with the applications installed by the administrators or locally by you. As you can see in [the description of your user file system](user_file_system.md), there is place where Lmod will look for your modulefiles: `$HOME/local/opt/modulefiles`. The way to communicate
this to Lmod is including this path in your 'MODULEPATH' environment variable:

```bash
echo $MODULEPATH
```

Check the section [XXX](environment_modules.md) if you are not familiar it.

```{note}
There are many other environment modules defined for your session. You can easily find information about them on internet.
```

```{tip}
Have a look to the section of this user guide name 'Dot files and
directories'. You might want to define some other environment variables.
```

