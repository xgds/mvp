import falcon

class Status:
    def on_get(self, request, response):
        response.status = falcon.HTTP_NO_CONTENT
