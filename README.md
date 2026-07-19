# Takım İsmi
Grup 321

# Takım Elemanları
- Product Owner: Amina Betül Sinan
- Scrum Master: Ayşenur Şeker

# Ürün İsmi
StatAgent – Akıllı İstatistiki Veri Analizi ve Modelleme Ajanı

# Ürün Açıklaması
StatAgent, kullanıcıların yüklediği CSV veya Excel veri setlerini yapay zekâ destekli ajanlar aracılığıyla analiz eden akıllı bir veri analizi platformudur. Sistem, veri setini otomatik olarak inceleyerek eksik verileri ve değişken tiplerini belirler, kullanıcının doğal dilde sorduğu istatistiksel sorulara uygun analiz yöntemini seçer ve Python tabanlı analizleri gerçekleştirerek sonuçları grafikler ve yorumlarla birlikte sunar.

# Ürün Özellikleri
- CSV ve Excel veri seti yükleme
- Otomatik veri profilleme
- Eksik veri analizi
- Yapay zekâ destekli istatistiksel test seçimi
- Python ile otomatik analiz yürütme
- Grafik ve istatistiksel rapor oluşturma
- Çok ajanlı (CrewAI) mimari
- Hafıza (Memory) desteği ile geçmiş analizleri hatırlama

# Hedef Kitle
- Araştırmacılar
- Üniversite öğrencileri
- Veri analistleri
- Küçük işletmeler
- Start-up ekipleri
- İstatistik bilgisi sınırlı kullanıcılar
  
# Kullanılan Teknolojiler
- Python
- Streamlit
- CrewAI
- LangChain
- Pandas
- SciPy
- Statsmodels
- Matplotlib
- ChromaDB
- OpenAI API
  
# Sprint 1
# Sprint Notları

Sprint 1 kapsamında projenin temel mimarisi planlanmış ve Product Backlog oluşturulmuştur. Çok ajanlı sistem tasarımı belirlenmiş, ajanların görevleri tanımlanmış ve geliştirme ortamı hazırlanmıştır. Sprint boyunca öncelik, CrewAI tabanlı çalışan çekirdek sistemin oluşturulmasına verilmiştir.

# Sprint İçinde Tamamlanması Tahmin Edilen Puan
100 Puan

# Puan Tamamlama Mantığı
Toplam Product Backlog yaklaşık 300 puan olarak planlanmıştır. Bootcamp süreci üç sprintten oluştuğu için her sprint yaklaşık 100 puanlık iş yükü içermektedir. Story puanları takım üyeleri tarafından ortak değerlendirme ile belirlenmiştir.

# Sprint Backlog
Bu sprintte tamamlanması hedeflenen çalışmalar:
- Product Backlog oluşturulması
- GitHub repository oluşturulması
- Geliştirme ortamının hazırlanması
- Gerekli Python kütüphanelerinin kurulması
- CrewAI mimarisinin oluşturulması
- Statistician Agent tasarımı
- Data Profiler Agent tasarımı
- Python Coder Agent tasarımı
- Agent görevlerinin (Task) oluşturulması
- İlk terminal tabanlı prototipin geliştirilmesi
- CSV veri seti ile ilk testlerin gerçekleştirilmesi

  
# Daily Scrum

Takım üyelerinin farklı ders programlarına sahip olması nedeniyle Daily Scrum toplantılarının Slack üzerinden gerçekleştirilmesine karar verilmiştir. Günlük toplantılarda tamamlanan görevler, karşılaşılan problemler ve ertesi gün yapılacak çalışmalar paylaşılmıştır.

<img width="1335" height="780" alt="Screenshot 2026-07-05 151753" src="https://github.com/user-attachments/assets/38601246-fb70-4c30-b3d2-46c06a64fe09" />
<img width="600" height="450" alt="image" src="https://github.com/user-attachments/assets/cf0d3e1c-df6b-43ed-9a67-7ca3edea18e8" />

📄 [Daily Scrum Meeting Notes - Sprint 1](https://github.com/betulsinan/StatAgent/blob/main/DailyScrumMeetingNotesSprint1.pdf)


# Sprint Board Update

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/558b7e08-cd6e-4309-b6bd-8c053f86cc69" />



# Ürün Durumu

Sprint sonunda aşağıdaki çıktılar elde edilmiştir:
- Proje mimarisi tamamlandı.
- CrewAI tabanlı ajan yapısı oluşturuldu.
- Statistician Agent geliştirildi.
- Python Coder Agent geliştirildi.
- İlk görev (Task) yapıları oluşturuldu.
- CSV dosyaları terminal üzerinden okunarak test edildi.
- İlk analiz çıktıları başarıyla üretildi.

<img width="1600" height="850" alt="WhatsApp Image 2026-07-03 at 4 54 52 PM (1)" src="https://github.com/user-attachments/assets/0dc2f473-fefb-4c44-846c-08a0a8dec728" />
<img width="1600" height="850" alt="WhatsApp Image 2026-07-03 at 4 54 52 PM (2)" src="https://github.com/user-attachments/assets/1539a1c2-f2a6-4d30-a11b-392c6d6fbfa1" />
<img width="1600" height="850" alt="WhatsApp Image 2026-07-03 at 4 54 52 PM (3)" src="https://github.com/user-attachments/assets/3f877a66-6a46-49d4-9edb-1b6c33bb6962" />
<img width="1600" height="850" alt="WhatsApp Image 2026-07-03 at 4 54 52 PM (4)" src="https://github.com/user-attachments/assets/07d3a36e-98c0-4e4c-aaa5-c5852d7e999f" />
<img width="1600" height="850" alt="WhatsApp Image 2026-07-03 at 4 54 52 PM" src="https://github.com/user-attachments/assets/6c9d3887-6f80-48b7-89ea-b8e6bcf45a74" />


# Sprint Review
Sprint hedeflerinin büyük bölümü başarıyla tamamlanmıştır. Ajan mimarisinin beklendiği şekilde çalıştığı görülmüş ve terminal ortamında ilk analizler başarıyla gerçekleştirilmiştir. Bir sonraki sprintte sistemin Streamlit arayüzüne taşınmasına ve kullanıcı etkileşiminin geliştirilmesine karar verilmiştir.

# Sprint Review Katılımcıları
- Product Owner
- Scrum Master


# Sprint Retrospective
Git commitlerinin daha küçük ve düzenli yapılması kararlaştırıldı.
Kod dokümantasyonunun geliştirilmesine karar verildi.
Bir sonraki sprintte Streamlit arayüzünün öncelikli geliştirme hedefi olması kararlaştırıldı.
Memory (ChromaDB) entegrasyonunun Sprint 2'de tamamlanmasına karar verildi.


# Sprint 2
# Sprint Notları

Sprint 2 (6 Temmuz - 19 Temmuz) kapsamında proje, terminal tabanlı bir prototipten kullanıcı dostu, web tabanlı bir ürüne dönüştürülmüştür. Bu sprintte öncelik, Streamlit tabanlı arayüzün geliştirilmesine ve istatistiksel görselleştirme yeteneklerinin güçlendirilmesine verilmiştir. Kılavuzda +15 ekstra puan kazandıran ajan hafızası (ChromaDB) özelliğinin bu sprintte tam olarak tamamlanamayacağı öngörülmüş ve bu iş kalemi Sprint 3'e ertelenmiştir.

# Sprint İçinde Tamamlanması Tahmin Edilen Puan
100 Puan

# Puan Tamamlama Mantığı
Toplam Product Backlog yaklaşık 300 puan olarak planlanmıştır. Sprint 2, bootcamp sürecinin ikinci sprinti olduğu için yaklaşık 100 puanlık iş yükü hedeflenmiştir. Story puanları takım üyeleri tarafından ortak değerlendirme ile belirlenmiştir.

# Sprint Backlog
Bu sprintte tamamlanması hedeflenen çalışmalar:
- Streamlit tabanlı web arayüzünün tasarlanması ve geliştirilmesi
- Sürükle-bırak yöntemiyle CSV veri seti yükleme alanının oluşturulması
- Analiz sonuçlarını gösteren görsel panel (dashboard) tasarımı — yan menüler, butonlar, Markdown formatlı çıktılar
- Kullanıcının web arayüzü üzerinden ajanlara doğrudan talimat/soru gönderebilmesi
- Matplotlib/Seaborn ile gelişmiş istatistiksel görselleştirme (bar chart, box plot, dağılım ve anomali grafikleri)
- Statistics Engine modülünün geliştirilmesi (statistics_engine.py)
- Uçtan uca analiz akışının bağlanması (analysis.py)
- ~~ChromaDB tabanlı agent hafızası entegrasyonu~~ → **Sprint 3'e ertelendi**
- Ortam değişkenlerinin (.env) güvenli şekilde yönetilmesi

# Daily Scrum

Sprint 1'de olduğu gibi Daily Scrum toplantıları Slack üzerinden gerçekleştirilmeye devam edilmiştir. Günlük toplantılarda tamamlanan görevler, karşılaşılan problemler ve ertesi gün yapılacak çalışmalar paylaşılmıştır.

📄 [Daily Scrum Meeting Notes - Sprint 2](LINK_EKLE)

# Sprint Board Update

[EKRAN GÖRÜNTÜSÜ EKLE]

# Ürün Durumu

Sprint sonunda aşağıdaki çıktılar elde edilmiştir:
- Streamlit tabanlı web arayüzü tamamlandı; kullanıcılar CSV dosyalarını sürükle-bırak ile yükleyebiliyor.
- Analiz sonuçları görsel panel üzerinden şık butonlar, yan menüler ve Markdown formatında sunuluyor.
- Kullanıcılar arayüz üzerinden ajanlara doğrudan yeni talimat/soru gönderebiliyor.
- İstatistiksel analiz motoru (statistics_engine.py) geliştirildi.
- Matplotlib/Seaborn ile gelişmiş görselleştirme modülleri (visualization.py, graphs.py) entegre edildi; departman bazlı ortalamalar, dağılımlar ve anomaliler grafiklerle gösterilebiliyor.
- Uçtan uca analiz akışı (analysis.py) bağlandı.
- ChromaDB tabanlı ajan hafızası bu sprintte tamamlanamamış, kapsam Sprint 3'e taşınmıştır.

[EKRAN GÖRÜNTÜSÜ / GIF EKLE]

# Sprint Review
Sprint hedeflerinin büyük bölümü başarıyla tamamlanmıştır. Streamlit arayüzü beklenen şekilde çalışmış, kullanıcılar veri yükleyip analiz sonuçlarını görsel olarak inceleyebilir hale gelmiştir. Ajan hafızası (ChromaDB) özelliğinin bu sprintte yetiştirilemeyeceği anlaşılmış ve kapsam planlaması gereği Sprint 3'e ertelenmesine karar verilmiştir. Bir sonraki sprintte öncelik, kısa ve uzun vadeli hafıza entegrasyonu ile ajan orkestrasyonunun tamamlanmasına verilecektir.

# Sprint Review Katılımcıları
- Product Owner
- Scrum Master

# Sprint Retrospective
- .env dosyasının yanlışlıkla commit edilmesi sonucu GitHub Push Protection devreye girmiş; bu konuda .gitignore kullanımı ve hassas bilgi yönetimi konusunda farkındalık artırılmıştır.
- Memory (ChromaDB) özelliğinin kapsamının Sprint 2 için fazla iddialı olduğu görülmüş, bir sonraki sprint planlamasında iş kalemlerinin daha gerçekçi tahmin edilmesine karar verilmiştir.
- Commit'lerin daha küçük parçalar halinde ve daha sık yapılmasına karar verilmiştir.
