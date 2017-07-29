
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
  * si no hay red:
  `dhclient ethx`
  * mirar para que haya red al arranque que el fichero /etc/sysconfig/network-scripts/ifcfg-eth1 tiene la opción ONBOOT=yes
  * `yum update`
  * `reboot` en caso de haber actualizado kernel con el último comando.
* Instalar paquetes de configuración base:
`yum install @base @core @development @network-file-system-client @directory-client @guest-agents`
* Instalar algunos paquetes de nodo de computación:
`yum install @debugging @hardware-monitoring @remote-system-management @performance @compat-libraries`
* Instalar algunos paquetes de nodo con gnome-desktop-environment
`yum install @desktop-debugging @fonts @gnome-desktop @guest-desktop-agents @input-methods @legacy-x @networkmanager-submodules @x11`
* Instalar el repositorio epel:
`yum install epel-\* ; yum clean all; yum makecache`
* Quito paquetes que se instalaron y no van a ser usados
`yum remove libreoffice* cheese`
* Instalo otros paquetes necesarios:
`yum install htop tmux mc emacs xemacs libpciaccess-devel.x86_64 numactl-devel.x86_64 libX11-devel.x86_64 libxml2-devel.x86_64 cairo-devel.x86_64 terminator`
`yum install numactl`
**** Para que usa pedro el midnight commander?
* Creo en /root un directorio provisional:
`mkdir other_packages`
* Instalo hwloc:
`wget https://www.open-mpi.org/software/hwloc/v1.11/downloads/hwloc-1.11.7.tar.gz -P /root/other_packages/.`
`cd /root/other_packages`
`tar -zxvf hwloc-1.11.7.tar.gz`
`cd hwloc-1.11.7`
`./configure`
`make`
`make -j4`
`make install`
* Quito el sysstat oficial e instalo el de github
`yum remove sysstat`
`wget https://github.com/sysstat/sysstat/archive/master.zip`
`mv sysstat-master sysstat-11.5.7`
`cd sysstat-11.5.7`
`./configure --prefix=/usr`
`make`
`make install`
* Instalo ipmi
`yum -y install OpenIPMI freeipmi ipmitool`
`systemctl enable ipmi.service`
`systemctl start ipmi.service`
`systemctl status ipmi.service`
* Instalo las librerias de Intel (todavía no tengo los compiladores)
`scp -r 192.168.0.100:/root/other_packages/Intel other_packages/.`
`cd /root/other_packages/Intel`
`tar -zxvf l_mkl_2017.3.196.tgz`
`tar -zxvf l_mpi_2017.3.196.tgz`
`tar -zxvf l_daal_2017.3.196.tgz`
`tar -zxvf l_ipp_2017.3.196.tgz`
`tar -zxvf l_tbb_2017.6.196.tgz`
`cd l_mkl_2017.3.196; ./install.sh`
`cd ..`
`cd l_mpi_2017.3.196; ./install.sh`
`cd ..`
`cd l_daal_2017.3.196; ./install.sh`
`cd ..`
`cd l_ipp_2017.3.196; ./install.sh`
`cd ..`
`cd l_tbb_2017.3.196; ./install.sh`
`cd ..`

### Corriendo el benchmark mp_linpack de mkl
pedro editó el fichero HPL.dat poniendo el threshold a -16?

### Tengo que probar estas librerias... 
Los benchmarks son bastante impresionantes
https://software.intel.com/en-us/distribution-for-python


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
