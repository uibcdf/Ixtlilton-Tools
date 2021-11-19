# Conda

## Installing Conda for multiple users

The multiuser installation will be administrated by a specific user named 'anaconda'.

```bash
su
adduser anaconda
```

Now, the installation script can be downloaded and handled.

```bash
mkdir /opt2/src/conda

wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
mv Miniconda3-latest-Linux-x86_64.sh /opt2/src/conda/.
cd /opt2/src/conda
chmod +x Miniconda3-latest-Linux-x86_64.sh

bash /opt2/src/conda/Miniconda3-latest-Linux-x86_64.sh  -b -p /opt2/apps/conda
```

Rights need to be fixed to be used by any user and to be administratated only by anaconda

```bash
chown -R anaconda:anaconda /opt2/apps/conda
chmod -R go-w /opt2/apps/conda
chmod -R go+rX /opt2/apps/conda
```

Finnally, the .condarc file of anaconda needs to look like:

```
auto_activate_base: false
channels:
  - uibcdf
  - omnia
  - salilab
  - defaults
  - conda-forge
  - ambermd
```

And at the end of the anaconda's .bashrc the following lines need to be included (as well as for every user):

```bash
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
# <<< conda initialize <<<
```

> **_More Info:_**    
> https://medium.com/@pjptech/installing-anaconda-for-multiple-users-650b2a6666c6    
> https://docs.anaconda.com/anaconda/install/linux/    
> https://docs.anaconda.com/anaconda/install/    
> https://docs.anaconda.com/anaconda/install/multi-user/    
> https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html    
> https://docs.conda.io/projects/conda/en/latest/user-guide/configuration/admin-multi-user-install.html    



## Conda administration

Conda envs is administrated by a user named 'anaconda':

```
su anaconda
```

This means that only the user 'anaconda' has the right to install, update or remove packages and
environments.

### Conda info

Some info about the channels and
installation configuration can be found with:

```bash
conda info
```

The environments created by the administrator can be checked as:

```bash
conda info --envs
```

### Update conda

```bash
conda update conda
```

```bash
conda clean -a
```

### Create environment for all users

For python 3.7:

```bash
conda create -n name_env python=3.7
```

### Activate environment

```bash
conda activate name_env
```

### Install packages in environment

```bash
conda install package1 package2 package3
```

### Update environment

```bash
conda activate name_env
conda update --all
conda clean -a
```

## UIBCDF_lab conda environments

This is the most stable environment to perform standard work at the UIBCDF. The environment is
kept updated in a central repository ([see instructions here](https://github.com/uibcdf/UIBCDF_lab)).

### UIBCDF_lab

```bash
conda activate UIBCDF_lab
```

```bash
conda list
```

The OpenMM package has no fixed version of cudatoolkit as dependency, although it does. The way to
avoid unwanted upgrades of this last package, the version can be pinned:

```bash
vim $CONDA_PREFIX/conda-meta/pinned
```

There, a line for cudatoolkit needs to be included:

```
cudatoolkit 10.1.*
```

