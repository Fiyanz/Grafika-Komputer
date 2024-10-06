def rgb_to_hsv(r, g, b):
    # Normalisasi nilai RGB ke rentang [0, 1]
    r_prime, g_prime, b_prime = r / 255.0, g / 255.0, b / 255.0
    
    # Hitung nilai maksimum dan minimum
    c_max = max(r_prime, g_prime, b_prime)
    c_min = min(r_prime, g_prime, b_prime)
    delta = c_max - c_min
    
    # Hitung Hue
    if delta == 0:
        h = 0
    elif c_max == r_prime:
        h = (60 * ((g_prime - b_prime) / delta) + 360) % 360
    elif c_max == g_prime:
        h = (60 * ((b_prime - r_prime) / delta) + 120) % 360
    elif c_max == b_prime:
        h = (60 * ((r_prime - g_prime) / delta) + 240) % 360
    
    # Hitung Saturation
    if c_max == 0:
        s = 0
    else:
        s = delta / c_max
    
    # Hitung Value
    v = c_max
    
    # Kembalikan nilai H, S, V
    return h, s * 100, v * 100

# Contoh penggunaan
# NIM : 230 202804
r, g, b = 20, 28, 0.4  # Warna merah
h, s, v = rgb_to_hsv(r, g, b)
print(f'Hue: {h}, Saturation: {s}%, Value: {v}%')
