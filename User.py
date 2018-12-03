import DB
import Document
import Taboo
import Account
import requests

"""
    Main class for User, subclasses will be SU, OU, and GU.
"""


class User():
    def __init__(self, email):
        self.email = email

    def openDoc(self, fileOwner, filename, version):
        Document.openfile(self.email, fileOwner, filename, version)

    def retriveOldVer(self, filename):
        """:return list of all docs versions"""
        Document.listallhistory(self.email, filename)

    def filomplain(self, filename, complain):
        DB.fileComplain(self.email, filename, complain)

    def suggestTaboo(self, listofwords):
        Taboo.suggestTaboo(self.email, listofwords)

    def getPermission(self, permissionType):
        """

        :param permissionType: private, public, restricted, shared
        :return: return all docs with the same permission type in dict{username:[list of filename]}
        """
        return Document.getPermissionFiles(permissionType)

    def mostPopular(self):
        """

        :return: three tuples of the most viewed documents
                Format is 'fileOwner','DocName', 'Views'
                Use open Doc to open the files

                CAUTION: check file property before open
        """
        return Document.getMostview()

    def getEmail(self):
        return self.email

class GU(User):
    def __init__(self, email):
        User.__init__(self, email)

    def apply(self, name, techInterests):
        """
            Apply to be an OU
        :param name:
        :param techInterests: list of tech interest
        :return:
        """
        Account.OUapplication(self.email, name, techInterests)
        return "Application sent, pending approval"

    def applybutton(self):
        """

        :return: 0 application not found for this GU, call Account.OUapplication(GUemail, name, listoftechInterests)
                1 already applied, display error message

        """
        if DB.getApplDecision(self.email) is None:
            return 0
        elif DB.getApplDecision(self.email) == 'Pending':
            return 1
        elif DB.getApplDecision(self.email) == 'Denied':
            return -1
        else:  # approved
            return 2

    def GUpromotion(self, psd):
        Account.GUpromotion(self.email, psd)


class OU(User):
    def __init__(self, email):
        User.__init__(self, email)

    def listallfiles(self):
        return Document.listallfiles(self.email)

    def saveDoc(self, docLocation, filename):
        """
            if file is locked, save rejected
        :param docLocation:
        :param filename:
        :return:
        """
        if not Document.isFileLocked(self.email, filename):
            Document.saveDoc(self.email, docLocation, filename)
        else:
            return "File is locked, save unsuccessful"

    def setPermission(self, filename, permissionINT):
        """each document default permission is private"""
        """
            permission: 1: public 2: restrict 3: shared 4: private
        """

        if permissionINT == 1:
            permission = "public"
        elif permissionINT == 2:
            permission = "restrict"
        elif permissionINT == 3:
            permission = "shared"
        elif permissionINT == 4:
            permission = "private"
        else:
            return False

        Document.setPermission(self.email, filename, permission)

    def invitation(self, email):  # also need ability to deny or cancel a invitation.
        pass

    def sentInvitation(self, email):
        pass

    def answerInvitation(self, email):
        pass

    def lockFile(self, filename):
        """currently can lock the file OU owned
            TODO: lock other OU files
            """
        Document.changeLock(self.email, filename)

        return Document.isFileLocked(self.email, filename)

    def ActionRestrict(self):
        pass
        # When the OU has been reported of using taboo word, all the activity under OU
        # will be restrict til the taboo word been fixed

    def Report(self):
        pass
        # report other OU's update to onwer
        # report onwer to SU

    def search(self):
        pass
        # search file by keyword
        # search other user by name or info


class SU(OU):
    def __init__(self, email):
        OU.__init__(self, email)

    def reviewApplication(self):
        """

        :return: a dictionary for all application
        """
        allApplication = DB.checkApplication()

        return allApplication

    def applicationDecision(self, GU, decision):
        """

        :param GU:
        :param decision: 1 for approve, 0 for deny
        :return:
        """
        if decision == 1:
            DB.applicationDecision(GU, 'Approved')
        elif decision == 0:
            DB.applicationDecision(GU, 'Denied')
        else:
            return "Decision input error"

    def getSuggestTaboo(self):
        """
        :return: Return the suggested Taboo word in dictionary.
        """
        return Taboo.getSuggestedTaboo()

    def getTaboo(self):
        """

        :return: current list of taboo words in database.
        """
        return Taboo.getTaboo()

    def deleteTaboo(self, listofwords):
        """

        :param listofwords:
        :return: True when finished deleting
        """
        return Taboo.deleteTaboo(listofwords)

    def addTaboo(self, listoftaboo):
        """

        :param listoftaboo:
        :return: added words
        """
        if Taboo.addTaboo(listoftaboo):
            return True

    def complain(self, DocID):
        """TODO: dont know what is this"""
        pass



if __name__ == "__main__":
    newuser = OU('viewtest')
    newuser.openDoc('viewtest','fafa','')
    #post()
