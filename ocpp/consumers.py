import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.middleware import BaseMiddleware
from channels.db import database_sync_to_async
import json
import logging
import jwt

from .models import Ocpp
from .message_processing import ocpp_request
from clients.models import Clients


from user.models import User
from cpinfo.models import Cpinfo

logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger('ocpp')

@database_sync_to_async
def channel_logging(cpnumber, channel_name):
  queryset = Clients.objects.filter(cpnumber=cpnumber).values()

  if queryset.count() == 0:
    client = Clients(
      cpnumber = cpnumber,
      channel_name_1 = channel_name,
    )
    client.save()
    logging.info('Channel saved successfully')
  else:
    Clients.objects.filter(cpnumber=cpnumber).update(channel_name_1=channel_name)
    logging.info('Channel updated successfully')

class OcppConsumer(AsyncWebsocketConsumer):
    async def connect(self, subprotocols=['ocpp1.6']):
        try:
            requested_protocols = [item[1] for item in self.scope['headers'] if item[0] == b'sec-websocket-protocol']
        except KeyError:
            print("Client hasn't requested any Subprotocol. Closing Connection")

        if self.scope['subprotocols']:
            print("Protocols Matched: ", self.scope['subprotocols'])
        else:
            print('Protocols Mismatched | Expected Subprotocols: %s, but client supports  %s | Closing connection', self.scope['subprotocols'], requested_protocols)
            self.disconnect()

        self.cp_id = self.scope['path_remaining']
        self.cp_group_name = f'group_{self.cp_id}'
        print('cp_id: ', self.cp_id)

        await self.channel_layer.group_add(
            self.cp_group_name,
            self.channel_name
        )
        await channel_logging(channel_name=self.channel_name, cpnumber=self.cp_id)

        await self.accept()
    
    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):

        message = json.loads(text_data)
        logging.info('OCPP_REQ received from {}: {}'.format(self.cp_id, message))

        await self.channel_layer.group_send(
            self.cp_group_name,
            {
                'type': 'ocpp_message',
                'message': message
            }
        )

    async def ocpp_message(self, event):
        message = event['message']

        # call your async task here
        cpnumber = self.cp_id
        conf = await ocpp_message_handler(cpnumber, message)

        await self.send(text_data=json.dumps(conf))

        logging.info('OCPP_CONF sent to {}: {}'.format(self.cp_id, conf))

@database_sync_to_async
def ocpp_message_handler(cpnumber, message):

    ocpp_req = {
        "msg_direction" : message[0],
        "connection_id" : message[1],
        "msg_name": message[2],
        "msg_content": message[3],
        'cpnumber': cpnumber,
    }

    Ocpp.objects.create(
        msg_direction = message[0],
        connection_id = message[1],
        msg_name = message[2],
        msg_content = message[3],
        cpnumber = cpnumber
    )

    ocpp_conf = ocpp_request(ocpp_req)

    Ocpp.objects.create(
        msg_direction = ocpp_conf[0],
        connection_id = ocpp_conf[1],
        msg_name = '',
        msg_content = ocpp_conf[2],
        cpnumber = cpnumber
    )

    return ocpp_conf


class JwtAuthMiddleware(BaseMiddleware):
    async def __call__(self, scope, receive, send):
        query_string = scope.get('query_string').decode('utf-8')
        token = [val.split('=')[1]
                 for val in query_string.split('&')
                 if val.startswitch('Authorization=')]
        print('Authorization: ', token)
        if token:
            user =await self.get_user_from_token(token[0])
            if user:
                scope['user'] = user
        return await super().__call__(scope, receive, send)
    
    @database_sync_to_async
    def get_cpid_from_token(self, token):
        try:
            payload = jwt.decode(token, "SECRET_KEY")
            cp_id = Cpinfo.objects.get(cpnumber=payload['username'])
            print('cp_id: ', cp_id)
            return cp_id
        except Exception as e:
            return None

# class JwtAuthMiddleware(BaseMiddleware):
#     async def __call__(self, scope, receive, send):
#         query_string = scope.get('query_string').decode('utf-8')
#         token = [val.split('=')[1]
#                  for val in query_string.split('&')
#                  if val.startswitch('token=')]
#         if token:
#             user =await self.get_user_from_token(token[0])
#             if user:
#                 scope['user'] = user
#         return await super().__call__(scope, receive, send)
    
#     @database_sync_to_async
#     def get_user_from_token(self, token):
#         try:
#             payload = jwt.decode(token, "SECRET_KEY")
#             user = User.objects.get(username=payload['username'])
#             return user
#         except Exception as e:
#             return None