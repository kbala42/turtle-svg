import math
from svg_turtle import SvgTurtle

# 1. Tuval Ayarları (Genişlik: 800, Yükseklik: 800)
# Not: SvgTurtle'da (0,0) noktası tuvalin tam ortasıdır.
width = 800
height = 800
t = SvgTurtle(width, height)
t.speed(0)  # En hızlı çizim modu

# --- DÜZELTME BAŞLANGICI ---
# bgcolor komutu çalışmadığı için manuel arka plan çiziyoruz
def arka_plani_boya(renk):
    # Kalemi kaldır ve sol alt köşeye git
    t.penup()
    t.goto(-width/2, -height/2) 
    t.pendown()
    
    # Rengi ayarla ve kutuyu çiz
    t.color(renk)
    t.begin_fill()
    for _ in range(4):
        t.forward(width) # Kenar uzunluğu kadar git
        t.left(90)       # Dön
    t.end_fill()
    
    # Çizim için merkeze geri dön
    t.penup()
    t.goto(0, 0) # Merkeze dön
    t.pendown()

# Önce sahneyi siyaha boyuyoruz
print("⬛ Arka plan oluşturuluyor...")
arka_plani_boya("black")
# --- DÜZELTME BİTİŞİ ---

# Renk Paleti (Neon Renkler)
colors = ["#FF007F", "#00FFFF", "#7FFF00", "#BF00FF", "#FFFF00"]

# 2. Algoritmik Çizim Fonksiyonu
def spirograph_ciz(yaricap, donus_sayisi):
    """
    İç içe döngüler kullanarak geometrik desen oluşturur.
    """
    print(f"🎨 Çizim başlıyor... Yarıçap: {yaricap}, Dönüş: {donus_sayisi}")
    
    for i in range(donus_sayisi):
        # Modüler aritmetik ile renk seçimi
        secilen_renk = colors[i % len(colors)]
        t.pencolor(secilen_renk)
        t.pensize(2)
        
        # Geometrik Hareket: Çember çiz
        t.circle(yaricap)
        
        # Açıyı değiştir (Simetri için 360/dönüş sayısı)
        aci = 360 / donus_sayisi
        t.left(aci)
        
        # İlerleme bilgisi
        if i % 10 == 0:
            print(f"   ⭕ {i}. döngü tamamlandı...")

# 3. Fonksiyonu Çalıştır
# Merkeze (0,0) konumundan çizime başlıyoruz.
# 150 birim yarıçap, 60 tekrar
spirograph_ciz(150, 60)

# 4. Çıktıyı Kaydet
filename = "dijital_sanat.svg"
t.save_as(filename)

print(f"✅ Çizim tamamlandı! Soldaki dosya listesinden '{filename}' dosyasına tıklayıp sonucu görebilirsin.")