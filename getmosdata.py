import pandas as pd

class get_mos_data():
    def __init__(self):
        self.mos2019data=pd.read_csv("./data/mos-20191.csv")[:]
        self.mos2018data=pd.read_csv("./data/mos-2018.csv")[:]
        self.mos2017data=pd.read_csv("./data/mos-2017.csv")[:]
        self.mos2016data=pd.read_csv("./data/mos-2016.csv")[:]
        self.mos2015data=pd.read_csv("./data/mos-2015.csv")[:]
        self.mos=pd.DataFrame()
        self.pdate={}
    def mosinfo2019(self):
        mos2019datelist = list(self.mos2019data['date'])
        mos2019moslist = list(self.mos2019data['mosnum'])
        mos2019date=[]
        for i in mos2019datelist:
            k=i.replace('2019-','')
            mos2019date.append(k)
        mosmos=[]
        for j in mos2019moslist:
            h = j.replace(',','')
            mosmos.append(int(h))
        mos2019 = pd.DataFrame(mosmos,columns=['2019'],index=mos2019date)
        self.mos=pd.concat([mos2019],axis=1)
    def mosinfo2018(self):
        mosdatelist = list(self.mos2018data['date'])
        mosmoslist = list(self.mos2018data['mosnum'])
        mosdate=[]
        for i in mosdatelist:
            k=i.replace('2018-','')
            mosdate.append(k)
        mosmos=[]
        for j in mosmoslist:
            h = j.replace(',','')
            mosmos.append(int(h))
        mos2018 = pd.DataFrame(mosmos,columns=['2018'],index=mosdate)
        self.mos=pd.concat([self.mos,mos2018],join='outer',axis=1)
    def mosinfo2017(self):
        mosdatelist = list(self.mos2017data['date'])
        mosmoslist = list(self.mos2017data['mosnum'])
        mosdate=[]
        for i in mosdatelist:
            k=i.replace('2017-','')
            mosdate.append(k)
        mosmos=[]
        for j in mosmoslist:
            h = j.replace(',','')
            mosmos.append(int(h))
        mos2017 = pd.DataFrame(mosmos,columns=['2017'],index=mosdate)
        self.mos=pd.concat([self.mos,mos2017],join='outer',axis=1)
    def mosinfo2016(self):
        mosdatelist = list(self.mos2016data['date'])
        mosmoslist = list(self.mos2016data['mosnum'])
        mosdate=[]
        for i in mosdatelist:
            k=i.replace('2016-','')
            mosdate.append(k)
        mosmos=[]
        for j in mosmoslist:
            h = j.replace(',','')
            mosmos.append(int(h))
        mos2016 = pd.DataFrame(mosmos,columns=['2016'],index=mosdate)
        self.mos=pd.concat([self.mos,mos2016],join='outer',axis=1)
    def mosinfo2015(self):
        mosdatelist = list(self.mos2015data['date'])
        mosmoslist = list(self.mos2015data['mosnum'])
        mosdate=[]
        for i in mosdatelist:
            k=i.replace('2015-','')
            mosdate.append(k)
        mosmos=[]
        for j in mosmoslist:
            h = j.replace(',','')
            mosmos.append(int(h))
        mos2015 = pd.DataFrame(mosmos,columns=['2015'],index=mosdate)
        self.mos=pd.concat([self.mos,mos2015],axis=1)
    def mosinfo(self):
        self.mosinfo2019()
        self.mosinfo2018()
        self.mosinfo2017()
        self.mosinfo2016()
        self.mosinfo2015()
        self.mos = self.mos.sort_index()
if __name__ == "__main__":
    a=get_mos_data()
    a.mosinfo()
    
    print(a.mos)
    

