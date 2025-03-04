# Dot files and directories

In a unix OS, the dot files or directories are those whose name starts with ".". This only fact makes them hidden. Try to type in your terminal de following:

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
where the user variables `HOME`, `WORK` or `SCRATCH`? That's right, but to load the definition of these
variables in every user, this is done in a common file with path 'opt/etc/user\_bashrc' where the
following lines are placed:

```bash
PS1="────────\n\033[1;37;42m{`hostname`}:\033[2;34m \w\033[0;0m \n\[\033[30;47m\][\[\033[31m\]\u\[\033[30;47m\]@:\W]$\[\033[00m\](\#)\[\$prevCmd\]->\[$RST\]"

export HOME=/home/$USER
export WORK=/work/$USER
export SCRATCH=/scratch/$USER

export DATA=/projects/DATA
export HOTDATA=/projects/HOTDATA

export HISTSIZE=10000
export HISTFILESIZE=10000

export PATH=$HOME/.local/bin${PATH}
export LIBRARY_PATH=$HOME/.local/lib:$HOME/.local/lib32:$HOME/.local/lib64:${LIBRARY_PATH}
export LD_LIBRARY_PATH=$HOME/.local/lib:$HOME/.local/lib32:$HOME/.local/lib64:${LD_LIBRARY_PATH}
export INCLUDE=$HOME/.local/include:${INCLUDE}

# Modulefiles
module use $HOME/.local/opt/modulefiles

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/opt2/apps/conda/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/opt2/apps/conda/etc/profile.d/conda.sh" ]; then
        . "/opt2/apps/conda/etc/profile.d/conda.sh"
    else
        export PATH="/opt2/apps/conda/bin:$PATH"
    fi
fi
unset __conda_setup
```

And this file is loaded by your '\$HOME/.bashrc' file with the lines:

```bash
# Source global user definitions
if [ -f /opt/etc/user_bashrc ]; then
        . /opt/etc/user_bashrc
fi
```

Many programs and scripts use this file to trigger the initial set up for the user. You can see how
'conda' usually adds some few lines. In your workstation or laptop, if you work with conda, you
will probably see a section like the following in your '~/.bashrc' file:

```bash
# >>> conda initialize >>>
...
...
...
unset __conda_setup
```

The administrators put these lines in '/opt/etc/user\_bashrc' to have these orders centralized for
all users in case the configuration of conda changes in Ixtlilton.

What other things can you do with you '.bashrc'? You can define the behaviour of your terminal, prompt, commands history record, etc. But to conclude this section, let's pay attention to the piece of code in your '\$HOME/.bashrc':

```bash
# My alias definitions
if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi
```

Your '.bashrc' file is executing, if exists, another shell script named '.bash\_aliases'. Let's see what this file is in the following section.

## '.bash\_aliases'

If you are reading this section you might not be familiar with the concept of 'alias' in linux.
You can define aliases for commands in your terminal. Try:

```bash
alias list="ls"
```

Now you can type in your terminal "list" and the `ls` command will be executed. You have defined an
alias. But this alias is not permanent. This alias will be forgotten as soon as you close your
terminal. That's why the alias must be define every time you open a session or a terminal. And this
can be done by means of the same '\$HOME/.bashrc' or by any other file loaded by '\$HOME/.bashrc'.


Thus, in case you want to define your own aliases, you can do it by adding them as new lines in your '\$HOME/.bashrc'. Or, if
you want to keep your '.bashrc' well organized, you can put these aliases definition in your
'.bash\_aliases' file. To show you the way, the administrators included the first useful alias in
this former file as you can see in the section ["Shell aliases"](shell_aliases.md).

## '.bash\_profile'

This shell script does not exist by default in all Linux distributions for users. The effect of this
script in the case of Ixtlilton users is a bit redundant. The role played by '.bash\_profile' is similar
to the one played by '.bashrc', but in different moments:

- '.bash\_profile' is executed when the user opens a new session.
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
user executed in chronological order. Did you notice that using the 'up arrow' key in your terminal, or
making use of the reverse-search with 'ctrl-r', you can recover a command that was receantly
executed? This is because your history record is stored in '.bash\_history'.

## '.ssh'

As it was introduced in the user guide section '[Login](login.md)', the SSH protocol is used to make
secure shell remote connections. This protocol, executed with the command 'ssh', needs some
user settings and credentials. And the directory '\$HOME/.ssh' is the place to store them.

Among the files you can find in your '\$HOME/.ssh', there is one you should know if you are GitHub
user: '\$HOME/.ssh/id\_rsa.pub'. This file stores the RSA key of your user. And this key is an
addition security filter to approve a remote connection between two machines. The machine receiving
the remote access petition can be configured to deny any ssh login request if the RSA public key is
not recognized as authorized -even if the user and passwords are ok-. Or, in case you want to, or
you have to, authorized remote connections without password, the SSH protocol can be configured to
work only with the RSA keys as validation method. This is the case of the remote data transfer with 'git' between your local repository clone and your remote GitHub repository.

## '.google\_authenticator'

Ixtlilton has the Google Authenticator two-factor login mechanism enabled for remote conexions.
Your two factor authentication credentials are stored in this file.

## '.emacs', '.emacs.d', '.vim', '.vimrc', and '.viminfo'

Text editors can also be very customizable. Some of them let you define commands, routines,
shortcuts, etc. In case you use emacs or vim you can find in your home directory hidden files and
directories as the ones in the title of this subsection.

## '.gitconfig'

Git also needs a place to store your user name and email, as well as some other user option as the
preferred text editor or your default branch name. This user settings can be defined via command
line (with the command 'git-config'), but if you know the '.gitconfig' syntax, you can also do it
editing this dot file.

## '.conda' and 'condarc'

Conda is the package and enviroments installed in Ixtlilton. The administrators performed a central
installation but each user has its own setting options and the possibility to define a private list
of environments. Again, this is defined in a couple of dot files and directories in your '\$HOME'. As such, the file '\$HOME/.condarc' stores your default list of conda channels and some configuration options of your user as the auto-activation of your base environment. Additionally the directory '\$HOME/.conda' include some internal information used by conda related with your user, as your list of environments.

