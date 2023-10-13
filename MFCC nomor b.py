# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 19:14:20 2023

@author: afifa
"""
print("Nama: M Rizki Akbar")
print("NRP: 5009211128")

# Jika Nilai A pada soal adalah 10(periode =10 )
#Nomor b, t=0,5A

import math
import cmath

def dft(x):
    N = len(x)
    X = [complex(0, 0) for _ in range(N)]

    for k in range(N):
        for n in range(N):
            angle = -2 * math.pi * k * n / N
            X[k] += x[n] * cmath.exp(complex(0, angle))

    return X

def mel_filter_bank(num_filters, fft_size, sample_rate):
    filters = []
    for i in range(num_filters):
        filters.append([0] * fft_size)
    
    min_freq = 300
    max_freq = sample_rate / 2
    mel_min = 1127 * math.log(1 + min_freq / 700)
    mel_max = 1127 * math.log(1 + max_freq / 700)

    for i in range(num_filters):
        filter_center = mel_min + (mel_max - mel_min) * (i + 1) / (num_filters + 1)
        f_min = 700 * (math.exp(filter_center / 1127) - 1)
        f_center = 700 * (math.exp(filter_center / 1127))
        f_max = 700 * (math.exp(filter_center / 1127) + 1)

        for j in range(fft_size):
            freq = j * sample_rate / fft_size
            if f_min <= freq <= f_center:
                filters[i][j] = (freq - f_min) / (f_center - f_min)
            elif f_center <= freq <= f_max:
                filters[i][j] = (f_max - freq) / (f_max - f_center)

    return filters

def mfcc(signal, sample_rate, num_filters, num_mfcc_coeffs):
    fft_size = len(signal)
    signal_spectrum = dft(signal)
    
    magnitude_spectrum = [abs(x) for x in signal_spectrum]

    filters = mel_filter_bank(num_filters, fft_size, sample_rate)

    mfccs = [0] * num_mfcc_coeffs

    for m in range(num_mfcc_coeffs):
        for k in range(num_filters):
            mfccs[m] += magnitude_spectrum[k] * math.cos((2 * math.pi * m * k) / num_filters)

    return mfccs

# Example usage:
sample_rate = 44100
signal_length = 10
signal = [1] * signal_length
num_filters = 20
num_mfcc_coeffs = 13

mfcc_coefficients = mfcc(signal, sample_rate, num_filters, num_mfcc_coeffs)
print(mfcc_coefficients)
