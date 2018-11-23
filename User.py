import DB

"""
    Main class for User, subclasses will be SU, OU, and GU.
"""

class User():
    def __init__(self, email):
        self.email = email

    def openDoc(self,DocID):
        pass

    def retriveOldVer(self,DocID,VerID):
        pass

    def complain(self, DocID):
        pass

    def suggestTaboo(self, words):
        pass

    def Apply(self):
        pass
    #sign up for membership


class GU(User):
    def __init__(self, email):
        User.__init__(self, email)

    def promote(self, name, techInterests):
        pass



class OU(User):
    def __init__(self,email):
        User.__init__(self, email)

    def createDoc(self):
        pass

    def setPermission(self, DocID):
        pass

    def invitation(self, email):#also need ability to deny or cancel a invitation.
        pass

    def lockFile(self, DocID):
        pass

    def unlockFile(self, DocID):# after when the file has been updated by other ou?
        pass

    def ActionRestrict(self):
        pass
        # When the OU has been reported of using taboo word, all the activity under OU
        # will be restrict til the taboo word been fixed

    def Report(self):
        pass
        #report other OU's update to onwer
        #report onwer to SU
    def search(self):
        pass
        #search file by keyword
        #search other user by name or info

class SU(OU):
    def __init__(self, email):
        OU.__init__(self, email)

    def manageMember(self, email, membership):#has ability to deny an application from new GU
        """
        :param email:
        :param membership: 2 for OU, 3 for GU
        :return: True for update successfully
                False for invalid membership input
        """
        if membership == 2 and membership == 3:
            sql = "UPDATE User SET UserType = '"+membership+"' WHERE Email = '" + email + "';"
            DB.cur.execute(sql)
            DB.db.commit()
            return True
        else:
            return False


    def getSuggestTaboo(self):
        """
            2D list which show who suggested what words
        :return: Return the suggested Taboo word.
        """
        return DB.getSugTaboo()

    def getTaboo(self):
        """
        :return: current list of taboo words in database.
        """
        return DB.getTaboo()

    def deleteTaboo(self, listofwords):
        """
        :param listofwords:
        :return: True when finished deleting
        """
        for word in listofwords:
            delete = "UPDATE Taboo SET TabooWord = NULL WHERE TabooWord = '"+word+"';"
            DB.cur.execute(delete)
        DB.db.commit()
        return True

    def addTaboo(self, listoftaboo):
        """
        :param listoftaboo:
        :return: added words
        """
        if DB.addTaboo(listoftaboo):
            return True


    def unlock(self, DocID): #if it's already in OU and SU reserved all the ability from OU and GU, we'll still need it in here? 

        """
        :param DocID:
        :return:  True: unlock success
                    False: error
        """
        if DB.unlockDoc(DocID):
            return True
        else:
            return False



    def complain(self,DocID):
        """TODO: dont know what is this"""
        pass
