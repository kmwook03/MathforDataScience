import math

def normal_pdf(x: float, mean: float, std_dev: float) -> float:
    part1 = 1 / ((2.0 * math.pi * std_dev ** 2)) ** 0.5
    part2 = math.exp(-1.0 * 0.5 * ((x - mean) / std_dev) ** 2)
    
    return part1 * part2