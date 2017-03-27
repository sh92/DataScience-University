import fitbit
import json
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('config.ini')
CLIENT_ID = config.get('ACCOUNT', 'CLIENT_ID')
CLIENT_SECRET = config.get('ACCOUNT', 'CLIENT_SECRET')
ACCESS_TOKEN = config.get('ACCOUNT','ACCESS_TOKEN')
REFRESH_TOKEN = config.get('ACCOUNT','REFRESH_TOKEN')

authd_client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET, access_token = ACCESS_TOKEN , refresh_token = REFRESH_TOKEN)

start_date = 12
end_date = 26


dir_name = 'step/'
for i in range(start_date, end_date+1):
    intraday_step = authd_client.intraday_time_series('activities/steps', base_date='2017-03-'+str(i), detail_level = '15min')
    with open(dir_name+'2017-03-'+str(i), 'w') as f:
        json.dump(intraday_step,f)
        f.flush()
    print(str(i)+' is finished')
