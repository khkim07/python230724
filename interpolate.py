#interpolate.py
import pandas as pd

#print( dir() )

# 원본 데이터프레임 생성 (일부 값이 결측치)
data = {'A': [1, 2, None, None, 5],
        'B': [None, 6, 7, None, 9]}
df = pd.DataFrame(data)

# 선형 보간을 적용하여 결측치를 채우기 (기본적으로 선형 보간이 적용됨)
df_interpolated = df.interpolate()

print("원본 데이터프레임:")
print(df)
print("\n선형 보간이 적용된 데이터프레임:")
print(df_interpolated)

# 스플라인 보간을 적용하여 결측치를 채우기
# df_spline_interpolated = df.interpolate(method='spline')

# print("스플라인 보간이 적용된 데이터프레임:")
# print(df_spline_interpolated)