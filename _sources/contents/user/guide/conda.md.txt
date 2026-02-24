# Conda

## What's conda?

Conda is a language-agnostic open-source packages and environments manager. In case you are not
familiar with conda, you need to know at least two things to follow this section:

- With conda you can install software in your computer without altering the OS. This 
  software come from conda repositories, called 'channels', pre-compiled as 'packages' to be used
  locally in your machine.
- Conda works with 'virtual working environments'. Each environment can have a list of packages
  installed independently of other environments or the OS.

## The channels and the .condarc file

By default conda downloads packages from a standard official "default" channel. But developers, labs and
users can deploy software via their own channels. For example, the UIBCDF has its own
channel were the last stable versions of the libraries developed by the lab are available to
be installed with conda. If you want to include a channel in your default list of channels used as
repositories include its name as new item in your `~/.condarc` file. Be aware that channels are
sorted there in priority order.

```bash
# .condard file
channels:
   - AAA
   - BBB
   - CCC
```

In the above example, if the same package is found the all channels, this wil be downloaded from
the first one in the list (AAA).

By default, your user has a list of channels configured by Ixtlilton administrators:

```bash
# .condard file
channels:
   - uibcdf
   - conda-forge
   - default
```

## The environments

Conda defines working environments. Each environment is a "closed box" where libraries can be
installed in a virtual space no matter the software pre-installed in the operating system. These
software can be used only with the environment activated. Once the environment is deactivated, the
user works in its linux session with the software in the system. Lets illustrate this with an
example. Execute in your terminal the following command:

```bash
python --version
```

The output will be `Python 2.7.5`. This is the version of the python interpreter installed in the
system for all users. You can check the location of this python with:

```bash
which python
```

As you see, this python is in '/usr/bin/'. Now activate an environment and try to do the same:

```bash
conda activate UIBCDF_lab
python --version
```

The version of the python interpreter has changed. This is because now you are using the set of
packages installed in the environment. Check for instance where is this python located:

```bash
which python
```

Conda allows us working with isolated working environments different packages and versions
installed. This way we can work without being worried of creating compatibility
problems with the software of the system.

The list of environments available for your user can be printed out in the terminal with the
command:

```bash
conda info --envs
```

### Activation

An environment can be loaded in your unix session typing in the terminal:

```bash
conda activate my_env
```

### Deactivation

To go back to your default unix session, deactivate the conda environment with:

```bash
conda deactivate
```

### List of installed packages

Once an environment has been activated, the list of installed packages can be shown with the
command:

```bash
conda list
```

This list can also be printed out with out entering in the environment. Lets lists the packages of
'UIBCDF\_lab' from anywhere:

```bash
conda list -n UIBCDF_lab
```

### The UIBCDF environments

The UIBCDF lab has defined some shared environments accessible to any user. Those environments are
manteined by the administrators. As such, the standard users can not install or remove
packages there. They are placed in the directory `/opt/apt2/conda` and are the following.

#### UIBCDF\_lab

The environment 'UIBCDF\_lab' keeps in a single place all the common packages used in the lab. They
can listed as:

```bash
conda list -n UIBCDF_lab
```

The UIBCDF libraries present in this environment are in its last stable version. If you want to use them in its developing
version, having your own environment named 'UIBCDF\_lab\_dev', for example, it is suggested to you.
Find the instructions to do that in the following subsection.

## Your own conda environments

The environments set up in `/opt2/apps/conda` are managed by the cluster administrators. However, all
users have rights to read and execute them. You can create and manage your own conda environment.

### Create a new environment

To create a new environment managed by your user, type:

```bash
# if the env is with python 3.7
conda create -n name_env python=3.7
```

where 'name\_env' should be replaced by the name of your election.

This environment will be created in your own conda config directory:

```bash
~/.conda
```

And no other user can use it or manage it. Your new environment appears now for you in the list:

```bash
conda info --envs
```

### Installing packages

With the environment activate

```bash
conda install package1 package2
```

If a package needs to be installed from specific channel named `channelX`:

```bash
conda install package1 -c channelX
```

The version of a package can also be included in the installation command:

```bash
conda install package1=2.3
```

### Removing packages

Within the environment from which some packages are going to be removed:

```bash
conda conda remove package1 package2
```

### Updating packages

All packages installed in a environment can be updated (if a newer version is present in the
list of channels in your file '.condarc'.

```bash
conda update --all
```

If specific package needs to be updated:

```bash
conda update package1
```

### Removing a conda environment

To remove a conda environment make sure it is deactivated, and then:

```bash
conda env remove -n env_name
```

where 'name\_env' should be replaced by the name of the environment you want to remove.


