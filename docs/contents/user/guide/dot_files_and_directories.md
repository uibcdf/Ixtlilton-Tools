# Dot files and directories

In a unix OS, the dot files or directories are those whose name starts with '.'. This only fact makes them hidden. Try to type in your terminal de following:

```bash
cd $HOME
ls
``` 

and now:

```bash
ls -a
``` 

Many files that you probably didn't know, if you are a Linux newbie, appeared. And why they are
hidden? Because they contain configuration commands, setting options or internal scripts defining the behaviour of your user, OS processes, or other third-party software. This files should not be modified by inexperienced users. And in case they are, it is something done with little frequency.

Let's have a look to some of them. If the computer, Ixtlilton in this case, is your work tool, it
is your duty to know how it works.

## '.bashrc'

The file '.bashrc' is one of the most important files to define the behaviour of your user and
terminal. Actually, this file is executed every time you open a new terminal, or you log in. Do you
want to test it? Open this file with your text editor and add as its first line:

```bash
echo "Welcome back pal!"
```

Now save the file, close it, close the terminal or log out your session... and open a new terminal or log in again. Aha! you see... the file '.bashrc' can be used to define the format and colors of your prompt, to load auxiliary files with scripts run before the user can do anything, and to trigger processes before a user works in its terminal.

You could define here the definition of new environment variables. Try to add a line as:

```bash
export KEYCODE='123456'
export VAR=100
```

Reload your '.bashrc' closing and opening your terminal or session, or doing:

```bash
source .bashrc
```

And type:

```bash
echo $KEYCODE
```

or:

```bash
echo $[$VAR+100]
```

Now, you are probably wondering -if you are linux user with few experience-: is this then the place
where the user variables HOME, WORK or SCRATCH? That's right, but to load the definition of these
variables in every user, this is done in a common file with path 'opt/etc/user\_bashrc' where the
following lines are placed:

```bash
PS1="────────\n\033[1;37;42m{`hostname`}:\033[2;34m \w\033[0;0m \n\[\033[30;47m\][\[\033[31m\]\u\[\033[30;47m\]@:\W]$\[\033[00m\](\#)\[\$prevCmd\]->\[$RST\]"

export HOME=/home/$USER
export WORK=/work/$USER
export SCRATCH=/scratch/$USER

export DATA=/projects/DATA
export HOTDATA=/projects/HOTDATA

alias cdh="cd $HOME"
alias cds="cd $SCRATCH"
alias cdw="cd $WORK"

export HISTSIZE=10000
export HISTFILESIZE=10000

export PATH=$HOME/opt/bin:${PATH}
export LIBRARY_PATH=$HOME/opt/lib:$HOME/opt/lib32:$HOME/opt/lib64:${LIBRARY_PATH}
export LD_LIBRARY_PATH=$HOME/opt/lib:$HOME/opt/lib32:$HOME/opt/lib64:${LD_LIBRARY_PATH}
export INCLUDE=$HOME/opt/include:${INCLUDE}

# Own modulefiles
module use $HOME/opt/modulefiles
```

And this file is loaded by your '$HOME/.bashrc' file with the lines:

```bash
# Source global user definitions
if [ -f /opt/etc/user_bashrc ]; then
        . /opt/etc/user_bashrc
fi
```

Many programs and scripts use this file to trigger the initial set up for the user. You can see how
'conda' added some few lines between the lines:

```bash
# >>> conda initialize >>>
...
...
...
unset __conda_setup
```

You can define the behaviour of your terminal, prompt, commands history record, etc. But to conclude this section, let's pay attention to the piece of code in your '$HOME/.bashrc':

```bash
# My alias definitions
if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi
```

This is not the first time the word 'alias' is shown in this section. Go above to find the lines:

```bash
alias cdh="cd $HOME"
alias cds="cd $SCRATCH"
alias cdw="cd $WORK"
```

Let's see what are these alias -in case you don't know it yet- in the following section.

## '.bash\_aliases'

If you are reading this section you might not be familiar with the concept of 'alias' in linux.
You can define aliases for commands in your terminal. Try:

```bash
alias list="ls"
```

Now you can type in your terminal "list" and the "ls" command will be executed. You have defined an
alias. But this alias is not permanent. This alias will be forgotten as soon as you close your
terminal. That's why the alias must be define every time you open a session or a terminal. And this
can be done by means of the same '$HOME/.bashrc' or by any other file loaded by '$HOME/.bashrc'. In
the case of the common aliases to all users:

```bash
alias cdh="cd $HOME"
alias cds="cd $SCRATCH"
alias cdw="cd $WORK"
```

their definition are included by the administrators in the file '/opt/etc/user\_bashrc'. Now, in case you
want to define new aliases, you can do it adding them as new lines in your '$HOME/.bashrc'. Or, if
you want to keep your '.bashrc' well organized, you can put these aliases definition in your
'.bash\_aliases' file. To show you the way, the administrators included the first useful alias in
your dot file:

```bash
alias squeuel='squeue --format="%.18i %24j %.8u %.12T %.12M %.12l %.6D %.12P %R"'
```

## '.bash\_profile'

This shell script does not exist by default in all Linux distributions for users. The effect of this
script in the case of Ixtlilton users is a bit redundant. The role played by '.bash\_profile' is similar
to the one played by '.bashrc', but in different moments:

- '.bash_profile' is executed when the user opens a new session.
- '.bashrc' is executed when the user executes bash

But in the case of Ixtlilton there is no difference, since the user '.bash\_profile' is loading the '.bashrc' file of the same user:

```bash
# Get the aliases and functions
if [ -f ~/.bashrc ]; then
        . ~/.bashrc
fi
```

## '.bash\_history'

The '.bash\_history' is not a shell script. This dot file stores the recent list of commands your
user executed in chronological order. Did you notice that using the 'up arrow' in your terminal, or
making use of the reverse-search with 'ctr-r', you can recover a command that was receantly
executed? This is because your history record is stored in '.bash\_history'.

## '.ssh'



## '.google\_authenticator'

## '.emacs', '.emacs.d', '.vim', '.vimrc', and '.viminfo'

## '.gitconfig'

## '.conda' and 'condarc'

