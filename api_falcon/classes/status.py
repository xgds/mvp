import falcon

class Status:
    def on_get(self, request, response):
        response.media = {}
        response.status = falcon.HTTP_NO_CONTENT

