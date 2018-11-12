import json
import urllib
from time import strftime, localtime

from firebase_admin import db
from Firebase_cred.Firebase import initial

initial()

root = db.reference()
tabooWord = root.child('Taboo_word')
user = root.child('User')
test = 'hi'


def removeIllegalChar(str):
    return ''.join(e for e in str if e.isalnum())

def tolower(word):
    return word.lower()+test


def checkUserExists(email):
    try:
        ref = user.child(removeIllegalChar(email))
        if not ref.get() == None:
            return True
        else:
            return False
    except Exception as e:
        print("checkUserExists()")
        print(e)


def addUser(email, psd, userType):
    try:
        user.child(removeIllegalChar(email)).set({
            'Email': email,
            'Password': psd,
            'User_type': userType,
            'Logged_in': False
        })

        return True
    except Exception as e:
        print("addUser()")
        print(e)


def loginPassword(email):
    try:
        ref = user.child(removeIllegalChar(email)).get()
        return ref['Password']
    except Exception as e:
        print("login()")
        print(e)


def checkLoginStat(email):
    try:
        ref = user.child(removeIllegalChar(email)).get()
        return ref['Logged_in']

    except Exception as e:
        print("checkLoginStat")
        print(e)

def changeUserType(email, userType):
    try:
        ref = user.child(removeIllegalChar(email))
        ref.update({
            'User_type' : userType
        })

    except Exception as e:
        print("changeUserType()")
        print(e)

def changeLoginStat(email, stat):
    """

    :param email:
    :param stat: False for logged out, True for logged in
    :return:
    """
    if stat == False or stat == True:
        try:
            ref = user.child(removeIllegalChar(email))
            ref.update({
                'Logged_in': stat
            })

        except Exception as e:
            print("changeLoginStat()")
            print(e)


def SUexists():
    try:
        snapshot = user.order_by_child('User_type').equal_to('0').get()
        if snapshot:
            return True
        else:
            return False

    except Exception as e:
        print("SUexists")
        print(e)


def currentUserGroup(email):
    try:
        ref = user.child(removeIllegalChar(email)).get()
        return ref['User_type']

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
    timeCode = strftime("%Y-%m-%d-%H-%M-%S", localtime())
    userID = removeIllegalChar(email)
    file = open(doc, "rb")
    file_in = file.read()
    target = "https://firebasestorage.googleapis.com/v0/b/llhc-db662.appspot.com/o/savedocs%2F" + userID + "%2F" + fileName + "%2F" + timeCode
    head = {'Content-Type': 'text/plain'}

    req = urllib.request.Request(target, data=file_in, headers=head, method="POST")

    try:
        urllib.request.urlopen(req)
    except urllib.error.URLError as e:
        msg = json.loads(e.read())
        print(msg['error']['message'])
    else:
        fileHisotry = root.child('User').child(removeIllegalChar(email)).child('Document_history')
        fileHisotry.update({
            timeCode: fileName
        })
        return True


def addTaboo(listoftaboo):
    try:
        for word in listoftaboo:
            tabooWord.update({
                tolower(word): tolower(word)
            })

        return True

    except Exception as e:
        print("addTaboo()")
        print(e)

def getTaboo():
    try:
        listoftaboo = tabooWord.get()
        listoftaboo.pop(0)
        return listoftaboo

    except Exception as e:
        print("getTaboo()")
        print(e)


def deleteTaboo(listofword):
    try:
        ref = tabooWord
        for word in listofword:
           ref.child(tolower(word)).delete()

        return True

    except Exception as e:
        print("deleteTaboo()")
        print(e)

def suggestTaboo(email, listofword):
    try:
        ref = user.child(removeIllegalChar(email))
        for word in listofword:
            ref.update({'Suggest_taboo':{
                word:word
            }})

    except Exception as e:
        print("suggestTaboo()")
        print(e)

def deleteSuggestTaboo(email, listofword):
    try:
        ref = user.child(removeIllegalChar(email)).child('Suggest_taboo')
        for word in listofword:
            ref.child(tolower(word)).delete()

        return True

    except Exception as e:
        print("deleteSuggestTaboo")
        print(e)



if __name__ == '__main__':
    addUser('newuser','abc','1')