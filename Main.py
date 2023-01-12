import argparse
import os
from createfiles import createfiles
from writejs import writejs

parser = argparse.ArgumentParser()

parser.add_argument("-s", "--site",default="http://localhost:1234/cors.html", help="Enter Your URL, EXAMPLE: https://burcollab/. Default is : http://localhost:1234/cors.html")
parser.add_argument("-c", "--csrf",default='a', help="Enable CSRF Token Pulling : Y")
parser.add_argument('-a', '--auth',default='a', help='Disable Credentials Pulling: Y')

if __name__ == "__main__":
    args = parser.parse_args()
    # Creates The Files Needed
    cf = createfiles(args)
    # Write The XSS/CORS Code in JS
    writejs(args,cf)
    # Optional Server Opening
    if input("Do You Want To Open A Python Server ? : Y/N ").lower() == 'y': 
        create = os.system("python -m http.server --directory ./CORS_Javascript 1234")