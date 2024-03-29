import uuid
import logging

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from clients.models import Clients

logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger('ocpp')

def get_cardtag(cpnumber, userid):
  response_timeout = 10
  vendorId = "gresystem"
  messageId = "uvStartCardRegMode"
  msg = {
    "memberId":userid,
    "targetcp":cpnumber
  }
  ocpp_req = {
        "msg_direction" : 2,
        "connection_id" : str(uuid.uuid4()),
        "msg_name": "DataTransfer",
        "msg_content": {'vendorId':vendorId,'messageId':messageId,'data': msg},
      }

  message = [2, ocpp_req['connection_id'], ocpp_req['msg_name'], ocpp_req['msg_content']]
  print('data transfer req: ', message)
  queryset = Clients.objects.filter(cpnumber=cpnumber).values()
  channel_name = queryset[0]['channel_name_1']

  channel_layer = get_channel_layer()
  async_to_sync(channel_layer.send)(
    channel_name,
    {
      'type':'ocpp16_message',
      'message': message 
    }
  )

def reset_cpinfo(cpnumber, reset_type):
  ocpp_req = {
    "msg_direction" : 2,
    "connection_id" : "",
    "msg_name": "Reset",
    "msg_content": {'type': reset_type},
  }
  ocpp_request_to_cp(cpnumber, ocpp_req)

def update_cpinfo(cpnumber):
  ocpp_req = {
    "msg_direction" : 2,
    "connection_id" : "",
    "msg_name": "UpdateFirmware",
    "msg_content": {},
  }
  ocpp_request_to_cp(cpnumber, ocpp_req)

def clearcache_cpinfo(cpnumber):
  ocpp_req = {
    "msg_direction" : 2,
    "connection_id" : "",
    "msg_name": "ClearCache",
    "msg_content": {},
  }
  ocpp_request_to_cp(cpnumber, ocpp_req)

def remotestart_cpinfo(cpnumber, id_tag, charging_profile):
  print(charging_profile)
  if charging_profile['charging_profile_id'] == '':
    ocpp_req = {
      "msg_direction" : 2,
      "connection_id" : "",
      "msg_name": "RemoteStartTransaction",
      "msg_content": {
        'idTag': id_tag,
      },
    }
  else:
    ocpp_req = {
      "msg_direction" : 2,
      "connection_id" : "",
      "msg_name": "RemoteStartTransaction",
      "msg_content": {
        'idTag': id_tag,
        'chargingProfile': {
          'chargingProfileId' : int(charging_profile['charging_profile_id']),
          'stackLevel' : int(charging_profile['charging_profile_level']),
          'chargingProfilePurpose' : charging_profile['charging_profile_purpose'],
          'chargingProfileKind' : charging_profile['charging_profile_kind'],
          'chargingSchedule' : {
            'chargingRateUnit' : 'W',
            'chargingSchedulePeriod' : charging_profile['charging_schedule_period']
          },
        },
      },
    }

  ocpp_request_to_cp(cpnumber, ocpp_req)

def remotestop_cpinfo(cpnumber, transaction_id):
  ocpp_req = {
    "msg_direction" : 2,
    "connection_id" : "",
    "msg_name": "RemoteStopTransaction",
    "msg_content": {'transactionId': transaction_id},
  }
  ocpp_request_to_cp(cpnumber, ocpp_req)

def unlock_connector(cpnumber, connector_id):
  ocpp_req = {
    "msg_direction" : 2,
    "connection_id" : "",
    "msg_name": "UnlockConnector",
    "msg_content": {'connectorId': connector_id},
  }
  ocpp_request_to_cp(cpnumber, ocpp_req)

def get_conf(cpnumber, key_list):
  ocpp_req = {
    "msg_direction" : 2,
    "connection_id" : "",
    "msg_name": "GetConfiguration",
    "msg_content": {'key': key_list},
  }
  ocpp_request_to_cp(cpnumber, ocpp_req)

def set_conf(cpnumber, key_list):
  # key_list = json.loads(msg_content)
  ocpp_req = {
    "msg_direction" : 2,
    "connection_id" : "",
    "msg_name": "ChangeConfiguration",
    "msg_content": {'key': key_list[0]['key'], 'value': key_list[0]['value']},
  }
  ocpp_request_to_cp(cpnumber, ocpp_req)

def set_charging_profile(cpnumber, profile):
  ocpp_req = {
    "msg_direction" : 2,
    "connection_id" : "",
    "msg_name": "SetChargingProfile",
    "msg_content": {
      'connectorId': int(profile['connectorId']),
      'csChargingProfiles': {
        'chargingProfileId': int(profile['chargingProfileId']),
        'stackLevel': int(profile['stackLevel']),
        'chargingProfilePurpose': profile['chargingProfilePurpose'],
        'chargingProfileKind': profile['chargingProfileKind'],
        'chargingSchedule': profile['chargingSchedule'],
      }
    },
  }
  ocpp_request_to_cp(cpnumber, ocpp_req)

def get_locallist(cpnumber):
  ocpp_req = {
    "msg_direction" : 2,
    "connection_id" : "",
    "msg_name": "GetLocalListVersion",
    "msg_content": {},
  }
  ocpp_request_to_cp(cpnumber, ocpp_req)

def send_locallist(cpnumber, list_version, update_type, local_authorization_list):
  ocpp_req = {
    "msg_direction" : 2,
    "connection_id" : "",
    "msg_name": "SendLocalList",
    "msg_content": {
      'listVersion': int(list_version),
      'updateType': update_type,
      'localAuthorizationList': local_authorization_list
    },
  }
  ocpp_request_to_cp(cpnumber, ocpp_req)

def update_firmware(cpnumber, location, retrieve_date, **kwargs):
  ocpp_req = {
    "msg_direction" : 2,
    "connection_id" : "",
    "msg_name": "UpdateFirmware",
    "msg_content": {
      'location': location,
      'retrieveDate': retrieve_date,
    },
  }
  
  ocpp_request_to_cp(cpnumber, ocpp_req)

def get_diagnostics(cpnumber, location, **kwargs):
  ocpp_req = {
    "msg_direction" : 2,
    "connection_id" : "",
    "msg_name": "GetDiagnostics",
    "msg_content": {
      'location': location,
    },
  }
  
  ocpp_request_to_cp(cpnumber, ocpp_req)

def reserve_now(cpnumber, connector_id, expiry_date, id_tag, parent_id_tag, reservation_id):
  ocpp_req = {
    "msg_direction" : 2,
    "connection_id" : "",
    "msg_name": "ReserveNow",
    "msg_content": {
      'connectorId': connector_id,
      'expiryDate': expiry_date,
      'idTag': id_tag,
      'parentIdTag': parent_id_tag,
      'reservationId': reservation_id
    },
  }
  
  ocpp_request_to_cp(cpnumber, ocpp_req)

def cancel_reservation(cpnumber, reservation_id):
  ocpp_req = {
    "msg_direction" : 2,
    "connection_id" : "",
    "msg_name": "CancelReservation",
    "msg_content": {
      'reservationId': reservation_id
    },
  }
  
  ocpp_request_to_cp(cpnumber, ocpp_req)

def trigger_message(cpnumber, requested_message):
  ocpp_req = {
    "msg_direction" : 2,
    "connection_id" : "",
    "msg_name": "TriggerMessage",
    "msg_content": {
      'requestedMessage': requested_message
    },
  }
  
  ocpp_request_to_cp(cpnumber, ocpp_req)

def change_available(cpnumber, connector_id, op_type):
  ocpp_req = {
    "msg_direction" : 2,
    "connection_id" : "",
    "msg_name": "ChangeAvailability",
    "msg_content": {
      'connectorId': connector_id,
      'type': op_type,
    },
  }
  
  ocpp_request_to_cp(cpnumber, ocpp_req)

def get_composite_schedule(cpnumber, connectorId, duration):
  ocpp_req = {
    "msg_direction" : 2,
    "connection_id" : "",
    "msg_name": "GetCompositeSchedule",
    "msg_content": {
      'connectorId': int(connectorId),
      'duration': int(duration),
    },
  }
  ocpp_request_to_cp(cpnumber, ocpp_req)

def clear_charging_profile(cpnumber, connectorId, id):
  ocpp_req = {
    "msg_direction" : 2,
    "connection_id" : "",
    "msg_name": "ClearChargingProfile",
    "msg_content": {
      'connectorId': int(connectorId),
      'id': int(id),
    },
  }
  ocpp_request_to_cp(cpnumber, ocpp_req)

def data_transfer(cpnumber, vendor_id, message_id, data):
  ocpp_req = {
    "msg_direction" : 2,
    "connection_id" : "",
    "msg_name": "DataTransfer",
    "msg_content": {
      'vendorId': vendor_id,
      'messageId': message_id,
      'data': data,
    },
  }
  ocpp_request_to_cp(cpnumber, ocpp_req)



def send_request(cpnumber, message):
  print('OCPP Message : Send to {} : {}'.format(cpnumber, message))
  queryset = Clients.objects.filter(cpnumber=cpnumber).values()
  channel_name = queryset[0]['channel_name_1']

  channel_layer = get_channel_layer()
  async_to_sync(channel_layer.send)(
    channel_name,
    {
      'type':'ocpp16_message',
      'message': message 
    }
  )

def connectionid_logging(cpnumber, connection_id, msg_name):
  queryset = Clients.objects.filter(cpnumber=cpnumber).values()

  if queryset.count() == 0:
    client = Clients(
      cpnumber = cpnumber,
      connection_id_1 = connection_id,
      channel_status_1 = msg_name
    )
    client.save()
    print('connection_id saved successfully')
  else:
    if not (queryset[0]['connection_id_1'] == connection_id):
      Clients.objects.filter(cpnumber=cpnumber).update(connection_id_1=connection_id, channel_status_1 =msg_name)
      print('connection_id updated successfully')

def ocpp_request_to_cp(cpnumber, ocpp_req):

  global Job_List 

  ocpp_req['msg_direction'] = 2
  ocpp_req['connection_id'] = str(uuid.uuid4())

  if ocpp_req['msg_name'] == 'Reset':
    pass
  elif ocpp_req['msg_name'] == 'UpdateFirmware':
    pass
    # ocpp_req['msg_content'] = {
    #   'location':'http://127.0.0.1:8000/SW_FileDownload/skb_firmware_v1.1.6.bin',
    #   'retrieveDate': datetime.now().strftime('%Y-%m-%dT%H:%M:%S') + "Z",
    #   'retries': 1,
    #   'retryInterval': 1
    # }
  elif ocpp_req['msg_name'] == 'ClearCache':
    ocpp_req['msg_content'] = {}
  elif ocpp_req['msg_name'] == 'RemoteStartTransaction':
    pass
  elif ocpp_req['msg_name'] == 'RemoteStopTransaction':
    ocpp_req['msg_content'] = {'transactionId': 1}
  elif ocpp_req['msg_name'] == 'UnlockConnector':
    pass
  elif ocpp_req['msg_name'] == 'GetConfiguration':
    pass
  elif ocpp_req['msg_name'] == 'ChangeConfiguration':
    pass
  elif ocpp_req['msg_name'] == 'GetLocalListVersion':
    pass
  elif ocpp_req['msg_name'] == 'SendLocalList':
    pass
  elif ocpp_req['msg_name'] == 'SetChargingProfile':
    pass
  elif ocpp_req['msg_name'] == 'GetDiagnostic':
    pass
  elif ocpp_req['msg_name'] == 'ReserveNow':
    pass
  elif ocpp_req['msg_name'] == 'ChangeAvailability':
    pass
  elif ocpp_req['msg_name'] == 'TriggerMessage':
    pass
  elif ocpp_req['msg_name'] == 'GetCompositeSchedule':
    pass
  elif ocpp_req['msg_name'] == 'ClearChargingProfile':
    pass
  elif ocpp_req['msg_name'] == 'DataTransfer':
    pass
  else:
    pass
  
  # Websocket message composition, sending and logging
  message = [ocpp_req['msg_direction'], ocpp_req['connection_id'], ocpp_req['msg_name'], ocpp_req['msg_content']]
  send_request(cpnumber, message)
  connectionid_logging(cpnumber, ocpp_req['connection_id'], ocpp_req['msg_name'])




  # response = Ocpp16Consumer.get_specific_response(unique_id=ocpp_req['connection_id'], timeout=response_timeout)
  # print('CardReg response 3: ', response)



    # async def cancel_reservation(self):
    #     request = call.CancelReservationPayload(
    #         revervation_id = 1
    #     )

    #     response = await self.call(request)
    #     if response.id_tag_info['status'] == RegistrationStatus.accepted:
    #         print("===================================")
    #         print("Calcel Reservation is accepted.")
    #         print("===================================")

    # async def change_availability(self):
    #     request = call.ChangeAvailabilityPayload(
    #         connector_id = 1,
    #         type = 'AvailabilityType'
    #     )

    #     response = await self.call(request)
    #     if response.id_tag_info['status'] == RegistrationStatus.accepted:
    #         print("===================================")
    #         print("Change Availability is accepted.")
    #         print("===================================")

    # async def change_configuration(self):
    #     request = call.ChangeConfigurationPayload(
    #         key = 'str', 
    #         value = 'Any'
    #     )

    #     response = await self.call(request)
    #     if response.id_tag_info['status'] == RegistrationStatus.accepted:
    #         print("===================================")
    #         print("Change Configuration is accepted.")
    #         print("===================================")

    # async def clear_cache(self):
    #     request = call.ClearCachePayload()

    #     response = await self.call(request)
    #     print("===================================")
    #     print("Clear Cache transferred.....")
    #     print("===================================")

    # async def clear_charging_profile(self):
    #     request = call.ClearChargingProfilePayload(
    #         # options: id, connector_id, charging_profile_purpose, stack_level
    #     )

    #     response = await self.call(request)
    #     if response.id_tag_info['status'] == RegistrationStatus.accepted:
    #         print("===================================")
    #         print("Clear Change Profile is accepted.")
    #         print("===================================")




    # async def get_composite_schedule(self):
    #     request = call.GetCompositeSchedulePayload(
    #         connector_id = 1,
    #         duration = 60
    #     )

    #     response = await self.call(request)
    #     if response.id_tag_info['status'] == RegistrationStatus.accepted:
    #         print("===================================")
    #         print("Get Composite Schedule is accepted.")
    #         print("===================================")

    # async def get_configuration(self):
    #     request = call.GetConfigurationPayload(
    #         # options : key
    #     )

    #     response = await self.call(request)
    #     if response.id_tag_info['status'] == RegistrationStatus.accepted:
    #         print("===================================")
    #         print("Get Configuration is accepted.")
    #         print("===================================")

    # async def get_diagnostics(self):
    #     request = call.GetDiagnosticsPayload(
    #         location = 'str'
    #         # options : retries, retry_interval, start_time, stop_time
    #     )

    #     response = await self.call(request)
    #     if response.id_tag_info['status'] == RegistrationStatus.accepted:
    #         print("===================================")
    #         print("Get Diagnostics is accepted.")
    #         print("===================================")

    # async def get_local_list_version(self):
    #     request = call.GetLocalListVersionPayload()

    #     response = await self.call(request)
    #     print("===================================")
    #     print("Get Local List Version transferred.....")
    #     print("===================================")

    # async def remote_start_transaction(self):
    #     request = call.RemoteStartTransactionPayload(
    #         id_tag = 'str'
    #         # options : connector_id, changing_profile
    #     )

    #     response = await self.call(request)
    #     if response.id_tag_info['status'] == RegistrationStatus.accepted:
    #         print("===================================") 
    #         print("Remote Start Transaction is accepted.")
    #         print("===================================")

    # async def remote_stop_transaction(self):
    #     request = call.RemoteStopTransactionPayload(
    #         transaction_id = 1
    #     )

    #     response = await self.call(request)
    #     if response.id_tag_info['status'] == RegistrationStatus.accepted:
    #         print("===================================")
    #         print("Remote Stop Transaction is accepted.")
    #         print("===================================")

    # async def reserve_now(self):
    #     request = call.ReserveNowPayload(
    #         connector_id = 1,
    #         expiry_date = "datatime str",
    #         id_tag = 'str',
    #         reservation_id = 1, 
    #         # options: parent_id_tag
    #     )

    #     response = await self.call(request)
    #     if response.id_tag_info['status'] == RegistrationStatus.accepted:
    #         print("===================================")
    #         print("Reserve Now is accepted.")
    #         print("===================================")

# def reset(cpnumber):
#   request = call.ResetPayload(
#       type = 'Reset Type'
#   )

#   response = await self.call(request)
#   if response.id_tag_info['status'] == RegistrationStatus.accepted:
#       print("===================================")
#       print("Reset is accepted.")
#       print("===================================")

    # async def send_local_list(self):
    #     request = call.SendLocalListPayload(
    #         type = 'Reset Type'
    #     )

    #     response = await self.call(request)
    #     if response.id_tag_info['status'] == RegistrationStatus.accepted:
    #         print("===================================")
    #         print("Send Local List is accepted.")
    #         print("===================================")

    # async def set_charging_profile(self):
    #     request = call.SetChargingProfilePayload(
    #         connector_id = 1,
    #         cs_charging_profiles = 'Dict'
    #     )

    #     response = await self.call(request)
    #     if response.id_tag_info['status'] == RegistrationStatus.accepted:
    #         print("===================================")
    #         print("Set Charging Profile is accepted.")
    #         print("===================================")

    # async def trigger_message(self):
    #     request = call.TriggerMessagePayload(
    #         requested_message = 'MessageTrigger'
    #         # connector_id: Optional[int] = None
    #     )

    #     response = await self.call(request)
    #     if response.id_tag_info['status'] == RegistrationStatus.accepted:
    #         print("===================================")
    #         print("Trigger Message is accepted.")
    #         print("===================================")

    # async def unlock_connector(self):
    #     request = call.UnlockConnectorPayload(
    #         connector_id = 1
    #     )

    #     response = await self.call(request)
    #     if response.id_tag_info['status'] == RegistrationStatus.accepted:
    #         print("===================================")
    #         print("Unlock Connector is accepted.")
    #         print("===================================")

    # async def update_firmware(self):
    #     request = call.UpdateFirmwarePayload(
    #         location = 'str',
    #         retrieve_date = 'datetime str'
    #         # options: retries: int, retry_interval: int
    #     )

    #     response = await self.call(request)
    #     if response.id_tag_info['status'] == RegistrationStatus.accepted:
    #         print("===================================")
    #         print("Update Firmware is accepted.")
    #         print("===================================")

  