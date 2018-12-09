import firebase_admin
from firebase_admin import credentials


def initial():
    cred = credentials.Certificate("Firebase_cred/llhc-db662-firebase-adminsdk-xggy5-5c08106dab.json")

    firebase_admin.initialize_app(cred, {
        'databaseURL' : 'https://llhc-db662.firebaseio.com/'
    })

