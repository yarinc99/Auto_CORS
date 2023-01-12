import os,re

class createfiles():
    def __init__(self, args):
        self.args = args
        self.arg = ''
        self.reg = ''
        self.path=os.getcwd()
        if not os.path.exists("CORS_Javascript"):
            os.mkdir("CORS_Javascript")
        if not os.path.exists("arguments.txt"):
            fp = open('arguments.txt', 'x')
            fp.close()
        if self.args.method.upper() != 'GET':
            with open ("arguments.txt", "r") as l:
                self.arg = l.read()
            if  self.arg == '':
                pause = input(f'''The arguments file is empty. {self.path}/arguments.txt 
    Please write the arguments to the file and press ENTER''')
            elif self.args.csrf.lower() == 'y':
                try:
                    self.reg = re.search("[c?x?]srf=(.*?)&", self.arg,re.DOTALL)[1]
                    self.arg = self.arg.replace(self.reg.strip() ,"${csrf}")
                except:
                    print("No CSRF TOKEN FOUND IN ARGUMENTS")
                pause = input(f'''The arguments that were enter are: {self.arg} ,Press ENTER To Continue''') 
            else:
                pause = input(f'''The arguments that were enter are: {self.arg} , 
    Press ENTER To Continue''') 
        if not (os.path.exists("CORS_Javascript/cors.html")):
            with open ("CORS_Javascript/cors.html", "w") as s:
                s.write('<html>\n<title>CORS POC GENERATOR</title>\n<body>\n<h1>CORS POC CREATOR</h1>\n<script src="./cors.js"></script>\n</body>\n</html>')