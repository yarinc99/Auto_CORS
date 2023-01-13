import os,re

class createfiles():
    def __init__(self, args):
        self.args = args
        self.arg = ''
        self.reg = ''
        self.wcsrf=''
        self.content = ''
        self.body = ''
        self.path=os.getcwd()
        if not os.path.exists("CORS_Javascript"):
            os.mkdir("CORS_Javascript")
        if not os.path.exists("request.txt"):
            fp = open('request.txt', 'x')
            fp.close()
        with open ("request.txt", "r") as l:
            self.arg = l.read()
        if self.arg == '':
            print(f'''The request file is empty. {self.path}/request.txt''')
            exit()
        self.headers = self.arg.split("\n\n")[0]
        self.method = self.headers.split(" ")[0]
        if self.method.upper() == 'POST':
            self.body = self.arg.split("\n\n")[1]
            self.content = re.search("Content-Type: (.*)",self.headers)[1]
        self.domain = re.search("Host: (.*)",self.headers)[1]
        self.domain = f'https://{self.domain}'
        self.url = self.headers.split(" ")[1]
        self.url = self.domain.strip()+self.url
        if self.args.csrf.lower() == 'y':
            if 'csrf' or 'xsrf' in self.headers:
                self.csheader = re.search("(.*c?x?srf.*?):",self.headers)[1]
                self.wcsrf = f"xhr.setRequestHeader('{self.csheader}', csrf)"
            if 'json' not in self.content:
                try:
                    self.reg = re.search("[c?x?]srf=(.*?)&", self.body,re.DOTALL)[1]
                    self.body = self.body.replace(self.reg.strip() ,"${csrf}")
                except:
                    pass
        if not (os.path.exists("CORS_Javascript/cors.html")):
            with open ("CORS_Javascript/cors.html", "w") as s:
                s.write('<html>\n<title>CORS POC GENERATOR</title>\n<body>\n<h1>CORS POC CREATOR</h1>\n<script src="./cors.js"></script>\n</body>\n</html>')