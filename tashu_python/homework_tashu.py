# Using the magic encoding
# -*- coding: utf-8 -*-
import csv
from operator import itemgetter
import matplotlib.pyplot as plt
import numpy as np

def get_top10_station(tashu_dict, station_dict):
    """
    [역할]
    정류장 Top10 출력하기
    대여 정류장과 반납정류장을 합한 총 사용빈도수 Top10

    [입력]
    tashu_dict : csv.DictReader 형태의 타슈대여정보
    station_dict : csv.DictReader 형태의 정류장 정보

    [출력]
    Top10 정류장 리스트
    ex.) [[정류장 이름1, 정류장 번호1, 정류장1 count], [정류장 이름2, 정류장 번호2, 정류장2 count], .....] 형태
    """
    station_count={}
    for row in tashu_dict:
        rent= row['RENT_STATION']
        rtn= row['RETURN_STATION']
        if rent not in station_count:
            station_count[rent] = 1
        else:
            station_count[rent] += 1

        if rtn not in station_count:
            station_count[rtn] = 1
        else:
            station_count[rtn] += 1
    sorted_x = sorted(station_count.items(), key = itemgetter(1), reverse=True)

    station_name = {}
    for x in station_dict:
        station_name[x['번호']] = x['명칭']

    ans = []
    i=0
    for x in sorted_x:
        if i==10:
            break
        i=i+1
        no = str(int(float(x[0])))
        count = int(x[1])
        name = station_name[no]
        ans.append([name,no,count])
    return ans

def get_top10_trace(tashu_dict, station_dict):
    """
    [역할]
    경로 Top10 출력하기
    (대여정류장, 반납정류장)의 빈도수 Top10

    [입력]
    tashu_dict : csv.DictReader 형태의 타슈대여정보
    station_dict : csv.DictReader 형태의 정류장 정보

    [출력]
    Top10 경로 리스트
    ex.) [[출발정류장 이름1, 출발정류장 번호1, 반납정류장 이름1,
        반납정류장 번호2, 경로 count], [출발정류장 이름2, 출발정류장 번호2,
        반납정류장 이름2,  반납정류장 번호2, 경로count2], .....] 형태
    """
    station_name = {}
    for x in station_dict:
        station_name[x['번호']] = x['명칭']

    station_count = {}
    for row in tashu_dict:
        rent = row['RENT_STATION']
        rtn = row['RETURN_STATION']
        if (rent,rtn) not in station_count:
            station_count[(rent,rtn)] = 1
        else:
            station_count[(rent,rtn)] += 1
    sorted_x = sorted(station_count.items(), key = itemgetter(1), reverse=True)
    i=0
    ans = []
    for x in sorted_x:
        if i==10:
            break
        i=i+1
        rent_no = str(int(float(x[0][0])))
        rtn_no = str(int(float(x[0][1])))
        count = int(x[1])
        rent_name = station_name[rent_no]
        rtn_name = station_name[rtn_no]
        ans.append([rent_name,rent_no,rtn_name,rtn_no,count])
    return ans

