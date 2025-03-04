# Hardware

## MotherBoard

        Manufacturer: ASUSTeK COMPUTER INC.
        Product Name: Z10PE-D16 WS
        Version: Rev 1.xx

https://www.asus.com/Motherboards/Z10PED16_WS/

### Versión de Bios mínima recomendada

E5-2630 V4(2.20GHz,85W,L3:25M,10C,HT)           version: 3204

https://www.asus.com/us/Motherboards/Z10PED16_WS/HelpDesk_CPU/

## Opciones de la bios para max performance

https://github.com/bravegag/z9pe-d8_ws-optimization-guide

<!-- processor: lscpu -->
<!-- ram: free -m -->
<!-- storage: lsblk -->
<!-- graphics: lspci | grep VGA      o      sudo lshw -C video -->
<!-- network: lspci | egrep -i --color 'network|ethernet'   o   lshw -class network -->
<!-- motherboard: sudo dmidecode | grep -A4 'Base Board' -->
<!-- os and kernel: less /etc/*elease -->

