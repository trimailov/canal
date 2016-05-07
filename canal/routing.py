from channels import include
from channels.routing import route
from canal import consumers


message_routing = [
    route("websocket.connect", consumers.ws_connect),
    route("websocket.receive", consumers.ws_message),
    route("websocket.disconnect", consumers.ws_disconnect),
]


long_task_routing = [
    route("websocket.connect", consumers.ws_connect),
    route("websocket.receive", consumers.slow_ws_message),
    route("websocket.disconnect", consumers.ws_disconnect),
]


channel_routing = [
    route("chat-messages", consumers.msg_consumer),
    route("slow-chat-messages", consumers.slow_msg_consumer),

    include("canal.routing.message_routing", path=r"^/chat"),
    include("canal.routing.long_task_routing", path=r"^/second-chat"),
]
