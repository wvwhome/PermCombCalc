#    03/25/2019
#   Permuations and Combinations Calculator  for AWS Lambda version ... restructure folders and files
#
#  example:  https://medium.freecodecamp.org/how-to-create-a-serverless-service-in-15-minutes-b63af8c892e5
#
#    Folder for source:  (py37_lambda) C:\aaWVW\programs\AWS\lambda-perm-calc>
#    Environment setup: 
#                   C:\aaWVW\programs\Python\environments\py37_lambda>scripts\activate
#    python run_app.py    for local testing
#
from web_app import app
if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5080)