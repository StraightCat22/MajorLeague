import pandas as pd

# 비교과 데이터 불러옴
data = pd.read_excel('nonsubject_test.xlsx')


# 앞 몇줄 확인
data.head()

data.loc[:,'이수여부']


# 이수여부가 미이수인 인덱스 추출, 삭제, 재정렬
noat = data[data['이수여부'].str.contains('미이수')].index
data.drop(noat, inplace=True)
data.reset_index(drop=True, inplace=True)


# 학번 별로 활동점수 합계 저장
result = data.groupby('ID',as_index=False).sum()

result['활동점수'][1]


# 300점이 넘으면 그냥 300점으로 환산하는 함수   
def score_re(x):
    if x >= 300:
        return 300
    else : return x
    
# 치환 함수 적용
result['활동점수'] = result['활동점수'].apply(score_re)


# 데이터 엑셀로 저장
result.to_csv('score.csv',index = True)


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


