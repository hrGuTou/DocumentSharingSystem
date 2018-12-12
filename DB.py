from firebase_admin import db
from Firebase_cred import Firebase

Firebase.initial()

root = db.reference()
tabooWord = root.child('Taboo_word')
user = root.child('User')
pendingApp = root.child("Pending_application")
suggestTaboo = root.child('Suggest_taboo')
complains = root.child("Complains")

def removeIllegalChar(str):
    return ''.join(e for e in str if e.isalnum())


def tolower(word):
    return word.lower()


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

def checkAppExist(email):
    try:
        ref = pendingApp.child(removeIllegalChar(email))
        if not ref.get() == None:
            return True
        else:
            return False
    except Exception as e:
        print("checkappexist")
        print(e)

def getPendingApp():
    try:
        ref = pendingApp.get()
        return ref
    except Exception as e:
        print(e)

def addGuestPending(email, psd, userType, name, techInterest):
    try:
        pendingApp.child(removeIllegalChar(email)).set({
            'Email': email,
            'Password': psd,
            'User_type': userType,
            'Logged_in': False,
            'Name': tolower(name),
            'Tech_interest': techInterest
        })
        return True
    except Exception as e:
        print(e)


def addUser(email, psd, userType, name, techInterest):
    try:
        user.child(removeIllegalChar(email)).set({
            'Email': email,
            'Password': psd,
            'User_type': userType,
            'Logged_in': False,
            'Name': tolower(name)
        })


        user.child(removeIllegalChar(email)).update({
                "Tech_interest": techInterest
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
            'User_type': userType
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


def firstTimeApply(email):
    """Verify that each GU can send application only once"""
    ref = user.child(removeIllegalChar(email))
    if ref.child("Application").get() is None:
        return True
    else:
        return False




def fileComplain(email, filename, content):
    try:
        print(email, filename, content)
        ref = root.child("Complains").child(removeIllegalChar(email))
        ref.update({
            filename: content
        })

    except Exception as e:
        print("fileComplain()")
        print(e)


def checkApplication():
    """For SU to review GU applications"""
    try:
        ref = user.get()
        result = {}
        for key in ref:
            if "Application" in ref[key]:
                result[key] = ref[key]["Application"]

        return result
    except:
        print("checkApplication()")

def applicationDecision(email, result):
    try:
        ref = user.child(removeIllegalChar(email)).child("Application")
        ref.update({
            "Status":result
        })
    except Exception as e:
        print("applicationDecision()")
        print(e)

def getApplDecision(email):
    try:
        ref = user.child(removeIllegalChar(email)).child("Application/Status").get()
        return ref
    except Exception as e:
        print("getApplDecision()")
        print(e)


def shareTarget(src, filename, target, link):
    try:
        ref = user.child(removeIllegalChar(target)).child('Invitation').child(removeIllegalChar(src))
        ref.update({
                 filename:{
                        'Link': link

            }
        })

        return True
    except Exception as e:
        print(e)


def getInvitation(email):
    try:
        ref = user.child(removeIllegalChar(email)).child("Invitation").get()
        return ref
    except Exception as e:
        print(e)

def deleteInvitation(email,target,filename):
    try:
        ref = user.child(removeIllegalChar(email)).child('Invitation').child(removeIllegalChar(target)).child(filename)
        ref.delete()
    except Exception as e:
        print(e)

def allUsers():
    """

    :return: list
    """
    try:
        ref = user.get()
        result = []
        if ref is not None:
            for key in ref:
                result.append(key)
        return result
    except Exception as e:
        print(e)


def getUserINFO(name):
    try:
        result=[]

        ref= user.get()
        if ref is not None:
            for person in ref:
                if ref[person]["Name"]== name:
                    result.append(ref[person]['Email'])
                    result.append(ref[person]['Tech_interest'])
                    result.append(ref[person]['Name'])
        return result

    except Exception as e:
        print(e)


def GUpromote(email):
    try:
        ref = pendingApp.child(removeIllegalChar(email))
        store = ref.get()
        user.child(removeIllegalChar(store['Email'])).update(store)
        ref.delete()

    except Exception as e:
        print(e)

def GUdeleteAPP(email):
    try:
        ref = pendingApp.child(removeIllegalChar(email))
        ref.delete()

    except Exception as e:
        print(e)

def getComplains():
    try:
        ref = complains.get()
        return ref
    except Exception as e:
        print(e)

def resolveComplains(email,filename):
    try:
        ref = complains.child(removeIllegalChar(email)).child(filename).delete()
    except Exception as e:
        print(e)

if __name__ == '__main__':
    print(getUserINFO('SU'))