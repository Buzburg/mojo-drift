import time
from drift import evaluate_drift

def run_benchmark():
    goal = "Fix JWT authentication token expiration in auth controller"
    action = "Inspect auth_controller.py and check token refresh logic"

    # Warmup
    for _ in range(50):
        evaluate_drift(goal, action)

    iterations = 500
    start = time.perf_counter()
    for _ in range(iterations):
        evaluate_drift(goal, action)
    total_time = time.perf_counter() - start

    avg_us = (total_time / iterations) * 1_000_000
    print(f"=== mojo-drift Benchmark ===")
    print(f"Iterations: {iterations}")
    print(f"Average drift check latency: {avg_us:.2f} µs ({avg_us/1000:.3f} ms)")
    print(f"Evaluations per second: {iterations / total_time:.1f}")

if __name__ == "__main__":
    run_benchmark()
