import pandas as pd

# 학적파일 불러오기
DF_univ = pd.read_excel('학적테이블_조회기준일(20221016).xlsx', engine = "openpyxl")
print(DF_univ)

# 22년 제적 학번 삭제
index_univ = DF_univ[(DF_univ['입학학년도'] == 2022)
                & (DF_univ['학적상태(조회기준일)'] == '제적') ].index
DF_univ.drop(index_univ, inplace=True)

# 성적파일 불러오기 
DF_grade= pd.read_excel('성적테이블_조회기준일(20221016).xlsx', engine = "openpyxl")
print(DF_grade)

# 학적파일과 성적파일 학번 기준 merge  
total = pd.merge(DF_univ, DF_grade, on="ID", how = "inner")
total.to_excel('total.xlsx', index=False)

# 일학년 성적만 남기기 ( 입학년도 2020- 학년도 2020, 2021- 2021, 2022-2022 )
total = total[  (total['입학학년도']==2020) &  (total['학년도']==2020)  | (total['입학학년도']==2021) &  (total['학년도']==2021) | (total['입학학년도']==2022) &  (total['학년도']==2022)]   # total.to_excel('total2.xlsx', index=False) #테스트 - 데이터프레임엔 값 안나오는데 엑셀엔 잘 나옴

# id별 평균값 구하기
meanscore = pd.DataFrame(total.groupby("ID")['평균점수(평균)'].mean())
score = pd.DataFrame(total[['ID','대학','학과(전공)', '입학학년도']])
score = score.drop_duplicates() # 중복행 제거
finalscore = pd.merge(score, meanscore, on="ID", how = "inner") # meanscore 컬럼 더하기  
#finalscore.to_excel('finalscore.xlsx', index=False)
# 성적 계산 식 = 평균평점 *1.5 
gradepoint = finalscore['평균점수(평균)']*(1.5)
finalscore['gradepoint'] = gradepoint
finalscore.to_excel('평점평균.xlsx', index=False)
    
#입학학년도 22학번 삭제
finalscore = finalscore[finalscore.입학학년도 != 2022]
finalscore.to_excel('평점평균.xlsx', index=False)
