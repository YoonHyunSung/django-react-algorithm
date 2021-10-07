from django.db import models
from admin.common.models import DFrameGenerator,Reader,Printer
class CrimeCctvModel():
    generator  = DFrameGenerator()
    reader = Reader()
    printer = Printer()

    def __init__(self):

        self.crime_columns = ['살인발생','강도발생','강간발생','절도발생','폭력발생']
        self.arrest_columns = ['살인검거','강도검거','강간검거','절도검거','폭력검거']
        self.crime_rate_columns = ['살인검거율','강도검거율','강간검거율','절도검거율','폭력검거율']

    def create_crime_model(self):
        generator = self.generator
        reader = self.reader
        printer = self.printer

        generator.context ='admin/crime/data/'
        generator.fname = 'crime_in_Seoul'
        crime_file_name = reader.new_file(generator)
        print(f'파일명:{crime_file_name}')
        crime_model = reader.csv(crime_file_name)
        printer.dframe(crime_model)
        return crime_model

    def create_police_position(self):
        crime = self.create_crime_model()
        reader = self.reader
        station_names = []
        for name in crime['관서명']:
            station_names.append('서울'+str(name[:-1] + '경찰서'))
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
        crime.to_csv(self.generator.context+'new_data/police_positions.csv')









# Create your models here.
