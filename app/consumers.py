from django.http import HttpResponse
from channels.handler import AsgiHandler


def http_consumer(message):
    # Make standard HTTP response - access ASGI path attribute directly
    string = "Hello world! You asked for %s" % message.content['path']
    response = HttpResponse(string)
    # Encode that response into message format (ASGI)
    for chunk in AsgiHandler.encode_response(response):
        message.reply_channel.send(chunk)
