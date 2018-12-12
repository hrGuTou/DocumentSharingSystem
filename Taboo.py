import DB

#For SU
"================================================="

def addTaboo(word):
    try:

        DB.tabooWord.update({
                DB.tolower(word): DB.tolower(word)
            })

        return True

    except Exception as e:
        print("addTaboo()")
        print(e)

def getTaboo():
    try:
        listoftaboo = DB.tabooWord.get()
        result =[]
        for key in listoftaboo:
            result.append(listoftaboo[key])

        return result

    except Exception as e:
        print("getTaboo()")
        print(e)


def deleteTaboo(word):
    try:
        ref = DB.tabooWord

        ref.child(DB.tolower(word)).delete()

        return True

    except Exception as e:
        print("deleteTaboo()")
        print(e)

def getSuggestedTaboo():
    try:
        ref = DB.root.child('Suggest_taboo').get()
        taboo = []
        if ref is not None:
            for key in ref:
                taboo.append(ref[key])
        print(taboo)
        return taboo
    except Exception as e:
        print("getSuggestedTaboo")
        print(e)

"================================================"

def suggestTaboo(listofword):
    try:
        ref = DB.root.child('Suggest_taboo')
        for word in listofword:
            ref.update({
                DB.tolower(word):DB.tolower(word)
            })

    except Exception as e:
        print("suggestTaboo()")
        print(e)

def deleteSuggestTaboo(word):
    try:
        ref = DB.suggestTaboo

        ref.child(DB.tolower(word)).delete()

        return True

    except Exception as e:
        print("deleteSuggestTaboo")
        print(e)

def deleteAllTaboo():
    try:
        DB.tabooWord.delete()

    except Exception as e:
        print(e)

def deleteAllSuggest():
    try:
        DB.suggestTaboo.delete()
    except Exception as e:
        print(e)
if __name__ == '__main__':
    deleteTaboo('7')