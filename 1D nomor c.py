import math

def dft(x):
    N = len(x)
    X = [0] * N

    for k in range(N):
        X_real = 0
        X_imag = 0
        for n in range(N):
            angle = -2 * math.pi * k * n / N
            X_real += x[n] * math.cos(angle)
            X_imag += x[n] * math.sin(angle)
        X[k] = complex(X_real, X_imag)

    return X

def step_signal(N):
    return [1 if n >= 0 else 0 for n in range(N)]

# Create a step signal
# Jika Nilai A pada soal adalah 10(periode =10 
# 1 dimensional FT
# nomor 2, t = 3A
# Identitas diri
print("Nama: M Rizki Akbar")
print("NRP: 5009211128")
N = 60 #umber of samples
x = step_signal(N)

# Calculate the Fourier Transform
X = dft(x)

# Display the magnitude of the Fourier Transform
X_magnitude = [abs(X[k]) for k in range(N)]
print(X_magnitude)
