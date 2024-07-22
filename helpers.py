import time

from memory_profiler import memory_usage


def measure_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.perf_counter(), time.process_time()
        mem_usage, result = memory_usage((func, args, kwargs), retval=True)
        t2 = time.perf_counter(), time.process_time()
        print(f"Result: {result}")
        print(
            f"  Real time: {t2[0] - t1[0]:.8f} seconds",
            "\n",
            f" CPU time: {t2[1] - t1[1]:.8f} seconds",
            "\n",
            f" Maximum memory usage: {max(mem_usage)}",
        )

        return result

    return wrapper
