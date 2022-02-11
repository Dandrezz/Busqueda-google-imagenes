import requests
import webbrowser
from os import walk
import time

pathFolder = "directorio"
filenames = next(walk(pathFolder), (None, None, []))[2]
extensiones = ["png","jpg"]
for i in filenames:
    if True in [(j in i) for j in extensiones]:
        filePath = '{}/{}'.format(pathFolder,i)
        searchUrl = 'http://www.google.hr/searchbyimage/upload'
        multipart = {'encoded_image': (filePath, open(filePath, 'rb')), 'image_content': ''}
        response = requests.post(searchUrl, files=multipart, allow_redirects=False)
        fetchUrl = response.headers['Location']
        webbrowser.open(fetchUrl)
        time.sleep(10)
