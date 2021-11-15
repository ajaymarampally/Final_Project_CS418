from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import csv


def write_to_csv(json_data,filename):
    '''function to write the json output to csv file'''
    api_data_file = open(filename,'w',newline='')
    csv_writer = csv.writer(api_data_file)

    cnt = 0
    for data in json_data.data:
        if cnt ==0:
            header = json_data.keys()
            csv_writer.writerow(header)
            cnt+=1
        csv_writer.writerow(json_data.values())
    api_data_file.close()



url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'50',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '9b695354-825b-4a21-ae0e-7efe986c090b',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  write_to_csv(data,'api_data.csv')
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)



