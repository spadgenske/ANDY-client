#Andy CLI Client
#By Tyler Spadgenske

import socket, sys, time

class Client():
    def __init__(self):
        self.logo()
        print 'Connecting to Andy. Please Wait...'
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.file = open('ip.txt', 'r')
        self.host = self.file.readline()
        self.file.close()
        
        self.port = 5150
        try:
            self.server.connect((self.host, self.port))
            self.data = self.server.recv(1024)
            print bytes.decode(self.data)
            print 'Type "cmds" for list of cmds, "help" for help, "exit" for exiting.'
        except:
            print 'Cannot Connect to Andy'
            time.sleep(10)
            sys.exit()

        
    def logo(self):
        print'           _   _ _______     __'
        print'     /\   | \ | |  __ \ \   / /'
        print'    /  \  |  \| | |  | \ \_/ / '
        print'   / /\ \ | . ` | |  | |\   /  '
        print'  / ____ \| |\  | |__| | | |   '
        print' /_/    \_\_| \_|_____/  |_|'
        print'+++++++++++++++++++++++++++++++++++++++++++++++'                             
        print
        print 'ANDY Humanoid Robot CLI Interface'
        print 'Copyright (c) 2014 Tyler Spadgenske'
        print
        print '+++++++++++++++++++++++++++++++++++++++++++++++'

    def info(self):
        print '+++++++++++++++++++++++++++++++++++++++++++++++'
        print
        print 'CLI Help Guide                             v0.1'
        print
        print '+++++++++++++++++++++++++++++++++++++++++++++++'
        print 'Andy is an advanced robot controlled by speech.'
        print 'Sometimes though you will need to send him commands'
        print 'from a location Andy may not hear you. This is '
        print 'where the Command line interface (CLI) comes in. '
        print "Instead of saying 'ANDY', just type the command."
        print 'Andy can only execute one command at a time, so '
        print 'avoid sending another command before the previous'
        print 'command is complete. Type "cmds" to view a list of'
        print 'Andys commands. learn more at:'
        print 'https://github.com/spadgenske/ANDY/wiki'

    def cmds(self):
        print'+++++++++++++++++++++++++++++++++++++++++++++++'
        print
        print'Commands                                   v0.1'
        print
        print'+++++++++++++++++++++++++++++++++++++++++++++++'

        print'Walk'
        print'========'
        print'The first command is walk. After the walk command, '
        print'you must tell Andy direction and distance. For '
        print'example: "Walk forward 10 steps" will make Andy '
        print'walk forward ten steps. If you leave out the '
        print'"steps" he will still walk forward ten steps. If '
        print'you leave out the 10, Andy will walk forward until'
        print'you give the stop command. The same is for the backward '
        print'command. i.e "walk backward 3 steps."'

        print
        raw_input('Press Enter to see Another Command')
        print
        
        print'Turn'
        print'========'
        print'Another important command is the turn command. After '
        print'getting Andys attention by saying "Andy" and hearing'
        print' a beep, you can use the turn command like this: '
        print'"Turn right 180" Where 180 is the degrees Andy turns. '
        print'Negative numbers also work. If you leave out the '
        print'distance, Andy will move just 90 degrees. For example, '
        print'if you give Andy this command "turn right" Andy will '
        print'turn right 90 degrees.'

        print
        raw_input('Press Enter to see Another Command')
        print
        
        print'What'
        print'========'
        print'"What" is a basic command. Using the what command, you '
        print'can ask Andy basic questions like "what is your name?"'
        print'or "what time is it?" or even "what is 5+13x43?" "What"'
        print'commands are pre-programmed so you cant just ask Andy'
        print'anything. Here is a list of what commands:'

        print'What is [MATH EQUATION] '
        print'What time is it '
        print'What day is it today '
        print'What is your name '
        print'What is your problem'

        print
        raw_input('Press Enter to see Another Command')
        print
        
        print'Take'
        print'========'
        print'The "take" command is for the camera. There are two '
        print'commands: "take picture", and "take video". Take picture'
        print'will just take a snapshot right from the current view.'
        print'With take video, it will start the video and record. All'
        print'videos are saved under /home/pi/ANDY/videos and all '
        print'pictures are saved under /home/pi/ANDY/pictures'

        print
        raw_input('Press Enter to see Another Command')
        print
        
        print'Tell'
        print'========'
        print'The "tell" command can only be used in two ways: "tell joke"'
        print'or "tell riddle." After giving Andy one of these commands,'
        print'he will pick a random joke (or riddle) and repeat it back to you.'

        print
        raw_input('Press Enter to see Another Command')
        print
        
        print'Shutdown'
        print'========'
        print'The "shutdown" command is used to shut Andy down. If you '
        print'said, "shutdown", Andy will shut down his software and '
        print'hardware then safely shutdown the pi. This command will '
        print'only shut down the pi, so to turn off the batteries you must'
        print'flip the switch.'

        print
        raw_input('Press Enter to see Another Command')
        print
        
        print'Meet'
        print'========'
        print'The "meet" command is a very complex command. It deals with'
        print'the people table in Andys database. It is used like this: '
        print'"Andy". (beep) "meet Bob" Andy will then create a column for'
        print'Bob and store his name. Then Andy will take a picture with '
        print'the Pi Camera and store the file path in the Bob column. Now,'
        print'whenever the Pi camera detects Bob and Social Mode is on,' 
        print'Andy will ask Bob a question and store the answer in his database.'

        print
        raw_input('Press Enter to see Another Command')
        print
        
        print'Who'
        print'========'
        print'The "Who" command is used to get information from the "people"'
        print'table in Andys database. For example, if your command is'
        print'"Who is Bob" then Andy will read off information about Bob. '
        print'If Bob was never added to the database with the meet command, '
        print'Andy will obviously not know who Bob is.'

        print
        raw_input('Press Enter to see Another Command')
        print
        
        print'Run'
        print'========'
        print'Sometimes it is impossible to get Andy to do what you want in '
        print'one command. Thats where the run command comes in. First, '
        print'create a file with a list of the commands you wish Andy to '
        print'execute like this:'

        print'walk forward 10'
        print'turn right 90'
        print'walk backward 13'

        print'Save the file as test.txt in /home/pi/ANDY/sequences then tell'
        print'Andy this command: "run sequence test." Andy will now run all'
        print'three commands in one command.'

        print
        raw_input('Press Enter to see Another Command')
        print
        
        print'Sleep'
        print'========'
        print'The sleep command is very similar to the shutdown command. But,'
        print'the sleep command only shuts down the software, not the Pi itself. '
        print'This is handy if you are working on Andy and you want to shut just '
        print'the software down and not the entire system.'
        

    def send_cmd(self):
        while True:
            self.data = raw_input('>>')
            if self.data == 'exit':
                break
            if self.data.lower() == 'help':
                self.info()
            if self.data.lower() == 'cmds' or self.data.lower() == 'commands':
                self.cmds()
            if self.data.lower() != 'cmds' or self.data.lower() != 'help' or self.data.lower() != 'exit':
                self.server.send(str.encode(self.data))
                

    def end(self):
        print 'Closing Connection...'
        self.server.close()

if __name__ == '__main__':
    cli = Client()
    cli.send_cmd()
