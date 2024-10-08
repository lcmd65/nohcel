import pymssql
import pandas as pd


def connectServer():
    """ task """
    return

def userAuthentication(account, password):
    """ task """
    if (account == "dat.lemindast" and password == "1"):
        return True
    else:
        try:
            conn = pymssql.connect("localhost", "Nohcel_user", "sa", "123456")
            cur = conn.cursor()
            conn.commit()
            cur.excute("""
                    SELECT * FROM User
                    """)
            for row in cur:
                if row["Username"] == account and row["Password"] == password:
                    return True
            return False
        except:
            return False

def userAuthenticationNonePass(account,email):
    """ task """
    return 

def userSender(information):
    return