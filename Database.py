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

        suggestedTaboo = 'CREATE TABLE IF NOT EXISTS suggestTaboo(' \
                         'Email VARCHAR(500) NOT NULL PRIMARY KEY,' \
                         'TabooWord VARCHAR(500),' \
                         'FOREIGN KEY (Email) REFERENCES User(Email));'

        tabooWords = 'CREATE TABLE IF NOT EXISTS Taboo(' \
                     'WordID INT PRIMARY KEY AUTO_INCREMENT,' \
                     'TabooWord VARCHAR(500);'

        document = 'CREATE TABLE IF NOT EXISTS Document(' \
                   'DocID CHAR(36) CHARACTER SET ascii,' \
                   'VersionID INT NOT NULL,' \
                   'Email VARCHAR(500) NOT NULL PRIMARY KEY,' \
                   'Document TEXT,' \
                   'Status CHAR(1) NOT NULL,' \
                   'LastMod TIMESTAMP NOT NULL,' \
                   'UNIQUE (VersionID),' \
                   'FOREIGN KEY (Email) REFERENCES User(Email))'

        cur.execute(users)
        cur.execute(userType)
        cur.execute(suggestedTaboo)
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
        print("At Database.makeTable() " + e)


def checkUserExists(email):
    """
            Check if the email OR username already in db
        :param email: user email in string
        :return: If exists, return True; if not then False
        """
    query = "SELECT * FROM User WHERE Email='" + email + "';"
    cur.execute(query)

    data = cur.fetchall()
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
    val = (email, psd, userType, '0')
    cur.execute(query, val)
    db.commit()
    return True


def login(email):
    """
            Log in function
        :param email:
        :return: Hashed password
        """
    query = "SELECT Password FROM User WHERE Email = '" + email + "';"
    cur.execute(query)
    row = cur.fetchone()
    return row[0]


def checkLoginStat(email):
    query = "SELECT LoginStat FROM User WHERE Email = '" + email + "';"
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
    sql = "SELECT Type FROM User NATURAL JOIN UserGroup WHERE Email ='" + email + "';"
    cur.execute(sql)
    row = cur.fetchone()
    return row[0]


def logInStat(email):
    query = "SELECT LoginStat FROM User WHERE Email = '" + email + "';"
    cur.execute(query)
    loginStat = cur.fetchone()[0]
    return loginStat


def unlockDoc(DocID):
    """
                U is unlock, L is locked
            :param DocID:
            :return: True: unlock success
                    False: no action
            """
    sql = "SELECT Status FROM Document WHERE DocID = '" + DocID + "';"
    cur.execute(sql)
    lockStatus = cur.fetchone()[0]

    if lockStatus == 'L':
        unlock = "UPDATE Document SET Status = 'U' WHERE DocID = '" + DocID + "';"
        cur.execute(unlock)
        db.commit()
        return True
    else:
        print("Doc is already unlocked.")
        return False

def getTaboo():
    sql = "SELECT TabooWord FROM Taboo;"
    cur.execute(sql)
    return [item[0] for item in cur.fetchall()]

def getSugTaboo():
    sql = "SELECT * FROM suggestTaboo;"
    cur.execute(sql)
    result = []
    for row in cur.fetchall():
        result.append(list(row))

    return result

def addTaboo(listoftaboo):
    """

            :param listoftaboo: list of approved taboo words
            :return: True after addition completes
            """

    for word in listoftaboo:
        sql = "INSERT INTO Taboo(TabooWord) VALUE (%s);"
        val = (word)
        cur.execute(sql, val)
    db.commit()

    return True