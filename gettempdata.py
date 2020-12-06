import pandas as pd
import numpy as np
class get_temp_data():
    def __init__(self):
        self.tempdata=pd.read_csv("./data/temp.csv")[:]
        self.temp=pd.DataFrame()
        self.pdate={}
        self.avgtemp=pd.DataFrame()
        self.maxtemp=pd.DataFrame()
        self.mintemp=pd.DataFrame()
        self.datelist = list(self.tempdata['date'])
        self.avgtemplist = list(self.tempdata['avg_temp'])
        self.maxtemplist = list(self.tempdata['max_temp'])
        self.mintemplist = list(self.tempdata['min_temp'])
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
        
        
    def getavgtempdata(self):
        temp=[]
        for j in self.avgtemplist:
            temp.append(float(j))
        datelen=len(self.date2014)
        data2014 = pd.DataFrame(temp[:datelen],columns=['2014'],index=self.date2014)
        self.avgtemp=pd.concat([data2014],axis=1)
        datelen+=len(self.date2015)
        data2015 = pd.DataFrame(temp[datelen-len(self.date2015):datelen],columns=['2015'],index=self.date2015)
        self.avgtemp=pd.concat([self.avgtemp,data2015],axis=1)
        datelen+=len(self.date2016)
        data2016 = pd.DataFrame(temp[datelen-len(self.date2016):datelen],columns=['2016'],index=self.date2016)
        self.avgtemp=pd.concat([self.avgtemp,data2016],axis=1)
        datelen+=len(self.date2017)
        data2017 = pd.DataFrame(temp[datelen-len(self.date2017):datelen],columns=['2017'],index=self.date2017)
        self.avgtemp=pd.concat([self.avgtemp,data2017],axis=1)
        datelen+=len(self.date2018)
        data2018 = pd.DataFrame(temp[datelen-len(self.date2018):datelen],columns=['2018'],index=self.date2018)
        self.avgtemp=pd.concat([self.avgtemp,data2018],axis=1)
        datelen+=len(self.date2019)
        data2019 = pd.DataFrame(temp[datelen-len(self.date2019):datelen],columns=['2019'],index=self.date2019)
        self.avgtemp=pd.concat([self.avgtemp,data2019],axis=1)

    def getmaxtempdata(self):
        temp=[]
        for j in self.maxtemplist:
            temp.append(float(j))
        datelen=len(self.date2014)
        data2014 = pd.DataFrame(temp[:datelen],columns=['2014'],index=self.date2014)
        self.maxtemp=pd.concat([data2014],axis=1)
        datelen+=len(self.date2015)
        data2015 = pd.DataFrame(temp[datelen-len(self.date2015):datelen],columns=['2015'],index=self.date2015)
        self.maxtemp=pd.concat([self.maxtemp,data2015],axis=1)
        datelen+=len(self.date2016)
        data2016 = pd.DataFrame(temp[datelen-len(self.date2016):datelen],columns=['2016'],index=self.date2016)
        self.maxtemp=pd.concat([self.maxtemp,data2016],axis=1)
        datelen+=len(self.date2017)
        data2017 = pd.DataFrame(temp[datelen-len(self.date2017):datelen],columns=['2017'],index=self.date2017)
        self.maxtemp=pd.concat([self.maxtemp,data2017],axis=1)
        datelen+=len(self.date2018)
        data2018 = pd.DataFrame(temp[datelen-len(self.date2018):datelen],columns=['2018'],index=self.date2018)
        self.maxtemp=pd.concat([self.maxtemp,data2018],axis=1)
        datelen+=len(self.date2019)
        data2019 = pd.DataFrame(temp[datelen-len(self.date2019):datelen],columns=['2019'],index=self.date2019)
        self.maxtemp=pd.concat([self.maxtemp,data2019],axis=1)
    
    def getmintempdata(self):
        temp=[]
        for j in self.mintemplist:
            temp.append(float(j))
        datelen=len(self.date2014)
        data2014 = pd.DataFrame(temp[:datelen],columns=['2014'],index=self.date2014)
        self.mintemp=pd.concat([data2014],axis=1)
        datelen+=len(self.date2015)
        data2015 = pd.DataFrame(temp[datelen-len(self.date2015):datelen],columns=['2015'],index=self.date2015)
        self.mintemp=pd.concat([self.mintemp,data2015],axis=1)
        datelen+=len(self.date2016)
        data2016 = pd.DataFrame(temp[datelen-len(self.date2016):datelen],columns=['2016'],index=self.date2016)
        self.mintemp=pd.concat([self.mintemp,data2016],axis=1)
        datelen+=len(self.date2017)
        data2017 = pd.DataFrame(temp[datelen-len(self.date2017):datelen],columns=['2017'],index=self.date2017)
        self.mintemp=pd.concat([self.mintemp,data2017],axis=1)
        datelen+=len(self.date2018)
        data2018 = pd.DataFrame(temp[datelen-len(self.date2018):datelen],columns=['2018'],index=self.date2018)
        self.mintemp=pd.concat([self.mintemp,data2018],axis=1)
        datelen+=len(self.date2019)
        data2019 = pd.DataFrame(temp[datelen-len(self.date2019):datelen],columns=['2019'],index=self.date2019)
        self.mintemp=pd.concat([self.mintemp,data2019],axis=1)
        
    def tempinfo(self):
        self.getavgtempdata()
        self.getmaxtempdata()
        self.getmintempdata()
        self.avgtemp = self.avgtemp.sort_index()
        self.maxtemp = self.maxtemp.sort_index()
        self.mintemp = self.mintemp.sort_index()
        
if __name__ == "__main__":
    a = get_temp_data()
    a.tempinfo()
    print(a.mintemp['2019'])
    
