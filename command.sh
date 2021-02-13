#!/usr/bin/env bash

python3 -m venv ~/venv
source ~/venv/bin/activate
pip install -r requirements.txt


az group create -l japaneast -n  udagroup
az appservice plan create -g udagroup -n my-service-plan --is-linux --sku B1  
az webapp create -g udagroup -p my-service-plan -n my-appservice --runtime "Python|3.6"  