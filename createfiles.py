import os,re,eel

class createfiles():
    def __init__(self, args):
        self.args = args
        self.arg = args.request
        self.reg = ''
        self.wcsrf=''
        self.error = False
        self.content = ''
        self.body = ''
        self.path=os.getcwd()
        if not os.path.exists("CORS_Javascript"):
            os.mkdir("CORS_Javascript")
        if self.arg == '':
            # print(f'''The request file is empty. {self.path}/request.txt''')
            eel.error("Request block is empty")
            self.error = True
            return
        self.headers = self.arg.split("\n\n")[0]
        self.method = self.headers.split(" ")[0]
        if self.method.lower() not in ['get','post','patch','delete']:
            self.error = True
            eel.error("Couldn't find Method")
            return
        if self.method.upper() == 'POST':
            self.body = self.arg.split("\n\n")[1]
            self.content = re.search("Content-Type: (.*)",self.headers)[1]
        self.domain = re.search("Host: (.*)",self.headers)[1]
        self.domain = f'https://{self.domain}'
        self.url = self.headers.split(" ")[1]
        self.url = self.domain.strip()+self.url
        if self.args.csrf:
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