import fitbit
import json
import ConfigParser
import datetime

config = ConfigParser.RawConfigParser()
config.read('config.ini')
CLIENT_ID = config.get('ACCOUNT', 'CLIENT_ID')
CLIENT_SECRET = config.get('ACCOUNT', 'CLIENT_SECRET')
ACCESS_TOKEN = config.get('ACCOUNT','ACCESS_TOKEN')
REFRESH_TOKEN = config.get('ACCOUNT','REFRESH_TOKEN')

authd_client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET, access_token = ACCESS_TOKEN , refresh_token = REFRESH_TOKEN)

start_date = 12
end_date = 24

#intraday_heart = authd_client.intraday_time_series('activities/heart', base_date    = '2017-03-22', detail_level = '1sec', start_time   = None, end_time = None)
#intraday_activity = authd_client.intraday_time_series('activities/activities', base_date    = '2017-03-22', detail_level = '15min', start_time   = None, end_time = None)

dir_name = 'sleep/'
for i in range(start_date, end_date+1):
    intraday_sleep= authd_client.get_sleep(datetime.date(2017,03,i))
    with open(dir_name+'2017-03-'+str(i), 'w') as f:
        json.dump(intraday_sleep,f)
        f.flush()
    print(str(i)+' is finished')

date_string = '201703'+str(i)+'000000'
date = datetime.datetime.strptime(date_string, '%Y%m%d%H%M%S')
start_time = date.strftime('%H:%M')
duration = 240000*11
with open('sleep_log','w') as f:
    json.dump(authd_client.log_sleep(date,duration),f)
    f.fush()
print("finish sleeplog")
