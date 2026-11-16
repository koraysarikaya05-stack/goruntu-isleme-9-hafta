import cv2
import numpy as np
import time

# 1. 8K çözünürlükte (7680x4320) 3-kanallı örnek bir BMP resmi oluştur
genislik, yukseklik = 7680, 4320
olusturulan_resim = np.random.randint(0, 256, (yukseklik, genislik, 3), dtype=np.uint8)
cv2.imwrite("8k_orijinal.bmp", olusturulan_resim)

# 2. Oluşturulan 8K BMP resmini OpenCV ile aç (Süre ölçümüne dahil değil)
resim = cv2.imread("8k_orijinal.bmp")

# 3. SADECE düzenleme (piksel değerlerini 2'ye bölme) süresini hassas ölç
baslangic = time.perf_counter()

duzenlenmis_resim = resim // 2  # Tam sayı bölmesi ile değerleri yarıya düşürür (uint8 korunur)

bitis = time.perf_counter()
gecen_sure = bitis - baslangic

# 4. Düzenlenen resmi BMP formatında kaydet (Süre ölçümüne dahil değil)
cv2.imwrite("8k_duzenlenmis.bmp", duzenlenmis_resim)

print(f"Görüntü Boyutu (Yükseklik, Genişlik, Kanal): {resim.shape}")
print(f"Piksel değerlerini 2'ye bölme süresi: {gecen_sure:.6f} saniye ({gecen_sure * 1000:.2f} ms)")

"""
NOT:
- 8K çözünürlük 7680 x 4320 pikseldir. 3 kanal ile birlikte toplam 99.532.800 piksel/kanal değeri işlenir.
- time.perf_counter() fonksiyonu, işlemci saatini kullanarak nanosaniye hassasiyetinde ölçüm yaptığı için
  time.time() fonksiyonuna göre çok daha hassas sonuç verir.
- "// 2" (tam sayı bölmesi) kullanıldığı için piksel değerleri ondalıklı sayıya (float) dönüşmeden
  doğrudan 0-127 aralığında uint8 olarak kalır ve görüntü parlaklığı yarıya iner.
"""