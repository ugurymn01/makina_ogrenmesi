# 💊 ABD Opioid Reçete ve Ölüm Analizi (Regression Model)

![Python](https://img.shields.io/badge/Python-3.x-blue) ![Data Science](https://img.shields.io/badge/Alan-Data_Science-purple) ![Status](https://img.shields.io/badge/Durum-Tamamlandı-green)

Bu proje, ABD'deki opioid reçete sayıları, yıllar ve ölüm oranları (Crude Rate) arasındaki ilişkiyi analiz etmek ve makine öğrenmesi yöntemleriyle geleceğe yönelik tahminlerde bulunmak amacıyla geliştirilmiştir.

---

## 🎯 Projenin Amacı
Halk sağlığını etkileyen önemli bir veri seti üzerinde çalışılarak:
1.  Yıllara göre reçete dağılımının incelenmesi.
2.  Hangi eyaletlerde ölüm oranlarının daha yüksek olduğunun görselleştirilmesi.
3.  **Reçete Sayısı** ve **Ölüm Oranları** arasındaki ilişkinin matematiksel olarak modellenmesi (Linear Regression).

---

## 📊 1. Veri Analizi ve Görselleştirme (EDA)

Veriyi anlamlandırmak için çeşitli görselleştirme teknikleri kullanılmıştır.

### 🔍 Değişkenler Arası İlişki (Korelasyon)
Hangi değişkenin diğeriyle bağlantılı olduğunu görmek için Isı Haritası (Heatmap) kullanılmıştır.

![Korelasyon Matrisi](ss1.png)
*(Yukarıdaki matriste görüldüğü üzere değişkenler arasındaki ilişki katsayıları renklerle ifade edilmiştir. Kırmızıya yakın renkler güçlü ilişkiyi temsil eder.)*

---

### 📈 Yıllara Göre Reçete Sayısı
Opioid reçetelerinin yıllar içindeki değişim trendi analiz edilmiştir.

![Yıl Bazlı Reçete](ss4.png)
*(Grafikte, reçete sayılarının belirli bir yıla kadar arttığı, sonrasında ise düşüş eğilimine girdiği gözlemlenmektedir.)*

---

### 🏙️ Eyaletlere Göre Ölüm Dağılımı
Hangi eyaletlerde ölümlerin daha yoğun olduğu analiz edilmiştir.

![Eyalet Bazlı Ölümler](ss2.png)
*(California, Florida ve New York gibi nüfusun yoğun olduğu eyaletlerde sayıların daha yüksek olduğu görülmektedir.)*

---

## 🤖 2. Makine Öğrenmesi Modeli (Linear Regression)

Veri seti içerisindeki **Reçete Sayısı** ve **Crude Rate (Ölüm Oranı)** arasındaki ilişki modellenmiştir.

* **Bağımsız Değişken (X):** Crude Rate
* **Hedef Değişken (y):** Reçete Sayısı (Prescriptions Dispensed)

Model eğitildikten sonra elde edilen regresyon doğrusu aşağıdadır:

![Regresyon Sonucu](ss3.png)

### 📝 Grafik Yorumu:
* **Kırmızı Çizgi:** Modelin öğrendiği trend çizgisidir (Best Fit Line).
* **Kırmızı Alan:** Güven aralığını temsil eder.
* Grafik, ölüm oranları (Crude Rate) ile dağıtılan reçete miktarı arasında **pozitif bir ilişki** olduğunu (biri artarken diğerinin de arttığını) göstermektedir.

---

## 💻 Kurulum ve Çalıştırma

Bu projeyi çalıştırmak için aşağıdaki kütüphanelerin yüklü olması gerekir:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
