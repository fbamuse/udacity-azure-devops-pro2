from locust import HttpUser, TaskSet, task, between, constant

class UserBehavior(TaskSet):
    @task(1)
    def home(self):
        self.client.get("/")

    @task(2)
    def any(self):
        self.client.get("/any")


    @task(3)   
    def checkPredict(self):
        self.client.post("/predict", json={
            "CHAS":{
                "0":0
            },
            "RM":{
                "0":6.575
            },
            "TAX":{
                "0":296.0
            },
            "PTRATIO":{
                "0":15.3
            },
            "B":{
                "0":396.9
            },
            "LSTAT":{
                "0":4.98
            }
        })


class WebsiteUser(HttpUser):
    tasks = {UserBehavior:1}
    wait_time = constant(0)