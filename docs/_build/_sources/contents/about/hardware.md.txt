# Hardware

<!-- processor: lscpu -->
<!-- ram: free -m -->
<!-- storage: lsblk -->
<!-- graphics: lspci | grep VGA      o      sudo lshw -C video -->
<!-- network: lspci | egrep -i --color 'network|ethernet'   o   lshw -class network -->
<!-- motherboard: sudo dmidecode | grep -A4 'Base Board' -->
<!-- os and kernel: less /etc/*elease -->


### Ixtlilton

|                 | Master Node                                                                                                      |
| ---             | ---                                                                                                              |
| **processor**   | 2 Sockets: Intel(R) Xeon(R) CPU E5-2630 v4 @ 2.20GHz <br/> 10 Cores per Socket * 2 Threads per core = 40 threads |
| **ram**         | 64 Gb                                                                                                            |
| **storage**     | 250 Gb SSD [ / -home included-] <br/> 4x3Tb raid5 (8.2 Tb) [ /work ]                                             |
| **graphics**    | Chipset Integrated ASPEED Graphics Family <br/> Nvidia GeForce GT 710                                            |
| **network**     | (2x) Intel Corporation I210 Gigabit Network Connection                                                           |
| **motherboard** | ASUSTeK COMPUTER INC., Z10PE-D16 WS                                                                              |
| **os**          | centos 7.3.1611                                                                                                  |
| **kernel**      | 3.10.0-327.el7.x86_64                                                                                            |


> ***Note***: This node should be included in the "CPUs computation" section. Once the cluster has some storage server nodes, 
> the directory /work with the raid 5 should not be here but in the storage section.
> This node should also execute tasks from the queues "test" and "short".

### Section CPUs computation

|                 | 2 Nodes                                                                                                          |
| ---             | ---                                                                                                              |
| **processor**   | 2 Sockets: Intel(R) Xeon(R) CPU E5-2630 v4 @ 2.20GHz <br/> 10 Cores per Socket * 2 Threads per core = 40 threads |
| **ram**         | 64 Gb                                                                                                            |
| **storage**     | 250 Gb SSD [ / -home included-] <br/> 1x3Tb [ /local_storage ]                                                   |
| **graphics**    | Chipset Integrated ASPEED Graphics Family <br/> Nvidia GeForce GT 710                                            |
| **network**     | (2x) Intel Corporation I210 Gigabit Network Connection                                                           |
| **motherboard** | ASUSTeK COMPUTER INC., Z10PE-D16 WS                                                                              |
| **os**          | centos 7.3.1611                                                                                                  |
| **kernel**      | 3.10.0-514.16.1.el7.x86_64                                                                                       |


### Section GPUs computation

|                 | 2 Nodes                                                                                                          |
| ---             | ---                                                                                                              |
| **processor**   | 2 Sockets: Intel(R) Xeon(R) CPU E5-2630 v4 @ 2.20GHz <br/> 10 Cores per Socket * 2 Threads per core = 40 threads |
| **ram**         | 64 Gb                                                                                                            |
| **storage**     | 250 Gb SSD [ / -home included-] <br/> 2x3Tb raid5 (5.5Tb) [ /local_storage ]                                     |
| **graphics**    | Chipset Integrated ASPEED Graphics Family <br/> (2x) Nvidia GeForce GTX 1080                                     |
| **network**     | (2x) Intel Corporation I210 Gigabit Network Connection                                                           |
| **motherboard** | ASUSTeK COMPUTER INC., Z10PE-D16 WS                                                                              |
| **os**          | centos 7.3.1611                                                                                                  |
| **kernel**      | 3.10.0-514.16.1.el7.x86_64                                                                                       |

> ***Note***: This nodes should have 4 GPUs. They should also have a fast communication among them. 

### Section Storage



## TODO list:

- [x] task 1
- [x] task 2
- [ ] task 3
- [ ] task 4

#### Notas:
- Todos los raid están montados via software (mdadm).

### Definición de colas: 

Creo que el nodo master debería de estar tambien haciendo trabajos para el gestor pero sólo para los "tests" y las tareas "cortas". 


### Dudas:

- Pusimos un kernel con hyperthreading. Hemos hecho bien?


##### Aqui mas:

## Cluster Admin

## Descripción de los Componentes:

### Redes

IP Rangos:
 193.168.0.1 - 19                       (DHCP WIFI)
 193.168.0.20 - 49                     (Workstations)
 193.168.0.50 - 99                     (Perifericos y equipo de laboratorio)
 193.168.0.100 - 101                (Ixtlilton)
 193.168.0.102 - 253                (Nodos CPU y GPU)
 193.168.0.254                          (Router)

#### Switches
2 Switches (uno por rack)

#### Router

193.168.0.254
uibcdf
adm1n4147

#### Wifi

Hay dos puntos de anclaje: UIBCDF y UIBCDF5G

193.168.0.51
admin
adm1n4147

#### NAS
En la próxima compra esto quedará para uso de backups de usuarios (nauta y spika)
197.168.0.50
uibcdf
adm1n4147

para ssh:
ssh sshd@192.168.0.203
adm1n4147

### Nodo Master

 193.168.0.100           Ixtlilton
 193.168.0.101           Ixtlilton-2

Operating System: CentOS Linux 7 (Core)
CPE OS Name: cpe:/o:centos:centos:7
Kernel: Linux 3.10.0-327.el7.x86_64


### Nodos CPUs

### Nodos GPUs

### Nodos Storage

### Workstations

### Impresora

http://193.168.0.52/general/status.html

-----------------

## HOST FILE 
193.168.0.254 router
193.168.0.50  nas
193.168.0.51  wifi
193.168.0.52  printer

193.168.0.20 spika
193.168.0.21 spika-2
193.168.0.22 nauta
193.168.0.23 nauta-2

193.168.0.100 ixtlilton
193.168.0.101 ixtlilton-2

193.168.0.102 cpu01
193.168.0.103 cpu01-2
193.168.0.104 cpu02
193.168.0.105 cpu02-2

193.168.0.140 gpu01
193.168.0.141 gpu01-2
193.168.0.142 gpu02
193.168.0.143 gpu02-2


## Software administration:

## OS

***Dilema:***
OS disto:  CentOS, Ubuntu, Debian, TOSS, etc? 

***Respuesta:***
Me gustaría probar ubuntu por que estoy mas habituado y por que esta bien actualizado y soportado por una comunidad grande.

Voy a usar CentOS siendo conservador porque está más extendido en el uso de entornos HPC. Es robusto y compatible, no está actualizado y por eso mi pega... usa kernel 3 y no 4. Pero la verions 7 esta mante4nida hasta el año 25 y la verdad es que ubuntu server LTS esta soportado oficilamente solo 5 años.

## MPI Options


***Dilema:***
MPICH2, MVAPICH2, Open MPI, Intel MPI, ?

***Respuesta:***
Open MPI?

## Provisioning Software

***Dilema:***

Cobbler, Warewulf, xCAT, Openstack, Platform HPC

***Respuesta:***

## Configuration Management


***Dilema:***
Warewulf, Puppet, Chef, Ansible, ?

***Respuesta:***

## Resource and Job Scheduler


***Dilema:***
Torque, Lava, Maui, Moab, SLURM, Grid Engine, Son of Grid Engine, Univa, Platform LSF, etc… others?

***Respuesta:***


## SSH

- Cada usuario tiene que ser miembro del grupo sshusers (he licitado en /etc/ssh/sshd_config solo por grupo podria hacerlo por usuarios).
- No he desviado el puerto todavía
- 
## Volumen y home en ixtlilton
- Creo que sería mejor que hiciera un solo volumen con lvm: https://askubuntu.com/questions/7002/how-to-set-up-multiple-hard-drives-as-one-volume


He exportado las cosas... 
He creado en Ixtlilton un volumen llamado scratch que será para el futuro incorporar un disco de ssd y poner algo ahí que tenga una lectura-escritura más rápida que el work. scratch tendrá que tener fecha de caducidad o cuota -probablemente baste con cuota... esto lo tengo que pensar-

Tengo que arreglar el tema de los permisos... buscar nfs use mapping.
