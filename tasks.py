from crewai import Task
from agents import istatistik_uzman_ajan_olustur, python_kodcu_ajan_olustur

def gorevleri_olustur(kullanici_sorusu: str, veri_ozeti: str):
    istatistik_ajani = istatistik_uzman_ajan_olustur()
    kodcu_ajan = python_kodcu_ajan_olustur()

    test_secim_gorevi = Task(
        description=f"""
        Kullanıcı şu soruyu sordu: '{kullanici_sorusu}'
        
        Yüklenen verinin özeti aşağıdadır:
        {veri_ozeti}
        
        Bu soruya yanıt vermek için:
        1. Hangi istatistiksel test veya model kullanılmalıdır? Neden?
        2. Testin varsayımları nelerdir?
        3. H0 ve H1 hipotezlerini yaz.
        4. Kullanılacak Python kütüphanesi nedir?
        """,
        expected_output="""
        - Önerilen test adı ve gerekçesi
        - Testin varsayımları
        - H0 (Null) hipotezi
        - H1 (Alternatif) hipotezi
        - Kullanılacak Python fonksiyonu
        """,
        agent=istatistik_ajani
    )

    kod_yazma_gorevi = Task(
        description=f"""
        İstatistik uzmanının önerdiği analizi gerçekleştir.
        
        Veri 'data/ornek_veri.csv' dosyasında bulunuyor.
        Kullanıcının sorusu: '{kullanici_sorusu}'
        
        Şunları yap:
        1. Veriyi pandas ile oku.
        2. Gerekli istatistiksel testi scipy/statsmodels ile uygula.
        3. Sonuçları (p-değeri, test istatistiği) yorumla.
        4. Uygun bir grafik çiz ve 'output.png' olarak kaydet.
        5. Sonucu sade Türkçe ile özetle.
        """,
        expected_output="""
        - Çalışan Python kodu
        - Test istatistiği ve p-değeri
        - H0 reddedildi mi?
        - Grafiğin kaydedildiği onayı
        - Analiz sonucunun sade dil özeti
        """,
        agent=kodcu_ajan,
        context=[test_secim_gorevi]
    )

    return [test_secim_gorevi, kod_yazma_gorevi], istatistik_ajani, kodcu_ajan
    