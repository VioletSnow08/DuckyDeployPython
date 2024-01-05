A Flipper Zero/Ducky script that runs a pre-packaged Python .exe.

## How to use

### Server
- Edit the IP address in the `server.py` file (by default it automatically uses your private IP address).
- Run it

### Client
- Edit the IP address in the `client.py` file.
- Run `pyinstaller --onefile --add-data "commands/*;commands/" --add-data "helpers.py;." --add-data ".;Client" client.py -n [filename]`
- After compiled, upload the file to a web server of sorts.
- Change the URL in `computer-control.txt` to be the URL of where the payload resides.
- Upload file to Flipper Zero(or USB Ducky)
- Run it!

### Options
- In `Server/helpers.py` you can change the `DEBUG` status. This is set to `False` by default.
- In 'Server/server.py' you can change the `PORT` value. This is set to `5616`.

## Commands
#### LIST
LIST will display all the connected clients to the server, with corresponding IDs that way you can access them.
#### RSHELL [id]
RSHELL [id] will create a reverse shell with the provided ID.
If you would like to leave the RSHELL, you can type `exit`
#### ROLL
ROLL will simply open Google Chrome and rickroll the client.
#### ADVLIST
Similar to LIST, it will display the connected clients, but with more information.
#### CHROME [id] [url]
CHROME will open a Google Chrome tab on the client. This is automatically done when you run ROLL.
#### EXEC [id] [command]
EXEC will run a single command on the cllient. This is good if you don't want to open up a reverse shell.

