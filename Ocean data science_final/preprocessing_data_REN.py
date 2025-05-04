import pandas as pd
import numpy as np

# 事故データと波浪データを読み込む
accident_data = pd.read_csv('filtered_data.csv')  # 緯度、経度、時間、事故データを含む
wave_data = pd.read_csv('wave_parameters_all.csv')  # 緯度、経度、時間、MWP、MWD、SWHを含む

# 欠損値の行を削除
accident_data.dropna(inplace=True)
wave_data.dropna(inplace=True)

# 時間形式を変換して、日付のみを保持
accident_data['Time'] = pd.to_datetime(accident_data['Var7']).dt.date
wave_data['Time'] = pd.to_datetime(wave_data['Time']).dt.date

# 事故データの緯度と経度を波浪データに一致する形式に調整（0または0.5に丸める）
def round_to_nearest_half(x):
    return np.round(x * 2) / 2

accident_data['Latitude'] = accident_data['Latitude'].apply(round_to_nearest_half)
accident_data['Longitude'] = accident_data['Longitude'].apply(round_to_nearest_half)

# 波浪データに事故ラベルを初期化
wave_data['Accident'] = 0

# 事故データを波浪データに統合
for _, row in accident_data.iterrows():
    match = (wave_data['Latitude'] == row['Latitude']) & \
            (wave_data['Longitude'] == row['Longitude']) & \
            (wave_data['Time'] == row['Time'])
    wave_data.loc[match, 'Accident'] = 1

# 統合後のデータを確認
print(wave_data.head())

# 統合後のデータを保存
wave_data.to_csv('labeled_wave_data2.csv', index=False)
