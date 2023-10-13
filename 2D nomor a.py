print("Nama: M Rizki Akbar")
print("NRP: 5009211128")


# Jika Nilai A pada soal adalah 10(periode =10 )
# 1 dimensional FT
import math

def dft2D(image):
    M, N = len(image), len(image[0])
    result = [[complex(0, 0) for _ in range(N)] for _ in range(M)]

    for u in range(M):
        for v in range(N):
            for x in range(M):
                for y in range(N):
                    angle = -2 * math.pi * (u * x / M + v * y / N)
                    result[u][v] += image[x][y] * complex(math.cos(angle), -math.sin(angle))

    return result

def step_signal_2D(M, N):
    return [[1 if x >= 0 and y >= 0 else 0 for y in range(N)] for x in range(M)]

# Nomor a, t=A
M, N = 60, 60  # Dimensions
image = step_signal_2D(M, N)

# Calculate the 2D Fourier Transform
result = dft2D(image)

# You can access the Fourier Transform result as result[u][v]

# For example, let's print the magnitude of the result at (u, v) = (32, 32)
magnitude = abs(result[1][10])
print(magnitude)
