#!/usr/bin/env bash

python3 -m venv ~/venv
source ~/venv/bin/activate

pip install locust==1.4.3


locust -H https://my-appservice.azurewebsites.net  --run-time 300s --headless
