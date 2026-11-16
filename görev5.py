import cv2
import numpy as np
import os

# Kodun bulunduğu klasör yolunu al
klasor = os.path.dirname(os.path.abspath(__file__))

resim_yolu = os.path.join(klasor, "insanlar.jpg")
bgr = cv2.imread(resim_yolu)

# ==========================================
# 1. RGB RENK UZAYINDA TEN TESPİTİ
# ==========================================
B, G, R = cv2.split(bgr)

# Taşma (overflow) olmaması için int16'ya çevirip kuralları uygula
R_int = R.astype(np.int16)
G_int = G.astype(np.int16)
B_int = B.astype(np.int16)

max_rgb = np.maximum(np.maximum(R_int, G_int), B_int)
min_rgb = np.minimum(np.minimum(R_int, G_int), B_int)

rgb_maske = (
    (R_int > 95) &
    (G_int > 40) &
    (B_int > 20) &
    ((max_rgb - min_rgb) > 15) &
    (np.abs(R_int - G_int) > 15) &
    (R_int > G_int) &
    (R_int > B_int)
)

rgb_sonuc = bgr.copy()
rgb_sonuc[~rgb_maske] = [0, 0, 255]  # Ten olmayan yerleri tam kırmızı yap (BGR: 0, 0, 255)

# ==========================================
# 2. YCbCr RENK UZAYINDA TEN TESPİTİ
# ==========================================
# Not: OpenCV YCrCb sırasında döndürür (0: Y, 1: Cr, 2: Cb)
ycrcb = cv2.cvtColor(bgr, cv2.COLOR_BGR2YCrCb)
Y, Cr, Cb = cv2.split(ycrcb)

ycbcr_maske = (
    (Y > 80) &
    (Cr >= 133) & (Cr <= 173) &
    (Cb >= 77) & (Cb <= 127)
)

ycbcr_sonuc = bgr.copy()
ycbcr_sonuc[~ycbcr_maske] = [0, 0, 255]

# ==========================================
# 3. HSV RENK UZAYINDA TEN TESPİTİ
# ==========================================
hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
H, S, V = cv2.split(hsv)

hsv_maske = (
    (H >= 0) & (H <= 25) &
    (S >= 15) & (S <= 170) &
    (V > 50)
)

hsv_sonuc = bgr.copy()
hsv_sonuc[~hsv_maske] = [0, 0, 255]

# Sonuçları kaydet ve ekranda göster
cv2.imwrite(os.path.join(klasor, "ten_tespit_rgb.jpg"), rgb_sonuc)
cv2.imwrite(os.path.join(klasor, "ten_tespit_ycbcr.jpg"), ycbcr_sonuc)
cv2.imwrite(os.path.join(klasor, "ten_tespit_hsv.jpg"), hsv_sonuc)

cv2.imshow("1 - RGB Ten Tespiti", rgb_sonuc)
cv2.imshow("2 - YCbCr Ten Tespiti", ycbcr_sonuc)
cv2.imshow("3 - HSV Ten Tespiti", hsv_sonuc)

print("Tüm sonuçlar kaydedildi: ten_tespit_rgb.jpg, ten_tespit_ycbcr.jpg, ten_tespit_hsv.jpg")

cv2.waitKey(0)
cv2.destroyAllWindows()

"""
KARŞILAŞTIRMA YORUMU:
- RGB uzayında parlaklık ve renk bilgisi birbirine karışık olduğu için koyu ten tonları veya
  gölgede kalan yüz kısımları maske dışında kalabilmekte, turuncu/sarı arka planlar ise ten sanılabilmektedir.
- YCbCr ve HSV uzayları ise ışık şiddetini (Y ve V) renk bilgisinden ayırdığı için farklı aydınlatma
  koşullarında ve farklı ten renklerinde yüzleri çok daha tutarlı şekilde ayırt eder.
"""