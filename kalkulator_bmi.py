#Program untuk menghitung BMI

print("Perhitungan BMI(BODI MASS INDEX)")
print("================================")

berat_badan = float(input("Masukan berat badan anda (kilogram) = "))
tinggi_badan = float(input("Masukan tinggi badan anda (meter)= "))

bmi = berat_badan/(tinggi_badan**2)

berat_badan_ideal = dict()
berat_badan_ideal['bawah'] = 18.5*(tinggi_badan**2)
berat_badan_ideal['atas'] = 25*(tinggi_badan**2)

if bmi < 18.5:
      kategori = "Anda Kekurangan Berat Badan"
elif bmi < 25:
      kategori = "Nilai BMI anda Normal"
elif bmi < 30:
      kategori = "Anda Kelebihan Berat Badan"
else:
      kategori = "Anda Obesitas"

print("\nHasil Kalkulator BMI anda adalah : ")
print("---------------------------------")
print(f"Nilai BMI anda adalah = {bmi:.2f} kg/m^2")
print(kategori)
print(f"Berat badan ideal anda adalah dalam rentang "
      f"{berat_badan_ideal['bawah']:.2f} kg - {berat_badan_ideal['atas']:.2f} kg")

print("Terima Kasih telah menggunakan Program ini")
print("================================")