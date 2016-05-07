from channels import include
from channels.routing import route
from canal.consumers import ws_connect, ws_message, ws_disconnect, msg_consumer


message_routing = [
    route("websocket.connect", ws_connect),
    route("websocket.receive", ws_message),
    route("websocket.disconnect", ws_disconnect),
]


channel_routing = [
    route("chat-messages", msg_consumer),
    include("canal.routing.message_routing", path=r"^/chat"),
]
