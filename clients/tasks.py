from datetime import datetime, timedelta

from celery import shared_task

from clients.models import Clients

@shared_task(bind=True)
def cp_status_check(self): 
    query_lists = Clients.objects.all()

    for cpinfo in query_lists:
        queryset = Clients.objects.filter(cpnumber=cpinfo).values()
        last_updated = queryset[0]['check_dttm'].replace(tzinfo=None) + timedelta(hours=9)
        current_time = datetime.now()
        timegap = current_time - last_updated
        if queryset[0]['cpstatus'] == '정상':
            if timegap.seconds > 600:
                Clients.objects.filter(cpnumber=cpinfo).update(cpstatus="통신장애", check_dttm=current_time)    # 통신이상
        elif queryset[0]['cpstatus'] == '통신장애':
            if timegap.seconds > 3600:
                Clients.objects.filter(cpnumber=cpinfo).update(cpstatus="충전기장애", check_dttm=current_time)    # 충전기장애
            # print('================================================================')
            # print('last_updated: {}, current_time: {}, timegap: {}'.format(last_updated, current_time, timegap))
            # print('================================================================')
        else:
            pass

    return 'Done'
