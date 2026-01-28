def time_controller(d, h, m):
    if d <0 or h < 0 or m<0 :
        raise ValueError("all numeric values must be positive")

    total_seconds = d * 86400 + h * 3600 + m * 60

    return total_seconds