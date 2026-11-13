import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Час виконання функції: {end - start:.3f} секунди")
        return result

    return wrapper


@measure_time
def calculate_sum(n):
    return sum(range(1, n + 1))


total = calculate_sum(1_000_000)
print(f"Сума чисел: {total}")
