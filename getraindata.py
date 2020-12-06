import pandas as pd
import numpy as np
class get_rain_data():
    def __init__(self):
        self.raindata=pd.read_csv("./data/rain.csv")[1:-1]
        self.rain=pd.DataFrame()
        self.pdate={}
        self.datelist = list(self.raindata['date'])
        self.precipitationlist = list(self.raindata['precipitation(mm)'])
        self.precipitation = pd.DataFrame()
        self.date2019=[]
        self.date2018=[]
        self.date2017=[]
        self.date2016=[]
        self.date2015=[]
        self.date2014=[]
        
        for i in self.datelist:
            k=''
            if '2019' in i:
                k=i.replace('2019-','')
                self.date2019.append(k)
            elif '2018' in i:
                k=i.replace('2018-','')
                self.date2018.append(k)
            elif '2017' in i:
                k=i.replace('2017-','')
                self.date2017.append(k)
            elif '2016' in i:
                k=i.replace('2016-','')
                self.date2016.append(k)
            elif '2015' in i:
                k=i.replace('2015-','')
                self.date2015.append(k)
            elif '2014' in i:
                k=i.replace('2014-','')
                self.date2014.append(k)
        
        
    def getprecipitationdata(self):
        precipitation=[]
        for j in self.precipitationlist:
            precipitation.append(float(j))
        datelen=len(self.date2014)
        data2014 = pd.DataFrame(precipitation[:datelen],columns=['2014'],index=self.date2014)
        self.precipitation=pd.concat([data2014],axis=1)
        datelen+=len(self.date2015)
        data2015 = pd.DataFrame(precipitation[datelen-len(self.date2015):datelen],columns=['2015'],index=self.date2015)
        self.precipitation=pd.concat([self.precipitation,data2015],axis=1)
        datelen+=len(self.date2016)
        data2016 = pd.DataFrame(precipitation[datelen-len(self.date2016):datelen],columns=['2016'],index=self.date2016)
        self.precipitation=pd.concat([self.precipitation,data2016],axis=1)
        datelen+=len(self.date2017)
        data2017 = pd.DataFrame(precipitation[datelen-len(self.date2017):datelen],columns=['2017'],index=self.date2017)
        self.precipitation=pd.concat([self.precipitation,data2017],axis=1)
        datelen+=len(self.date2018)
        data2018 = pd.DataFrame(precipitation[datelen-len(self.date2018):datelen],columns=['2018'],index=self.date2018)
        self.precipitation=pd.concat([self.precipitation,data2018],axis=1)
        datelen+=len(self.date2019)
        data2019 = pd.DataFrame(precipitation[datelen-len(self.date2019):datelen],columns=['2019'],index=self.date2019)
        self.precipitation=pd.concat([self.precipitation,data2019],axis=1)
   
    def raininfo(self):
        self.getprecipitationdata()
        self.precipitation = self.precipitation.sort_index().fillna(0)
        
if __name__ == "__main__":
    a = get_rain_data()
    a.raininfo()
    print(a.precipitation)