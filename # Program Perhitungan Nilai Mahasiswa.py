# Program Perhitungan Nilai Mahasiswa

print("=== Program Perhitungan Nilai Mahasiswa ===")

# 1. Meminta input nama mahasiswa
nama = input("Masukkan Nama Mahasiswa: ")

# 2. Meminta input nilai tugas, UTS, dan UAS
nilai_tugas = float(input("Masukkan Nilai Tugas: "))
nilai_uts = float(input("Masukkan Nilai UTS: "))
nilai_uas = float(input("Masukkan Nilai UAS: "))

# 3. Menghitung nilai akhir dengan bobot (Tugas: 30%, UTS: 30%, UAS: 40%)
nilai_akhir = (0.30 * nilai_tugas) + (0.30 * nilai_uts) + (0.40 * nilai_uas)

# Menentukan status kelulusan (Minimal 60 Lulus, kurang dari 60 Belum Lulus)
if nilai_akhir >= 60:
    status = "Lulus"
else:
    status = "Belum Lulus"

# Menampilkan hasil output program
print("\n--- Hasil Akhir ---")
print(f"Nama Mahasiswa : {nama}")
print(f"Nilai Akhir    : {nilai_akhir:.2f}")
print(f"Status Kelulusan: {status}")