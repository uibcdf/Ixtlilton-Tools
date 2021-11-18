# README

This directory contains instructions to create or update the conda environments to work with this
repository.

The following two subsections need the python scripts with executable rights:

```bash
chmod +x create_conda_env.py
chmod +x update_conda_env.py
```

And the Python library `pyyaml` needs to be installed:

```bash
conda install pyyaml
```

## How to make a new conda environment

Let's show how to create a new conda environment named 'Ixtlilton' with the Python version 3.7 and the list of packages and channels found in the yaml file 'development_env.yaml', for instance.

```bash
./create_conda_env.py -n Ixtlilton -p 3.7 development_env.yaml
```

## How to update a pre-existing conda environment

Let's show here how to update a conda environment named 'Ixtlilton', previously created, with the
list of packages and channels in the yaml file 'development_env.yaml', for instance.

```bash
conda activate Ixtlilton
./update_conda_env.py development_env.yaml
```

