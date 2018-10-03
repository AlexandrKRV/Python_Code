import os
import csv
from zeep import Client, exceptions
from zeep.wsse.username import UsernameToken
import mysql.connector

# def savedocfromfstore (key):
#     head = {"ip": "127.0.0.1", "login": "yourlogin", "mac": "digitalmacaddr"}
#     client = Client("http://hostname.ru:28080/filestore?wsdl",
#                     wsse=UsernameToken('yourlogin', 'yourpassword', use_digest=True))
#     key=r'%s' %key
#     keyvalue = {"key":  key}
#     print (keyvalue)
#     result = client.service.readFile(head, keyvalue)
#     doc = (result["document"])
#     cont = doc["content"]
#     typedoc = doc["mimeType"]
#     type = ""
#     i = 0
#     for char in typedoc:
#         i = i + 1
#         if char == "/":
#             n = i
#     doctype = typedoc[n:i]
#     path=os.getcwd()+"""\ExportFstore\\"""
#     src = key
#     key = src.split('/')[5]
#     filename =path+key+"_"+policynum+"."+doctype
#     out_file = open(filename, "wb")
#     out_file.write(cont)
#     out_file.close()
#     return ("777")


def charinstring(str,ch):
    r=0
    for char in str:
        if char==ch:
         r = 1
    return r





def savedocfromfstore (key,numbso):
    head = {"ip": "127.0.0.1", "login": "yorlogin", "mac": "digitmacaddress"}
    client = Client("http://cc-haproxy.rgs.ru:28080/filestore?wsdl",
                    wsse=UsernameToken('yourlogin', 'yourpassword', use_digest=True))
    keyvalue = {"key": key}
    result = client.service.readFile(head, keyvalue)
    doc = (result["document"])
    cont = doc["content"]
    typedoc = doc["mimeType"]
    type = ""
    i = 0
    for char in typedoc:
        i = i + 1
        if char == "/":
            n = i
    doctype = typedoc[n:i]
    path=os.getcwd()+"""/ExportFstore/"""
    res=charinstring(key,'/')
    if res == 1:
       src = key
       key = src.split('/')[5]
    print (key)
    filename =path+key+"_"+numbso+"."+doctype
    out_file = open(filename, "wb")
    out_file.write(cont)
    out_file.close()
    return ("777")



def connectmysql ():
    conn = mysql.connector.connect(host='ipmysqldatabase',
                                       database='namedatabase',
                                       user='logindatabase',
                                       password='youpassword')

    return conn


def readcsv(filename):
    r=[]
    with open(filename, newline='') as myFile:
        reader = csv.reader(myFile, delimiter=";")
        for row in reader:
         r.append(row)
    return r





