from firebase_admin import db
from Firebase_cred import Firebase

Firebase.initial()

root = db.reference()
tabooWord = root.child('Taboo_word')
user = root.child('User')


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


def addUser(email, psd, userType, name, techInterest):
    try:
        user.child(removeIllegalChar(email)).set({
            'Email': email,
            'Password': psd,
            'User_type': userType,
            'Logged_in': False,
            'Name': name
        })

        for interest in techInterest:
            user.child(removeIllegalChar(email)).child('Tech_interest').update({
                interest:interest
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


def application(email, name, listofinterest):
    try:
        ref = user.child(removeIllegalChar(email))
        ref.update({
            "Application": {
                "Status": "Pending",
                "Name": name
            }
        })

        for interest in listofinterest:
            ref.child("Application/Tech_interest").update({
                interest: interest
            })
        return True

    except Exception as e:
        print("application()")
        print(e)


def fileComplain(email, filename, content):
    try:
        ref = user.child(removeIllegalChar(email)).child("Complains")
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


if __name__ == '__main__':
    print(SUexists())