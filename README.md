# 💬 Customer Service Chatbot

Chatbot sederhana untuk mencatat **keluhan atau pertanyaan pelanggan**, dibangun dengan **Streamlit**, **OpenAI API**, dan **SQLite**.\

VIDEO DEMO: https://drive.google.com/file/d/1aCVFeiZUJjuWBQ0xDtJl8FfuhyW27gjh/view?usp=sharing

---

## 🚀 Cara Menjalankan

1. **Install dependency**
   pip install streamlit openai python-dotenv pandas

2. **Buat file `.env`**
   OPENAI_API_KEY=your_openai_api_key_here

3. **Jalankan aplikasi**
   streamlit run app.py

---

## ⚙️ Fitur

- 🧍 User Mode — kirim keluhan atau pertanyaan pelanggan  
- 🧑‍💼 Admin Mode — lihat semua data keluhan dari database  
- 💾 Data otomatis disimpan ke SQLite (customer_service.db)  
- 🤖 Chat interaktif dengan model OpenAI  

---

## 🗂️ Struktur File

app.py                # File utama Streamlit  
customer_service.db   # Database SQLite (otomatis dibuat)  
.env                  # Menyimpan API Key OpenAI  
requirements.txt      # Daftar dependency  

---

## 🔐 Default Login Admin

username: admin  
password: admin123  

