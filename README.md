A Flipper Zero/Ducky script that runs a pre-packaged Python .exe.

## How to use
- Edit the IP address in the `client.py` file.
- Run `pyinstaller ./client.py --onefile -n [filename]`
- After compiled, upload the file to a web server of sorts.
- Change the URL in `computer-control.txt` to be the URL of where the payload resides.
- Upload file to Flipper Zero(or USB Ducky)
- Run it!

## Commands
#### LIST
LIST will display all of the connected clients to the server, with corresponding IDs that way you can access them.
#### RSHELL [id]
RSHELL [id] will create a reverse shell with the provided ID.
If you would like to leave the RSHELL, you can type `exit`
#### ROLL
ROLL will simply open Google Chrome and rickroll the client.
