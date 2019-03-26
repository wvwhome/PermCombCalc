#   main.py
#    03/04/2019  Warren Van Wyck,    Ferrisburgh, Vermont USA
#    03/14/2019 WVW: Deploy version 2.0 in GCP App Engine project wvw-proj-perm
#    03/25/2019 WVW: Module version instead of Package '__init__.py' version
#
#       Permutations and Combinations Calculators in Python - Flask
#       handles duplicate/multiples
#       Enumerates (Counts) and Generates (Lists)
#        
#       The only logging done now is using stdout.  MySQL is not used.
#
#       This is a rewrite of the Rexx version of this from 2010 on HostMonster 
#       Virtual Private Server for Linux.
#       served http://www.webviewworks.com/math/index.html
#       Source code saved here: C:\aaWVW\programs\Rexx Regina\Permutations_Calculator
#
#
#   Setup Python environment for local development and testing:
#
#            pip install flask
#            pip install flask_wtf
#            pip install sympy
#
# (py37_perm_2_env) C:\aaWVW\programs\GCP\Python\Perm_Calc>pip freeze
# Click==7.0
# Flask==1.0.2
# Flask-WTF==0.14.2
# itsdangerous==1.1.0
# Jinja2==2.10
# MarkupSafe==1.1.1
# mpmath==1.1.0
# sympy==1.3
# Werkzeug==0.14.1
# WTForms==2.2.1
# #
#      pip freeze  > requirements.txt    

#
#   C:\aaWVW\programs\Python\environments\py37_perm_2_env\Scripts\activate
#   cd C:\aaWVW\programs\GCP\Python\Perm_Calc_module
#   python main.py

#      For Google Cloud Platform:
#       Start GCP SDK Shell:
#      C:\windows\system32\cmd.exe /k ""C:\Users\wvw\AppData\Local\Google\Cloud SDK\cloud_env.bat""
#      gcloud init
#       [1] Re-initialize this configuration [default] with new settings
#       [1] wvanwyck@gmail.com
#       [1] wvw-proj-perm
#
#      gcloud app deploy
#
#      The standard URL is
#               https://wvw-proj-perm.appspot.com/
#
#           You can stream logs from the command line by running:
#                gcloud app logs tail -s default
#
#   Base programs:
#      03/05/19.  Rename from run.py to main.py for Google App Engine
#        Copy from Corey Schafer demo:  C:\aaWVW\programs\GCP\Python\Flask_Blog\06-Login-Auth
#        I originally download the code_snippets from his GitHub site.
#        https://github.com/CoreyMSchafer
#        Major modifications for my purposes.  Remove any SQL.
#    
from web_app import app

#  03/15/2019  host='0.0.0.0'  allows access on my LAN
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5080)   
