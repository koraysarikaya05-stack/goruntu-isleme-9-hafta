import cv2
import numpy as np
import os

# Kodun bulunduğu klasör yolunu al
klasor = os.path.dirname(os.path.abspath(__file__))

# Klasördeki 'renkliresim.jpg' dosyasını oku ve ödev gereği önce RGB BMP olarak kaydet
kaynak_jpg = os.path.join(klasor, "renkliresim.jpg")
girdi_bmp = os.path.join(klasor, "orijinal_rgb.bmp")

gecici_resim = cv2.imread(kaynak_jpg)
if gecici_resim is None:
    raise FileNotFoundError(f"'{kaynak_jpg}' bulunamadı! Dosya adını ve uzantısını kontrol et.")

cv2.imwrite(girdi_bmp, gecici_resim)

# 1. RGB (OpenCV BGR sırasıyla okur) BMP görüntüsünü aç
bgr_resim = cv2.imread(girdi_bmp)

# 2. HSV Dönüşümü ve BMP Kaydı
hsv_resim = cv2.cvtColor(bgr_resim, cv2.COLOR_BGR2HSV)
cv2.imwrite(os.path.join(klasor, "sonuc_hsv.bmp"), hsv_resim)

# 3. YUV Dönüşümü ve BMP Kaydı
yuv_resim = cv2.cvtColor(bgr_resim, cv2.COLOR_BGR2YUV)
cv2.imwrite(os.path.join(klasor, "sonuc_yuv.bmp"), yuv_resim)

# 4. CIE Lab Dönüşümü ve BMP Kaydı
lab_resim = cv2.cvtColor(bgr_resim, cv2.COLOR_BGR2Lab)
cv2.imwrite(os.path.join(klasor, "sonuc_cielab.bmp"), lab_resim)

# 5. HSI Dönüşümü (OpenCV'de hazır fonksiyon olmadığı için matematiksel formülle hesaplanır)
def bgr_to_hsi(bgr):
    img = bgr.astype(np.float32) / 255.0
    B, G, R = img[:, :, 0], img[:, :, 1], img[:, :, 2]

    # Intensity (Parlaklık)
    I = (R + G + B) / 3.0

    # Saturation (Doygunluk)
    min_rgb = np.minimum(np.minimum(R, G), B)
    toplam = R + G + B + 1e-6
    S = 1.0 - (3.0 * min_rgb / toplam)

    # Hue (Renk Özü)
    pay = 0.5 * ((R - G) + (R - B))
    payda = np.sqrt((R - G) ** 2 + (R - B) * (G - B)) + 1e-6
    theta = np.arccos(np.clip(pay / payda, -1.0, 1.0))

    H = np.where(B <= G, theta, (2 * np.pi) - theta)
    H = H / (2 * np.pi)  # 0-1 aralığına normalize et

    hsi = np.stack([H * 255, S * 255, I * 255], axis=-1).astype(np.uint8)
    return hsi

hsi_resim = bgr_to_hsi(bgr_resim)
cv2.imwrite(os.path.join(klasor, "sonuc_hsi.bmp"), hsi_resim)

print("İşlem başarılı! 'orijinal_rgb.bmp' ve 4 renk uzayı dönüşümü (.bmp) klasöre kaydedildi.")