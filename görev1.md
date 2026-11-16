1. RGB (Red, Green, Blue)
Kameraların ve ekranların doğrudan kullandığı temel renk uzayıdır. Kırmızı, yeşil ve mavi ışıkların farklı oranlarda karışmasıyla diğer tüm renkleri oluşturur.

Avantajları: Ekstra dönüşüm gerektirmez, ekranlar ve kameralar zaten bu formatta çalışır. Anlaması ve kullanması basittir.
Dezavantajları: Renk bilgisiyle ışık (parlaklık) bilgisi birbirine karışıktır. Ortam ışığı azaldığında veya arttığında 3 kanalın da değeri değişir; bu yüzden renk takibi yapmak zorlaşır.
Tercih edildiği problemler: Görüntüyü ekranda göstermede, dosya kaydetmede ve derin öğrenme modellerine görsel verirken kullanılır.


2. HSV (Hue, Saturation, Value)
İnsan gözünün rengi algılama şekline daha yakın bir sistemdir. H (Hue) rengin kendisini, S (Saturation) rengin canlılığını/doygunluğunu, V (Value) ise parlaklığını tutar.

Avantajları: Rengi parlaklıktan ayırır. Ortam ışığı değişse veya gölge düşse bile rengin özü (H kanalı) kolay kolay bozulmaz.
Dezavantajları: RGB'den dönüştürürken ekstra matematiksel işlem gerekir. Ayrıca kırmızı renk 0 ve 360 derece uçlarında kaldığı için filtreleme yaparken iki ayrı aralık yazmak gerekir.
Tercih edildiği problemler: Renk tabanlı nesne takibinde (örneğin yeşil top takibi veya yeşil perde işlemleri) ve renk filtrelemede tercih edilir.


3. YUV / YCbCr
Televizyon yayınları ve video sıkıştırma için geliştirilmiştir. Y kanalı siyah-beyaz parlaklık bilgisini, U ve V (veya Cb ve Cr) kanalları ise renk bilgisini taşır.

Avantajları: Parlaklık ile rengi birbirinden tamamen ayırır. İnsan gözü parlaklığa daha duyarlı olduğu için renk kanallarının kalitesi biraz düşürülerek dosya boyutu ciddi oranda küçültülebilir.
Dezavantajları: Kanallara tek tek bakıldığında insan gözüyle ne olduğunu anlamak zordur.
Tercih edildiği problemler: JPEG resim ve MPEG/H.264 video sıkıştırma algoritmalarında ve aydınlatma farkından etkilenmeyen insan teni tespitinde kullanılır.


4. CIE Lab
İnsan gözünün görebildiği tüm renkleri kapsayan ve cihazdan bağımsız çalışan (her ekranda veya yazıcıda aynı sonucu vermeyi amaçlayan) bir uzaydır. L açıklık/parlaklık, a yeşil-kırmızı ekseni, b ise mavi-sarı eksenidir.

Avantajları: İki renk arasındaki matematiksel fark, insan gözünün algıladığı farkla birebir örtüşür. Renkleri bozmadan sadece parlaklık (L) üzerinde oynama yapmaya imkan tanır.
Dezavantajları: Dönüşüm formülleri karmaşıktır, işlemciyi diğerlerine göre biraz daha fazla yorar.
Tercih edildiği problemler: İki nesne arasındaki renk farkını hassas ölçmede, renk eşleştirmede ve renkleri bozmadan kontrast artırma işlemlerinde kullanılır.


5. Grayscale (Gri Tonlama)
Renk bilgisini tamamen atıp sadece siyah ile beyaz arasındaki ışık şiddetini (0-255 arası tek bir değer) tutan formattır.

Avantajları: 3 kanal yerine tek kanal olduğu için hafızada 3 kat az yer kaplar ve kodlar çok daha hızlı çalışır.
Dezavantajları: Tüm renk bilgisi kaybolur; aynı parlaklıktaki kırmızı ile yeşil nesne birbirinden ayırt edilemez.
Tercih edildiği problemler: Kenar bulma (Canny, Sobel), plaka/yazı okuma (OCR), barkod okuma ve rengin önemli olmadığı şekil veya yüz tanıma işlemlerinde kullanılır.


Özet: Hangi Problemde Hangi Renk Uzayı Tercih Edilir?

- Görüntüyü ekranda gösterme ve ham dosya kaydetme: RGB (Kamera ve ekranların doğal formatı olduğu için)
- Renk bazlı nesne takibi ve renk filtreleme: HSV (Rengi ve parlaklığı ayırdığı için gölge ve ışık değişimlerinden en az bu uzay etkilenir)
- İnsan teni tespiti: YCbCr ve HSV (Farklı ten renkleri ve ışık koşulları altında bile cilt tonları bu uzaylarda çok dar ve net bir aralığa sıkışır)
- Video ve fotoğraf sıkıştırma (JPEG, MPEG): YUV / YCbCr (İnsan gözü renk kaybını parlaklık kaybı kadar fark etmediği için renk kanalları sıkıştırılarak boyut düşürülür)
- Renk farkı ölçme ve renkleri bozmadan kontrast artırma: CIE Lab (İnsan gözünün renk algısıyla birebir uyumlu olduğu ve parlaklık kanalını ayrı tuttuğu için)
- Kenar bulma, plaka/yazı okuma ve şekil analizi: Grayscale (Rengin önemsiz olduğu yerlerde tek kanalla çalışarak işlem hızını 3 kat artırmak için)