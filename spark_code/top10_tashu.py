from pyspark import SparkContext
import pandas as pd
import numpy as np

sc = SparkContext()


def getTop10Station(filePath):
    lines = sc.textFile(filePath,1)
    frequencies = lines.flatMap(lambda x: x.split(' ')).map(lambda x:(x,1)).reduceByKey(lambda x,y: x+y)
    top10 = frequencies.takeOrdered(10)
    return top10

def save_rentStation(data):
    result = list(data['RETURN_STATION'])
    with open('return_station.csv','w') as f:
        for item in result:
            if np.isnan(item):
                 continue
            f.write(str(int(item))+ ',')
            f.write('\n')

if __name__ == "__main__":
    directory = "../../data/1/"
    fileName = "tashu.csv"

    data =  pd.read_csv(directory + fileName)
    save_rentStation(data)

    saveFileName = "return_station.csv"
    filePath = saveFileName
    top10 = []
    top10 = getTop10Station(filePath)
    print(top10)
