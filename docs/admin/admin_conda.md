# Conda

# Conda as module to be loaded

```bash
module avail conda

-------------------------------------------------------------------------- /opt2/modulefiles ---------------------------------------------------------------------------
   conda/gcc-4.8.5_miniconda (L)    conda/intel-2018_miniconda (D)

  Where:
   L:  Module is loaded
   D:  Default Module

Use "module spider" to find all possible modules.
Use "module keyword key1 key2 ..." to search for all possible modules matching any of the "keys".
```

```bash
module load conda/gcc-4.8.5_miniconda
```

The module had dependencies that where loaded at once.

```bash
module list

Currently Loaded Modules:
  1) CUDA/gcc-4.8.5_10.0   2) cmake/gcc-4.8.5_3.13.4   3) openmpi/gcc-4.8.5_CUDA-10.0_4.0.0   4) conda/gcc-4.8.5_miniconda
```

The environments created by the administrator can be checked as:

```bash
conda info --envs

# conda environments:
#
UIBCDF_lab_dev           /home/diego/.conda/envs/UIBCDF_lab_dev
base                  *  /opt2/apps/conda/gcc-4.8.5_miniconda
PyMOL_open-source        /opt2/apps/conda/gcc-4.8.5_miniconda/envs/PyMOL_open-source
PyRosetta                /opt2/apps/conda/gcc-4.8.5_miniconda/envs/PyRosetta
UIBCDF_lab               /opt2/apps/conda/gcc-4.8.5_miniconda/envs/UIBCDF_lab
```

## Managing the conda environments

The conda envs are administrated by a user named 'anaconda':

```
su anaconda
```

This means that only the user 'anaconda' has the right to install, update or remove packages and
environments.

Once the user has been logged in, the module to be managed needs to be loaded:

```
module load conda
```

At this point the administration of conda is as done normally. Some info about the channels and
installation configuration can be found with:

```bash
conda info
```

The list of environments is obtained with:

```bash
conda info --envs
```

### UIBCDF_lab environment

This is the most stable environment to perform standard work at the UIBCDF. The environment is
kept updated in a central repository ([see instructions here](https://github.com/uibcdf/UIBCDF_lab)).


