# Copyright 2018 Cleuton Sampaio

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import requests

globalFoto = '/Users/cleuton/Documents/projetos/DL_iot/unknown_0001.jpg' # retirar

def uploadFoto(foto):
    url = 'http://localhost:8088'
    files = {'file': open(foto, 'rb')}
    r = requests.post(url, files=files)
    return r.status_code

def checkFoto():
    retorno = False
    if len(globalFoto) > 0:   # mudar isso
        return globalFoto,True
    return globalFoto,False

def waitFoto():
    global globalFoto
    foto,haveFoto = checkFoto()
    if haveFoto:
        print('@@@ Processando foto...')
        retorno = uploadFoto(foto)
        globalFoto = '' #retirar
        print('*** Retorno do processamento da foto: ', retorno)

while (True):
    waitFoto()