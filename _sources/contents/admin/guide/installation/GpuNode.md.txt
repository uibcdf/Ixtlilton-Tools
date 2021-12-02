
## Instalación

Los nodos con tarjeta gráfica no arrancan el instalador del usb.

1)

En instalación:
nomodeset rdblacklist=nouveau

despues de instalar, en el /etc/grub.conf despues de las opciones del kernel:
nomodeset rdblacklist=nouveau

yum install nvidia-detect
6. Navigate to http://www.nvidia.com/Download/index.aspx?lang=en-us and choose your graphic card and operating system and download the driver. Make sure you download the correct driver.
7. chmod +x ./name_of_your_downloaded_driver.run
8. yum isntall gcc
9. yum kernel update
10. init 3
11. login as root
12. cd to the downloaded nvidia driver and ./name_of_your_downloaded_driver.run to run the installer. Follow the instructions.
13. reboot
