import pandas as pd

def veri_yukle(dosya) -> pd.DataFrame:
    if dosya.name.endswith(".csv"):
        return pd.read_csv(dosya)
    elif dosya.name.endswith((".xlsx", ".xls")):
        return pd.read_excel(dosya)
    else:
        raise ValueError("Sadece CSV veya Excel dosyaları desteklenmektedir.")

def veri_ozeti_olustur(df: pd.DataFrame) -> str:
    ozet = f"""
    Satır sayısı: {df.shape[0]}
    Sütun sayısı: {df.shape[1]}

    Sütunlar:
    {df.dtypes.to_string()}

    Eksik değerler:
    {df.isnull().sum().to_string()}
    """
    return ozet

def veri_istatistikleri(df):

    sayisal = len(df.select_dtypes(include="number").columns)

    kategorik = len(df.select_dtypes(exclude="number").columns)

    eksik = int(df.isnull().sum().sum())

    return {
        "Sayısal Değişken": sayisal,
        "Kategorik Değişken": kategorik,
        "Eksik Veri": eksik
    }