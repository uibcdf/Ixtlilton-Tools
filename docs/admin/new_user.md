# Instructions to set up a new user

## Ssh set up

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
