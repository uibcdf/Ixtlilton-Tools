
# Instalación CentOS7

* Poner las opciones default de la bios
* Checar que en la bios (tecla: supr) la opción de HyperThreading está dehabilitada.
* Checar que en la bios está 'sólo legacy' en las opciones ACPI (por qué??)
* Crear usb booteable con CentOS7:
  * descargar la imagen iso de la versión minima en https://www.centos.org/download/
  * formatear una memoria usb
  * crear la copia booteable con la imagen iso en la memoria usb:
  `dd if=file.iso of=/dev/sdx bs=8M`
  donde sdx es el device correspondiente a la memoria usb.
* Instalar CentOS7:
  * Arrancar el nodo con el usb.
  * Elegir por precaución la opción 'Checar el medio e instalar Centos'
  * Incluir opciones de instalación:
    * tecla TAB para opciones de configuración
    * selinux=0 y net.ifnames=0 
  * Particionar disco ssd a mano con tabla de particiones msdos, particiones estandard (por qué no LVM??) y formato xfs según:
    * 100G para /
    * 8G para swap
    * 115G -o el resto- para /home
  * Realizar instalación mínima.
  * Configurar red, definir: hostname, contraseña de root y usuario UIBCDF. (por qué?)
  * Reiniciar tras instalación.
* Tras iniciar por primera vez:
  * Comprobar configuración de red:
  `ip address`
* Instalar el repositorio epel
* Instalar los paquetes htop, tmux

yum-y install htop tmux

* Desinstalar sysstat e instalarlo del repositorio Github

>> Pedro Creó una cuenta provisional llamada ixtlilton con password ixtli.2017

## Primeros tests de monitoreo de Hardware:

* turbostat
* cpupower

* hwloc da info del hardware
* lstopo
* hwloc-ls
* openipmi (ipmi.service)

mkl --> mp_linpack   para ver si el diagnostico de hw está bien

xhpl_intel64_static


Mirar openmp vs mpi :

Lawrence Libermore
Introductgion to parallel computing
computing.linl.gov/tutorials

Sacar el rendimiento real y ponerlo para documentar

numastat <-- free por cpupower
numactl

numactl_m0

ipmitool chassis bootdev bios
