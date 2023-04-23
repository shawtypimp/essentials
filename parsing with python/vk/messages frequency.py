from datetime import datetime
import vk_api
import csv
tok3n = ""
user_id = 258746971
peer_id = 2000000235
count = 200

session = vk_api.VkApi(token = tok3n)
vk = session.get_api()

get_messages = session.method("messages.getHistory", { "count": count, "user_id": user_id, "peer_id": peer_id})
#делаю запрос
rawdates = [it['date'] for it in get_messages['items']]
#достаю только нужные значения 
dates = list(map(int, rawdates))
#преобразую словарь из str формата в int

normalized_dates = []
for date in dates:
    newdates = datetime.utcfromtimestamp(date).strftime('%Y-%m-%d %H:%M:%S')
    normalized_dates.append(newdates)
#т.к. все данные пришли в формате unixtime, их нужно преобразовать в привычный формат 

with open('results.csv', 'w+',  newline = '', encoding='utf8') as f:
    w = csv.writer(f, delimiter = ',', quoting=csv.QUOTE_NONE)
    for date in normalized_dates:
        w.writerow([date])








 
