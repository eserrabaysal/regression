🏨 Otel Rezervasyon Tahmini Projesi
Bu proje, sanal olarak oluşturulmuş otel rezervasyon verileriyle çalışarak müşterinin rezervasyon yapma olasılığını tahmin etmeyi amaçlamaktadır. Jupyter Notebook ortamında geliştirilmiş bu proje, veri analizi, makine öğrenmesi modelleri ve en sonunda web üzerinde kullanıcıya tahmin sunan bir arayüz içermektedir.

📌 Proje Özeti
Bu proje kapsamında:

Sanal (dummy) veriler ile bir otel rezervasyon dataseti oluşturuldu

Veriler üzerinde analiz ve ön işleme (feature engineering) işlemleri yapıldı

Makine öğrenmesi modelleri (örneğin Logistic Regression, Random Forest) kullanılarak tahminleme yapıldı

Kullanıcıdan bilgi alan ve tahmin sonucunu gösteren basit bir web arayüzü geliştirildi (Streamlit ile)

🔍 Veri Kümesi
Bu projede kullanılan veri seti, gerçek kullanıcı verisi değil; benzetim (simülasyon) amaçlı rastgele oluşturulmuş sanal verilerden oluşmaktadır. Bu sayede kişisel veri içermeden tahmin modelleri geliştirildi.


🤖 Modelleme Süreci
Notebook dosyasında aşağıdaki adımlar gerçekleştirildi:

Verinin Yüklenmesi ve Temizlenmesi

Görselleştirmeler ile Veri Analizi

Makine Öğrenmesi Modeli Eğitimi

Modelin Başarı Değerlendirmesi

Eğitilen modelin .pkl dosyası olarak kaydedilmesi

🌐 Web Arayüzü
Eğitilen model, Streamlit kullanılarak hazırlanan kullanıcı arayüzü ile entegre edildi. Kullanıcı, bazı bilgileri (yaş, ödeme türü vb.) girerek rezervasyonun iptal edilip edilmeyeceğini tahmin edebilir.

Web Arayüzünü Çalıştırmak için:
bash
Kopyala
Düzenle
cd app
streamlit run app.py
Arayüz açıldığında tarayıcınızda otomatik olarak gösterilecektir.

💬 Katkı Sağlayın
Her türlü katkıya açığım! Yeni veri setleri, görselleştirme önerileri veya model iyileştirmeleri gibi her fikir değerlidir.

📧 İletişim
Herhangi bir sorunuz veya öneriniz varsa benimle iletişime geçebilirsiniz:
📩 serrabaysal@gmail.com
