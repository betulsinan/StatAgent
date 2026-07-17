from crewai import Task
from agents import (
    istatistik_uzman_ajan_olustur,
    python_kodcu_ajan_olustur
)
 
 
def gorevleri_olustur(
    kullanici_sorusu,
    veri_ozeti,
    sutunlar,
    veri_ornegi
):
 
    # -------------------------------------------------
    # AJANLAR
    # -------------------------------------------------
 
    istatistik_ajani = istatistik_uzman_ajan_olustur()
    kodcu_ajan = python_kodcu_ajan_olustur()
 
    # -------------------------------------------------
    # GÖREV 1
    # -------------------------------------------------
 
    test_secim_gorevi = Task(
        description=f"""
Kullanıcının sorusu:
 
{kullanici_sorusu}
 
--------------------------------------------------
 
Veri Özeti
 
{veri_ozeti}
 
--------------------------------------------------
 
Sütunlar
 
{sutunlar}
 
--------------------------------------------------
 
İlk 5 Satır
 
{veri_ornegi}
 
--------------------------------------------------
 
Görevin:
 
1. En uygun istatistiksel testi belirle.
2. Test seçiminin gerekçesini açıkla.
3. Varsayımları yaz.
4. H0 ve H1 hipotezlerini oluştur.
5. Analizin nasıl gerçekleştirileceğini açıkla.
 
Kurallar:
 
- Asla veri uydurma.
- Asla örnek DataFrame oluşturma.
- Asla Python kodu yazma.
- Sadece verilen veri yapısını değerlendir.
- Gerçek sütun isimlerini kullan.
- Tüm cevaplarını Türkçe ver.
 
ÇOK ÖNEMLİ:
 
Raporunun en sonunda aşağıdaki formatta geçerli bir JSON üret.
 
Pearson / Spearman için:
 
```json
{{
    "test": "pearson",
    "x": "birinci_sutun",
    "y": "ikinci_sutun"
}}
```
 
Independent t-Test / Mann-Whitney için:
 
```json
{{
    "test": "independent_t",
    "group": "grup_sutunu",
    "value": "sayisal_sutun"
}}
```
 
Paired t-Test / Wilcoxon için:
 
```json
{{
    "test": "paired_t",
    "x": "once",
    "y": "sonra"
}}
```
 
ANOVA / Kruskal için:
 
```json
{{
    "test": "anova",
    "group": "grup",
    "value": "sayisal"
}}
```
 
Ki-Kare / Fisher için:
 
```json
{{
    "test": "chi_square",
    "x": "kategori1",
    "y": "kategori2"
}}
```
 
KURALLAR (ZORUNLU)
 
- Rapor bittikten sonra SON SATIRDA yalnızca JSON bulunacaktır.
- JSON'dan sonra hiçbir açıklama yazma.
- JSON'u ```json bloğu içinde verme.
- JSON geçerli (valid) olmalıdır.
- Çift tırnak (") kullan.
- Anahtar isimlerini değiştirme.
- Gerçek sütun isimlerini kullan.
JSON'daki "test" alanı yalnızca aşağıdaki değerlerden biri olabilir:
 
pearson
spearman
independent_t
paired_t
mann_whitney
wilcoxon
anova
kruskal
chi_square
fisher
 
Örnek çıktı:
 
{{
    "test": "pearson",
    "x": "egitim_yili",
    "y": "maas"
}}
""",
        expected_output="""
Türkçe analiz raporu.
 
Raporun sonunda yalnızca geçerli bir JSON bulunmalıdır.
""",
        agent=istatistik_ajani
    )
 
    # -------------------------------------------------
    # GÖREV 2
    # -------------------------------------------------
 
    kod_yazma_gorevi = Task(
        description=f"""
ÖNEMLİ
 
İstatistik uzmanının seçtiği testi DEĞİŞTİRME.
Context içinde gelen testi kullan.
Yeni test seçme.
JSON üretme.
 
Kullanıcının sorusu:
 
{kullanici_sorusu}
 
--------------------------------------------------
 
Veri Özeti
 
{veri_ozeti}
 
--------------------------------------------------
 
Sütunlar
 
{sutunlar}
 
--------------------------------------------------
 
İlk 5 Satır
 
{veri_ornegi}
 
--------------------------------------------------
 
Görevin:
 
Sadece istatistik uzmanının seçtiği testi bilimsel olarak açıkla.
 
Rapor yalnızca aşağıdaki başlıklardan oluşmalıdır:
 
📌 Kullanılan Test
 
📖 Testin Gerekçesi
 
📋 Hipotezler
 
⚙️ Varsayımlar
 
KESİNLİKLE YAZMA:
 
- 📊 Bulgular
- Test istatistiği
- p-değeri
- Karar
- Yorum
- Python Kodu
- "Sistem tarafından hesaplanacaktır"
- "Örnek sonuç"
- Placeholder ifadeleri
- Dummy veri
- JSON
 
Kurallar:
 
- Veri uydurma.
- Örnek analiz sonucu üretme.
- Test değiştirme.
- Markdown kullan.
- Tamamen Türkçe yaz.
 
Sadece yukarıdaki dört başlığı üret.
""",
        expected_output="""
Markdown formatında hazırlanmış kısa analiz raporu.
 
Rapor yalnızca aşağıdaki bölümlerden oluşmalıdır:
 
📌 Kullanılan Test
 
📖 Testin Gerekçesi
 
📋 Hipotezler
 
⚙️ Varsayımlar
""",
        agent=kodcu_ajan,
        context=[test_secim_gorevi]
    )
 
    return (
        [test_secim_gorevi, kod_yazma_gorevi],
        istatistik_ajani,
        kodcu_ajan
    )
