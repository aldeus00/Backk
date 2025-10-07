import os
import sys
import subprocess

# --------------------------
# 1️⃣ Sanal ortam oluştur
# --------------------------
VENV_DIR = "venv"

if not os.path.exists(VENV_DIR):
    print("⚡ Sanal ortam oluşturuluyor...")
    subprocess.run([sys.executable, "-m", "venv", VENV_DIR])
else:
    print("✅ Sanal ortam mevcut")

# Aktif etme yolu (Linux/WSL)
activate_path = os.path.join(VENV_DIR, "bin", "activate_this.py")
if not os.path.exists(activate_path):
    # Windows
    activate_path = os.path.join(VENV_DIR, "Scripts", "activate_this.py")

with open(activate_path) as f:
    exec(f.read(), {"__file__": activate_path})

# --------------------------
# 2️⃣ Paketleri yükle
# --------------------------
print("⚡ Gerekli paketler yükleniyor...")
requirements = [
    "pyrogram==2.0.106",
    "pytgcalls==3.0.0.dev6",
    "motor==3.3.1",
    "pymongo==4.5.0",
    "python-dotenv==1.0.1",
    "yt-dlp==2024.12.13",
    "tgcrypto==1.2.5",
    "aiohttp==3.10.11",
    "ffmpeg-python==0.2.0"
]

subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
subprocess.run([sys.executable, "-m", "pip", "install"] + requirements)

# --------------------------
# 3️⃣ Klasörler ve __init__.py
# --------------------------
folders = ["core", "player", "strings", "downloads"]
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    init_file = os.path.join(folder, "__init__.py")
    if not os.path.exists(init_file):
        open(init_file, "w").close()
        print(f"✅ {folder}/__init__.py oluşturuldu")

# --------------------------
# 4️⃣ .env kontrol
# --------------------------
if not os.path.exists(".env"):
    print("❌ .env dosyası bulunamadı! Lütfen oluşturun ve gerekli değişkenleri ekleyin.")
    print("Örnek .env içeriği:")
    print("""
API_ID=123456
API_HASH=abcdef
BOT_TOKEN=123456:ABC-DEF123
ASSISTANT_SESSION=abcdef123
MONGO_DB_URI=mongodb+srv://user:pass@cluster.mongodb.net/neva
DOWNLOADS_DIR=downloads
ADMINS=123456789
OWNER_ID=123456789
LOG_GROUP_ID=-1001234567890
""")
    sys.exit(1)

# --------------------------
# 5️⃣ Botu başlat
# --------------------------
print("🎵 Neva bot başlatılıyor...")
subprocess.run([sys.executable, "bot.py"])
