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

<img width="1361" height="744" alt="image" src="https://github.com/user-attachments/assets/139ce12d-724f-4355-bd67-272909c31eee" />
<img width="1197" height="944" alt="image" src="https://github.com/user-attachments/assets/cf0d3e1c-df6b-43ed-9a67-7ca3edea18e8" />



# Sprint Board Update

Sprint Board aşağıdaki sütunlardan oluşmaktadır:

Backlog
To Do
In Progress
Review
Done

(Buraya Trello / Jira / GitHub Projects ekran görüntüleri eklenecek.)

# Ürün Durumu

Sprint sonunda aşağıdaki çıktılar elde edilmiştir:
- Proje mimarisi tamamlandı.
- CrewAI tabanlı ajan yapısı oluşturuldu.
- Statistician Agent geliştirildi.
- Python Coder Agent geliştirildi.
- İlk görev (Task) yapıları oluşturuldu.
- CSV dosyaları terminal üzerinden okunarak test edildi.
- İlk analiz çıktıları başarıyla üretildi.

(Buraya terminal çıktısı veya ekran görüntüleri eklenecek.)

# Sprint Review
Sprint hedeflerinin büyük bölümü başarıyla tamamlanmıştır. Ajan mimarisinin beklendiği şekilde çalıştığı görülmüş ve terminal ortamında ilk analizler başarıyla gerçekleştirilmiştir. Bir sonraki sprintte sistemin Streamlit arayüzüne taşınmasına ve kullanıcı etkileşiminin geliştirilmesine karar verilmiştir.

# Sprint Review Katılımcıları
Product Owner
Scrum Master
Tüm geliştiriciler

# Sprint Retrospective
Git commitlerinin daha küçük ve düzenli yapılması kararlaştırıldı.
Kod dokümantasyonunun geliştirilmesine karar verildi.
Bir sonraki sprintte Streamlit arayüzünün öncelikli geliştirme hedefi olması kararlaştırıldı.
Memory (ChromaDB) entegrasyonunun Sprint 2'de tamamlanmasına karar verildi.
