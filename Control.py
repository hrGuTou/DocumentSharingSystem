from Account import *

"""
    All backend service/control functions will be included in this file
    Main service file 
"""

def startApp():
    db = Database
    db.makeTable()

def ROOTUSER(email):
    """
        GUI guide:  在初始登录界面，如果数据库有SU用户，可以直接登录SU

                    在OU用户登录后，出现一个管理按钮。如果数据库里没有SU，弹窗询问是否升级为SU
                    如果选择是，当前OU升级为SU
    :param email:
    :param password:
    :return:
    """
    if Database.SUexists() == False:
        promoteOU(email)


def signUp(email, password):
    """
       sign up to be an OU, if password field leave blank, to be a GU
    :param email:
    :param password:
    :return:
    """
    if password == "":
        if createGuest(email, password):
            return "Welcome guest!"

        if createAcc(email,password):
            return "Sign up success!"
        else:
            return "User already exists, please login."

def signIn(email, password):
    """

    :param email:
    :param password:
    :return:
    """

    if logIn(email, password):
        return "Welcome!"
    else:
        return "Login error."

def signOut(email):
    if logOut(email):
        return "Logout success!"


