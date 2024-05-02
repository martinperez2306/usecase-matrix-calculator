import numpy as np
import time

def matrix_multiplication(matrix1, matrix2):
    return np.dot(matrix1, matrix2)

def generate_random_matrix(rows, cols):
    return np.random.rand(rows, cols)

def benchmark(matrix_size):
    matrix1 = generate_random_matrix(matrix_size, matrix_size)
    matrix2 = generate_random_matrix(matrix_size, matrix_size)
    
    start_time = time.time()
    result = matrix_multiplication(matrix1, matrix2)
    end_time = time.time()
    
    return end_time - start_time

if __name__ == "__main__":
    matrix_size = 1000  # Tamaño de las matrices (ajustar según sea necesario)
    
    time_taken = benchmark(matrix_size)
    print(f"Tiempo tomado para multiplicar matrices de tamaño {matrix_size}x{matrix_size}: {time_taken} segundos")
