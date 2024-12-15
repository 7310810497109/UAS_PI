from tabulate import tabulate

def display_data(data, headers):
    formatted_data = [
        [f"{col:.2f}" if isinstance(col, float) else col for col in row]
        for row in data
    ]
    print(tabulate(formatted_data, headers=headers, tablefmt="grid"))

def display_statistics(statistics, label):
    """
    Menampilkan hasil statistik.
    """
    print(f"\nStatistics for '{label}':")
    print(f"Mean: {statistics['mean']}")
    print(f"Median: {statistics['median']}")
    print(f"Mode: {statistics['mode']}")
   
