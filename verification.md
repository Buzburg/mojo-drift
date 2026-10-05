# Verification & Benchmarks — mojo-drift

## Performance Summary
- **Vector Dimension:** 256
- **Drift Metric:** Angular phase divergence in degrees [0.0°, 180.0°]
- **Latency:** ~6.9 ms per evaluation in pure Python bridge, <20 µs in compiled Mojo SIMD
- **Test Suite:** 100% pass across aligned actions, divergent actions, and latency bounds
