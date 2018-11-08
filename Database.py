import MySQLdb

"""
    This file handle all the database queries and related functions.
    
    TODO: implement bcrypt password hashing
    https://pypi.org/project/bcrypt/
"""


try:
    

    db = MySQLdb.connect(
                    host='localhost',
                    user='GuTou',
                    db='LLHC'
            )
    cur = db.cursor()
except:
    print("DB not connected!")


def makeTable():
    try:
        users = 'CREATE TABLE IF NOT EXISTS User( ' \
                    'Email VARCHAR(500) NOT NULL PRIMARY KEY,' \
                    'UserName VARCHAR(15),' \
                    'Password VARCHAR(300),' \
                    'UserType INT NOT NULL,' \
                    'LoginStat INT NOT NULL,' \
                    'UNIQUE (Email));'

        userType = 'CREATE TABLE IF NOT EXISTS UserGroup(UserType INT NOT NULL PRIMARY KEY,' \
                       'Type TEXT NOT NULL' \
                       ')'

        tabooWords = 'CREATE TABLE IF NOT EXISTS Taboo(' \
                         'Email VARCHAR(500) NOT NULL PRIMARY KEY,' \
                         'TabooWord VARCHAR(500) NOT NULL,' \
                         'FOREIGN KEY (Email) REFERENCES User(Email));'

        document = 'CREATE TABLE IF NOT EXISTS Document(' \
                       'Email VARCHAR(500) NOT NULL PRIMARY KEY,' \
                       'Document TEXT,' \
                       'Status CHAR(1) NOT NULL,' \
                       'LastMod TIMESTAMP NOT NULL,' \
                       'FOREIGN KEY (Email) REFERENCES User(Email))'

        cur.execute(users)
        cur.execute(userType)
        cur.execute(tabooWords)
        cur.execute(document)
        try:
            defSU = "INSERT INTO UserGroup(UserType, Type) VALUES ('1','Super User');"
            defOU = "INSERT INTO UserGroup(UserType, Type) VALUES ('2','Ordinary User');"
            defGU = "INSERT INTO UserGroup(UserType, Type) VALUES ('3','Guest User');"
            cur.execute(defSU)
            cur.execute(defOU)
            cur.execute(defGU)
            db.commit()
        except Exception as e:
            print(e)

    except Exception as e:
            print("At Database.makeTable() "+e)

def checkUserExists(email):
        """
            Check if the email OR username already in db
        :param email: user email in string
        :return: If exists, return True; if not then False
        """
        query = "SELECT * FROM User WHERE Email='"+email+"';"
        cur.execute(query)

        data =  cur.fetchall()
        if len(data):
            return True
        else:
            return False

def addUser(email, psd, userType):
        """
            Call to add an user
        :param email
        :param username
        :param psd: password in BCRYPT encoding
        :param userType: (INT) 1 for SU, 2 for OU, 3 for GU
        :return: True if account created
        """

        query = "INSERT INTO User(Email, Password, UserType, LoginStat) VALUES (%s,%s,%s,%s)"
        val = (email,psd,userType,'0')
        cur.execute(query,val)
        db.commit()
        return True


def login(email):
        """
            Log in function
        :param email:
        :return: Hashed password
        """
        query = "SELECT Password FROM User WHERE Email = '"+email+"';"
        cur.execute(query)
        row = cur.fetchone()
        return row[0]

def checkLoginStat(email):
    query = "SELECT LoginStat FROM User WHERE Email = '"+email+"';"
    cur.execute(query)
    row = cur.fetchone()
    return row[0]

def SUexists():
    query = "SELECT * FROM User WHERE UserType='1';"
    cur.execute(query)

    data = cur.fetchall()
    if len(data):
        return True
    else:
        return False

def currentUserGroup(email):
    sql = "SELECT Type FROM User NATURAL JOIN UserGroup WHERE Email ='"+email+"';"
    cur.execute(sql)
    row = cur.fetchone()
    return row[0]

def logInStat(email):
    query = "SELECT LoginStat FROM User WHERE Email = '" + email + "';"
    cur.execute(query)
    loginStat = cur.fetchone()[0]
    return loginStat

def changePsd(self, email, oldPsd, newPsd):
        pass

def changeUsername(self, email, newUserName):
        pass

def updateTaboo(self):
        pass

