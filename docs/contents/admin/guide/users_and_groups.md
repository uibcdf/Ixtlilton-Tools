# Users and Groups

User Ids must run from 2000 to 2999.
This user id must apply for any system located not only in ixtlilton but in the UIBCDF.

| Name    |   Id | Description                                                    |
| ---     |  --- | ---                                                            |
| UIBCDF  | 1000 | Generic lab username to run admind tasks, tests and benchmarks |
| liliana | 2000 | Liliana                                                        |
| diego   | 2001 | Diego                                                          |
| homero  | 2002 | Homero                                                          |


## Notes
- Habla del fichero /opt/etc/user_bashrc
- Hay que copiar el .bashrc tipo y poner bien los permisos
- Poner un fichero .bash_aliases tipo y poner bien los permisos
- Poner un fichero .condarc tipo
- Crear el directorio .conda
- en el dir home/user/opt faltaban los dir lib, lib32, lib64 e include. Además debe tener los
  propietarios bien

## UIBCDF User

The user belongs to the groups: wheel, projects and archive.

## New User

### Internal

A new user from the UIBCDF has to update the groups he/she belongs to: projects 

'''
usermod -aG projects username
'''

### With lab rights

A new user from the UIBCDF with sudo rights should belong to the groups: wheel, projects and archive.

'''
usermod -aG projects username
usermod -aG archive username
'''

### External

A new external user does not belong to the group "projects" but to specific projects group defined ad hoc.

## Groups

Group Ids must run from 3000 to 3999.


| Name     | Id                   | Description                                                                                                       |
| ---      | ---                  | ---                                                                                                               |
| projects | 3000                 | Any project located in /Data/projects without specific groupid                                                    |
| projectA | 3000 + i (i=1,..499) | project A in /Data/projects with specific rights (e.g.: belonging to external user without access to any project) |
| archive  | 3500                 | Any project already stored in /ColdStorageRoom/archive                                                            |

## Adding new user

```
export NEW_USER_NAME='xxxx'
```

## User file system

```
mkdir /work/$NEW_USER_NAME
mkdir /scratch/$NEW_USER_NAME
chown -R $NEW_USER_NAME:$NEW_USER_NAME /work/$NEW_USER_NAME
chown -R $NEW_USER_NAME:$NEW_USER_NAME /scratch/$NEW_USER_NAME
```

## Local opt structure in the users home

To help the user keep things well organised a local 'opt' dir is created with 'apps', 'bin', 'etc',
'modulefiles' and 'src' inside.

```
mkdir /home/$NEW_USER_NAME/opt
mkdir /home/$NEW_USER_NAME/opt/apps
mkdir /home/$NEW_USER_NAME/opt/bin
mkdir /home/$NEW_USER_NAME/opt/etc
mkdir /home/$NEW_USER_NAME/opt/modulefiles
mkdir /home/$NEW_USER_NAME/opt/src
chown -R $NEW_USER_NAME:$NEW_USER_NAME /work/$NEW_USER_NAME
```

### Double Factor

Double Factor is enabled for ssh conexion coming from outside.

```bash
su username
google-authenticator
y
```

Go to the url with the QR andwith fshutter take selection shot of QR.
Save the QR as QR_username@ixtlilton

Take a selection shot of the codes. Save it as Codes_username@ixtlilton

```bash
y
y
y
y
```

Include both files attached to the email template with the data and instructions for the new user.

## Comunication with the new user

An email using the [following template](email_new_user.md) is send to the new user. This email includes private
information for the user and general user's instructions. Copy the template into the email body and
edit the text with the new username password and attach the user's QR and codes snapshots.

## Password, ip and port

The user password with ip and port will be sent via [TMWSD](https://thismessagewillselfdestruct.com/)
