import random
import time
import matplotlib.pyplot as plt

def generate_array(n, max_val, seed=None):
    if seed is not None:
        random.seed(seed)
    return [random.randint(1, max_val) for _ in range(n)]

def check_uniqueness(arr):
    unique_elements = set(arr)
    return len(unique_elements) == len(arr)

def measure_performance(n_values, max_val):
    worst_case_times = []
    average_case_times = []

    for n in n_values:
        # Generate multiple arrays to measure average case
        average_times = []
        for _ in range(10):  # Measure 10 samples for average case
            arr = generate_array(n, max_val, seed=random.randint(0, 10000))
            start_time = time.perf_counter()  # Higher precision
            check_uniqueness(arr)
            average_times.append(time.perf_counter() - start_time)

        # Measure worst case (all elements same)
        worst_case_array = [1] * n
        start_time = time.perf_counter()
        check_uniqueness(worst_case_array)
        worst_case_times.append(time.perf_counter() - start_time)

        average_case_times.append(sum(average_times) / len(average_times))

    return worst_case_times, average_case_times

def plot_graph(n_values, worst_case_times, average_case_times):
    plt.figure(figsize=(10, 6))
    plt.plot(n_values, worst_case_times, label="Worst Case", marker='o', color='red')
    plt.plot(n_values, average_case_times, label="Average Case", marker='o', color='blue')
    plt.title("Performance Analysis of Uniqueness Check")
    plt.xlabel("Number of Elements (n)")
    plt.ylabel("Time (seconds)")
    plt.legend()
    plt.grid()
    plt.savefig(f"performance_graph_{int(time.time())}.jpg")
    plt.show()

if __name__ == "__main__":
    # Input NIM and calculate max_val
    nim = "076"  # NIM tetap (076)
    try:
        last_three_digits = int(nim[-3:])  # Ambil tiga digit terakhir dari NIM
        max_val = 250 - last_three_digits
        if max_val <= 0:
            raise ValueError("Tiga digit terakhir NIM menghasilkan max_val <= 0. Harap periksa NIM Anda.")
    except ValueError as e:
        print(f"Error: {e}")
        exit()

    # Define n_values
    n_values = [1000, 2000, 3000, 4000, 5000, 10000, 20000]  # Perbesar ukuran array

    # Measure performance
    worst_case_times, average_case_times = measure_performance(n_values, max_val)

    # Save results to a text file
    with open("worst_avg.txt", "w") as f:
        f.write("n\tWorst Case\tAverage Case\n")
        for n, worst, avg in zip(n_values, worst_case_times, average_case_times):
            f.write(f"{n}\t{worst:.6f}\t{avg:.6f}\n")

    print("Hasil telah disimpan ke 'worst_avg.txt'.")

    # Plot and save the graph
    plot_graph(n_values, worst_case_times, average_case_times)
