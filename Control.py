from Account import *

"""
    All backend service/control functions will be included in this file
    Main service file 
"""


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
        promoteToSU(email)


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

    if createAcc(email, password):
        return "Sign up success!"
    else:
        return "User already exists, please login."


def signIn(email, password):
    """

    :param email: required
    :param password: required only for OU and SU, GU can leave it blank
    :return: login status in string format
    """
    status = logIn(email, password)

    if status == '1':
        return "Welcome!"
    elif status == '2':
        return "Already logged in"
    elif status == '3':
        return "Welcome! Guest"
    elif status == '-1':
        return "User not exists"
    else:
        return "Wrong password"


def signOut(email):
    """
        Use this function to log out user.
    :param email:
    :return: return log out status
    """
    if logOut(email):
        return "Logout success!"
    else:
        return "User not logged in"


if __name__ == '__main__':
    print(signIn('guest', 'asf'))
