import pandas as pd

def veri_yukle(dosya_yolu: str) -> pd.DataFrame:
    if dosya_yolu.endswith('.csv'):
        return pd.read_csv(dosya_yolu)
    elif dosya_yolu.endswith(('.xlsx', '.xls')):
        return pd.read_excel(dosya_yolu)
    else:
        raise ValueError("Sadece .csv veya .xlsx dosyaları destekleniyor.")

def veri_ozeti_olustur(df: pd.DataFrame) -> str:
    ozet = f"""
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
    return ozet
    