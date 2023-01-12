# Auto_CORS


usage: Main.py [-h] [-s SITE] -v VICTIM [-m METHOD] [-c CONTENT] [-a AUTH] [-cs CSRF]

optional arguments:
  -h, --help            show this help message and exit
  
  -s SITE, --site SITE  Enter Your URL, EXAMPLE: https://burcollab/. Default is : http://localhost:1234/cors.html
  
  -v VICTIM, --victim VICTIM
                        Enter Victim's Full URL, EXAMPLE: https://api.victimsite/changepassword/.
                        
  -m METHOD, --method METHOD
                        Enter The Desired Method: GET/POST.
                        
  -c CONTENT, --content CONTENT
                        Enter The Desired Content Type. Default: application/json.
                        
  -a AUTH, --auth AUTH  Disable Credentials Pulling: Y
  
  -cs CSRF, --csrf CSRF
                        Enable CSRF Token Pulling: Y| 
                        The token is saved as the variable "csrf" in the js please enter the variable into the correct place.
