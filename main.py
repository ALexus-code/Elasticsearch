import datetime
import ijson
import json5 as json
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import pandas as pd
import openpyxl
import pathlib
import openpyxl as xl
from openpyxl import Workbook
from openpyxl import load_workbook
from dateutil.parser import parse
from psycopg2 import sql
import numpy
import re
import requests
import uuid
import json
from psycopg2 import extensions
from bottle import run, get

#import psycopg2
#psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

#conn = psycopg2.connect(dbname='postgres', user='alekseivaganov',
                        #password='', host='localhost')
#conn.set_client_encoding('UTF8')

#cursor = conn.cursor()
#Cоздание базы из scv в postgresql
import csv

#sqlColumns = 'INSERT INTO posts (id, rubrics, text, create_date)'
#with open('posts.csv', newline='') as csvfile:
    #reader = csv.DictReader(csvfile)
    #for row in reader:
        #print(row)
        #id = str(uuid.uuid4())
        #rubrics = row['rubrics']
        #text = row['text']
        #createdate = row['created_date']
        #sqlValues = 'VALUES(' + "'" + id + "'" + ',' + "'" + str(rubrics).replace("'['", "").replace("']'", "").replace("'", "").replace("[", "").replace("]", "") + "'" + ',' + "'" + str(text).replace("'", '') + "'" + ',' + "'" + createdate + "'" + ')'
        #Vstavca = 'POST post/_bulk/n{"create":{'  + str(id)+ '}}\n{"text":' +  str(text).replace("'", '') + '}'
        #res = requests.get("https://opensearch.com/")
        #print(sqlValues)
        #cursor.execute(sqlColumns + ' ' + sqlValues)
        #conn.commit()

s = requests.session()

headers = {'login_username': 'admin',
           'login_password': 'ineedmore'}
url = 'https://opensearch.ru:9200'
page = s.get(url=url, verify = False, auth=(headers['login_username'], headers['login_password']))
print(page.text)
#Vstavca = 'POST post/_bulk/n{"create":{'
#with open('posts.csv', newline='') as csvfile:
    #reader = csv.DictReader(csvfile)
    #for row in reader:
        #print(row)
        #id = str(uuid.uuid4())
        #rubrics = row['rubrics']
        #text = row['text']
        #createdate = row['created_date']
        #Vstavca = 'POST post/_bulk\n{"create":{' + id + '}}' + '\n{"text":' + str(text).replace("'", '') + '}'
        #print(Vstavca)
        #res = requests.post("https://opensearch.ru:9200", verify = False)
#print(Vstavca)

#print("введите запрос")
#x = input()

#drug = ('GET post/_search {"query":{ "match":{ "text": "' + x + '" }}}')
#drug = "images/search?from=tabbar&text=как%20жить"
#print(drug)

#responce = requests.get("https://opensearch.ru:9200", verify = False, params = drug)
#print(responce.json)
#try:
    #response = get(, params=a)
#except ConnectionError:
    #print("Проверьте подключение к сети.")
#else:
    #print(response.content)


# Create an index with non-default settings.
from opensearchpy import OpenSearch
host = "https://opensearch.ru:9200"
auth = ('admin','ineedmore')
client = OpenSearch(
          hosts=host,
          http_compress=True,
          http_auth=auth,
          use_ssl=False,
          verify_certs=False,
          ssl_assert_hostname=False,
          ssl_show_warn=False
         )
index_name = 'python-test-index'
#index_body = {
#    'settings': {
#        'index': {
#            'number_of_shards': 2
#        }
#    }
#}

#response = client.indices.create(index_name, body=index_body)
#print('\nCreating index:')
#print(response)

#document = {
    #'title': 'Moneyball',
    #'director': 'Bennett Miller',
    #'year': '2011'
#}
##id = '1'

#response = client.index(
#    index=index_name,
#    body=document,
#    id=id,
#    refresh=True
#)

#print('\nAdding document:')
#print(response)


q = 'Ищу'
query = {
    'size': 5,
    'query': {
        'multi_match': {
            'query': q,
            'fields': ['title^2', 'director']
        }
    }
}

response = client.search(
    body=query,
    index=index_name
)
print('\nSearch results:')
print(response)