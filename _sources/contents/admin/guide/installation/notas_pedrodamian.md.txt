Aquí tengo que poner las notas:


----------------------
### email de pedro:

Hola Diego.

Hay que agregar las siguientes opiones en el dialogo de inicio al momento de intalar centos,  presionar tecla tabulador para obtener las opciones de arranque y escribir 

selinux=0
net.ifnames=0 

A partir de este punto, cualquier opciones de configuración con exepción de las particiones se pueden modificar una vez instalado el SO. 

Adicionalmente instale el repositorio   epel  y los paquetes  htop, tmux, desintale  sysstat y descarge de github la última versión.

Para el monitoreo del procesador utilice   turbostat y cpupower ambos son paquetes de la instalación base del SO.

Saludos,

-Pedro
--------------------------
