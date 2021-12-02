# Login

## Login from the UIBCDF local network

If you are using a machine in the UIBCDF lab, the conexion to the main node will be done via SecureShell (SSH) with the following
IP:

```
ssh user@192.168.0.100
```

If your machine is regularly working with Ixtlilton, there are two actions you can take to make
your life easier. Add Ixtlilton to the list of known hosts names in the file (/etc/hosts) with the
following line:

```bash
192.168.0.100 ixtlilton
```

This way your user can connect just with:

```
ssh ixtlilton
```

If your machine is a workstation of the lab, you can ask to the administrators to enable the SSH
connection without password.

## Login from outside the UIBCDF local network

To enter Ixtlilton remotely from outside the lab network you will receive instructions from the
administrators regarding the following two things:

   - The public static IP to connect remotely via ssh.
   - The activation of your multi-factor authentication.

Once you know the public static IP and your multi-factor authentication has been set up correctly,
execute in you machine:

```
ssh user@ip
```

As it was suggested in the previous section, you can include Ixtlilton in your list of known hosts
with the following line in the file `/etc/hosts`:

```bash
ip ixtlilton
```

Where 'ip' has to be replaced with the ip address numbers.

## X11 Forwarding

X11 forwarding allows a user to import from ixtlilton the graphical environment. With the above
instructions to connect with ixtliton, there is no way to run graphical applications exporting the windows to your machine. To enable this option the flag '-Y' has to be included after the command 'ssh':

```bash
ssh -Y user@ip
```

**X11 forwarding has to be used occasionally and with caution**. Exporting the graphical environment or running
graphical applications will reduce the performance of the GPUs in the main node, and they could be
in used by other processes and users. **Do not forward X if this is not strictly necessary**.

