import pandas as pd
import os

#다운로드받은 파일 읽어오기
rawair = pd.read_excel('C:/Users/woowahan/Downloads/여객_출발_시간표.xls')
print("초기파일",rawair.shape)

#운항되는 대표 항공편에 연계된 기타 항공사 제거
slave = rawair[rawair['CODESHARE'].str.contains('Slave')].index
rawair.drop(slave, inplace= True)
print("연계 항공편 제거",rawair.shape)

#불필요한 컬럼제거
rawair.drop(['운항편명','터미널','체크인 카운터','출발현황','CODESHARE'], axis=1, inplace=True)
print("불필요 컬럼 제거",rawair.shape)
rawair.reset_index(drop=True, inplace=True)


#서비스 가능 게이트 선별
con1 = 11 < rawair['탑승구'] 
con2 = rawair['탑승구'] < 25
con3 = 29 < rawair['탑승구']
con4 = rawair['탑승구'] < 42
conair = rawair.loc[(con1 & con2) | (con3 & con4)]

print("서비스 구역 선별",conair.shape)

conair=conair.reset_index(drop=True)
conair.index=conair.index+1
conair.to_excel('C:/Users/woowahan/Desktop/딜리.xlsx')
print('바탕화면에 엑실파일 저장!')

os.remove('C:/Users/woowahan/Downloads/여객_출발_시간표.xls')
print('다운받은 원본 파일 삭제!')