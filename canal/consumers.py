import time

from channels import Group, Channel
from channels.sessions import channel_session


# Connected to chat-messages
def msg_consumer(message):
    Group("chat-%s" % message.content['room']).send({
        "text": message.content['text'],
    })


# Connected to slwo-chat-messages
def slow_msg_consumer(message):
    time.sleep(5)
    Group("chat-%s" % message.content['room']).send({
        "text": message.content['text'],
    })


# Connected to websocket.connect
@channel_session
def ws_connect(message):
    # Work out room name from path (ignore slashes)
    room = message.content['path'].strip(b"/")
    # django session must be JSON serializable as `bytes` are not
    room = room.decode('utf-8')
    # Save room in session and add us to the group
    message.channel_session['room'] = room
    Group("chat-%s" % room).add(message.reply_channel)


# Connected to websocket.receive
@channel_session
def ws_message(message):
    Channel('chat-messages').send({
        "text": message.content['text'],
        "room": message.channel_session['room'],
    })


# Connected to websocket.receive
@channel_session
def slow_ws_message(message):
    message.reply_channel.send({
        "text": "message sent, wait for reply"
    })
    Channel('slow-chat-messages').send({
        "text": message.content['text'],
        "room": message.channel_session['room'],
    })


# Connected to websocket.disconnect
@channel_session
def ws_disconnect(message):
    Group("chat-%s" % message.channel_session['room']).discard(message.reply_channel)
