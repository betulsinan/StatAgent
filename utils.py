import io
import pandas as pd
import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle


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

# Sprint 3 - Adım 1 & Adım 2 İlavelerimiz
def validate_dataframe(df: pd.DataFrame) -> tuple[bool, str, list]:
    """
    Yüklenen veri setinin güvenlik, boyut ve eksik veri kontrollerini yapar.
    """
    if df is None or df.empty:
        return False, "Yüklenen dosya boş veya geçersiz.", []
    if len(df.columns) < 2:
        return False, "Analiz yapılabilmesi için veri setinde en az 2 sütun bulunmalıdır.", []
    if len(df) < 5:
        return False, "Anlamlı bir istatistiksel analiz için en az 5 satır veri gereklidir.", []
    
    # Eksik Veri Tespiti
    missing_info = []
    missing_series = df.isnull().sum()
    for col, count in missing_series.items():
        if count > 0:
            percentage = (count / len(df)) * 100
            missing_info.append(f"• **{col}**: {count} adet eksik veri (%{percentage:.1f})")
            
    return True, "Veri seti uygun.", missing_info

# PDF Dönüştürme Yardımcı Fonksiyonu
def text_to_pdf(text: str) -> bytes:
    """Markdown/Metin raporunu temiz bir PDF dosyasına çevirir."""
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    
    style = ParagraphStyle(
        'CustomStyle',
        parent=styles['Normal'],
        fontSize=10,
        leading=14,
        spaceAfter=8
    )
    
    story = []
    lines = text.split('\n')
    for line in lines:
        if line.strip():
            clean_line = line.replace('#', '').replace('*', '').replace('`', '').strip()
            story.append(Paragraph(clean_line, style))
            story.append(Spacer(1, 4))
            
    doc.build(story)
    buffer.seek(0)
    return buffer.getvalue()

# Güncellenmiş Çift Formatlı (MD + PDF) İndirme Butonu
def create_report_download_button(report_text: str, filename_prefix: str = "StatAgent_Analiz_Raporu"):
    """Kullanıcının raporu hem Markdown hem de PDF olarak indirmesini sağlar."""
    col1, col2 = st.columns(2)
    
    with col1:
        st.download_button(
            label="📥 Raporu İndir (.md)",
            data=report_text,
            file_name=f"{filename_prefix}.md",
            mime="text/markdown",
            use_container_width=True,
            help="Ajanların oluşturduğu detaylı istatistik raporunu Markdown olarak indirin."
        )
        
    with col2:
        try:
            pdf_data = text_to_pdf(report_text)
            st.download_button(
                label="📄 Raporu İndir (.pdf)",
                data=pdf_data,
                file_name=f"{filename_prefix}.pdf",
                mime="application/pdf",
                use_container_width=True,
                help="Ajanların oluşturduğu detaylı istatistik raporunu PDF olarak indirin."
            )
        except Exception:
            st.warning("PDF oluşturulurken bir hata oluştu, lütfen .md formatını kullanın.")