from locust import HttpLocust, TaskSet, task
import random
import string

class GreetingTaskSet(TaskSet):
    def on_start(self):
        self.client.headers = {'Content-Type': 'application/json; charset=utf-8'}

    @task
    def fetch_greeting(self):
        self.client.get("/greetings")

    @task
    def create_greeting(self):
        # 雑にランダム文字列で済ませちゃう。 (注: random.choices は 3.6 以降でしか使えません)
        self.client.post("/greetings", json={"text": ''.join(random.choices(string.ascii_letters, k=10))})

class GreetingLocust(HttpLocust):
    task_set = GreetingTaskSet

    min_wait = 100
    max_wait = 1000