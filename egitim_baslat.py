from ultralytics import YOLO
from roboflow import Roboflow

# Windows multiprocessing hatası için bu blok zorunludur
if __name__ == '__main__':
    
    # --- 1. VERİ SETİ İNDİRME ---
    # NOT: Roboflow'dan aldığın "Download Code" kısmını buraya yapıştırmalısın.
    # Örnek:
    # rf = Roboflow(api_key="SENIN_KEYIN")
    # project = rf.workspace("...").project("...")
    # dataset = project.version(1).download("yolov8")
    
    print("⚠️ Lütfen Roboflow kodunu buraya yapıştırdığından emin ol!") 
    
    # --- 2. MODELİ HAZIRLA ---
    print("\n🚀 Model Yükleniyor...")
    model = YOLO('yolov8n.pt') 

    # --- 3. EĞİTİMİ BAŞLAT ---
    print("\n🔥 Eğitim Başlıyor! Ekran kartın ısınabilir...")

    # 'dataset' değişkeninin yukarıdaki Roboflow kodundan geldiğine emin ol
    # Eğer dataset inmişse ve tekrar indirmek istemiyorsan data yolunu manuel verebilirsin
    try:
        data_path = f"{dataset.location}/data.yaml"
    except NameError:
        # Roboflow kodu yoksa manuel yol (Kendi yolunu yaz)
        data_path = "C:/Users/Tutunamadim/Desktop/YOLOv8/TANK-1/data.yaml"

    results = model.train(
        data=data_path,
        epochs=50,       
        imgsz=640,      
        device=0,       
        batch=16,       
        name='gozcu_tank_modeli',
        workers=4        
    )

    print("✅ Eğitim Tamamlandı!")