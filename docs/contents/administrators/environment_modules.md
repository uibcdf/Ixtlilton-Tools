# Environment Modules

### Sources: <br /> 
[wikipedia.org][1], <br />
[modules.sourceforge.net][2], <br /> [admin-magazine.com/.../Environment-Modules][3] (this one is good), <br />
[sourceforge.net/p/modules/...][4] (this one is good), <br />
[https://www.nersc.gov/.../modules/][5] (this one is good), <br />
[.../man/module.html][6] (the files structure described here is not the right one for ubuntu), <br />
[.../man/modulefile.html][7] <br />


http://modules.sourceforge.net/
https://en.wikipedia.org/wiki/Environment_Modules_(software)


## In Ixtlilton (Centos 7)

```bash
yum -y install install environment-modules tcl tk
```

Checking the paths where modules can be shared:

```bash
cat ${MODULESHOME}/init/.modulespath
```

The directory ```/etc/modulefiles``` is used to share global scientific software and tools.





## In a workstation (Ubuntu)


```bash
$ sudo apt-get install environment-modules
```
I do not follow the standard procedure. Instead, I just edit the file .bashrc to add at the beginning this first line:
```bash
$ . /etc/profile.d/modules.sh
```

This way the path of the modules is: <br />
/usr/share/modules/Modules/ <br />
/usr/bin/modulecmd <br />
/usr/bin/add.modules <br />
/usr/share/modules/init/.modulespath <br />
/etc/environment-modules/modules <br />
...
<br /><br />
Edit the .bashrc to add command module with the correct path to modulecmd this way:
```bash
#module() { eval `/usr/Modules/$MODULE_VERSION/bin/modulecmd $modules_shell $*`; }
module() { eval `/usr/bin/modulecmd $modules_shell $*`; }
```

Now check that all modules paths found in files /usr/share/modules/init/.modulespath and /etc/environment-modules/modulespath are accesible. In my case I had to remove a couple of lines:
```bash
/etc/environment-modules/modules
/usr/share/modules/versions                             # location of version files
/usr/Modules/$MODULE_VERSION/modulefiles        # Module pkg modulefiles (if versioning)
#/usr/Modules/modulefiles       # Module pkg modulefiles (if no versioning)
/usr/share/modules/modulefiles                          # General module files
#/usr/Modules/3.2.10/your_contribs                      # Edit for your requirements
```

A local folder in my home directory is created for my modules:
```bash
$ mkdir -p ~/Myusr/share/modules/modulefiles
```

I add a new line in my .bashrc:
```bash
export MODULEPATH=$MODULEPATH:/home/diego/Myusr/share/modules/modulefiles
```

And a section called '### LOAD DEFAULT MODULES' where the default modules will be added.

## Example:
Some examples can be found in sections 'GPUs: Nvidia drivers and CUDA', 'Intel Compilers', ...

---

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


### Useful commands:
Where xxx and yyy are names of modules available:

```bash
$ module help
$ module avail
$ module list
$ module load xxx
$ module help xxx
$ module whatis xxx
$ module show xxx
$ module switch xxx yyy
```


  [1]: http://%01%01https://en.wikipedia.org/wiki/Environment_Modules_%28software%29
  [2]: http://modules.sourceforge.net/
  [3]: http://www.admin-magazine.com/HPC/Articles/Environment-Modules
  [4]: http://sourceforge.net/p/modules/wiki/FAQ/
  [5]: https://www.nersc.gov/users/software/nersc-user-environment/modules/
  [6]: http://modules.sourceforge.net/man/module.html
  [7]: http://modules.sourceforge.net/man/modulefile.html
