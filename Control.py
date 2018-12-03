import Account
import DB
import Document
import User
"""
    All backend service/control functions will be included in this file
    Main service file 
"""

def userType(email):
    """

    :param email:
    :return: return the user type of current user
    """
    type = DB.currentUserGroup(email)
    if type == '0':
        return "Super User"
    elif type == '1':
        return "Ordinary User"
    else:
        return "Guest User"


def ROOTUSER(email):
    """
        GUI guide:  在初始登录界面，如果数据库有SU用户，可以直接登录SU

                    在OU用户登录后，出现一个管理按钮。如果数据库里没有SU，弹窗询问是否升级为SU
                    如果选择是，当前OU升级为SU
    :param email:
    :param password:
    :return:
    """
    if DB.SUexists() == False:
        Account.promoteToSU(email)


def signUp(email, password, name, techInterest):
    """
       sign up to be an OU, if password field leave blank, to be a GU
    :param email:
    :param password:
    :return:
    """
    if password == "":
        if Account.createGuest(email, password, name, techInterest):
            return 0

    if Account.createAcc(email, password, name, techInterest):
        return 1
    else:
        return -1


def signIn(email, password):
    """

    :param email: required
    :param password: required only for OU and SU, GU can leave it blank
    :return: login status in string format
    """
    status = Account.logIn(email, password)

    return status



def signOut(email):
    """
        Use this function to log out user.
    :param email:
    :return: return log out status
    """
    if Account.logOut(email):
        return "Logout success!"
    else:
        return "User not logged in"





def manage(email):
    """
         GUI for SU to manage the system
    :param email:
    :return:
    """
    pass



if __name__ == '__main__':
    signUp('test','123','haoran',['computer','sleep'])