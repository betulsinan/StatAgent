import os
import pandas as pd
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process

# .env dosyasındaki GEMINI_API_KEY'i yükle
load_dotenv()

# Dil modelini ücretsiz Gemini olarak tanımlıyoruz
gemini_llm = "gemini/gemini-2.5-flash"

# ============================================================
# 📊 ADIM 1: GERÇEK CSV VERİSİNİ PANDAS İLE YÜKLEME VE ÖZETLEME
# ============================================================
csv_dosya_adi = "../maas_verisi.csv"

if not os.path.exists(csv_dosya_adi):
    print(f"❌ Hata: {csv_dosya_adi} dosyası bulunamadı! Lütfen dosyayı oluşturun.")
    exit()

# Veriyi oku
df = pd.read_csv(csv_dosya_adi)

# Ajanların veriyi anlaması için otomatik bir teknik özet metni hazırlıyoruz
veri_ozeti = f"""
Satır sayısı: {df.shape[0]}
Sütun sayısı: {df.shape[1]}
Sütunlar ve veri tipleri:
{df.dtypes.to_string()}

İlk 5 satır:
{df.head().to_string()}

Temel istatistikler:
{df.describe().to_string()}

Eksik değerler:
{df.isnull().sum().to_string()}
"""

print("============================================================")
print("   StatAgent - Akıllı İstatistik Analizi")
print("============================================================")
print(f"\n✅ Veri yüklendi: {df.shape[0]} satır, {df.shape[1]} sütun")

# Kullanıcının sorusu (Bunu ileride arayüzden alacağız)
user_question = "Eğitim yılı ile maaş arasında anlamlı bir ilişki var mı?"
print(f"❓ Kullanıcı sorusu: {user_question}")
print("------------------------------------------------------------")

# ============================================================
# 🤖 ADIM 2: AJANLAR VE GÖREVLERİN TANIMLANMASI
# ============================================================

# 1. İSTATİSTİK UZMANI AJANI
statistician = Agent(
    role="Kıdemli Biyoistatistikçi ve Veri Bilimci",
    goal="Kullanıcının sorusuna ve veri özetine bakarak en doğru istatistiksel testi belirlemek.",
    backstory="Sen hipotez testleri ve modelleme konusunda dünya çapında bir uzmansın. Varsayımları incelemeden asla karar vermezsin.",
    verbose=True,
    llm=gemini_llm
)

# GÖREV 1: İstatistiksel Test Seçimi
task1 = Task(
    description=f"""Kullanıcı şu soruyu sordu: '{user_question}'
    
    Yüklenen verinin özeti aşağıdadır:
    {veri_ozeti}
    
    Bu soruya yanıt vermek için:
    1. Hangi istatistiksel test veya model kullanılmalıdır? Neden?
    2. Testin varsayımları nelerdir?
    3. H0 ve H1 hipotezlerini yaz.
    4. Kullanılacak Python kütüphanesi nedir?
    """,
    expected_output="Seçilen testin adı, gerekçesi, varsayımları, hipotezler ve kütüphane bilgisi.",
    agent=statistician
)

# EKİBİ KURUYORUZ
ekip = Crew(
    agents=[statistician], # Şimdilik sadece istatistikçi ajanımızı koşturup net bir metodoloji alıyoruz
    tasks=[task1],
    process=Process.sequential
)

print("\n🚀 Ekip çalışmaya başlıyor...\n")
result = ekip.kickoff()

print("\n🎯 --- NİHAİ ANALİZ METODOLOJİSİ --- 🎯\n")
print(result)
