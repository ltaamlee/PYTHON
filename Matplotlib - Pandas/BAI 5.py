import pandas as pd

data = pd.read_table('wind.data', delim_whitespace=True)

data['Yr'] = data['Yr'] + 1900
data['yyyy_MM_dd'] = pd.to_datetime(data[['Yr', 'Mo', 'Dy']].astype(str).agg('-'.join, axis=1))
print("a/ Hop nhat 3 cot dau tien thanh mot cot ngay thang voi dinh dang yyyy_MM_dd: ");
data_display = data.drop(['Yr', 'Mo', 'Dy'], axis=1)
data_display = data_display[['yyyy_MM_dd'] + [col for col in data_display.columns if col != 'yyyy_MM_dd']]
print(data_display.head())

del data_display

data.set_index('yyyy_MM_dd', inplace=True)

data_info = data.loc[:, 'RPT':'MAL'].describe().T
data_info['So_luong_hien_co'] = data_info['count']
data_info['So_luong_thieu'] = data.shape[0] - data_info['count']
print("So luong gia tri hien co va con thieu o cac cot tu RPT den MAL:")
print(data_info[['So_luong_hien_co', 'So_luong_thieu']])
print()

average_wind_speed = data.loc[:, 'RPT':'MAL'].mean().mean()
print(f"Toc do gio trung binh cho toan bo du lieu: {average_wind_speed:.2f} m/s")
print()

loc_stats = data.loc[:, 'RPT':'MAL'].agg(['min', 'max', 'mean', 'std'])
loc_stats.rename(index={
    'min': 'Toi thieu',
    'max': 'Toi da',
    'mean': 'Trung binh',
    'std': 'Do lech chuan'
}, inplace=True)
print("Thong ke toc do gio tai moi vi tri::")
print(loc_stats)
print()

january_avg = data[data.index.month == 1].loc[:, 'RPT':'MAL'].mean()
print("Toc do gio trung binh trong thang 1 o moi noi:")
print(january_avg)
print()

annual_stats = data.resample('YE').mean()
print("Thong ke hang nam:")
print(annual_stats.head())
print()

monthly_yearly_stats = data.resample('ME').mean()
print("Thong ke hang thang - nam:")
print(monthly_yearly_stats.head())
print()

weekly_monthly_yearly_stats = data.resample('W').mean()  
print("\nThong ke hang tuan - thang - nam:")
print(weekly_monthly_yearly_stats.head())