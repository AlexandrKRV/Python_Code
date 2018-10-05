import base64
import gzip
import xml.etree.ElementTree as ET

# функция разархивирования файла gz
# на входе имя gz файла который нужно разархивировать и имя выходного файла в который сохраняем извлеченные данные
def gz_extract (fnameinp, fnameout):
    f = gzip.open(fnameinp, 'rb')
    file_content = f.read()
    f_out = open(fnameout, 'wb')
    f_out.write(file_content)
    f.close()
    return ('success')


# функция преобразования base64 в строку
# на входе строка base64 на выходе расшифрованная строка
def base64_to_str (base64_data):
    norm_string = base64.b64decode(base64_data)
    return (norm_string)


# функция парсинга файла полученного от РСА
# на вход приходит xml на выход кол-во оставшихся бланков и дата ответа
def read_resp_rsa( xmlfile):
    tree = ET.parse(xmlfile)
    root = tree.getroot()
    count_bso = (root[0].text)
    date_resp = (root[1].text)
    return ([count_bso,date_resp])


# создание сообщения для отправки в SPLUNK
# передает индекс куда писать в SPLUNK, url-адрес сервиса к которому обращаемся, действие и окружение тестовое или пром
def create_splunk_message(index_to_save,url,action,message, env,company_name,time_rep,count_bso):
    dictjson = {
        "index": index_to_save,
        "sourcetype": "JSON",
        "event": {
            "url": url,
            "message": message,
            "Action": action,
            "Company":company_name,
            "Time_RSA":time_rep,
            "Count_free_bso":count_bso,
            "SystemUSE": "PYTHON_SCRIPT"
        }
    }
    return dictjson







