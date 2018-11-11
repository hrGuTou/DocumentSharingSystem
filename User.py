import Database

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

    def invitation(self, email):
        pass

    def lockFile(self, DocID):
        pass

    def unlockFile(self, DocID):
        pass




class SU(OU):
    def __init__(self, email):
        OU.__init__(self, email)

    def manageMember(self, email, membership):
        """
        :param email:
        :param membership: 2 for OU, 3 for GU
        :return: True for update successfully
                False for invalid membership input
        """
        if membership == 2 and membership == 3:
            sql = "UPDATE User SET UserType = '"+membership+"' WHERE Email = '" + email + "';"
            Database.cur.execute(sql)
            Database.db.commit()
            return True
        else:
            return False


    def getSuggestTaboo(self):
        """
            2D list which show who suggested what words
        :return: Return the suggested Taboo word.
        """
        return Database.getSugTaboo()

    def getTaboo(self):
        """

        :return: current list of taboo words in database.
        """
        return Database.getTaboo()

    def deleteTaboo(self, listofwords):
        """

        :param listofwords:
        :return: True when finished deleting
        """
        for word in listofwords:
            delete = "UPDATE Taboo SET TabooWord = NULL WHERE TabooWord = '"+word+"';"
            Database.cur.execute(delete)
        Database.db.commit()
        return True

    def addTaboo(self, listoftaboo):
        """

        :param listoftaboo:
        :return: added words
        """
        if Database.addTaboo(listoftaboo):
            return True

    def unlock(self, DocID):
        """

        :param DocID:
        :return:  True: unlock success
                    False: error
        """
        if Database.unlockDoc(DocID):
            return True
        else:
            return False



    def complain(self,DocID):
        """TODO: dont know what is this"""
        pass

