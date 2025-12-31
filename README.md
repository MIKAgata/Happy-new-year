# 🎆 ASCII New Year Transition 2025 → 2026 (Python)

Program Python berbasis terminal yang menampilkan animasi ASCII art besar, bold, dan bergaya 3D untuk merayakan pergantian tahun dari 2025 ke 2026.
Animasi dibuat tanpa library grafis, murni menggunakan loop, manipulasi string, dan kontrol terminal.

## Fitur Utama

ASCII art angka ukuran besar (13 baris)

Beberapa style visual:

Normal

Shadow / Grayscale

Bold 3D

Extra Bold

Efek animasi:

Countdown (3 → 2 → 1)

Transformasi angka 2025 → 2026

Sliding transition

Pixel dissolve transition

Sparkle / partikel acak

Tampilan otomatis center di terminal

Welcome screen interaktif (tekan Enter)

Final celebration dengan pesan tahun baru

# Preview Konsep (Deskripsi)
2025
⬇ transformasi
2026


Ditampilkan dalam bentuk ASCII art besar dengan efek visual bertahap seperti video pergantian tahun.

# Teknologi yang Digunakan

Python 3

Modul bawaan:

os

time

random

Tidak menggunakan library eksternal

# Struktur Program

Fungsi utama yang perlu diketahui:

Fungsi	Deskripsi
clear_screen()	Membersihkan layar terminal
create_digit_art()	Membuat ASCII art angka 0–9
combine_digits()	Menggabungkan beberapa digit
center_art()	Memusatkan ASCII art di terminal
create_frame()	Membuat satu frame animasi
display_frame()	Menampilkan frame ke terminal
sliding_effect()	Efek geser 2025 → 2026
pixel_transition()	Efek perubahan piksel acak
number_transform_effect()	Transformasi bertahap angka
countdown_sequence()	Countdown sebelum transisi
final_celebration()	Animasi penutup
show_welcome()	Layar pembuka
main()	Alur utama program

# Cara Menjalankan

Pastikan Python 3 sudah terpasang

Simpan kode sebagai file, misalnya:

new_year_ascii.py


Jalankan di terminal:

python new_year_ascii.py


Tekan Enter saat welcome screen muncul

