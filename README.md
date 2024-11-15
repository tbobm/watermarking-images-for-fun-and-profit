# Watermarking

This repository gathers the different example working scenario used to experiment
with watermarking in Python and Go.

## Python + Pillow

```console
hyperfine 'poetry run python3 example_pillow/main.py'
Benchmark 1: poetry run python3 example_pillow/main.py
  Time (mean ± σ):      1.100 s ±  0.036 s    [User: 2.540 s, System: 0.079 s]
  Range (min … max):    1.044 s …  1.160 s    10 runs
``` 

## Python + Libvips

```console
$ hyperfine 'poetry run python3 example_pyvips/main.py'
Benchmark 1: poetry run python3 example_pyvips/main.py
  Time (mean ± σ):      1.330 s ±  0.044 s    [User: 2.792 s, System: 0.141 s]
  Range (min … max):    1.277 s …  1.425 s    10 runs
```

## Golang + Libvips

```console
$ hyperfine  watermark-vips
Benchmark 1: watermark-vips
  Time (mean ± σ):     292.2 ms ±  24.3 ms    [User: 281.3 ms, System: 72.1 ms]
  Range (min … max):   252.6 ms … 321.3 ms    10 runs
```
