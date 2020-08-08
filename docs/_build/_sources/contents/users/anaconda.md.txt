# Conda

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
