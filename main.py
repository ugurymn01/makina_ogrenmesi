
# 0-KÜTÜPHANELER KISMI(yüklemeleri yapıldı)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

plt.style.use("ggplot")



# 1) datam.csv
df = pd.read_csv(r"C:\Users\YAMAN\Desktop\data\data\datam.csv")

# 2) eksik ve bozuk veri temizleme kısmı
df = df.drop(columns=["index"], errors="ignore")

numeric_cols = [
    "Deaths",
    "Crude Rate",
    "Crude Rate Lower 95% Confidence Interval",
    "Crude Rate Upper 95% Confidence Interval"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col].str.replace(",", "."), errors='coerce')
    df[col].fillna(df[col].median(), inplace=True)

# 3) x ve y seçimi yaptım, dağılım grafiği
y = df["Prescriptions Dispensed by US Retailers in that year (millions)"]

X = df[[
    "Year",
    "Population",
    "Deaths",
    "Crude Rate",
    "Crude Rate Lower 95% Confidence Interval",
    "Crude Rate Upper 95% Confidence Interval"
]]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4) linear regression modeli oluşturdum ve eğittim
model = LinearRegression() #modeli import ettim
model.fit(X_train, y_train) #modeli eğittik
y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R^2 Score: {r2:.2f}")

# 5) GÖRSELLEŞTİRME

# 5.1) Yılın trendi grafiği
plt.figure(figsize=(12,10))
sns.lineplot(data=df, x="Year", y="Prescriptions Dispensed by US Retailers in that year (millions)", ci=None)
plt.title("Yıl bazlı reçete sayısı trendi")
plt.ylabel("Reçeteler (milyonlar)")
plt.xlabel("Yıl")
plt.tight_layout()
plt.show()


# 5.2) Eyalet bazlı ortalama ölüm grafiği
plt.figure(figsize=(12,10))
state_deaths = df.groupby("State")["Deaths"].mean().sort_values(ascending=False)
sns.barplot(x=state_deaths.values, y=state_deaths.index)
plt.title("Eyaletlere göre ortalama ölümler")
plt.xlabel("Ortalama Ölümler")
plt.ylabel("Eyalet")
plt.tight_layout()
plt.show()


# 5.3) Korelasyon matris grafiği
plt.figure(figsize=(12,10))
corr = df[[
    "Year", "Population", "Deaths", "Crude Rate",
    "Crude Rate Lower 95% Confidence Interval",
    "Crude Rate Upper 95% Confidence Interval",
    "Prescriptions Dispensed by US Retailers in that year (millions)"
]].corr()

sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Özellikler arası korelasyon matrisi")
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()

# 5.4) Population vs Prescriptions
plt.figure(figsize=(8,6))
sns.regplot(x='Population', y='Prescriptions Dispensed by US Retailers in that year (millions)', data=df)
plt.title('Population vs Prescriptions with Regression Line')
plt.xlabel('Population')
plt.ylabel('Prescriptions (millions)')
plt.tight_layout()
plt.show()


# 5.5) Crude Rate vs Prescriptions (Gerçek vs Tahmin)
plt.figure(figsize=(8,6))
sns.regplot(
    x=X_test['Crude Rate'], 
    y=y_test, 
    line_kws={'color':'red'}, 
    label='Regresyon Çizgisi'
)
plt.xlabel('Crude Rate')
plt.ylabel('Reçeteler (milyonlar)')
plt.title('Crude Rate vs Reçeteler: Gerçek ve Tahmin')
plt.legend()
plt.tight_layout()
plt.show()

