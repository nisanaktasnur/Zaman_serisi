#  Zaman Serisi ile Tatil Sayısı Tahmin Projesi

Bu projede, Python ile zaman serisi analizi yapılarak aylık tatil sayılarının tahmini gerçekleştirilmiştir.

## Kullanılan Yöntemler ve Kütüphaneler

- **Pandas** – Veri işleme
- **Matplotlib** – Görselleştirme
- **Statsmodels** – SARIMA modeli

## Proje Özeti

- `holidays_events.csv` dosyasındaki tarih bilgileri ile aylık tatil sayısı hesaplandı.
- SARIMA(1,1,1)(1,1,1,12) modeli kurularak 12 aylık tahmin yapıldı.
- Tahmin sonuçları grafikle sunuldu.

## Kurulum

```bash
pip install -r requirements.txt
python zaman_serisi.py

