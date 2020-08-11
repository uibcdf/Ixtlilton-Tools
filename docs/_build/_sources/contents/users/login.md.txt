# Login

## Login from the UIBCDF local network

If you are using a machine in the UIBCDF lab, the conexion will be done via SSH enabling trusted
X11 forwarding (-Y) if necessary:

```
ssh user@192.168.0.100
```

or

```
ssh -Y user@192.168.0.100 # Exporting X11 is discourage, only special needs
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

   - The way to connect remotely via ssh
   - The activation of your multi-factor authentication

