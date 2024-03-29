# Transfer files

If you have to copy files from your machine to Ixtlilton, or from Ixtlilton to your machine, two
procedures equally safe are suggested in this section. In order to show how these two options work, let's assume that 'x.x.x.x' is the ip (public or local) of the main node of Ixtlilton.

## Remote copy with SCP

If you have to copy a small data volume, the Secure Copy Protocol (SCP) is your option. SCP allows files
to be copied using SSH (SecureShell) for data transfer. Let's see how to transfer the local file named 'traj.h5' to
the directory `project/trajectories` owned by the user `user`:

```bash
scp traj.h5 user@x.x.x.x:project/trajectories/.
```

As you can see, the destiny path is relative to the home directory of `user`. If there is no path,
the file will be placed in the same `/home/user` location. Absolute path can also be used. Let's
see now how to transfer the local directory 'solvated' with the absolute destiny path making use of
the flag '-r' to copy recursively:

```bash
scp -r solvated user@x.x.x.x:/home/user/project/trajectories/.
```

## Incremental transference with RSync over SSH

If you need to copy large data files or directories, you will want to be covered in case the remote
conexion is interrupted before the transference is finished. RSync -Remote Sync- is your ally in
this case.

RSync synchronizes the content of a local file or directory with a remote image by increments. And
this is done comparing the content at the origin and the finnal destination before sending the first chunk of data. This way RSync avoids transferring redundant information. That's why RSync is so widely used to make incremental backups. That's the reason, also, to make RSync the suitable tool in case the transference is interrumpted. RSync can resume the transfer from the point it was stopped.

Let's copy (syncronize) the file 'traj.h5'

```bash
rsync -a -P --rsh=ssh traj.h5 user@x.x.x.x:project/trajectories/.
```

The option '-P' will show in your terminal the transfer progress, and '-a' activates the archive
mode to conserve the file rights, owners, and creation and modification times. If instead of a
file, you want to transfer a directory, the flag '-a' includes the recursive copy already (there's
no need to add the flag '-r'). Finnally, if, by any reason, the remote synchronization is suspended, you only need to re-execute the same rsync command for the transference to be continued.

