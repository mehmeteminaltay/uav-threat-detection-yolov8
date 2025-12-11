# UAV Target Detection & Filtering System (YOLOv8 + OpenCV)

![Status](https://img.shields.io/badge/Status-Completed-success) ![Python](https://img.shields.io/badge/Python-3.11-blue) ![Technology](https://img.shields.io/badge/Tech-YOLOv8%20%7C%20OpenCV-orange)

## 🌍 Project Overview (English)
This project aims to detect armored vehicles (tanks) in real-time using drone footage for defense industry applications. Due to the geometric similarities between ruined structures/civilian vehicles and tanks in aerial views, a standard AI model often produces "False Positives". 

To solve this, a **Hybrid Filtering Algorithm** was developed using **OpenCV**:
1.  **Deep Learning:** YOLOv8n custom trained model detects potential targets.
2.  **Post-Processing:**
    * **Geometric Filter:** Eliminates objects that are too large (buildings) or too small (noise).
    * **Color Filter (HSV):** Filters out bright white/grey civilian vehicles based on saturation and brightness levels.

---

## 🇹🇷 Proje Detayları ve Teknik Rapor (Turkish)

### 1. Projenin Amacı
İnsansız Hava Araçları (İHA) görüntülerinde, askeri unsurların (Tank, Zırhlı Araç) sivil unsurlardan (Bina, Sivil Araç) ayırt edilmesi hedeflenmiştir.

### 2. Kullanılan Yöntemler
* **Model Eğitimi:** Roboflow üzerinden temin edilen askeri veri seti ile YOLOv8 Nano modeli RTX 2060 GPU üzerinde eğitilmiştir.
* **Sorun Tespiti:** Modelin, yıkık binaları ve beyaz sivil araçları tank olarak algıladığı (False Positive) görülmüştür.
* **Mühendislik Çözümü:**
    * `cv2.inRange` ve HSV dönüşümü kullanılarak **Renk Filtresi** geliştirildi.
    * Bounding Box boyutlarına göre **Geometrik Eşik Değeri** belirlendi.

### 3. Sonuç
Filtreleme sonrası sistem, sivil araçları ve binaları başarılı bir şekilde eleyerek sadece hedef odaklı tespit yapabilir hale gelmiştir.

---

### 💻 Nasıl Çalıştırılır? (How to Run)

1.  Gerekli kütüphaneleri yükleyin:
    ```bash
    pip install -r requirements.txt
    ```

2.  Eğitilmiş model dosyasını (`best.pt`) projenin ana dizinine veya belirtilen klasöre yerleştirin.

3.  Filtreleme kodunu çalıştırın:
    ```bash
    python gozcu_filtre.py
    ```

---
*Created by Mehmet Emin Altay*
