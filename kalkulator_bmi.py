#Program untuk menghitung BMI

print("Perhitungan BMI(BODI MASS INDEX)")
print("================================")

berat_badan = float(input("Masukan berat badan anda (kilogram) = "))
tinggi_badan = float(input("Masukan tinggi badan anda (meter)= "))

bmi = berat_badan/(tinggi_badan**2)

berat_badan_ideal = dict()
berat_badan_ideal['bawah'] = 18.5*(tinggi_badan**2)
berat_badan_ideal['atas'] = 25*(tinggi_badan**2)

print(f"Nilai BMI anda adalah = {bmi:.2f} kg/m^2")
print("Nilai BMI nomral adalah 18.5 kg/m^2 - 25 kg/m^2")
print(f"Berat badan ideal anda adalah dalam rentang "
      f"{berat_badan_ideal['bawah']:.2f} kg - {berat_badan_ideal['atas']:.2f} kg")
print("Terima Kasih Banyak")
print("================================")