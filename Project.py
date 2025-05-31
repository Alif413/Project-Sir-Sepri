import tkinter as tk
from tkinter import ttk, messagebox

def konversi():
    nilai = entry_nilai.get()
    jenis_konversi = combo_jenis.get()

    try:
        if jenis_konversi == "Biner ke Desimal":
            hasil = int(nilai, 2)
            proses = proses_biner_ke_desimal(nilai)
        elif jenis_konversi == "Desimal ke Biner":
            hasil = bin(int(nilai))[2:]
            proses = proses_desimal_ke_biner(int(nilai))

        label_hasil.config(text=f"Hasil: {hasil}")
        text_proses.config(state="normal")
        text_proses.delete("1.0", tk.END)
        text_proses.insert(tk.END, proses)
        text_proses.config(state="disabled")
        listbox_riwayat.insert(tk.END, f"{jenis_konversi}: {nilai} → {hasil}")

    except ValueError:
        messagebox.showerror("Error", "Input tidak valid! Harap masukkan angka yang sesuai.")

def proses_biner_ke_desimal(biner):
    penjelasan = []
    total = 0
    biner = biner[::-1]

    for i, bit in enumerate(biner):
        nilai = int(bit) * (2 ** i)
        penjelasan.append(f"{bit} × 2^{i} = {nilai}")
        total += nilai

    return "\n".join(penjelasan) + f"\nTotal = {total}"

def proses_desimal_ke_biner(n):
    langkah = []
    asal = n

    while n > 0:
        langkah.append(f"{n} ÷ 2 = {n // 2}, sisa {n % 2}")
        n //= 2

    return "\n".join(langkah[::-1]) + f"\nBiner dari {asal} = {bin(asal)[2:]}"


app = tk.Tk()
app.title("Konversi Biner ⇄ Desimal")
app.geometry("950x460")
app.configure(bg="#f0f0f0")
app.resizable(False, False)

frame_kiri = tk.Frame(app, bg="#f0f0f0")
frame_kiri.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

frame_tengah = tk.Frame(app, bg="#e6e6e6", bd=1, relief="solid", width=300)
frame_tengah.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=10)

frame_kanan = tk.Frame(app, bg="#ffffff", bd=1, relief="solid", width=250)
frame_kanan.pack(side=tk.RIGHT, fill=tk.BOTH, padx=10, pady=10)

tk.Label(frame_kiri, text="Konversi Biner ⇄ Desimal", font=("Helvetica", 16, "bold"), bg="#f0f0f0").pack(pady=10)

frame_input = tk.Frame(frame_kiri, bg="#f0f0f0")
frame_input.pack(pady=5)

tk.Label(frame_input, text="Nilai:", bg="#f0f0f0").grid(row=0, column=0, padx=5, pady=5)
entry_nilai = tk.Entry(frame_input, width=30)
entry_nilai.grid(row=0, column=1, padx=5, pady=5)

frame_jenis = tk.Frame(frame_kiri, bg="#f0f0f0")
frame_jenis.pack(pady=5)

tk.Label(frame_jenis, text="Jenis:", bg="#f0f0f0").grid(row=0, column=0, padx=5, pady=5)
combo_jenis = ttk.Combobox(frame_jenis, values=["Biner ke Desimal", "Desimal ke Biner"], state="readonly", width=27)
combo_jenis.grid(row=0, column=1, padx=5, pady=5)
combo_jenis.current(0)

tk.Button(frame_kiri, text="Konversi", command=konversi, bg="#4CAF50", fg="white",
          font=("Helvetica", 10, "bold")).pack(pady=10)

label_hasil = tk.Label(frame_kiri, text="Hasil: ", font=("Helvetica", 12), bg="#f0f0f0")
label_hasil.pack(pady=5)

tk.Label(frame_kiri, text="Riwayat:", font=("Helvetica", 11, "bold"), bg="#f0f0f0").pack(pady=(10, 5))

frame_riwayat = tk.Frame(frame_kiri)
frame_riwayat.pack()

scrollbar_riwayat = tk.Scrollbar(frame_riwayat)
scrollbar_riwayat.pack(side=tk.RIGHT, fill=tk.Y)

listbox_riwayat = tk.Listbox(frame_riwayat, height=7, width=50, yscrollcommand=scrollbar_riwayat.set)
listbox_riwayat.pack()
scrollbar_riwayat.config(command=listbox_riwayat.yview)

tk.Label(frame_tengah, text="📄 Proses Perhitungan", font=("Helvetica", 12, "bold"), bg="#e6e6e6").pack(pady=10)

text_proses = tk.Text(frame_tengah, width=40, height=22, bg="#f9f9f9", font=("Courier", 10))
text_proses.pack(padx=10)
text_proses.config(state="disabled")

tk.Label(frame_kanan, text="📘 Petunjuk", font=("Helvetica", 12, "bold"), bg="#ffffff").pack(padx=10, pady=(10, 0), anchor="w")

petunjuk_text = (
    "1. Masukkan angka:\n"
    "   - Biner: 1010\n"
    "   - Desimal: 10\n"
    "2. Pilih jenis konversi\n"
    "3. Klik 'Konversi'\n"
    "4. Proses dan hasil ditampilkan"
)
tk.Label(frame_kanan, text=petunjuk_text, justify="left", wraplength=230, bg="#ffffff", font=("Helvetica", 10)).pack(padx=10, pady=(0, 10))

tk.Label(frame_kanan, text="🧪 Contoh", font=("Helvetica", 12, "bold"), bg="#ffffff").pack(padx=10, pady=(5, 0), anchor="w")

contoh_text = (
    "• Biner ke Desimal:\n"
    "   1010 → 10\n\n"
    "• Desimal ke Biner:\n"
    "   10 → 1010"
)
tk.Label(frame_kanan, text=contoh_text, justify="left", wraplength=230, bg="#ffffff", font=("Helvetica", 10)).pack(padx=10, pady=(0, 10))

app.mainloop()
