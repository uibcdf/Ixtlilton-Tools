# SSH

## Importing OpenGL

By default the X server does not import OpenGL.
The solution is allowing indirect GLX in the client. To check if the problem was solved one of the following commands executed in Ixtlilton should print no errors:
```
glxinfo
glxgears
```

### Ubuntu

#### Option 1
Edit the file /usr/share/lightdm/lightdm.conf.d/50-xserver-command.conf
```
[SeatDefaults]
# Dump core
xserver-command=X -core +iglx
```
After which you either reboot or Ctrl-Alt-F1, login, and 'sudo service lightdm restart'.

#### Option 2

Edit the file /etc/X11/xorg.conf

```
Section "ServerFlags"  
    Option "AllowIndirectGLX" "on"  
    Option "IndirectGLX" "on"  
EndSection
```

After which reboot the client.

## Login via ssh without password

At the workstation with your user:

```
ssh-keygen -t rsa
ssh-copy-id -i ~/.ssh/id_rsa.pub ixtlilton 
# With empty passphrase
```

At Ixtlilton with your user:

```
ssh-copy-id -i ~/.ssh/id_rsa.pub nauta
```

