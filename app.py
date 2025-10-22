import streamlit as st
import sqlite3
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def init_db():
    conn = sqlite3.connect("customer_service.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS complaints (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            issue_type TEXT,
            description TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()


init_db()


st.set_page_config(
    page_title="Customer Service Assistant", page_icon="🤖", layout="centered"
)
st.title("🤖 Asisten Customer Service")

role = st.selectbox("Pilih peran Anda:", ["User", "Admin"])


if role == "User":
    st.write(
        "Halo! 👋 Saya bisa bantu mencatat keluhan atau menjawab pertanyaan seputar produk dan website."
    )

    # Formulir keluhan
    with st.form("complaint_form"):
        st.subheader("📝 Formulir Keluhan / Pertanyaan")
        name = st.text_input("Nama Lengkap")
        email = st.text_input("Email")
        issue_type = st.selectbox(
            "Jenis Masalah",
            [
                "Produk rusak",
                "Error login",
                "Tidak bisa checkout",
                "Masalah pengiriman",
                "Lainnya",
            ],
        )
        description = st.text_area("Deskripsi singkat masalah")

        submitted = st.form_submit_button("Kirim")

    # Saat user kirim form
    if submitted:
        if not name or not email or not description:
            st.warning("⚠️ Mohon isi semua field sebelum mengirim.")
        else:
            conn = sqlite3.connect("customer_service.db")
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO complaints (name, email, issue_type, description) VALUES (?, ?, ?, ?)",
                (name, email, issue_type, description),
            )
            conn.commit()
            conn.close()

            user_message = f"""
            Nama: {name}
            Email: {email}
            Masalah: {issue_type}
            Deskripsi: {description}
            """
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": "Kamu adalah customer service AI yang sopan, empatik, dan profesional.",
                    },
                    {"role": "user", "content": user_message},
                    {
                        "role": "assistant",
                        "content": "Buatkan respons konfirmasi yang sopan dan natural untuk pelanggan.",
                    },
                ],
            )

            st.success("✅ Laporan kamu sudah tercatat!")
            st.chat_message("assistant").write(response.choices[0].message.content)

    st.divider()
    st.subheader("💬 Tanya Lebih Lanjut")
    user_question = st.text_input("Ada pertanyaan lain seputar layanan kami?")
    if st.button("Kirim Pertanyaan"):
        if user_question:
            resp = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": "Kamu adalah customer service AI. Jawab pertanyaan umum pelanggan dengan ramah dan informatif.",
                    },
                    {"role": "user", "content": user_question},
                ],
            )
            st.chat_message("assistant").write(resp.choices[0].message.content)


elif role == "Admin":
    st.subheader("📋 Daftar Keluhan Pengguna")
    password = st.text_input("Masukkan password admin:", type="password")

    if password == "admin123":
        conn = sqlite3.connect("customer_service.db")
        cur = conn.cursor()
        data = cur.execute(
            "SELECT * FROM complaints ORDER BY timestamp DESC"
        ).fetchall()
        conn.close()

        if data:
            import pandas as pd

            df = pd.DataFrame(
                data,
                columns=["ID", "Nama", "Email", "Jenis Masalah", "Deskripsi", "Waktu"],
            )

            issue_filter = st.selectbox(
                "Filter berdasarkan jenis masalah:",
                ["Semua"] + df["Jenis Masalah"].unique().tolist(),
            )
            if issue_filter != "Semua":
                df = df[df["Jenis Masalah"] == issue_filter]

            st.dataframe(df, use_container_width=True)
        else:
            st.info("Belum ada keluhan dari pengguna.")
    elif password != "":
        st.error("❌ Password salah!")
