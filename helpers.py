import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.perf_counter(), time.process_time()
        result = func(*args, **kwargs)
        t2 = time.perf_counter(), time.process_time()
        print(f"Result: {result}")
        print(
            f" Real time: {t2[0] - t1[0]:.8f} seconds\n CPU time: {t2[1] - t1[1]:.8f} seconds"
        )
        return result

    return wrapper
