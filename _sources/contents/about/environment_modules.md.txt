# Environment modules

## What is an environment module system?

An HPC cluster needs to be used by different users with different needs.
With this in mind, installing the scientific software in the operating system is not functional.
Some times different versions of the same software is needed. Some times the software required has
dependencies with compatibility issues. In this sceneario, having an environment modules manager is highly
recommended. This is one of the best ways to dinamically change the users environment
(environmental variables such as binary paths, library paths, etc). 

## Lmod

To work with environment modules, Ixtlilton operates with Lmod. As user, in principle you only need
to know how to check the modules available for you, and how to load and unload them.

### Listing the available modules

The following command shows the list of modules available for you to be used:

```bash
module avail
```

or

```bash
module spider
```

Notice that modules are located in different places. Those in `/opt/modulefiles` and
`/opt2/modulefiles` are managed by the cluster administrators. The modules you can find there
correspond to already compiled software that you load and unloaded. As you will see at the end of
this document, your user can also define modules locally and only available for you.

### Looking for a module

Modules can be located with a keyword this way:

```bash
module keyword
```

or

```bash
module spider keyword
```

### Loading modules

To load a module:

```bash
module load gromacs/intel-2018_mkl_2019.1
```

Some modules depend on others. Lmod usually handle this without out disturbing the user. If this is
not the case, a message like this one will be returned with information of the modules the user
needs to load as dependencies:

```bash
Lmod has detected the following error:  Cannot load module "gromacs/gcc-4.8.5_ownfftw_2019.1". At least one of these module(s) must be loaded:
   openmpi/gcc-4.8.5_CUDA-10.0_4.0.0 cmake/gcc-4.8.5_3.13.4 CUDA/gcc-4.8.5_10.0

While processing the following module(s):
    Module fullname                   Module Filename
    ---------------                   ---------------
    gromacs/gcc-4.8.5_ownfftw_2019.1  /opt2/modulefiles/gromacs/gcc-4.8.5_ownfftw_2019.1
```

### Showing loaded modules

To show the loaded modules:

```bash
module list
```

### Unloading modules

To unload a module:

```bash
module unload gromacs/gcc-4.8.5_ownfftw_2019.1
```

Notice that the module loaded as dependencies will be also unloaded.

If all loaded modules need to be unloaded at once, you can type:

```bash
module purge
```

### Default modules

Module names are long. When a program was compiled in different flavors (version, compilation
options, etc) this is specified in the name. For example, you can find gromacs in at least two
versions in the output of `module avail`:

```bash
----------- /opt2/modulefiles -------------
   gromacs/gcc-4.8.5_ownfftw_2019.1 (D)
   gromacs/gcc-6.4.0_ownfftw_2019.1  
```

When this happens, there is always a module marked with "(D)". This is default module. If only the
name of the family of modules, in this case 'gromacs' is invoked as argument of `module load`:

```bash
module load gromacs
```

the default module is loaded:

```bash
module list


Currently Loaded Modules:
  1) CUDA/gcc-4.8.5_10.0   2) cmake/gcc-4.8.5_3.13.4   3) openmpi/gcc-4.8.5_CUDA-10.0_4.0.0   4) gromacs/gcc-4.8.5_ownfftw_2019.1

```

### Printing out information about modules

There are some different commands to print out information about a specific module. It is worth
giving a try to each of them, the resulting level of detail in the output is different.

```bash
module help gromacs/gcc-4.8.5_ownfftw_2019.1
```

```bash
module whatis gromacs/gcc-4.8.5_ownfftw_2019.1
```

```bash
module show gromacs
```

```bash
module spider gromacs
```

## Your own environment modules

Every user can have its own environment modules: private and locally stored in their home directories.

It is suggested that for this purpose, the software to be loaded as modules is placed in your
`~/opt` directory. For example, if you need to install XXX in the version 4.7:

```bash
mkdir -p ~/opt/XXX/4.7
```

Once the proper compilation was finished, you can store the modulefile with the loading
instructions in the directory:

```bash
cd ~/opt/modulefiles
```

The former directory is checked for environment modules by default for every user. If you want to
include other directories with modulefiles, chech the the variable 'MODULEPATH' is rewritten with
the following line in your '~/.bashrc' file:

```bash
export MODULEPATH=$MODULEPATH:/home/username/directories_path_to/modulefiles
```

> **_More Info:_**    
> http://lmod.readthedocs.org   
> https://github.com/TACC/Lmod   
> https://lmod.sf.net    
> https://www.tacc.utexas.edu/research-development/tacc-projects/lmod    
> http://modules.sourceforge.net/     
> https://en.wikipedia.org/wiki/Environment_Modules_(software)    
> http://%01%01https://en.wikipedia.org/wiki/Environment_Modules_%28software%29    
> http://modules.sourceforge.net/    
> http://www.admin-magazine.com/HPC/Articles/Environment-Modules     
> http://sourceforge.net/p/modules/wiki/FAQ/    
> https://www.nersc.gov/users/software/nersc-user-environment/modules/    
> http://modules.sourceforge.net/man/module.html    
> http://modules.sourceforge.net/man/modulefile.html    


