import pandas as pd
from django.db import models
from icecream import ic
import pandas as pd

from admin.common.models import ValueObject,Reader,Printer
class CrimeCctvModel():
    vo  = ValueObject()
    reader = Reader()
    printer = Printer()

    def __init__(self):
        self.crime_columns = ['살인발생','강도발생','강간발생','절도발생','폭력발생']
        self.arrest_columns = ['살인검거','강도검거','강간검거','절도검거','폭력검거']
        self.crime_rate_columns = ['살인검거율','강도검거율','강간검거율','절도검거율','폭력검거율']

    def create_crime_model(self):
        generator = self.vo
        reader = self.reader

        generator.context ='admin/crime/data/'
        generator.fname = 'crime_in_Seoul'
        crime_file_name = reader.new_file(generator)
        #print(f'파일명:{crime_file_name}')
        crime_model = reader.csv(crime_file_name)
        #self.printer.dframe(crime_model)
        return crime_model


    def create_police_position(self):
        crime = self.create_crime_model()
        reader = self.reader
        station_names = []
        [station_names.append('서울'+str(name[:-1] + '경찰서')) for name in crime['관서명']]


        station_address = []
        station_lats = []
        station_lngs = []
        gmaps = reader.gmaps()
        for name in station_names:
            temp = gmaps.geocode(name, language='ko')
            station_address.append(temp[0].get('formatted_address'))
            temp_loc = temp[0].get('geometry')
            station_lats.append(temp_loc['location']['lat'])
            station_lngs.append(temp_loc['location']['lng'])
            print(f'name : {temp[0].get("formatted_address")}')
        gu_names = []
        for name in station_address:
            temp = name.split()
            gu_name = [gu for gu in temp if gu[-1] == '구'][0]
            print(f'구 이름: {gu_name}')
            gu_names.append(gu_name)
        crime['구별'] = gu_names
        # 금천경찰서는 관악구에 있어서 금천구로 변경
        print('==================================================')
        print(f"샘플 중 혜화서 정보 : {crime[crime['관서명'] == '혜화서']}")
        print(f"샘플 중 금천서 정보 : {crime[crime['관서명'] == '금천서']}")
        #crime.to_csv(self.vo.context+'new_data/police_positions.csv')

    def create_cctv_model(self):
        value = self.vo
        reader = self.reader
        printer = self.printer
        value.context ='admin/crime/data/'
        value.fname = 'CCTV_in_Seoul'
        cctv_file_name = reader.new_file(value)
        cctv_model = reader.csv(cctv_file_name)
        cctv_model.rename(columns={'기관명': '구별'}, inplace=True)
        printer.dframe(cctv_model)
        cctv_model.to_csv(self.vo.context + 'new_data/cctv_model.csv')
        return cctv_model

    def create_population_model(self):
        value = self.vo
        reader = self.reader
        printer = self.printer
        value.context = 'admin/crime/data/'
        value.fname = 'population_in_Seoul'
        population_file_name = reader.new_file(value)
        population_model = reader.xls(population_file_name,2,'B,D,G,J,N')
        population_model.rename(columns={population_model.columns[0]:'구별',
                                         population_model.columns[1]:'인구수',
                                         population_model.columns[2]:'한국인',
                                         population_model.columns[3]:'외국인',
                                         population_model.columns[4]:'고령자',}, inplace=True)
        population_model.drop([26], inplace=True)
        printer.dframe(population_model)
        population_model.to_csv(self.vo.context+'new_data/population_model.csv')
        return population_model
    def merge_cctv_pop(self):
        printer = self.printer
        cctv = self.create_cctv_model()
        pop = self.create_population_model()
        cctv_pop = pd.merge(cctv,pop)
        '''
         r이 -1.0과 -0.7 사이이면, 강한 음적 선형관계,
        r이 -0.7과 -0.3 사이이면, 뚜렷한 음적 선형관계,
        r이 -0.3과 -0.1 사이이면, 약한 음적 선형관계,
        r이 -0.1과 +0.1 사이이면, 거의 무시될 수 있는 선형관계,
        r이 +0.1과 +0.3 사이이면, 약한 양적 선형관계,
        r이 +0.3과 +0.7 사이이면, 뚜렷한 양적 선형관계,
        r이 +0.7과 +1.0 사이이면, 강한 양적 선형관계
        '''
        print('#'*100)
        ic(cctv_pop.corr())

        '''
                           소계    2013년도 이전   2014년    2015년     2016년    인구수     한국인     외국인     고령자
          소계           1.000000   0.862756  0.450062  0.624402  0.593398  0.306342  0.304287 -0.023786  0.255196
          2013년도 이전   0.862756   1.000000  0.121888  0.257748  0.355482  0.168177  0.163142  0.048973  0.105379
          2014년         0.450062   0.121888  1.000000  0.312842  0.415387  0.027040  0.025005  0.027325  0.010233
          2015년         0.624402   0.257748  0.312842  1.000000  0.513767  0.368912  0.363796  0.013301  0.372789
          2016년         0.593398   0.355482  0.415387  0.513767  1.000000  0.144959  0.145966 -0.042688  0.065784
          인구수          [0.306342]   0.168177  0.027040  0.368912  0.144959  1.000000  0.998061 -0.153371  0.932667
          한국인          [0.304287]   0.163142  0.025005  0.363796  0.145966  0.998061  1.000000 -0.214576  0.931636
          외국인         [-0.023786]  0.048973  0.027325  0.013301 -0.042688 -0.153371 -0.214576  1.000000 -0.155381
          고령자          [0.255196]   0.105379  0.010233  0.372789  0.065784  0.932667  0.931636 -0.155381  1.000000

        '''

        printer.dframe(cctv_pop)
        #cctv_pop.to_csv(f'{self.vo.context}' + 'new_data/merge_cctv_pop.csv')

    def crime_sum(self):
        printer = self.printer
        reader = self.reader
        vo = self.vo
        vo.context = 'admin/crime/data/new_data/'
        vo.fname = 'police_positions'
        crime_sum_name = reader.new_file(vo)
        crime_sum = reader.csv(crime_sum_name)


        gu_sum = crime_sum.groupby(['구별']).sum()
        gu_sum.drop(gu_sum.columns[0], axis=1 ,inplace=True)
        a = gu_sum.loc['강남구',['살인 발생','강도 발생','강간 발생']]

        #printer.dframe(gu_sum)
        '''
        구별,살인 발생,살인 검거,강도 발생,강도 검거,강간 발생,강간 검거,절도 발생,절도 검거,폭력 발생,폭력 검거
        강남구,13,10,21,18,449,349,3850,1650,4284,3705
        강동구,4,3,6,8,156,123,2366,789,2712,2248
        강북구,7,8,14,13,153,126,1434,618,2649,2348
        관악구,9,8,12,14,320,221,2706,827,3298,2642
        광진구,4,4,14,26,240,220,3026,1277,2625,2180
        구로구,8,6,15,11,281,164,2335,889,3007,2432
        금천구,3,4,6,6,151,122,1567,888,2054,1776
        노원구,10,10,7,7,197,121,2193,801,2723,2329
        도봉구,3,3,9,10,102,106,1063,478,1487,1303
        동대문구,5,5,13,13,173,146,1981,814,2548,2227
        동작구,5,5,9,5,285,139,1865,661,1910,1587
        마포구,8,8,14,10,294,247,2555,813,2983,2519
        서대문구,2,2,5,4,154,124,1812,738,2056,1711
        서초구,8,6,9,6,393,249,2635,1091,2399,2098
        성동구,4,4,9,8,126,119,1607,597,1612,1395
        성북구,5,5,5,4,150,124,1785,741,2209,1855
        송파구,11,10,13,10,220,178,3239,1129,3295,2786
        양천구,10,13,19,16,382,296,3986,1932,5716,4748
        영등포구,14,12,22,20,295,183,2964,978,3572,2961
        용산구,5,5,14,14,194,173,1557,587,2050,1704
        은평구,3,3,9,6,166,141,1914,711,2653,2306
        종로구,6,5,11,9,211,161,2184,837,2293,1931
        중구,3,2,9,6,170,111,2548,859,2224,1964
        중랑구,13,12,11,9,187,148,2135,829,2847,2407
        '''
        gu_sum.to_csv(f'{vo.context}' + 'test.csv')
        printer.dframe(a)













# Create your models here.
