

### Marking a version as default

An auxiliary soft link is created with the name 'default' pointint to the module file to be used as
default version. More info can be found in [the online documentation](https://lmod.readthedocs.io/en/latest/060_locating.html#marking-a-version-as-default).

```
cd /opt2/modulefiles/gromacs/
ln -s gcc-4.8.5_ownfftw_2019.1 default
```

The result can be easily checked with:

```
module avail gromacs
```
