import re
import traceback
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

from analysis import analizi_baslat
from memory import save_analysis, retrieve_memory

from utils import (
    veri_yukle,
    veri_istatistikleri,
    validate_dataframe,
    create_report_download_button
)
from graphs import (
    histogram,
    boxplot,
    scatter_plot,
    correlation_matrix
)
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
    kruskal_test
)

# --------------------------------------------------
# 1. Sayfa Yapılandırması
# --------------------------------------------------
st.set_page_config(
    page_title="StatAgent - Yapay Zekâ Destekli İstatistik Asistanı",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# 2. Custom CSS (Strict Light Theme Force)
# --------------------------------------------------
st.markdown("""
<style>

/* Genel görünüm */
.metric-card {
    background: var(--secondary-background-color);
    color: var(--text-color);
    padding: 16px;
    border-radius: 12px;
    border-left: 5px solid var(--primary-color);
    box-shadow: 0 4px 10px rgba(0,0,0,0.08);
    text-align: center;
}

.metric-title{
    font-size:0.85rem;
    font-weight:600;
    opacity:0.75;
    text-transform:uppercase;
}

.metric-value{
    font-size:1.7rem;
    font-weight:700;
    color:var(--primary-color);
}

/* Sistem mimarisi kartı */
.architecture-card{
    background: linear-gradient(135deg,#1e3c72,#2a5298);
    color:white;
    padding:15px;
    border-radius:12px;
    margin-bottom:20px;
}

.architecture-card *{
    color:white !important;
}

</style>
""", unsafe_allow_html=True)
# --------------------------------------------------
# 3. Çok Dilli Sözlük Altyapısı (i18n)
# --------------------------------------------------
TEXTS = {
    "TR": {
        "title": "📊 StatAgent",
        "subtitle": "Yapay zekâ destekli istatistiksel veri analizi platformu",
        "description": "CSV veya Excel dosyanızı yükleyin ve istatistiksel sorunuzu doğal dilde yazın. StatAgent sizin için uygun analizi belirlesin, çalıştırsın ve profesyonel raporunuza dönüştürsün.",
        "arch_title": "🚀 Sistem Mimarisi",
        "guide_title": "📋 Hızlı Kullanım Rehberi",
        "guide_1": "1. **📁 Veri Yükle:** CSV veya Excel dosyanı yükle.",
        "guide_2": "2. **🔍 Kontrol:** Otomatik eksik veri analizini incele.",
        "guide_3": "3. **💬 Soru Sor:** İstatistiksel hipotezini yaz.",
        "guide_4": "4. **📄 Rapor Al:** Profesyonel PDF çıktını indir.",
        "tip": "💡 **Biyoistatistik İpucu**\n\nParametrik testlerin geçerliliği için eksik verileri ve dağılım grafiklerini analiz öncesinde mutlaka kontrol edin.",
        "upload_label": "📁 CSV veya Excel dosyanızı yükleyin",
        "missing_warning": "⚠️ **Veri Setinde Eksik Veriler Tespit Edildi!**",
        "summary_title": "📊 Veri Seti Özet Bilgileri",
        "rows": "Toplam Satır",
        "cols": "Toplam Sütun",
        "num_vars": "Sayısal Değişken",
        "cat_vars": "Kategorik Değişken",
        "missing": "Eksik Veri",
        "preview": "🔍 Veri Setinin İlk 5 Satırını İncele",
        "question_title": "💬 Analiz Sorusu",
        "question_placeholder": "Örnek: Eğitim yılı ile maaş arasında anlamlı bir ilişki var mı?",
        "start_button": "🚀 Analizi Başlat",
        "status_main": "🤖 **StatAgent Ajanları Çalışıyor...**",
        "status_1": "🔍 **1. Veri Doğrulama Ajanı:** Kontrol ediliyor...",
        "status_2": "📊 **2. İstatistikçi Ajan:** p-değeri hesaplanıyor...",
        "status_3": "📝 **3. Raporlayıcı Ajan:** PDF hazırlanıyor...",
        "status_complete": "✅ **Analiz Tamamlandı!**",
        "no_file_error": "❌ Lütfen önce bir CSV veya Excel dosyası yükleyin.",
        "no_q_warning": "⚠️ Lütfen analiz etmek istediğiniz soruyu yazın.",
        "ai_instruction": ""
    },
    "EN": {
        "title": "📊 StatAgent",
        "subtitle": "AI-Powered Statistical Data Analysis Platform",
        "description": "Upload your CSV or Excel file and write your statistical question in natural language. StatAgent will determine the appropriate test, execute it, and turn it into your professional report.",
        "arch_title": "🚀 System Architecture",
        "guide_title": "📋 Quick User Guide",
        "guide_1": "1. **📁 Upload Data:** Upload CSV or Excel file.",
        "guide_2": "2. **🔍 Validate:** Review automatic missing data analysis.",
        "guide_3": "3. **💬 Ask Question:** Type your statistical hypothesis.",
        "guide_4": "4. **📄 Get Report:** Download professional PDF output.",
        "tip": "💡 **Biostatistics Tip**\n\nCheck missing values and distribution plots prior to parametric testing.",
        "upload_label": "📁 Upload your CSV or Excel file",
        "missing_warning": "⚠️ **Missing Data Detected in Dataset!**",
        "summary_title": "📊 Dataset Summary Metrics",
        "rows": "Total Rows",
        "cols": "Total Columns",
        "num_vars": "Numeric Variables",
        "cat_vars": "Categorical Variables",
        "missing": "Missing Values",
        "preview": "🔍 Preview First 5 Rows of Dataset",
        "question_title": "💬 Analysis Question",
        "question_placeholder": "Example: Is there a significant relationship between education years and salary?",
        "start_button": "🚀 Start Analysis",
        "status_main": "🤖 **StatAgent Agents Working...**",
        "status_1": "🔍 **1. Validation Agent:** Checking data...",
        "status_2": "📊 **2. Statistician Agent:** Computing p-value...",
        "status_3": "📝 **3. Reporter Agent:** Generating PDF...",
        "status_complete": "✅ **Analysis Completed!**",
        "no_file_error": "❌ Please upload a CSV or Excel file first.",
        "no_q_warning": "⚠️ Please enter the question you want to analyze.",
        "ai_instruction": " (Please write the analysis report strictly in English with an academic tone)"
    },
    "DE": {
        "title": "📊 StatAgent",
        "subtitle": "KI-gestützte Plattform für statistische Datenanalyse",
        "description": "Laden Sie Ihre CSV- oder Excel-Datei hoch und formulieren Sie Ihre statistische Frage. StatAgent führt die passende Analyse durch und erstellt einen professionellen Bericht.",
        "arch_title": "🚀 Systemarchitektur",
        "guide_title": "📋 Schnellanleitung",
        "guide_1": "1. **📁 Daten Hochladen:** CSV- oder Excel-Datei hochladen.",
        "guide_2": "2. **🔍 Überprüfen:** Fehlende Werte automatisch analysieren.",
        "guide_3": "3. **💬 Frage Stellen:** Statistische Hypothese eingeben.",
        "guide_4": "4. **📄 Bericht Erhalten:** Professionelles PDF herunterladen.",
        "tip": "💡 **Biostatistik-Tipp**\n\nÜberprüfen Sie vor parametrischen Tests stets fehlende Werte und Verteilungsdiagramme.",
        "upload_label": "📁 CSV- oder Excel-Datei hochladen",
        "missing_warning": "⚠️ **Fehlende Daten im Datensatz erkannt!**",
        "summary_title": "📊 Datensatz-Zusammenfassung",
        "rows": "Gesamte Zeilen",
        "cols": "Gesamte Spalten",
        "num_vars": "Numerische Variablen",
        "cat_vars": "Kategoriale Variablen",
        "missing": "Fehlende Werte",
        "preview": "🔍 Vorschau der ersten 5 Zeilen",
        "question_title": "💬 Analysefrage",
        "question_placeholder": "Beispiel: Gibt es einen signifikanten Zusammenhang zwischen Ausbildungsjahren und Gehalt?",
        "start_button": "🚀 Analyse Starten",
        "status_main": "🤖 **StatAgent-Agenten arbeiten...**",
        "status_1": "🔍 **1. Validierungsagent:** Daten werden geprüft...",
        "status_2": "📊 **2. Statistik-Agent:** p-Wert wird berechnet...",
        "status_3": "📝 **3. Berichtsagent:** PDF wird erstellt...",
        "status_complete": "✅ **Analyse abgeschlossen!**",
        "no_file_error": "❌ Bitte laden Sie zuerst eine CSV- oder Excel-Datei hoch.",
        "no_q_warning": "⚠️ Bitte geben Sie Ihre Analysefrage ein.",
        "ai_instruction": " (Bitte schreiben Sie den Analysebericht streng auf Deutsch in akademischem Ton)"
    },
    "FR": {
        "title": "📊 StatAgent",
        "subtitle": "Plateforme d'analyse statistique assistée par IA",
        "description": "Téléchargez votre fichier CSV ou Excel et posez votre question statistique. StatAgent exécutera l'analyse appropriée et générera votre rapport professionnel.",
        "arch_title": "🚀 Architecture Système",
        "guide_title": "📋 Guide Rapide",
        "guide_1": "1. **📁 Charger Données:** Importer fichier CSV ou Excel.",
        "guide_2": "2. **🔍 Vérifier:** Analyser automatiquement les données manquantes.",
        "guide_3": "3. **💬 Poser Question:** Saisir votre hypothèse statistique.",
        "guide_4": "4. **📄 Obtenir Rapport:** Télécharger le rapport PDF.",
        "tip": "💡 **Conseil Biostatistique**\n\nVérifiez les valeurs manquantes et la distribution avant les tests paramétriques.",
        "upload_label": "📁 Téléchargez votre fichier CSV ou Excel",
        "missing_warning": "⚠️ **Données manquantes détectées!**",
        "summary_title": "📊 Résumé du jeu de données",
        "rows": "Lignes Totales",
        "cols": "Colonnes Totales",
        "num_vars": "Variables Numériques",
        "cat_vars": "Variables Catégorielles",
        "missing": "Valeurs Manquantes",
        "preview": "🔍 Aperçu des 5 premières lignes",
        "question_title": "💬 Question d'analyse",
        "question_placeholder": "Exemple: Existe-t-il une relation significative entre les années d'études et le salaire?",
        "start_button": "🚀 Lancer l'Analyse",
        "status_main": "🤖 **Agents StatAgent en cours...**",
        "status_1": "🔍 **1. Agent Validation:** Vérification...",
        "status_2": "📊 **2. Agent Statistique:** Calcul de la p-valeur...",
        "status_3": "📝 **3. Agent Rapport:** Génération du PDF...",
        "status_complete": "✅ **Analyse terminée!**",
        "no_file_error": "❌ Veuillez d'abord télécharger un fichier CSV ou Excel.",
        "no_q_warning": "⚠️ Veuillez saisir votre question d'analyse.",
        "ai_instruction": " (Veuillez rédiger le rapport d'analyse strictement en français sur un ton académique)"
    },
    "IT": {
        "title": "📊 StatAgent",
        "subtitle": "Piattaforma di analisi dati statistici con IA",
        "description": "Carica il tuo file CSV o Excel e scrivi la tua domanda in linguaggio naturale. StatAgent eseguirà l'analisi adeguata e genererà il tuo report professionale.",
        "arch_title": "🚀 Architettura Sistema",
        "guide_title": "📋 Guida Rapida",
        "guide_1": "1. **📁 Carica Dati:** Carica file CSV o Excel.",
        "guide_2": "2. **🔍 Controlla:** Analisi automatica dei dati mancanti.",
        "guide_3": "3. **💬 Fai Domanda:** Scrivi la tua ipotesi statistica.",
        "guide_4": "4. **📄 Scarica Report:** Scarica il report in PDF.",
        "tip": "💡 **Suggerimento Biostatistica**\n\nVerifica i valori mancanti e i grafici di distribuzione prima dei test parametrici.",
        "upload_label": "📁 Carica il tuo file CSV o Excel",
        "missing_warning": "⚠️ **Dati mancanti rilevati nel set di dati!**",
        "summary_title": "📊 Riepilogo del set di dati",
        "rows": "Righe Totali",
        "cols": "Colonne Totali",
        "num_vars": "Variabili Numeriche",
        "cat_vars": "Variabili Categoriali",
        "missing": "Valori Mancanti",
        "preview": "🔍 Anteprima prime 5 righe",
        "question_title": "💬 Domanda di analisi",
        "question_placeholder": "Esempio: Esiste una relazione significativa tra anni di studio e stipendio?",
        "start_button": "🚀 Avvia Analisi",
        "status_main": "🤖 **Agenti StatAgent al lavoro...**",
        "status_1": "🔍 **1. Agente Validazione:** Controllo dati...",
        "status_2": "📊 **2. Agente Statistico:** Calcolo p-value...",
        "status_3": "📝 **3. Agente Report:** Creazione PDF...",
        "status_complete": "✅ **Analisi Completata!**",
        "no_file_error": "❌ Carica prima un file CSV o Excel.",
        "no_q_warning": "⚠️ Inserisci la domanda da analizzare.",
        "ai_instruction": " (Si prega di redigere il rapporto di analisi rigorosamente in italiano con un tono accademico)"
    },
    "ZH": {
        "title": "📊 StatAgent",
        "subtitle": "人工智能驱动的统计数据分析平台",
        "description": "上传您的 CSV 或 Excel 文件，用自然语言输入您的统计问题。StatAgent 将为您确定合适的测试并生成专业报告。",
        "arch_title": "🚀 系统架构",
        "guide_title": "📋 快速使用指南",
        "guide_1": "1. **📁 上传数据:** 上传 CSV 或 Excel 文件。",
        "guide_2": "2. **🔍 检查数据:** 自动查看缺失值分析。",
        "guide_3": "3. **💬 提出问题:** 输入您的统计假设。",
        "guide_4": "4. **📄 获取报告:** 下载专业 PDF 报告。",
        "tip": "💡 **生物统计学提示**\n\n在进行参数检验之前，请务必检查缺失值和分布图。",
        "upload_label": "📁 上传您的 CSV 或 Excel 文件",
        "missing_warning": "⚠️ **数据集中检测到缺失数据！**",
        "summary_title": "📊 数据集摘要信息",
        "rows": "总行数",
        "cols": "总列数",
        "num_vars": "数值变量",
        "cat_vars": "分类变量",
        "missing": "缺失值",
        "preview": "🔍 预览数据集前 5 行",
        "question_title": "💬 分析问题",
        "question_placeholder": "例如：受教育年限与薪资之间是否存在显著关系？",
        "start_button": "🚀 开始分析",
        "status_main": "🤖 **StatAgent 智能体工作中...**",
        "status_1": "🔍 **1. 数据验证智能体:** 正在检查...",
        "status_2": "📊 **2. 统计师智能体:** 正在计算 p 值...",
        "status_3": "📝 **3. 报告智能体:** 正在生成 PDF...",
        "status_complete": "✅ **分析完成！**",
        "no_file_error": "❌ 请先上传 CSV 或 Excel 文件。",
        "no_q_warning": "⚠️ 请输入您想要分析的问题。",
        "ai_instruction": " (请严格使用中文和学术语气撰写分析报告)"
    }
}

def kodu_ayir(metin):
    pattern = r"```(?:python)?\s*(.*?)```"
    eslesme = re.search(pattern, metin, re.DOTALL | re.IGNORECASE)

    if eslesme:
        kod = eslesme.group(1).strip()
        yeni_metin = re.sub(pattern, "", metin, flags=re.DOTALL | re.IGNORECASE)
        return yeni_metin.strip(), kod

    return metin, None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# --------------------------------------------------
# Sidebar (Yan Menü & Dil Seçimi)
# --------------------------------------------------
with st.sidebar:
    # 🌐 Dil Seçim Kutusu
    lang_map = {
        "Türkçe 🇹🇷": "TR",
        "English 🇬🇧": "EN",
        "Deutsch 🇩🇪": "DE",
        "Français 🇫🇷": "FR",
        "Italiano 🇮🇹": "IT",
        "中文 🇨🇳": "ZH"
    }
    selected_lang_label = st.selectbox("🌐 Language / Dil", list(lang_map.keys()), index=0)
    lang_code = lang_map[selected_lang_label]
    t = TEXTS[lang_code]

    st.title(t["title"])
    st.caption("v1.0.0 | Enterprise SaaS Edition")
    
    st.markdown(f"""
    <div class="architecture-card">
        <h4>{t["arch_title"]}</h4>
        <p><b>1. UI:</b> Streamlit Dynamic Interface</p>
        <p><b>2. Multi-Agent:</b> CrewAI Engine</p>
        <p><b>3. AI Model:</b> Google Gemini 2.5</p>
        <p><b>4. Output:</b> ReportLab PDF Generator</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
### {t["guide_title"]}

{t["guide_1"]}
{t["guide_2"]}
{t["guide_3"]}
{t["guide_4"]}
""")
    st.divider()
    st.info(t["tip"])

# --------------------------------------------------
# Ana Başlık
# --------------------------------------------------
st.title(t["title"])
st.caption(t["subtitle"])

st.markdown(t["description"])

st.divider()

uploaded_file = st.file_uploader(
    t["upload_label"],
    type=["csv", "xlsx"]
)

if uploaded_file is not None:
    df = veri_yukle(uploaded_file)
    is_valid, msg, missing_info = validate_dataframe(df)
    if not is_valid:
        st.error(f"❌ {msg}")
        st.stop()

    if missing_info:
        with st.warning(t["missing_warning"]):
            st.write("Aşağıdaki sütunlarda eksik değerler bulunmaktadır:")
            for info in missing_info:
                st.markdown(info)

    istatistikler = veri_istatistikleri(df)

    st.markdown(f"### {t['summary_title']}")
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.markdown(f'<div class="metric-card" style="border-left-color: #4e73df;"><div class="metric-title">{t["rows"]}</div><div class="metric-value">{df.shape[0]}</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="metric-card" style="border-left-color: #1cc88a;"><div class="metric-title">{t["cols"]}</div><div class="metric-value">{df.shape[1]}</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="metric-card" style="border-left-color: #36b9cc;"><div class="metric-title">{t["num_vars"]}</div><div class="metric-value">{istatistikler["Sayısal Değişken"]}</div></div>', unsafe_allow_html=True)
    with col4:
        st.markdown(f'<div class="metric-card" style="border-left-color: #f6c23e;"><div class="metric-title">{t["cat_vars"]}</div><div class="metric-value">{istatistikler["Kategorik Değişken"]}</div></div>', unsafe_allow_html=True)
    with col5:
        eksik_renk = "#e74a3b" if istatistikler['Eksik Veri'] > 0 else "#858796"
        st.markdown(f'<div class="metric-card" style="border-left-color: {eksik_renk};"><div class="metric-title">{t["missing"]}</div><div class="metric-value" style="color: {eksik_renk};">{istatistikler["Eksik Veri"]}</div></div>', unsafe_allow_html=True)
    
    st.markdown("---")

    with st.expander(t["preview"], expanded=False):
        st.dataframe(df.head(), use_container_width=True)

    tab1, tab2, tab3, tab4 = st.tabs(["📊 Histogram", "📦 Box Plot", "📈 Scatter Plot", "🔥 Korelasyon"])
    numeric_cols = df.select_dtypes(include="number").columns

    with tab1:
        if len(numeric_cols) > 0:
            hist_col = st.selectbox("Sütun seç", numeric_cols, key="hist")
            fig = histogram(df, hist_col)
            if fig: st.pyplot(fig)
    with tab2:
        if len(numeric_cols) > 0:
            box_col = st.selectbox("Sütun seç", numeric_cols, key="box")
            fig = boxplot(df, box_col)
            if fig: st.pyplot(fig)
    with tab3:
        if len(numeric_cols) >= 2:
            sc_col1, sc_col2 = st.columns(2)
            x_col = sc_col1.selectbox("X ekseni", numeric_cols, key="x")
            y_col = sc_col2.selectbox("Y ekseni", numeric_cols, key="y")
            if x_col != y_col:
                fig = scatter_plot(df, x_col, y_col)
                if fig: st.pyplot(fig)
    with tab4:
        if len(numeric_cols) >= 2:
            fig = correlation_matrix(df)
            if fig: st.pyplot(fig)

st.divider()
st.subheader(t["question_title"])
question = st.text_area("", placeholder=t["question_placeholder"])

if st.button(t["start_button"], use_container_width=True):
    if uploaded_file is None:
        st.error(t["no_file_error"])
    elif question.strip() == "":
        st.warning(t["no_q_warning"])
    else:
        status_box = st.status(t["status_main"], expanded=True)
        with status_box:
            st.write(t["status_1"])
            st.write(t["status_2"])
            st.write(t["status_3"])
            try:
                # Seçilen dile göre AI modeline yönlendirme ekle
                prompt_q = question + t["ai_instruction"]
                sonuc = analizi_baslat(df, prompt_q)
                rapor = sonuc["rapor"]
                test_sonucu = sonuc["analiz"]
                status_box.update(label=t["status_complete"], state="complete", expanded=False)
                

                st.divider()
                metin, kod = kodu_ayir(rapor)
                with st.container(border=True):
                    st.markdown(metin)
                    st.divider()
                    create_report_download_button(rapor)

                if test_sonucu is not None:

                    p = test_sonucu["p"]

                    if p < 0.001:
                        p_text = "<0.001"
                    else:
                        p_text = f"{p:.4f}"

                    col1, col2, col3 = st.columns(3)

                    with col1:
                        st.metric(
            "🧪 Test",
            test_sonucu["test"]
        )

                    with col2:
                        st.metric(
            "📈 İstatistik",
            f'{test_sonucu["istatistik"]:.4f}'
        )

                    with col3:
                        st.metric(
            "🎯 p-değeri",
            p_text
        )

                st.info(f"📌 {test_sonucu['karar']}")

                st.success(test_sonucu["yorum"])
            except Exception as e:
                status_box.update(label="❌ Hata Oluştu", state="error")
                st.error(
    "🚨 Yapay zekâ servisi şu anda kullanılamıyor. "
    "Lütfen birkaç dakika sonra tekrar deneyin."
)
                with st.expander("Teknik hata ayrıntısı"):
                    st.code(traceback.format_exc())  