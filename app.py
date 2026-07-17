import streamlit as st
import matplotlib.pyplot as plt
import re

from analysis import analizi_baslat

from utils import (
    veri_yukle,
    veri_istatistikleri
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

import re

def kodu_ayir(metin):

    pattern = r"```(?:python)?\s*(.*?)```"

    eslesme = re.search(
        pattern,
        metin,
        re.DOTALL | re.IGNORECASE
    )

    if eslesme:

        kod = eslesme.group(1).strip()

        yeni_metin = re.sub(
            pattern,
            "",
            metin,
            flags=re.DOTALL | re.IGNORECASE
        )

        return yeni_metin.strip(), kod

    return metin, None
# ------------------------------------
# Session State
# ------------------------------------

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# --------------------------------------------------
# Sayfa Ayarları
# --------------------------------------------------

st.set_page_config(
    page_title="StatAgent",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:

    st.title("📊 StatAgent")

    st.markdown("""
### Yapay Zekâ Destekli Veri Analizi

StatAgent;

✅ CSV / Excel dosyalarını analiz eder.

✅ En uygun istatistiksel testi belirler.

✅ Sonuçları yapay zekâ ile yorumlar.

✅ Grafik ve rapor oluşturur.
""")

    st.divider()

    st.info(
        "💡 İpucu\n\n"
        "Önce veri dosyanızı yükleyin, ardından analiz etmek istediğiniz soruyu yazın."
    )

# --------------------------------------------------
# Ana Sayfa
# --------------------------------------------------

st.title("📊 StatAgent")

st.caption("Yapay zekâ destekli istatistiksel veri analizi platformu")

st.markdown("""
CSV veya Excel dosyanızı yükleyin ve istatistiksel sorunuzu doğal dilde yazın.

StatAgent sizin için uygun analizi belirlesin, çalıştırsın ve sonuçları yorumlasın.
""")

st.divider()

# --------------------------------------------------
# Dosya Yükleme
# --------------------------------------------------

uploaded_file = st.file_uploader(
    "📁 CSV veya Excel dosyanızı yükleyin",
    type=["csv", "xlsx"]
)

# --------------------------------------------------
# Dosya Yüklendi
# --------------------------------------------------

if uploaded_file is not None:

    df = veri_yukle(uploaded_file)

    istatistikler = veri_istatistikleri(df)

    st.success("✅ Dosya başarıyla yüklendi!")

    st.subheader("📋 Veri Seti Özeti")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="📄 Dosya",
            value=uploaded_file.name
        )

    with col2:
        st.metric(
            label="📈 Satır",
            value=df.shape[0]
        )

    with col3:
        st.metric(
            label="📊 Sütun",
            value=df.shape[1]
        )

    st.divider()

    st.subheader("📈 Veri Özeti")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "🔢 Sayısal Değişken",
             istatistikler["Sayısal Değişken"]
    )

    with c2:
        st.metric(
        "📝 Kategorik Değişken",
        istatistikler["Kategorik Değişken"]
    )

    with c3:
        st.metric(
        "❗ Eksik Veri",
        istatistikler["Eksik Veri"]
    )

    st.divider()

    st.subheader("📌 Sütun İsimleri")

    st.write(", ".join(df.columns))

    st.divider()

    st.subheader("🔍 İlk 5 Satır")

    st.dataframe(
        df.head(),
        use_container_width=True
    )
    st.divider()

    tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Histogram",
    "📦 Box Plot",
    "📈 Scatter",
    "🔥 Korelasyon"
])
    numeric_cols = df.select_dtypes(include="number").columns


    with tab1:

        st.subheader("📊 Histogram")

        if len(numeric_cols) == 0:
            st.warning("⚠️ Histogram için veri setinde sayısal sütun bulunamadı.")

        else:
            hist_col = st.selectbox(
            "Sütun seç",
            numeric_cols,
            key="hist"
        )

            try:
                fig = histogram(df, hist_col)

                if fig:
                    st.pyplot(fig)
                    plt.close(fig)

            except Exception as e:
                st.error(
                f"❌ Histogram oluşturulamadı.\n\n"
                f"Sebep: {e}"
            )



    with tab2:

        st.subheader("📦 Box Plot")

        if len(numeric_cols) == 0:
            st.warning("⚠️ Box Plot için veri setinde sayısal sütun bulunamadı.")

        else:
            box_col = st.selectbox(
            "Sütun seç",
            numeric_cols,
            key="box"
        )

            try:
                fig = boxplot(df, box_col)

                if fig:
                    st.pyplot(fig)
                    plt.close(fig)

            except Exception as e:
                st.error(
                f"❌ Box Plot oluşturulamadı.\n\n"
                f"Sebep: {e}"
            )



    with tab3:

        st.subheader("📈 Scatter Plot")

        if len(numeric_cols) < 2:

            st.warning(
            "⚠️ Scatter Plot için en az iki sayısal sütun gereklidir."
        )

        else:

            col1, col2 = st.columns(2)

            with col1:
                x_col = st.selectbox(
                "X ekseni",
                numeric_cols,
                key="x"
            )

            with col2:
                y_col = st.selectbox(
                "Y ekseni",
                numeric_cols,
                key="y"
            )


            if x_col == y_col:

                st.info(
                "ℹ️ Scatter Plot için iki farklı sütun seçmelisin."
            )

            else:

                try:
                    fig = scatter_plot(df, x_col, y_col)

                    if fig:
                        st.pyplot(fig)
                        plt.close(fig)

                except Exception as e:

                    st.error(
                    f"❌ Scatter Plot oluşturulamadı.\n\n"
                    f"Sebep: {e}"
                )



    with tab4:

        st.subheader("🔥 Korelasyon Matrisi")


        if len(numeric_cols) < 2:

            st.warning(
            "⚠️ Korelasyon analizi için en az iki sayısal sütun gereklidir."
        )

        else:

            try:

                fig = correlation_matrix(df)

                if fig:
                    st.pyplot(fig)
                    plt.close(fig)


            except Exception as e:

                st.error(
                f"❌ Korelasyon matrisi oluşturulamadı.\n\n"
                f"Sebep: {e}"
            )
# --------------------------------------------------
# Kullanıcı Sorusu
# --------------------------------------------------

st.divider()

st.subheader("💬 Analiz Sorusu")

question = st.text_area(
    "",
    placeholder="Örnek: Eğitim yılı ile maaş arasında anlamlı bir ilişki var mı?"
)

# --------------------------------------------------
# Analiz Butonu
# --------------------------------------------------

if st.button("🚀 Analizi Başlat", use_container_width=True):

    if uploaded_file is None:
        st.error("❌ Lütfen önce bir CSV veya Excel dosyası yükleyin.")

    elif question.strip() == "":
        st.warning("⚠️ Lütfen analiz etmek istediğiniz soruyu yazın.")

    else:

        with st.spinner("🤖 StatAgent analiz yapıyor..."):

            try:
                st.write("1- analizi_baslat çağrılıyor")
                sonuc = analizi_baslat(df, question)
                st.write("2- analizi_baslat bitti")
                rapor = sonuc["rapor"]
                test_sonucu = sonuc["analiz"]

                st.success("✅ Analiz tamamlandı!")

                st.divider()

                st.subheader("📊 Analiz Sonucu")

                # CrewAI sonucunu metne çevir
                sonuc_metin = rapor

                # Kodu ve metni ayır
                metin, kod = kodu_ayir(sonuc_metin)

                # Analiz açıklaması
                with st.container(border=True):
                    st.markdown(metin)
                if test_sonucu is not None:

                    st.divider()

                    st.subheader("📈 Gerçek İstatistiksel Sonuç")

                    col1, col2 = st.columns(2)

                    with col1:
                        st.metric(
            "Test",
            test_sonucu["test"]
        )

                        st.metric(
            "Test İstatistiği",
            test_sonucu["istatistik"]
        )

                    with col2:
                        st.metric(
            "p-değeri",
            test_sonucu["p"]
        )

                        st.metric(
            "Karar",
            test_sonucu["karar"]
        )

                    st.info(test_sonucu["yorum"])

                    if test_sonucu["varsayimlar"]:

                        st.markdown("### 📋 Varsayımlar")

                        for v in test_sonucu["varsayimlar"]:
                            st.write(f"• {v}")
                # Python kodu varsa açılır kutuda göster
                if kod:

                    with st.expander("💻 Kullanılan Python Kodu"):

                        st.code(kod, language="python")

                # Geçmişe ekle
                st.session_state.chat_history.append({
    "question": question,
    "answer": rapor
})

            except Exception as e:
                import traceback

                st.error("🚨 Yapay zekâ servisine şu anda ulaşılamıyor.")

                with st.expander("Teknik hata ayrıntısı"):
                    st.code(traceback.format_exc())
# ------------------------------------
# Önceki Analizler
# ------------------------------------

if st.session_state.chat_history:

    st.divider()

    st.subheader("📝 Analiz Geçmişi")

    for chat in reversed(st.session_state.chat_history):

        with st.expander(f"💬 {chat['question']}"):

            st.write(chat["answer"])