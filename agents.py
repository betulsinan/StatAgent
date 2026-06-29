import os
from crewai import Agent
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

def istatistik_uzman_ajan_olustur() -> Agent:
    return Agent(
        role="Kıdemli Biyoistatistikçi ve Veri Bilimci",
        goal="Kullanıcının sorusuna ve veri yapısına bakarak en doğru istatistiksel testi/modeli belirlemek.",
        backstory="""Sen hipotez testleri, regresyon modelleri, parametrik ve 
        parametrik olmayan testler konusunda 15 yıllık deneyime sahip bir uzmansın. 
        Varsayımları (normallik, varyans homojenliği vb.) kontrol etmeden asla 
        test önermezsin. Kararlarını her zaman gerekçelendirir ve H0/H1 hipotezlerini açıkça yazarsın.""",
        verbose=True,
        llm="gpt-4o-mini"
    )

def python_kodcu_ajan_olustur() -> Agent:
    return Agent(
        role="Python Veri Analitiği Uzmanı",
        goal="Belirlenen istatistiksel analizi gerçekleştirecek hatasız Python kodunu yazmak ve çalıştırmak.",
        backstory="""Sen pandas, scipy, statsmodels ve matplotlib konusunda uzman 
        bir Python geliştiricisisin. Temiz, yorum satırlı kod yazarsın. 
        Grafikleri her zaman 'output.png' olarak kaydedersin ve sonuçları 
        sade bir dille yorumlarsın.""",
        verbose=True,
        allow_code_execution=True,
        llm="gpt-4o-mini"
    )
    