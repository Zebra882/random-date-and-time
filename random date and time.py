import random
import time
def getRandomDate(startDate,endDate):
    #defining function
    print("printing random date between",startDate,"and",endDate)
    randomGenerator=random.random()
    dateFormat='%m/%d/%Y'
    startTime=time.mktime(time.strptime(startDate,dateFormat))
    endTime=time.mktime(time.strptime(endDate,dateFormat)) 
    randomTime=startTime+randomGenerator*(endTime-startTime)
    randomDate=time.strftime(dateFormat,time.localtime(randomTime))
    return randomDate
print("randomdate= ",getRandomDate("1/1/2015","12/12/2020"))
    