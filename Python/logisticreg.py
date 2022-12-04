import pandas as pd

# 전처리 한 데이터 불러오기
filename = 'result.csv'
data = pd.read_csv(filename, encoding='utf-8')
data = data.drop(data.columns[0], axis=1)
data.head()

major = '사이버보안전공'

# 전공별 예측 모델
fn_1 = data[data['Rank1']==major]
fn_1['rank']=1
fn_1=fn_1.drop(columns=['Rank2','Rank3','Rank4','Rank5','Rank6','Rank7','Rank8','score2','score3','score4','score5','score6','score7','score8','total2','total3','total4','total5','total6','total7','total8'])

#fn_1.head()

fn_2 = data[(data['Rank2']==major)&(data['c_result']!=data['Rank1'])]
fn_2['rank']=2
fn_2=fn_2.drop(columns=['Rank1','Rank3','Rank4','Rank5','Rank6','Rank7','Rank8','score1','score3','score4','score5','score6','score7','score8','total1','total3','total4','total5','total6','total7','total8'])
fn_2.rename(columns = {'Rank2' : 'Rank1'}, inplace = True)
fn_2.rename(columns = {'score2' : 'score1'}, inplace = True)
fn_2.rename(columns = {'total2' : 'total1'}, inplace = True)
#fn_2.head()

fn_3 = data[(data['Rank3']==major)&(data['c_result']!=data['Rank1'])&(data['c_result']!=data['Rank2'])]
fn_3['rank']=3
fn_3=fn_3.drop(columns=['Rank1','Rank2','Rank4','Rank5','Rank6','Rank7','Rank8','score1','score2','score4','score5','score6','score7','score8','total1','total2','total4','total5','total6','total7','total8'])
fn_3.rename(columns = {'Rank3':'Rank1'}, inplace = True)
fn_3.rename(columns = {'score3' : 'score1'}, inplace = True)
fn_3.rename(columns = {'total3' : 'total1'}, inplace = True)
#fn_3.head()

fn = pd.concat([fn_1,fn_2,fn_3])
#fn.head(50)

# ID, Rank1, c_result, gradepoint, takepoint, total1 : features
fn_r = fn[['c_year','ID','c_result','score1','활동점수','gradepoint','takepoint','total1','rank']]
#fn_r.head(100)

# 선발결과 boolean으로 변경
fn_r.loc[(fn_r['c_result']==major), 'c_result']=1
fn_r.loc[(fn_r['c_result']!= 1), 'c_result']=0
fn_r['c_result'] = fn_r[['c_result']].apply(pd.to_numeric)
fn_r.rename(columns = {'활동점수' : 'mileage'}, inplace = True)

fn_r = fn_r.dropna(axis = 0)

fn_r.head(100)

# 결과 엑셀파일로 저장
fn_r.to_csv('cs.csv')
fn_r.to_csv('cs.xlsx')

features = fn_r[['score1','mileage','gradepoint','takepoint','total1',]]
result = fn_r['c_result']

# 학습, 테스트 세트 분리
from sklearn.model_selection import train_test_split
train_features, test_features, train_labels, test_labels = train_test_split(features, result)

# 데이터 정규화
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

train_features = scaler.fit_transform(train_features)
test_features = scaler.transform(test_features)

# 정확도
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(train_features, train_labels)

print(model.score(train_features, train_labels))

# 테스트 세트 확인
print(model.score(test_features, test_labels))

# 새로운 데이터 넣어서 예측
import numpy as np

# [전공탐색이수점수, 비교과 활동 점수, 평점평균, 이수학점, 총점, 지망순위]
kds = np.array([400, 300, 142, 150, 992, 2])

predict_major = np.array([kds])

# 새로운 데이터 스케일링
predict_major = scaler.transform(predict_major)

# 예측
print(model.predict(predict_major))