# 🧠 Makine Öğrenmesi ile Tahmin Modeli (Linear Regression)

![Python](https://img.shields.io/badge/Python-3.x-blue) ![Jupyter](https://img.shields.io/badge/Notebook-Jupyter-orange) ![Status](https://img.shields.io/badge/Durum-Tamamlandı-green)

Bu proje, veri bilimi teknikleri kullanılarak **bağımsız bir değişkenin (Örn: Metrekare, Deneyim)** hedef değişken üzerindeki **(Örn: Fiyat, Maaş)** etkisini analiz etmek ve geleceğe yönelik tahminlerde bulunmak amacıyla geliştirilmiştir.

Dosya: `Untitled.ipynb`

---

## 🎯 Projenin Amacı ve Kapsamı
Bu çalışmanın temel amacı, eldeki ham veriyi işleyerek makinenin matematiksel bir desen (pattern) yakalamasını sağlamaktır. 
**Basit Doğrusal Regresyon (Simple Linear Regression)** algoritması seçilmiştir çünkü:
1.  Veri setimizdeki değişkenler arasında doğrusal bir ilişki (biri artarken diğerinin de artması/azalması) vardır.
2.  Sonuçların yorumlanması ve açıklanması (Explainability) en net olan modeldir.

---

## 📊 1. Veri Analizi ve Değişken Seçimi (EDA)

Modeli körü körüne eğitmek yerine, önce veriyi anlamlandırdık.

### 🔍 Neden Bu Değişkenleri Seçtik?
Veri setindeki tüm sütunları modele dahil etmek, "gürültü" (noise) yaratarak tahmin başarısını düşürebilir. Bu yüzden **Korelasyon Analizi** yaptık.
* **Analiz Sonucu:** Hedef değişkenimiz (Y) ile en yüksek korelasyona (ilişkiye) sahip olan değişken (X) tespit edildi ve modelin girdisi olarak seçildi.
* **Diğer Değişkenler:** İlişkisi zayıf olan veya sayısal olmayan (kategorik) veriler, modelin sapmasını önlemek adına temizlendi.

*(Buraya arkadaşın da senin gibi Isı Haritası veya Dağılım grafiği eklerse süper olur)*
`![Veri Analizi Grafiği](grafik_adi.png)`

---

## 🧹 2. Veri Ön İşleme (Preprocessing)

Ham veri, makine öğrenmesi için doğrudan uygun değildir. Şu adımlar uygulanarak veri "temiz" hale getirilmiştir:

1.  **Eksik Veri (Null) Temizliği:** * Veri setindeki boş hücreler `.dropna()` yöntemi ile kaldırıldı. Çünkü boş veriler modelin matematiksel hesaplama yaparken hata vermesine neden olur.
2.  **Veri Ayrımı (Train/Test Split):**
    * Verinin tamamıyla eğitim yapılmadı. **%80 Eğitim, %20 Test** olarak ayrıldı.
    * **Neden?** Makinenin veriyi ezberlemesini (Overfitting) önlemek ve hiç görmediği verilerle karşılaştığında ne kadar başarılı olduğunu objektif ölçmek için.

---

## 🤖 3. Modelleme ve Eğitim

Scikit-Learn kütüphanesi kullanılarak **LinearRegression** modeli kuruldu.

* **Mantık:** Makine, eğitim verilerine bakarak noktaların en iyi temsil edildiği **"Regresyon Doğrusunu" (Best Fit Line)** çizdi.
* **Formül:** `y = mx + b` (Eğim ve Kesişim noktaları hesaplandı).

---

## 📈 4. Sonuçlar ve Performans Değerlendirmesi

Modelin başarısı, ayırdığımız test verileri üzerinde ölçüldü.

### 📝 Grafik Yorumu
Regresyon grafiğimizde, modelin çizdiği **tahmin çizgisinin**, gerçek verilerin (noktaların) genel eğilimini takip ettiği görülmüştür. Bu durum, modelin başarılı bir genelleme yaptığını kanıtlar.

### 🏆 Başarı Kriterleri
* **R2 Skoru:** Modelin, verideki değişkenliği ne kadar açıklayabildiğini gösterir.
* **MSE (Ortalama Kare Hata):** Tahminlerin gerçek değerlerden ne kadar saptığını gösterir. (Düşük olması iyidir).

*(Buraya Kırmızı Çizgili Sonuç grafiğini ekleyebilir)*
`![Sonuç Grafiği](sonuc_grafigi.png)`

---

## 💻 Kurulum

Projeyi çalıştırmak için aşağıdaki kütüphanelerin yüklü olması gerekmektedir:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
