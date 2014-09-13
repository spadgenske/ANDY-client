ANDY-client
===========

Learn more: http://hackaday.io/project/1205

#About
Andy-client is a quick way to send Andy commands instead of talking to him. This
is great for wirelessly controlling him from another room.

#Setup
How to install ANDY-client for your system.

##Linux

###Step One: Clone
Run the command
`git clone https://github.com/spadgenske/ANDY-client.git`

### Step Two: Setup IP.txt
Go into the CLI folder and change the first line to Andy's ip adrress.

###Step Three: Run
Run the client.py file while Andy is running. It should connect. 
Now you can send Andy commands from your Linux computer!

##Windows

###Step One: Download
Go to https://github.com/spadgenske/ANDY-client/releases and click on the latest release. 
Click on the green download button to download a file similar to `ANDY-client.1.1.exe` Run the file
to install.


###Step Two: Setup IP Address
Double click on the client.exe file while Andy is running. The CLI will fail to 
connect. Type in Andy's IP address when the program asks. Close out of the program.

###Step Three: Restart
Restart ANDY-client by running client.exe again. The CLI should connect to ANDY. Now
you can send Andy commands from your Windows System!

##Mac
ANDY-client is not tested using Mac. It should work if you run it via the source code.