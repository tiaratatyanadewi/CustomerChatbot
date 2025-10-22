#💬 CUSTOMER SERVICE CHATBOT

Chatbot sederhana untuk mencatat keluhan atau pertanyaan pelanggan, dibangun dengan Streamlit, OpenAI API, dan SQLite.


🚀 CARA MENJALANKAN

1. Install dependency:
   pip install streamlit openai python-dotenv pandas

2. Buat file .env:
   OPENAI_API_KEY=your_openai_api_key_here

3. Jalankan aplikasi:
   streamlit run app.py


⚙️ FITUR

- Mode USER → kirim keluhan atau pertanyaan
- Mode ADMIN → lihat semua data keluhan dari database
- Data otomatis disimpan ke SQLite (customer_service.db)


🧩 STRUKTUR FILE

app.py                -> File utama Streamlit
customer_service.db   -> Database SQLite (otomatis dibuat)
.env                  -> Menyimpan API Key OpenAI
requirements.txt      -> Daftar dependency


🔐 DEFAULT LOGIN ADMIN

username: admin
password: admin123
