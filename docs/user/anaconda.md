# Using Conda

## Loading the module

With `module avail conda` you will see we have more than module available:

```
-------------------------------------- /opt2/modulefiles ----------------------------------------
   conda/gcc-6.4.0_miniconda    conda/intel-2018_miniconda (D)

  Where:
   D:  Default Module

Use "module spider" to find all possible modules.
Use "module keyword key1 key2 ..." to search for all possible modules matching any of the "keys".
```

In principle you are encouraged to use conda with the last gcc compiler.
The version with intel compilers is a experimental module. Intel has its own version of common
libraries such as numpy o scipy. Apparently they achieve a much better performance, but we have to
test it first.


## Creating your own conda environments

The environments already set up in those modules are managed by a user named anaconda. However, all
users have rights to read and execute them. If you want to create your own conda environment, do it
as usual:

```bash
conda create -n name_env python=3.7
```

This will be created in your own conda config directory:

```
~/.conda
```

And no other user will see it.
