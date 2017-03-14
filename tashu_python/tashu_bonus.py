# Using the magic encoding
# -*- coding: utf-8 -*-
import csv
from operator import itemgetter
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib
import numpy as np
import datetime
import pandas as pd

matplotlib.rc('font', family="AppleMyungjo")

def get_num_region(tashu_dict,station_dict):
    region_name = {}
    i=0
    for x in station_dict:
        region_name[x['번호']] = x['구별']
        i=i+1
    wordcount = {}

    for row in tashu_dict:
        rent = int(float(row['RENT_STATION']))
        rtn = int(float(row['RETURN_STATION']))
        
        if rent < 145:
            rent=str(rent)
            rent_region = region_name[rent]
            if rent_region not in wordcount:
                wordcount[rent_region] = 1
            else:
                wordcount[rent_region] +=1

        if rtn < 145:
            rtn = str(rtn)
            rtn_region = region_name[rtn]
            if rtn_region not in wordcount:
                wordcount[rtn_region] = 1
            else:
                wordcount[rtn_region] += 1 


    sorted_x = sorted(wordcount.items(), key = itemgetter(1), reverse=True)

    region = []
    count = []
    i=0
    for x in sorted_x:
        if i==10:
            break
        i=i+1
        region.append(x[0])
        count.append(x[1])
    fig, ax = plt.subplots()
    fig.suptitle('각 구별 이용 횟수 비교')
    ind = np.arange(len(count))
    width = 0.35
    rects1 = ax.bar(ind, count, width, color='r')
    ax.set_xticks(ind)
    ax.set_xticklabels(region)
    plt.show()

def get_station_per_region(tashu_dict,station_dict):
    s1 = set()
    station={}
    for row in station_dict:
        if row['구별'] not in station:
            station[row['구별']] = set(row['번호'])
        else:
            tmp = station[row['구별']]
            tmp.add(row['번호'])
            station[row['구별']] = tmp
    for k,v in station.items():
        station[k] = len(v)
        
    sorted_x = sorted(station.items(), key = itemgetter(1), reverse=True)

    i=0
    region = []
    count = []
    for x in sorted_x:
        if x == 10:
            break
        #region.append(station_en[x[0]])
        region.append(x[0])
        count.append(x[1])
    fig, ax = plt.subplots()
    fig.suptitle('각 구별 정류장 개수 비교')
    ind = np.arange(len(region))
    width = 0.35
    rects1 = ax.bar(ind,count, width, color='r')
    ax.set_xticks(ind)
    ax.set_xticklabels(region)
    plt.show()
    pass


def getDay(y,m,d):
    day = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    return day[datetime.date(y,m,d).weekday()]


def get_num_by_day(tashu_dict,station_dict):
    Month_count = {'MON':0,'TUE':0,'WED':0,'THU':0,'FRI':0,'SAT':0,'SUN':0}
    Day_seq = {'SUN':0,'MON':1,'TUE':2,'WED':3,'THU':4,'FRI':5,'SAT':6}

    for row in tashu_dict:
        rent = row['RENT_DATE']
        year = rent[:4]
        month = rent[4:6]
        th = rent[6:8]
        time = rent[8:]
        day= getDay(int(year),int(month),int(th))
        Month_count[day] = Month_count[day]+1
        rtn = row['RETURN_DATE']
        year = rtn[:4]
        month = rtn[4:6]
        th = rtn[6:8]
        time = rtn[8:]
        day= getDay(int(year),int(month),int(th))
        Month_count[day] = Month_count[day]+1
    day = []
    count = []
    cnt = [ 0 for i in range(len(Day_seq))]
    day = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    for k,v in Month_count.items():
        count.append(v)
        cnt[Day_seq[k]]=v


    fig, ax = plt.subplots()
    fig.suptitle('요일별 이용 횟수 비교')
    ind = np.arange(len(day))
    width = 0.35
    rects1 = ax.bar(ind,cnt, width, color='r')
    ax.set_xticks(ind)
    ax.set_xticklabels(day)
    plt.show()
    pass

def get_num_by_time(tashu_dict,station_dict):
    time_count={'00':0,'01':0,'02':0,'03':0,'04':0,'05':0,'06':0,'07':0,'08':0,'09':0,'10':0,'11':0,'12':0,'13':0,'14':0,'15':0,'16':0,'17':0,'18':0,'19':0,'20':0,'21':0,'22':0,'23':0}
    for row in tashu_dict:
        rent = row['RENT_DATE']
        year = rent[:4]
        month = rent[4:6]
        th = rent[6:8]
        time = rent[8:]
        time_count[time[:2]] = time_count[time[:2]] +1
        '''
        rtn = row['RETURN_DATE']
        year = rtn[:4]
        month = rtn[4:6]
        th = rtn[6:8]
        time = rtn[8:]
        rent_day = int(float(rent_day)) - int(float(rtn_day))
        print(datetime.date(int(year), int(month), int(th)))
        '''

    time = []
    count = []
    sorted_x = sorted(time_count.items(), key = itemgetter(0))
    for k,v in sorted_x:
        time.append(k)
        count.append(v)
        

    fig, ax = plt.subplots()
    fig.suptitle('시간별 이용 횟수 비교 ')
    ind = np.arange(len(time_count))
    width = 0.35
    rects1 = ax.bar(ind,count, width, color='r')
    ax.set_xticks(ind)
    ax.set_xticklabels(time)
    plt.show()
    pass

