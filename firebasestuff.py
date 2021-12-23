import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred_obj = credentials.Certificate('C:\\Users\\braun_p\\Desktop\\Prog\\Python\\get_data\\adminsdk.json')
default_app = firebase_admin.initialize_app(cred_obj, {
        'databaseURL':"https://prices-42ff3-default-rtdb.europe-west1.firebasedatabase.app/"
        })


def firebasepost(what):

    ref = db.reference("/")
    ref.set({
	    "Profit":
	    {
		    "Ordered": -1
	    }
    })

    ref = db.reference("/Profit/Ordered")

    for entry in what : 
        x = entry.split(";")


        ref.push().set(x)


# Get the entry with maximum price from firebase
def firebaseget():
    ref = db.reference("/Profit/Ordered/")
    snapshot = ref.order_by_child("2").limit_to_last(1).get() # only returns the value with most profit
    for key, val in snapshot.items():
        myval = val

    return (myval)