import pandas as pd

from scipy.stats import (
    pearsonr,
    spearmanr,
    ttest_ind,
    ttest_rel,
    mannwhitneyu,
    wilcoxon,
    chi2_contingency,
    fisher_exact,
    f_oneway,
    kruskal
)


# -------------------------------------------------
# Ortak Sonuç Fonksiyonu
# -------------------------------------------------

def sonuc_olustur(test, istatistik, p, varsayimlar=None):

    return {
        "test": test,
        "istatistik": round(float(istatistik), 4),
        "p": round(float(p), 6),
        "karar": "H0 reddedildi" if p < 0.05 else "H0 reddedilemedi",
        "yorum": (
            "İstatistiksel olarak anlamlı sonuç bulundu."
            if p < 0.05
            else "İstatistiksel olarak anlamlı sonuç bulunamadı."
        ),
        "varsayimlar": varsayimlar or []
    }


# -------------------------------------------------
# Pearson Korelasyonu
# -------------------------------------------------

def pearson_test(df, x, y):

    r, p = pearsonr(df[x], df[y])

    return sonuc_olustur(
        "Pearson Korelasyonu",
        r,
        p,
        [
            "Normallik",
            "Doğrusal ilişki",
            "Bağımsız gözlemler"
        ]
    )


# -------------------------------------------------
# Spearman Korelasyonu
# -------------------------------------------------

def spearman_test(df, x, y):

    r, p = spearmanr(df[x], df[y])

    return sonuc_olustur(
        "Spearman Korelasyonu",
        r,
        p,
        [
            "Monoton ilişki",
            "Bağımsız gözlemler"
        ]
    )


# -------------------------------------------------
# Independent t-Test
# -------------------------------------------------

def independent_t_test(df, group_col, value_col):

    groups = df[group_col].dropna().unique()

    if len(groups) != 2:
        raise ValueError("Independent t-Test için grup sayısı 2 olmalıdır.")

    g1 = df[df[group_col] == groups[0]][value_col]
    g2 = df[df[group_col] == groups[1]][value_col]

    t, p = ttest_ind(g1, g2)

    return sonuc_olustur(
        "Independent t-Test",
        t,
        p,
        [
            "Normallik",
            "Varyans homojenliği",
            "Bağımsız gözlemler"
        ]
    )


# -------------------------------------------------
# Paired t-Test
# -------------------------------------------------

def paired_t_test(df, col1, col2):

    t, p = ttest_rel(df[col1], df[col2])

    return sonuc_olustur(
        "Paired t-Test",
        t,
        p,
        [
            "Normallik",
            "Eşleştirilmiş gözlemler"
        ]
    )


# -------------------------------------------------
# Mann Whitney U
# -------------------------------------------------

def mann_whitney_test(df, group_col, value_col):

    groups = df[group_col].dropna().unique()

    if len(groups) != 2:
        raise ValueError("Mann-Whitney U testi için grup sayısı 2 olmalıdır.")

    g1 = df[df[group_col] == groups[0]][value_col]
    g2 = df[df[group_col] == groups[1]][value_col]

    u, p = mannwhitneyu(g1, g2)

    return sonuc_olustur(
        "Mann-Whitney U",
        u,
        p,
        [
            "Bağımsız gözlemler"
        ]
    )


# -------------------------------------------------
# Wilcoxon
# -------------------------------------------------

def wilcoxon_test(df, col1, col2):

    w, p = wilcoxon(df[col1], df[col2])

    return sonuc_olustur(
        "Wilcoxon",
        w,
        p,
        [
            "Eşleştirilmiş gözlemler"
        ]
    )


# -------------------------------------------------
# Ki-Kare
# -------------------------------------------------

def chi_square_test(df, col1, col2):

    table = pd.crosstab(df[col1], df[col2])

    chi, p, _, _ = chi2_contingency(table)

    return sonuc_olustur(
        "Ki-Kare Testi",
        chi,
        p,
        [
            "Beklenen frekanslar yeterli olmalı"
        ]
    )


# -------------------------------------------------
# Fisher Exact
# -------------------------------------------------

def fisher_test(df, col1, col2):

    table = pd.crosstab(df[col1], df[col2])

    odds, p = fisher_exact(table)

    return sonuc_olustur(
        "Fisher Exact Testi",
        odds,
        p,
        [
            "2x2 çapraz tablo"
        ]
    )


# -------------------------------------------------
# One-Way ANOVA
# -------------------------------------------------

def anova_test(df, group_col, value_col):

    groups = [
        df[df[group_col] == g][value_col]
        for g in df[group_col].dropna().unique()
    ]

    F, p = f_oneway(*groups)

    return sonuc_olustur(
        "One-Way ANOVA",
        F,
        p,
        [
            "Normallik",
            "Varyans homojenliği",
            "Bağımsız gözlemler"
        ]
    )


# -------------------------------------------------
# Kruskal-Wallis
# -------------------------------------------------

def kruskal_test(df, group_col, value_col):

    groups = [
        df[df[group_col] == g][value_col]
        for g in df[group_col].dropna().unique()
    ]

    h, p = kruskal(*groups)

    return sonuc_olustur(
        "Kruskal-Wallis",
        h,
        p,
        [
            "Bağımsız gözlemler"
        ]
    )