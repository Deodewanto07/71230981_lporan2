def hitung_pendapatan(gaji_per_jam, jam_kerja_per_minggu):
    jam_kerja = jam_kerja_per_minggu * 5  
    pendapatan_sebelum_pajak = gaji_per_jam * jam_kerja
    
    pajak = 0.14 * pendapatan_sebelum_pajak
    pendapatan_setelah_pajak = pendapatan_sebelum_pajak - pajak
    
    belanja_baju_aksesoris = 0.10 * pendapatan_setelah_pajak
    belanja_alat_tulis = 0.01 * pendapatan_setelah_pajak
    
    sisa_uang_belanja = pendapatan_setelah_pajak - belanja_baju_aksesoris - belanja_alat_tulis
    sedekah = 0.25 * sisa_uang_belanja
    
    sedekah_anak_yatim = 0.30 * sedekah
    sedekah_kaum_dhuafa = 0.70 * sedekah
    
    return (pendapatan_sebelum_pajak, pendapatan_setelah_pajak, belanja_baju_aksesoris,
            belanja_alat_tulis, sedekah, sedekah_anak_yatim, sedekah_kaum_dhuafa)

gaji_per_jam = float(input("Masukkan gaji per jam yang Anda inginkan: "))
jam_kerja_per_minggu = int(input("Masukkan jumlah jam kerja per minggu: "))

pendapatan_sebelum_pajak, pendapatan_setelah_pajak, belanja_baju_aksesoris, belanja_alat_tulis, sedekah, sedekah_anak_yatim, sedekah_kaum_dhuafa = hitung_pendapatan(gaji_per_jam, jam_kerja_per_minggu)

print(f"1. Pendapatan Budi selama libur musim panas sebelum melakukan pembayaran pajak: Rp {pendapatan_sebelum_pajak}")
print(f"2. Pendapatan Budi selama libur musim panas setelah melakukan pembayaran pajak: Rp {pendapatan_setelah_pajak}")
print(f"3. Jumlah uang yang akan Budi habiskan untuk membeli pakaian dan aksesoris: Rp {belanja_baju_aksesoris}")
print(f"4. Jumlah uang yang akan Budi habiskan untuk membeli alat tulis: Rp {belanja_alat_tulis}")
print(f"5. Jumlah uang yang akan Budi sedekahkan: Rp {sedekah}")
print(f"6. Jumlah uang yang akan diterima anak yatim: Rp {sedekah_anak_yatim}")
print(f"7. Jumlah uang yang akan diterima kaum dhuafa: Rp {sedekah_kaum_dhuafa}")
