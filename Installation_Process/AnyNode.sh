yum update
reboot
yum install @base @core @development @network-file-system-client @directory-client @guest-agents
yum install @debugging @hardware-monitoring @remote-system-management @performance @compat-libraries
yum install @desktop-debugging @fonts @gnome-desktop @guest-desktop-agents @input-methods @legacy-x @networkmanager-submodules @x11
yum install epel-\* ; yum clean all; yum makecache
yum remove libreoffice* cheese
yum install htop tmux mc emacs xemacs libpciaccess-devel.x86_64 numactl-devel.x86_64 libX11-devel.x86_64 libxml2-devel.x86_64 cairo-devel.x86_64 terminator
yum install numactl
mkdir /root/other_packages
wget https://www.open-mpi.org/software/hwloc/v1.11/downloads/hwloc-1.11.7.tar.gz -P /root/other_packages/.
cd /root/other_packages
tar -zxvf hwloc-1.11.7.tar.gz
cd hwloc-1.11.7
./configure
make
make -j4
make install
cd /root/

# Quito el sysstat oficial e instalo el de github
cd /root
yum remove sysstat
wget https://github.com/sysstat/sysstat/archive/master.zip
unzip master.zip
mv sysstat-master sysstat-11.5.7
cd sysstat-11.5.7
./configure --prefix=/usr
make
make install
cd /root

# Instalo ipmi
cd /root
yum -y install OpenIPMI freeipmi ipmitool
systemctl enable ipmi.service
systemctl start ipmi.service
systemctl status ipmi.service

# Additional packages
yum -y install environment-modules tcl tk

# Instalo las librerias de Intel (todavía no tengo los compiladores)
scp -r 192.168.0.100:/root/other_packages/Intel /root/other_packages/.
cd /root/other_packages/Intel
tar -zxvf l_mkl_2017.3.196.tgz
tar -zxvf l_mpi_2017.3.196.tgz
tar -zxvf l_daal_2017.3.196.tgz
tar -zxvf l_ipp_2017.3.196.tgz
tar -zxvf l_tbb_2017.6.196.tgz
cd /root/other_packages/Intel/l_mkl_2017.3.196; ./install.sh
cd /root/other_packages/Intel/l_mpi_2017.3.196; ./install.sh
cd /root/other_packages/Intel/l_daal_2017.3.196; ./install.sh
cd /root/other_packages/Intel/l_ipp_2017.3.196; ./install.sh
cd /root/other_packages/Intel/l_tbb_2017.6.196; ./install.sh

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

## UIBCDF GitHub admin tools and files
(some examples in /media/diego/Thorin/diego/Myusr/share/modules/modulefiles)

git clone https://github.com/uibcdf/Ixtlilton /root/Admin_Tools_and_Files

## MyLab

mkdir /opt/MyLab
git clone https://github.com/dprada/MyTools /opt/MyLab/MyTools
git clone https://github.com/dprada/MyTools /opt/MyLab/MyKinLab
git clone https://github.com/dprada/MyTools /opt/MyLab/MyMDLab
git clone https://github.com/dprada/MyTools /opt/MyLab/MyMolLab
git clone https://github.com/dprada/MyTools /opt/MyLab/MyMathLab
git clone https://github.com/dprada/MyTools /opt/MyLab/MyNetLab
git clone https://github.com/dprada/MyTools /opt/MyLab/MyPlotLab

mkdir -p /etc/modulefiles/Python
cp /root/Admin_Tools_and_Files/environment_modules/Python/MyLab /etc/modulefiles/Python/MyLab
