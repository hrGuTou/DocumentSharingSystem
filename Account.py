"""
    Account Management

    TODO: change password and add userName
"""

import Database
import bcrypt



def createAcc(email, psd):
    """
        For OU
    :param email:
    :param psd:
    :return: false: user already exists, ask if forget password or change password
             true: user added into database
    """

    if Database.checkUserExists(email):
        return False

    else:
        """password encoded"""
        hashedPSD = bcrypt.hashpw(psd.encode('utf8'), bcrypt.gensalt())
        Database.addUser(email, hashedPSD, '2')  # 2 for OU
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

    if Database.checkUserExists(email):
        if Database.logInStat(email) == 0:
            """
                if account exists and not logged in, proceed login
                
            """
            if not (psd == "" and Database.currentUserGroup(email) == "Guest User"):
                """
                    If the password string is not empty and is not a GU, proceed psd check 
                """
                hashed = Database.login(email)
                if bcrypt.checkpw(psd.encode('utf8'), hashed.encode('utf8')):
                    sql = "UPDATE User SET LoginStat = '1' WHERE Email = '" + email + "';"
                    Database.cur.execute(sql)
                    Database.db.commit()
                    return True
                else:
                    return False
            else:
                return True
        else:
            print("Already logged in!")
            return '2'
    else:
        print("User not exists")
        return '-1'


def logOut(email):
    """
        For both SU and OU
    :param email:
    :return:
    """
    if Database.checkLoginStat(email) == 1:
        sql = "UPDATE User SET LoginStat = '0';"
        Database.cur.execute(sql)
        Database.db.commit()
        return True


def promoteOU(email):
    """
        If current database doesn't contain a super user, promote the current logged
        in user to be a super user.
    :param email:
    :return:
    """
    sql = "UPDATE User SET UserType = '1' WHERE Email = '" + email + "';"
    Database.cur.execute(sql)
    Database.db.commit()
    return True


def createGuest(email, password):
    """
        For GU
    :param email:
    :param password: IS AN EMPTY STRING
    :return:
    """
    if not Database.checkUserExists(email):
        Database.addUser(email, password, '3')  # 3 for GU
        return True
