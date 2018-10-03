import os,paramiko,requests


def writejsontosplunk (jsontext,adr,port_,token_):
    url = adr
    port = port_
    securitytoken = token_
    os.environ['NO_PROXY'] = url
    # authHeader = {'Authorization': 'Splunk {}'.format(securitytoken)}

    authHeader = {'Authorization': 'Splunk {}'.format(securitytoken),'Content-type': 'application/json; profile=urn:splunk:event:1.0; charset=utf-8'}

    print (authHeader)
    jsonDict = jsontext
    try:
     print('''https://''' + url + ':' + port + '/services/collector/event''')
     r1 = requests.post('''http://''' + url + ':' + port + '/services/collector/event', headers=authHeader,json=jsonDict, verify=False)
     print ('''https://''' + url + ':' + port + '/services/collector/event''')
     d = eval(r1.text)
     print (d)
     r = (d["code"])
     print (r)
    except:

        r=777
    return r



def extractdigit(inputstring):
    digits = ''
    for symbol in inputstring:
        if '1234567890.'.find(symbol) != -1:
            digits=digits+symbol
    return digits

def redis_run_command(runcommand):
    host = '10.221.1.39'
    user = 'apkrutov'
    secret = 'Putin2019'
    port = 22
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, username=user, password=secret, port=port)
    stdin, stdout, stderr =client.exec_command(runcommand)
    data = stdout.read() + stderr.read()
    return data

def create_splunk_message(index_to_save,ip,action, mem_free,proc_util,Health):
    dictjson = {"index": index_to_save,
                "sourcetype": "JSON",

                "event": {
                    "URL":ip,
                    "Action": action,
                    "MEMORYFREE": mem_free+" GB",
                    "PROCESSOR_UTIL": proc_util+" %",
                    "SystemUSE": "PYTHON_SCRIPT",
                    "SQL_Health": Health

                }
                }

    return dictjson



def create_splunk_message_MYSQL(index_to_save,ip,action,Health):
    dictjson = {"index": index_to_save,
                "sourcetype": "JSON",
    "event": {
                    "URL":ip,
                    "Action": action,
                    "SQL_HEALTH": Health,
                    "SystemUSE": "PYTHON_SCRIPT",
                    }}


    return dictjson
