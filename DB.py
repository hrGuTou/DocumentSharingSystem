import json
import urllib
from time import strftime, localtime

from firebase_admin import db
from firebase_admin import storage

from Firebase_cred.Firebase import initial

initial()

root = db.reference()
# Add a new user under /users.

#
"""
users_ref = root.child('User')
users_ref.child('hrgutougmailcom').set({
    'date_of_birth': 'June 23, 1912',
    'full_name': 'Alan Turing'
})


ref = db.reference('User').child('hrgutougmailcom')
print(ref.get())
"""
def removeIllegalChar(str):
    return ''.join(e for e in str if e.isalnum())

def checkUserExists(email):
    try:
        ref = db.reference('User').child(removeIllegalChar(email))
        if not ref.get() == None:
            return True
        else:
            return False
    except Exception as e:
        print("checkUserExists()")
        print(e)

def addUser(email, psd, userType):
    try:
        newUser = root.child('User')
        newUser.child(removeIllegalChar(email)).set({
            'Email':email,
            'Password':psd,
            'User_Type':userType,
            'Logged_in': '0'
        })
        return True
    except Exception as e:
        print("addUser()")
        print(e)

def loginPassword(email):
    try:
        ref = db.reference('User').child(removeIllegalChar(email)).get()
        return ref['Password']
    except Exception as e:
        print("login()")
        print(e)

def checkLoginStat(email):
    try:
        ref = db.reference('User').child(removeIllegalChar(email)).get()
        return ref['Logged_in']

    except Exception as e:
        print("checkLoginStat")
        print(e)

def changeLoginStat(email, stat):
    """

    :param email:
    :param stat: 0 for logged out, 1 for logged in
    :return:
    """
    if stat == '0' or stat == '1':
        try:
            ref = db.reference('User').child(removeIllegalChar(email))
            ref.update({
                'Logged_in': stat
            })

        except Exception as e:
            print("changeLoginStat()")
            print(e)

def SUexists():
    try:
        ref = db.reference('User')
        snapshot = ref.order_by_child('User_Type').equal_to('0').get()
        if snapshot:
            return True
        else:
            return False

    except Exception as e:
        print("SUexists")
        print(e)

def currentUserGroup(email):
    try:
        ref = db.reference('User').child(removeIllegalChar(email)).get()
        return ref['User_Type']

    except Exception as e:
        print("currentUserGroup()")
        print(e)

def uploadDoc(email, doc, fileName):
    """
        CITED FROM https://github.com/PhantomInsights/firebase-python/blob/master/storage/README.md
        CREATOR: https://github.com/agentphantom
        TODO: IMPLEMENT VERSION HISTORY
    :param email: unique ID
    :param doc: location of the file
    :return: True for load successfully
    """
    userID = removeIllegalChar(email)
    file = open(doc, "rb")
    file_in = file.read()
    target = "https://firebasestorage.googleapis.com/v0/b/llhc-db662.appspot.com/o/savedocs%2F"+userID+"%2F"+fileName
    head = {'Content-Type': 'text/plain'}

    req = urllib.request.Request(target, data=file_in, headers=head, method="POST")

    try:
        urllib.request.urlopen(req)
    except urllib.error.URLError as e:
        msg = json.loads(e.read())
        print(msg['error']['message'])
    else:
        time = strftime("%Y-%m-%d %H:%M:%S", localtime())
        fileHisotry = root.child('User').child(removeIllegalChar(email)).child('Document History')
        fileHisotry.update({
            time : fileName
        }
    )
        return True

def addTaboo()
    pass