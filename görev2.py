import cv2
import numpy as np
import os

ornek_resim = np.zeros((1000, 1000, 3), dtype=np.uint8)
ornek_resim[:, :500] = [255, 0, 0]     # Sol yarı mavi (BGR)
ornek_resim[:, 500:] = [0, 165, 255]   # Sağ yarı turuncu
cv2.imwrite("renkli_1000x1000.bmp", ornek_resim)

# 1. Renkli BMP resmini OpenCV ile aç ve ekranda göster
renkli = cv2.imread("renkli_1000x1000.bmp")
cv2.imshow("Renkli Resim (1000x1000)", renkli)

# 2. Gri tonlamaya dönüştür ve BMP formatında kaydet
gri = cv2.cvtColor(renkli, cv2.COLOR_BGR2GRAY)
cv2.imwrite("gri_1000x1000.bmp", gri)
cv2.imshow("Gri Tonlu Resim (1000x1000)", gri)

# 3. Çözünürlük, kanal sayısı ve disk boyutlarını kıyasla
renkli_boyut = os.path.getsize("renkli_1000x1000.bmp")
gri_boyut = os.path.getsize("gri_1000x1000.bmp")

print(f"Renkli Resim -> Boyut/Kanal: {renkli.shape} | Disk Boyutu: {renkli_boyut} byte ({renkli_boyut / (1024*1024):.2f} MB)")
print(f"Gri Resim    -> Boyut/Kanal: {gri.shape} | Disk Boyutu: {gri_boyut} byte ({gri_boyut / (1024*1024):.2f} MB)")
print(f"Boyut Oranı  -> Renkli resim, gri resmin yaklaşık {renkli_boyut / gri_boyut:.2f} katı yer kaplıyor.")

cv2.waitKey(0)
cv2.destroyAllWindows()

"""
ÇÖZÜNÜRLÜK, KANAL SAYISI VE DİSK BOYUTU KIYASLAMASI:

1. Çözünürlük Etkisi:
   Her iki resmin de çözünürlüğü 1000x1000 (toplam 1.000.000 piksel) olarak aynıdır.
   Yani dosya boyutları arasındaki fark çözünürlükten kaynaklanmamaktadır.

2. Kanal Sayısı Etkisi:
   - Renkli BMP resmi 3 kanallıdır (B, G, R). Her piksel için 3 byte veri tutulur.
     Hesap: 1000 x 1000 x 3 = 3.000.000 byte (BMP başlık bilgisiyle ~3.000.054 byte / ~2.86 MB).
   - Gri tonlu BMP resmi 1 kanallıdır (sadece parlaklık yoğunluğu). Her piksel için 1 byte veri tutulur.
     Hesap: 1000 x 1000 x 1 = 1.000.000 byte (BMP başlık ve palet bilgisiyle ~1.001.078 byte / ~0.95 MB).

3. Sonuç:
   BMP formatı sıkıştırma yapmadan ham piksel verisini kaydettiği için dosya boyutu
   doğrudan (Genişlik x Yükseklik x Kanal Sayısı) ile orantılıdır. Çözünürlük aynı kalsa bile
   kanal sayısı 3'ten 1'e düştüğü için gri tonlu resim diskte yaklaşık 3 kat daha az yer kaplar.
"""