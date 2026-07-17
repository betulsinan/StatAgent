from utils import veri_ozeti_olustur
from tasks import gorevleri_olustur
from crewai import Crew, Process
print("ANALYSIS.PY ÇALIŞTI")
from statistics_engine import (
    pearson_test,
    spearman_test,
    independent_t_test,
    paired_t_test,
    mann_whitney_test,
    wilcoxon_test,
    chi_square_test,
    fisher_test,
    anova_test,
    kruskal_test)

import re
import json

def json_bul(metin):

    eslesmeler = re.findall(r"```json(.*?)```", metin, re.DOTALL)

    print("=" * 80)
    print("Bulunan JSON sayısı:", len(eslesmeler))

    for json_str in eslesmeler:

        print("JSON ADAYI:")
        print(json_str)

        try:
            return json.loads(json_str.strip())

        except Exception as e:
            print("JSON okunamadı:", e)

    return None

# -------------------------------------------------
# Testi Bul
# -------------------------------------------------

def testi_bul(metin):

    print("=" * 80)
    print("testi_bul'a gelen veri tipi:", type(metin))
    print("=" * 80)
    print(metin)
    print("=" * 80)

    metin = str(metin).lower()

    if "pearson" in metin:
        return "pearson"

    elif "spearman" in metin:
        return "spearman"

    elif "independent t-test" in metin or "independent t test" in metin:
        return "independent_t"

    elif "paired t-test" in metin or "paired t test" in metin:
        return "paired_t"

    elif "mann" in metin:
        return "mann_whitney"

    elif "wilcoxon" in metin:
        return "wilcoxon"

    elif "anova" in metin:
        return "anova"

    elif "kruskal" in metin:
        return "kruskal"

    elif "ki-kare" in metin or "chi-square" in metin:
        return "chi_square"

    elif "fisher" in metin:
        return "fisher"

    return None


# -------------------------------------------------
# Analizi Başlat
# -------------------------------------------------

def analizi_baslat(df, kullanici_sorusu):
    print("analizi_baslat() çağrıldı")
    veri_ozeti = veri_ozeti_olustur(df)

    sutunlar = list(df.columns)

    veri_ornegi = df.head().to_markdown(index=False)

    gorevler, istatistik_ajani, kodcu_ajan = gorevleri_olustur(
        kullanici_sorusu,
        veri_ozeti,
        sutunlar,
        veri_ornegi
    )

    ekip = Crew(
        agents=[istatistik_ajani, kodcu_ajan],
        tasks=gorevler,
        process=Process.sequential,
        verbose=True
    )

    sonuc = ekip.kickoff()
    print("\n" + "="*60)
    print("SONUC TİPİ:", type(sonuc))
    print("="*60)

    print("\ndir(sonuc):")  
    print(dir(sonuc))

    print("\n__dict__:")
    if hasattr(sonuc, "__dict__"):
        print(sonuc.__dict__)
    sonuc_metin = sonuc.raw if hasattr(sonuc, "raw") else str(sonuc)
    json_veri = json_bul(sonuc_metin)
    print("JSON VERİ:", json_veri)
    sonuc = ekip.kickoff()

    print("="*80)
    print(type(sonuc))
    print(dir(sonuc))
    print("="*80)
    
    # -------------------------------------------------
    # Seçilen testi bul
    # -------------------------------------------------

    if json_veri:
        secilen_test = json_veri["test"]
    else:
        secilen_test = None
    
    print("Seçilen test:", secilen_test)

    # -------------------------------------------------
    # Şimdilik sadece Pearson / Spearman
    # -------------------------------------------------

    analiz_sonucu = None
    if secilen_test == "pearson":

        analiz_sonucu = pearson_test(
    df,
    json_veri["x"],
    json_veri["y"]
)
    
    elif secilen_test == "spearman":

        analiz_sonucu = spearman_test(
    df,
    json_veri["x"],
    json_veri["y"]
)
    elif secilen_test == "independent_t":

        analiz_sonucu = independent_t_test(
    df,
    json_veri["group"],
    json_veri["value"]
)
    elif secilen_test == "paired_t":

        analiz_sonucu = paired_t_test(
    df,
    json_veri["x"],
    json_veri["y"]
)
    elif secilen_test == "mann_whitney":

        analiz_sonucu = mann_whitney_test(
    df,
    json_veri["group"],
    json_veri["value"]
)
    elif secilen_test == "wilcoxon":

        analiz_sonucu = wilcoxon_test(
    df,
    json_veri["x"],
    json_veri["y"]
)
    elif secilen_test == "anova":

        analiz_sonucu = anova_test(
    df,
    json_veri["group"],
    json_veri["value"]
)
    elif secilen_test == "chi_square":

        analiz_sonucu = chi_square_test(
    df,
    json_veri["x"],
    json_veri["y"]
)  
    elif secilen_test == "fisher":

        analiz_sonucu = fisher_test(
    df,
    json_veri["x"],
    json_veri["y"]
) 
    elif secilen_test == "kruskal":

        analiz_sonucu = kruskal_test(
    df,
    json_veri["group"],
    json_veri["value"]
)
             
    # -------------------------------------------------
    # Gerçek sonuçları ekrana yazdır
    # -------------------------------------------------

    if analiz_sonucu:

        print(analiz_sonucu)

    return {
    "rapor": sonuc_metin,
    "analiz": analiz_sonucu
}    
