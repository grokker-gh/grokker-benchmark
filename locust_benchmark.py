from locust import FastHttpUser, task


class HelloWorldUser(FastHttpUser):

    host = "http://localhost:8000"

    @task
    def hello_world(self):
        self.client.post(
            "/grok",
            json={
                "text": "[Sun Jan 22 21:45:40 2006] [error] [client 64.182.1.110] File does not exist: /var/www/html/awstats/awstats.pl"
            }
        )
