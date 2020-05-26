from django.shortcuts import render
from django.contrib import auth as authe
import pyrebase
config = {
  "apiKey": "AIzaSyCZRreQ8JOOI8JywqSlHV0NHuIZdm3xsmA",
  "authDomain": "filesharing-9e2ca.firebaseapp.com",
  "databaseURL": "https://filesharing-9e2ca.firebaseio.com",
  "projectId": "filesharing-9e2ca",
  "storageBucket": "filesharing-9e2ca.appspot.com",
  "messagingSenderId": "365933125226",
  "appId": "1:365933125226:web:48ca391d66571e34cc7413",
  "measurementId": "G-8MEK13RPWZ"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
database=firebase.database()
def login(request):
    return render(request, "index.html")
def postloginin(request):
    email=request.POST.get('email')
    passw=request.POST.get('pass')
    try:
        user = auth.sign_in_with_email_and_password(email,passw)
    except:
        message = "invalid credentials"
        return render(request, "index.html", {"msg":message})
    #print(user)
    print(user['idToken'])
    session_id = user['idToken']
    request.session['uid'] = str(session_id)
    return render(request, "welcome.html",{"e":email})


def postsignup(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    passw = request.POST.get('pass')
    try:
        user = auth.create_user_with_email_and_password(email, passw)
        uid = user['localId']
        data = {"name": name, "status": "1"}
        database.child("users").child(uid).child("details").set(data)
    except:
        message = "Unable to create account try again"
        return render(request, "index.html", {"msg": message})

    return render(request, "index.html")
def logout(request):
    authe.logout(request)
    return render(request,"index.html")
def resetpass(request):
    email = request.POST.get('email')
    auth.send_password_reset_email(email)
    return render(request,"index.html")

def resetp(request):
    return render(request,"resetpass.html")
def index(request):
    return render(request, "index.html")
