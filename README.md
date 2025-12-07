# ABD Opioid Reçete ve Ölüm Oranları Üzerine Regresyon Analizi

Bu proje, ABD’deki opioid reçete sayıları, yıllar ve eyaletlere göre ölüm oranları arasındaki ilişkiyi incelemek, veriyi temizlemek ve Lineer Regresyon modeli ile tahmin yapmak amacıyla hazırlanmıştır.

---

## 1. Kullanılan Veri Seti

Projede kullanılan veri seti (datam.csv) aşağıdaki değişkenleri içermektedir:

- Year: Yıl bilgisi  
- State: Eyalet  
- Prescriptions Dispensed by US Retailers in that year (millions): O yıl dağıtılan reçete sayısı  
- Deaths: İlgili yıldaki ölüm sayısı  
- Crude Rate: 100.000 kişi başına düşen ölüm oranı  

---

## 2. Veri Temizleme Süreci

### Eksik Değer Kontrolü
- Veri seti yüklendikten sonra eksik değer analizi yapılmıştır.  
- NaN veya boş değer içeren satırlar temizlenmiştir.

### Veri Tiplerinin Düzenlenmesi
- Sayısal değişkenlerin veri tipleri kontrol edilmiştir.  
- Yanlış formatlı değerler uygun tiplere dönüştürülmüştür.

### Hatalı / Tutarsız Değerlerin Düzeltilmesi
- Negatif veya mantık dışı değerler analiz edilmiştir.  
- Veri bütünlüğünü bozan satırlar çıkarılmıştır.

### Analize Hazırlama
- Modelde bağımsız değişken (X) Crude Rate olarak seçilmiştir.  
- Modelde bağımlı değişken (y) Prescriptions Dispensed olarak belirlenmiştir.

---

## 3. Projenin Amacı ve Tahmin Edilen Değer

Bu çalışmada:

Yıllara göre reçete sayılarının değişimi incelenmiştir.  
Eyaletlerdeki ölüm oranları analiz edilmiştir.  
Crude Rate ile reçete sayısı arasındaki ilişki değerlendirilmiştir.  
Lineer Regresyon modeliyle reçete tahmini yapılmıştır.  

**Tahmin edilen değer (y):** Prescriptions  
**Bağımsız değişken (X):** Crude Rate  

---

## 4. Kullanılan Makine Öğrenmesi Modeli

Projede Linear Regression modeli kullanılmıştır.

Model adımları:

1. Adım = X ve y değişkenlerinin seçilmesi  
2. Adım = Eğitim-test ayrımı yapılması  
3. Adım = Modelin eğitilmesi  
4. Adım = Tahminlerin üretilmesi  
5. Adım = Gerçek ve tahmini değerlerin karşılaştırılması  

---

## 5. Veri Analizi ve Görselleştirmeler

Bu bölümde Jupyter Notebook’taki beş grafik yer almaktadır.  

---

### 5.1 Yıllara Göre Reçete Sayısı Trend Grafiği
![tablo](ss1.png)

---

### 5.2 Eyaletlere Göre Ortalama Ölüm Sayısı
![tablo](ss2.png)
---

### 5.3 Korelasyon Matrisi
![tablo](ss3.png)

---

### 5.4 Gerçek ve Tahmin Değer Karşılaştırma Grafiği
![tablo](ss5.png)

---

### 5.5 Crude Rate ve Prescriptions Arasındaki Regresyon Grafiği
![tablo](ss4.png)

---

## 6. Model Performans Metrikleri

Notebook içerisinde hesaplanan değerlendirme metrikleri:

- **R² Skoru:** Modelin açıklayıcılık oranını gösterir.  
- **RMSE (Root Mean Squared Error):** Tahminlerin ortalama hata büyüklüğünü gösterir.  

---

