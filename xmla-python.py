# Databricks notebook source
import requests
import pandas as pd
from requests.auth import HTTPBasicAuth

# Rest Endpoint to invoke, along with the azure analysis services query as query string
url = 'https://<myappsvc>.azurewebsites.net/api/Query?query=Evaluate <Database_Name>'

#service principal credentials
user = 'app:<clientId><@TenantId>' # e.g. 'app:123456-7890-1234-5678-901234@123456-7890-1234-5678-9012345'
secret = 'mysecret'

# call REST endpoint (Databricks --> App Service REST API --> Azure Analysis Service)
res = requests.get(url, auth=HTTPBasicAuth(user, secret))

# load json in dataframe
data = pd.read_json(res.content)

#print
display(data)


# COMMAND ----------


