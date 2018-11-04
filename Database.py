import MySQLdb

"""
    This file handle all the database queries and related functions.
"""

class Database(object):
    try:
        def __init__(self):

            self.db = MySQLdb.connect(
                    host='localhost',
                    user='GuTou',
                    db='LLHC'
            )
            self.cur = self.db.cursor()
    except:
        print("DB not connected!")


    def makeTable(self):
        try:
            users = 'CREATE TABLE IF NOT EXISTS User(' \
                    'Email VARCHAR(500) NOT NULL PRIMARY KEY,' \
                    'UserName VARCHAR(15) NOT NULL,' \
                    'Password char(16) NOT NULL,' \
                    'UserType INT NOT NULL,' \
                    'Document TEXT,' \
                    'UNIQUE (Email));'

            userType = 'CREATE TABLE IF NOT EXISTS UserType(TypeID INT NOT NULL PRIMARY KEY,' \
                       'Type TEXT NOT NULL' \
                       ')'

            tabooWords = 'CREATE TABLE IF NOT EXISTS Taboo(' \
                         'Email VARCHAR(500) NOT NULL PRIMARY KEY,' \
                         'TabooWord VARCHAR(500) NOT NULL,' \
                         'FOREIGN KEY (Email) REFERENCES User(Email));'

            self.cur.execute(users)
            self.cur.execute(userType)
            self.cur.execute(tabooWords)

            defSU = "INSERT INTO UserType(TypeID, Type) VALUES ('1','Super User');"
            defOU = "INSERT INTO UserType(TypeID, Type) VALUES ('2','Ordinary User');"
            defGU = "INSERT INTO UserType(TypeID, Type) VALUES ('3','Guest User');"
            self.cur.execute(defSU)
            self.cur.execute(defOU)
            self.cur.execute(defGU)
            self.db.commit()


        except Exception as e:
            print("At Database.makeTable() "+e)

    def checkUserExists(self, email, username):
        """
            Check if the email OR username already in db
        :param email: user email in string
        :param username: user name in string
        :return: If exists, return True; if not then False
        """
        query = "SELECT * FROM User WHERE Email='"+email+"' OR UserName = '"+username+"';"
        self.cur.execute(query)

        data = self.cur.fetchall()
        if len(data):
            return True
        else:
            return False

    def addUser(self, email, username, psd, userType):
        """
            Call to add an user
        :param email
        :param username
        :param psd: password in MD5 encoding
        :param userType: (INT) 1 for SU, 2 for OU, 3 for GU
        :return: False if user already exists, True if account created
        """
        if self.checkUserExists(email, username):
            return False
        else:
            query = "INSERT INTO User(Email, UserName, Password, UserType) VALUES (%s,%s,%s,%s)"
            val = (email,username,psd,userType)
            self.cur.execute(query,val)
            self.db.commit()
            return True


    def login(self,email,psd):
        """
            Log in function
        :param email:
        :param psd:
        :return: False for login error, True with user type for login successfully.
        """


    def changePsd(self, email, oldPsd, newPsd):
        pass


db = Database()
db.makeTable()