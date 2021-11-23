import requests
import mysql.connector
import time




count = 1

while count < 10:
    # request at coindesk
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    file_data = str(r.json()["chartName"] + ": " + str(r.json()["bpi"]["USD"]["rate"]))
    # name variable
    name_coin = r.json()["chartName"]
    price_coin =r.json()["bpi"]["USD"]["rate"]
    price_coin_db = r.json()["bpi"]["USD"]["rate"]
    price_coin_lst = price_coin.replace(",",  "")
    coin_dd = float(price_coin_lst)
    print(name_coin)
    print(price_coin)

    mydb = mysql.connector.connect(host="localhost", user='root', password="", database="bitcoin2")


    cryp = mydb.cursor()

    sql = "INSERT INTO cripto (naam, prijs) VALUES (%s, %s)"
    val = (name_coin, coin_dd)
    cryp.execute(sql, val)

    mydb.commit()
    # saving data
    logfile = open('C:\\users\Barbara\mylogfile' + '.txt', 'a')
    logfile.write(file_data)
    logfile.write("\n")
    logfile.close()

    print("current price {0} is: {1} ".format(name_coin, price_coin))
    count += 1
    time.sleep(30)