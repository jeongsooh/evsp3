from django import forms
from clients.models import Clients

# RESET_CHOICES = [('소프트', 'Soft'), ('하드', 'Hard'),]

class ClientsResetForm(forms.Form):

  cpnumber = forms.CharField(
    error_messages={
      'required': '충전기번호를 입력하세요.'
    },
    max_length=64, label='충전기번호'
  )
  reset_type = forms.CharField(
    max_length=10, required=False, label='리셋 타입',
    help_text='Soft 또는 Hard'
  )

  def clean(self):
    cleaned_data = super().clean()
    cpnumber = cleaned_data.get('cpnumber')

    if cpnumber:
      try:
        clients = Clients.objects.get(cpnumber=cpnumber)
      except Clients.DoesNotExist:
        self.add_error('cpnumber', '충전기번호가 없는 번호입니다.')
        return

      self.cpnumber = clients.id

class ClientsClearcacheForm(forms.Form):

  cpnumber = forms.CharField(
    error_messages={
      'required': '충전기번호를 입력하세요.'
    },
    max_length=64, label='충전기번호'
  )

  def clean(self):
    cleaned_data = super().clean()
    cpnumber = cleaned_data.get('cpnumber')

    if cpnumber:
      try:
        clients = Clients.objects.get(cpnumber=cpnumber)
      except Clients.DoesNotExist:
        self.add_error('cpnumber', '충전기번호가 없는 번호입니다.')
        return

      self.cpnumber = clients.id

class RemoteStartForm(forms.Form):
  cpnumber = forms.CharField(
    error_messages={
      'required': '충전기번호를 입력하세요.'
    },
    max_length=64, label='충전기번호'
  )
  id_tag = forms.CharField(
    max_length=64, initial="0000000000150049", label='아이디태그',
    help_text='충전프로파일 없으면 아이디테그까지만 입력하면 됨'
  )
  charging_profile_id = forms.IntegerField(
    required=False, label='충전프로파일아이디'
  )
  charging_profile_level = forms.IntegerField(
    required=False, label='충전프로파일스택레벨'
  )   
  charging_profile_purpose = forms.CharField(
    max_length=64, required=False, label='충전프로파일목적',
    help_text='ChargePointMaxProfile / TxDefaultProfile / TxProfile'
  )
  charging_profile_kind = forms.CharField(
    max_length=64, required=False, label='충전프로파일종류',
    help_text='Absolute / Recurring / Relative'
  )
  start_period1 = forms.IntegerField( required=False, label='첫번째 충전일정')
  period_limit1 = forms.DecimalField( required=False, label='첫번째 충전 리미트')
  start_period2 = forms.IntegerField( required=False, label='두번째 충전일정')
  period_limit2 = forms.DecimalField( required=False, label='두번째 충전 리미트')
  start_period3 = forms.IntegerField( required=False, label='세번째 충전일정')
  period_limit3 = forms.DecimalField( required=False, label='세번째 충전 리미트')
  start_period4 = forms.IntegerField( required=False, label='네번째 충전일정')
  period_limit4 = forms.DecimalField( required=False, label='네번째 충전 리미트')


  def clean(self):
    cleaned_data = super().clean()
    cpnumber = cleaned_data.get('cpnumber')

    if cpnumber:
      try:
        clients = Clients.objects.get(cpnumber=cpnumber)
      except Clients.DoesNotExist:
        self.add_error('cpnumber', '충전기번호가 없는 번호입니다.')
        return

      self.cpnumber = clients.id

class RemoteStopForm(forms.Form):

  cpnumber = forms.CharField(
    error_messages={
      'required': '충전기번호를 입력하세요.'
    },
    max_length=64, label='충전기번호'
  )
  transaction_id = forms.IntegerField(
    required=False, label='트랜젝션아이디',
  )

  def clean(self):
    cleaned_data = super().clean()
    cpnumber = cleaned_data.get('cpnumber')

    if cpnumber:
      try:
        clients = Clients.objects.get(cpnumber=cpnumber)
      except Clients.DoesNotExist:
        self.add_error('cpnumber', '충전기번호가 없는 번호입니다.')
        return

      self.cpnumber = clients.id

class ClientsUnlockConnForm(forms.Form):

  cpnumber = forms.CharField(
    error_messages={
      'required': '충전기번호를 입력하세요.'
    },
    max_length=64, label='충전기번호'
  )
  connector_id = forms.IntegerField(
    required=False, label='커넥터아이디',
  )

  def clean(self):
    cleaned_data = super().clean()
    cpnumber = cleaned_data.get('cpnumber')

    if cpnumber:
      try:
        clients = Clients.objects.get(cpnumber=cpnumber)
      except Clients.DoesNotExist:
        self.add_error('cpnumber', '충전기번호가 없는 번호입니다.')
        return

      self.cpnumber = clients.id


class ClientsGetconfForm(forms.Form):

  cpnumber = forms.CharField(
    error_messages={
      'required': '충전기번호를 입력하세요.'
    },
    max_length=64, label='충전기번호'
  )

  def clean(self):
    cleaned_data = super().clean()
    cpnumber = cleaned_data.get('cpnumber')

    if cpnumber:
      try:
        clients = Clients.objects.get(cpnumber=cpnumber)
      except Clients.DoesNotExist:
        self.add_error('cpnumber', '충전기번호가 없는 번호입니다.')
        return

      self.cpnumber = clients.id

class ClientsSetconfForm(forms.Form):

  cpnumber = forms.CharField(
    error_messages={
      'required': '충전기번호를 입력하세요.'
    },
    max_length=64, label='충전기번호'
  )
  keys = forms.CharField(
    max_length=256, required=False, label='설정값',
    help_text='[{"key":"KEY", "value":"VALUE"}]'
  )

  def clean(self):
    cleaned_data = super().clean()
    cpnumber = cleaned_data.get('cpnumber')

    if cpnumber:
      try:
        clients = Clients.objects.get(cpnumber=cpnumber)
      except Clients.DoesNotExist:
        self.add_error('cpnumber', '충전기번호가 없는 번호입니다.')
        return

      self.cpnumber = clients.id

class ChargingProfileForm(forms.Form):
  cpnumber = forms.CharField(
    error_messages={
      'required': '충전기번호를 입력하세요.'
    },
    max_length=64, label='충전기번호'
  )
  connector_id = forms.IntegerField(label='커넥터번호')
  charging_profile_purpose = forms.CharField(max_length=64, label='충전프로파일퍼포스')
  charging_profile_kind = forms.CharField(max_length=64, label='충전프로파일카인드')
  duration = forms.IntegerField(label='프로파일지속시간')

  def clean(self):
    cleaned_data = super().clean()
    cpnumber = cleaned_data.get('cpnumber')

    if cpnumber:
      try:
        clients = Clients.objects.get(cpnumber=cpnumber)
      except Clients.DoesNotExist:
        self.add_error('cpnumber', '충전기번호가 없는 번호입니다.')
        return

      self.cpnumber = clients.id

class ClientsGetLocalListForm(forms.Form):

  cpnumber = forms.CharField(
    error_messages={
      'required': '충전기번호를 입력하세요.'
    },
    max_length=64, label='충전기번호'
  )

  def clean(self):
    cleaned_data = super().clean()
    cpnumber = cleaned_data.get('cpnumber')

    if cpnumber:
      try:
        clients = Clients.objects.get(cpnumber=cpnumber)
      except Clients.DoesNotExist:
        self.add_error('cpnumber', '충전기번호가 없는 번호입니다.')
        return

      self.cpnumber = clients.id

class ClientsSendLocalListForm(forms.Form):

  cpnumber = forms.CharField(
    error_messages={
      'required': '충전기번호를 입력하세요.'
    },
    max_length=64, label='충전기번호'
  )
  list_version = forms.IntegerField(label='로컬리스트버전')
  update_type = forms.CharField(max_length=64, label='로컬리스트설정타입',
    help_text='Differential / Full'
  )
  # Authorization status: Accepted/Blocked/Expired/Invalid/ConcurrentTx
  local_authorization_list = forms.CharField(
    max_length=256, required=False, label='로컬리스트',
    help_text='[{"idTag":"IdToken", "idTagInfo":{"status": "Accepted"},}]'
  )

  def clean(self):
    cleaned_data = super().clean()
    cpnumber = cleaned_data.get('cpnumber')

    if cpnumber:
      try:
        clients = Clients.objects.get(cpnumber=cpnumber)
      except Clients.DoesNotExist:
        self.add_error('cpnumber', '충전기번호가 없는 번호입니다.')
        return

      self.cpnumber = clients.id

class ClientsUpdateFirmwareForm(forms.Form):

  cpnumber = forms.CharField(
    error_messages={
      'required': '충전기번호를 입력하세요.'
    },
    max_length=64, label='충전기번호'
  )
  location = forms.CharField(
    max_length=256, required=False, label='펌웨어화일경로',
    help_text='http://127.0.0.1:8000/SW_FileDownload/skb_firmware_v1.1.6.bin'
  )
  retrieve_date = forms.CharField(
    max_length=32, label='업데이트 시각',
    help_text='YYYY-MM-DD HH:mm:ss + Z'
  )


  def clean(self):
    cleaned_data = super().clean()
    cpnumber = cleaned_data.get('cpnumber')

    if cpnumber:
      try:
        clients = Clients.objects.get(cpnumber=cpnumber)
      except Clients.DoesNotExist:
        self.add_error('cpnumber', '충전기번호가 없는 번호입니다.')
        return

      self.cpnumber = clients.id

class ClientsGetDiagForm(forms.Form):

  cpnumber = forms.CharField(
    error_messages={
      'required': '충전기번호를 입력하세요.'
    },
    max_length=64, label='충전기번호'
  )
  location = forms.CharField(
    max_length=256, required=False, label='진단화일 저장폴더',
    help_text='http://127.0.0.1:8000/Diag_FileUpload/'
  )

  def clean(self):
    cleaned_data = super().clean()
    cpnumber = cleaned_data.get('cpnumber')

    if cpnumber:
      try:
        clients = Clients.objects.get(cpnumber=cpnumber)
      except Clients.DoesNotExist:
        self.add_error('cpnumber', '충전기번호가 없는 번호입니다.')
        return

      self.cpnumber = clients.id

class ClientsReserveNowForm(forms.Form):

  cpnumber = forms.CharField(
    error_messages={
      'required': '충전기번호를 입력하세요.'
    },
    max_length=64, label='충전기번호'
  )
  connector_id = forms.IntegerField(label='커넥터아이디')
  expiry_date = forms.CharField(
    max_length=32, label='예약종료시간',
    help_text='YYYY-MM-DD HH:mm:ss + Z'
  )
  id_tag = forms.CharField(max_length=32, label='아이디테그')
  parent_id_tag = forms.CharField(max_length=32, required=False, label='부모아이디테그')
  reservation_id = forms.IntegerField(label='예약번호')

  def clean(self):
    cleaned_data = super().clean()
    cpnumber = cleaned_data.get('cpnumber')

    if cpnumber:
      try:
        clients = Clients.objects.get(cpnumber=cpnumber)
      except Clients.DoesNotExist:
        self.add_error('cpnumber', '충전기번호가 없는 번호입니다.')
        return

      self.cpnumber = clients.id

class ClientsCancelReservationForm(forms.Form):

  cpnumber = forms.CharField(
    error_messages={
      'required': '충전기번호를 입력하세요.'
    },
    max_length=64, label='충전기번호'
  )
  reservation_id = forms.IntegerField(label='예약번호')

  def clean(self):
    cleaned_data = super().clean()
    cpnumber = cleaned_data.get('cpnumber')

    if cpnumber:
      try:
        clients = Clients.objects.get(cpnumber=cpnumber)
      except Clients.DoesNotExist:
        self.add_error('cpnumber', '충전기번호가 없는 번호입니다.')
        return

      self.cpnumber = clients.id

class ClientsChangeAvailableForm(forms.Form):

  cpnumber = forms.CharField(
    error_messages={
      'required': '충전기번호를 입력하세요.'
    },
    max_length=64, label='충전기번호'
  )
  connector_id = forms.IntegerField(label='커넥터아이디')
  op_type = forms.CharField(max_length=32, label='충전기사용여부', help_text='Inoperative / operative')

  def clean(self):
    cleaned_data = super().clean()
    cpnumber = cleaned_data.get('cpnumber')

    if cpnumber:
      try:
        clients = Clients.objects.get(cpnumber=cpnumber)
      except Clients.DoesNotExist:
        self.add_error('cpnumber', '충전기번호가 없는 번호입니다.')
        return

      self.cpnumber = clients.id

class ClientsTriggerMessageForm(forms.Form):

  cpnumber = forms.CharField(
    error_messages={
      'required': '충전기번호를 입력하세요.'
    },
    max_length=64, label='충전기번호'
  )
  requested_message = forms.CharField(max_length=32, label='메세지이름')

  def clean(self):
    cleaned_data = super().clean()
    cpnumber = cleaned_data.get('cpnumber')

    if cpnumber:
      try:
        clients = Clients.objects.get(cpnumber=cpnumber)
      except Clients.DoesNotExist:
        self.add_error('cpnumber', '충전기번호가 없는 번호입니다.')
        return

      self.cpnumber = clients.id

class CompositeScheduleForm(forms.Form):
  cpnumber = forms.CharField(
    error_messages={
      'required': '충전기번호를 입력하세요.'
    },
    max_length=64, label='충전기번호'
  )
  connector_id = forms.IntegerField(label='커넥터번호')
  duration = forms.IntegerField(label='프로파일지속시간')

  def clean(self):
    cleaned_data = super().clean()
    cpnumber = cleaned_data.get('cpnumber')

    if cpnumber:
      try:
        clients = Clients.objects.get(cpnumber=cpnumber)
      except Clients.DoesNotExist:
        self.add_error('cpnumber', '충전기번호가 없는 번호입니다.')
        return

      self.cpnumber = clients.id

class ClearChargingProfileForm(forms.Form):
  cpnumber = forms.CharField(
    error_messages={
      'required': '충전기번호를 입력하세요.'
    },
    max_length=64, label='충전기번호'
  )
  connector_id = forms.IntegerField(label='커넥터번호')
  profile_id = forms.IntegerField(label='프로파일아이디')

  def clean(self):
    cleaned_data = super().clean()
    cpnumber = cleaned_data.get('cpnumber')

    if cpnumber:
      try:
        clients = Clients.objects.get(cpnumber=cpnumber)
      except Clients.DoesNotExist:
        self.add_error('cpnumber', '충전기번호가 없는 번호입니다.')
        return

      self.cpnumber = clients.id

# vendorId = "gresystem"
#   messageId = "uvStartCardRegMode"
#   msg = {
#     "memberId":userid,
#     "targetcp":cpnumber
#   }

class DataTransferForm(forms.Form):
  cpnumber = forms.CharField(
    error_messages={
      'required': '충전기번호를 입력하세요.'
    },
    max_length=64, label='충전기번호'
  )
  vendor_id = forms.CharField(max_length=32, label='제조사아이디')
  message_id = forms.CharField(max_length=32, label='메세지아이디')
  data = forms.CharField(
    max_length=256, label='데이터',
    help_text='[{"memberId": "userid", "targetCp": "cpnumber"}]'
  )

  def clean(self):
    cleaned_data = super().clean()
    cpnumber = cleaned_data.get('cpnumber')

    if cpnumber:
      try:
        clients = Clients.objects.get(cpnumber=cpnumber)
      except Clients.DoesNotExist:
        self.add_error('cpnumber', '충전기번호가 없는 번호입니다.')
        return

      self.cpnumber = clients.id

