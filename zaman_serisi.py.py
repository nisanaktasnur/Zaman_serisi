import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX

# Veri setini yükleme
data = pd.read_csv('holidays_events.csv')
data['date'] = pd.to_datetime(data['date'])
data = data.sort_values('date')
data.set_index('date', inplace=True)

# Eksik veri kontrolü
print("Eksik veri kontrolü:")
print(data.isnull().sum())

# Aylık tatil sayısını hesaplama
monthly_holidays = data.resample('M').size()

# Görselleştirme
plt.figure(figsize=(10, 6))
monthly_holidays.plot(kind='bar', color='skyblue')
plt.title('Aylara Göre Tatil Sayısı')
plt.xlabel('Aylar')
plt.ylabel('Tatil Sayısı')
plt.xticks(rotation=45)
plt.show()

# SARIMA modeli
model = SARIMAX(monthly_holidays, order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
results = model.fit()
print(results.summary())

# Geleceğe yönelik tahmin
forecast = results.get_forecast(steps=12)
forecast_values = forecast.predicted_mean
future_dates = pd.date_range(start=monthly_holidays.index[-1] + pd.DateOffset(months=1), periods=12, freq='M')
forecast_series = pd.Series(forecast_values.values, index=future_dates)

# Tahmin görselleştirme
plt.figure(figsize=(10, 6))
plt.plot(monthly_holidays, label='Gerçek Tatil Sayıları')
plt.plot(forecast_series, label='Tahmin', linestyle='--')
plt.title('12 Aylık Tatil Sayısı Tahmini')
plt.xlabel('Zaman')
plt.ylabel('Tatil Sayısı')
plt.legend()
plt.show()
