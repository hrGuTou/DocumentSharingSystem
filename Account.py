"""
    Account Management

    TODO: change password and add userName
"""

import DB
import bcrypt


def createAcc(email, psd, name, techinterest):
    """
        For OU
    :param email:
    :param psd:
    :return: false: user already exists, ask if forget password or change password
             true: user added into database
    """

    if DB.checkUserExists(email):
        return False

    else:
        """password encoded"""
        hashedPSD = bcrypt.hashpw(psd.encode('utf8'), bcrypt.gensalt())
        print(type(hashedPSD))
        DB.addUser(email, hashedPSD.hex(), '1', name, techinterest)  # 1 for OU
        return True


def logIn(email, psd):
    """
        For both SU and OU
    :param email: login email
    :param psd: plain text password to be checked
    :return: True: login successes
             False: login failed
             IF USER NOT EXISTS, return string
             -1: user not exists
             2: already logged in

    """

    if DB.checkUserExists(email):
        if not DB.checkLoginStat(email):
            """
                if account exists and not logged in, proceed login
                
            """
            if not (psd == "" or DB.currentUserGroup(email) == "2"):
                """
                    If the password string is not empty and is not a GU, proceed psd check 
                """
                hashed = bytes.fromhex(DB.loginPassword(email))
                if bcrypt.checkpw(psd.encode('utf8'), hashed):
                    DB.changeLoginStat(email, True)
                    return 1
                else:
                    return 0
            else:
                DB.changeLoginStat(email, True)
                return 3
        else:

            return 2
    else:

        return -1


def logOut(email):
    """
        For both SU and OU
    :param email:
    :return:
    """
    if DB.checkLoginStat(email):
        DB.changeLoginStat(email, False)
        return True
    else:
        return False


def promoteToSU(email):
    """
        If current database doesn't contain a super user, promote the current logged
        in user to be a super user.
    :param email:
    :return:
    """
    DB.changeUserType(email, '0')
    return True


def createGuest(email, password, name, techInterest):
    """
        For GU
    :param email:
    :param password: IS AN EMPTY STRING
    :return:
    """
    hashedPSD = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())

    if not DB.checkUserExists(email):
        if not DB.checkAppExist(email):
            DB.addGuestPending(email, hashedPSD.hex() , '1', name, techInterest)
            return True
        else:
            return 2
    else:
        return -1


def OUapplication(email, name, listoftechinterests):
    """
        For GU to apply become an OU, SU has to approve it
        ONLY 1 APPLICATION FOR EACH GU
    :param email:
    :param name:
    :param listoftechinterests:
    :return: 1 for application sent successfully,
            -1 for reject because of multiple applications
    """
    if DB.firstTimeApply(email):
        DB.application(email, name, listoftechinterests)
        return True

    else:
        return False


def GUpromotion(email, psd):
    ref = DB.user.child(DB.removeIllegalChar(email))
    ref.child('Application').delete()
    hashedPSD = bcrypt.hashpw(psd.encode('utf8'), bcrypt.gensalt())

    ref.update({
        "User_type": '1',
        "Password":hashedPSD.hex()
    })


if __name__ == "__main__":
    #print(OUapplication('guest1', 'benzhou', ['google', 'baidu']))
    GUpromotion('guest','123')