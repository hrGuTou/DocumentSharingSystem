import DB

#For SU
"================================================="

def addTaboo(listoftaboo):
    try:
        for word in listoftaboo:
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


def deleteTaboo(listofword):
    try:
        ref = DB.tabooWord
        for word in listofword:
           ref.child(DB.tolower(word)).delete()

        return True

    except Exception as e:
        print("deleteTaboo()")
        print(e)

def getSuggestedTaboo():
    try:
        ref = DB.user.get()
        taboo = {}
        for key in ref:
            if "Suggest_taboo" in ref[key]:
                taboo[key] = ref[key]['Suggest_taboo']

        return taboo
    except Exception as e:
        print("getSuggestedTaboo")
        print(e)

"================================================"

def suggestTaboo(email, listofword):
    try:
        ref = DB.user.child(DB.removeIllegalChar(email)).child('Suggest_taboo')
        for word in listofword:
            ref.update({
                DB.tolower(word):DB.tolower(word)
            })

    except Exception as e:
        print("suggestTaboo()")
        print(e)

def deleteSuggestTaboo(email, listofword):
    try:
        ref = DB.user.child(DB.removeIllegalChar(email)).child('Suggest_taboo')

        for word in listofword:
            ref.child(DB.tolower(word)).delete()

        return True

    except Exception as e:
        print("deleteSuggestTaboo")
        print(e)


if __name__ == '__main__':
    print(getTaboo())