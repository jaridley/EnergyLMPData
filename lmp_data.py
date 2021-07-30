import pandas as pd_lmp

trade_date = '7/25/2021'
lmp_data = pd_lmp.read_csv('https://docs.misoenergy.org/marketreports/20210725_da_exante_lmp.csv', skiprows=4)
lmp_data.insert(3, 'Date', trade_date)

print(lmp_data.columns.values)
# print(lmp_data.dtypes)
print(lmp_data.head())
