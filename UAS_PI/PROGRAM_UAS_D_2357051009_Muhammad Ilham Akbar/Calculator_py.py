from collections import Counter
class Statistics:
    @staticmethod
    def mean(data):
        return sum(data) / len(data)

    @staticmethod
    def median(data):
        sorted_data = sorted(data)
        n = len(sorted_data)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            return sorted_data[mid]

    @staticmethod
    def mode(data):
        freq = Counter(data)
        max_count = max(freq.values())
        modes = [k for k, v in freq.items() if v == max_count]
        return modes[0] if len(modes) == 1 else modes  # Return the first mode if multiple modes exist
