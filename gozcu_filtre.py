from ultralytics import YOLO
import cv2
import os
import math
import numpy as np 

# --- AYARLAR ---
model_yolu = 'runs/detect/gozcu_tank_modeli/weights/best.pt'
video_yolu = 'test_video.mp4'
cikti_adi = 'operasyon_akilli_filtre2.mp4'

if not os.path.exists(model_yolu):
    print(f"HATA: Model dosyası bulunamadı! Yol: {model_yolu}")
    exit()

print(f"🚀 Model Yükleniyor...")
model = YOLO(model_yolu)

cap = cv2.VideoCapture(video_yolu)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

writer = cv2.VideoWriter(cikti_adi, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

print("🎥 Video işleniyor... (Boyut + Renk Filtresi Devrede)")

while cap.isOpened():
    success, frame = cap.read()
    
    if success:
        
        results = model.predict(frame, conf=0.10, verbose=False) 

        for r in results:
            boxes = r.boxes
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                
                w = x2 - x1
                h = y2 - y1
                
                # 1. BOYUT FİLTRESİ
                
                if w > 250 or h > 250: 
                    continue 
                
                if w < 25 or h < 25:
                    continue

                # 2. RENK FİLTRESİ 
               
                roi = frame[y1:y2, x1:x2]
                
                if roi.size > 0:
                    
                    hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
                    
                    
                    avg_brightness = np.mean(hsv_roi[:, :, 2])
                    
                    
                    avg_saturation = np.mean(hsv_roi[:, :, 1])

                    
                    if avg_brightness > 160 and avg_saturation < 60:
                        
                        continue

               
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                
                conf = math.ceil((box.conf[0] * 100)) / 100
                
                cv2.putText(frame, f"TANK {conf}", (x1, y1 - 10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

        writer.write(frame)

        try:
            cv2.imshow("GOZCU IHA - Akilli Filtre", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        except:
            pass
    else:
        break

cap.release()
writer.release()
cv2.destroyAllWindows()
print(f"\n✅ İşlem Tamamlandı! Video kaydedildi: {cikti_adi}")