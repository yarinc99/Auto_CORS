import argparse
import os,eel
from createfiles import createfiles
from writejs import writejs

parser = argparse.ArgumentParser()
if __name__ == "__main__":
    @eel.expose
    def start_script(form_data):
        global args
        finaldic = {"request":form_data["request"],
                    "site": form_data["site"],
                    "csrf":form_data["csrf"],
                    "auth":form_data["auth"],
                    "server":form_data["server"]}
        args = argparse.Namespace(**finaldic)
        # Creates The Files Needed
        cf = createfiles(args)
        if not cf.error:
            # Write The XSS/CORS Code in JS
            js = writejs(args,cf)
            eel.update_request_output(str(js.script))  
            # Optional Server Opening
            if args.server: 
                os.system("python -m http.server --directory ./CORS_Javascript 1234")
    eel.init('UI')
    eel.start('index.html', size=(1100, 900))