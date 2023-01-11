import firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
firebase_sdk = credentials.Certificate('ej4p-6ef9e-firebase-adminsdk-6rutu-f996a54e79.json')
firebase_admin.initialize_app(firebase_sdk,{"databaseURL":"https://ej4p-6ef9e-default-rtdb.firebaseio.com/"},'prueba')
