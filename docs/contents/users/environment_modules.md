
# Environment modules

La versión de gestor de Environment Modules instalada en ixtlilton es la llamada Lmod:

Documentation:    http://lmod.readthedocs.org
Github:           https://github.com/TACC/Lmod
Sourceforge:      https://lmod.sf.net
TACC Homepage:    https://www.tacc.utexas.edu/research-development/tacc-projects/lmod

Sobre el concepto general de Environment Modules puedes encontrar más información al final del notebook.

## Instalación y Configuración

https://lmod.readthedocs.io/en/latest/030_installing.html


Comprobando las rutas donde los módulos pueden ser compartidos:

```bash
cat ${MODULESHOME}/init/.modulespath
```

### Módulos comunes



### Módulos de cada usuario

A local folder in my home directory is created for my modules:
```bash
$ mkdir -p ~/Myusr/share/modules/modulefiles
```

I add a new line in my .bashrc:
```bash
export MODULEPATH=$MODULEPATH:/home/diego/Myusr/share/modules/modulefiles
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

## Más información

### Sources: <br /> 
[wikipedia.org][1], <br />
[modules.sourceforge.net][2], <br /> [admin-magazine.com/.../Environment-Modules][3] (this one is good), <br />
[sourceforge.net/p/modules/...][4] (this one is good), <br />
[https://www.nersc.gov/.../modules/][5] (this one is good), <br />
[.../man/module.html][6] (the files structure described here is not the right one for ubuntu), <br />
[.../man/modulefile.html][7] <br />


http://modules.sourceforge.net/
https://en.wikipedia.org/wiki/Environment_Modules_(software)




  [1]: http://%01%01https://en.wikipedia.org/wiki/Environment_Modules_%28software%29
  [2]: http://modules.sourceforge.net/
  [3]: http://www.admin-magazine.com/HPC/Articles/Environment-Modules
  [4]: http://sourceforge.net/p/modules/wiki/FAQ/
  [5]: https://www.nersc.gov/users/software/nersc-user-environment/modules/
  [6]: http://modules.sourceforge.net/man/module.html
  [7]: http://modules.sourceforge.net/man/modulefile.html


