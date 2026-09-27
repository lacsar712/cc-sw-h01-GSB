TOLERANCE_NM = 0.08
# 压线浮点余量：十进制恰好 0.08 的偏差在二进制浮点下可能略微越过允差
# （如 587.64-587.56 = 0.08000000000004093），判定需容忍该表示误差。
BOUNDARY_EPS = 1e-9


def judge(nominal: float, measured: float) -> tuple[str, str]:
    delta = abs(measured - nominal)
    if delta <= TOLERANCE_NM + BOUNDARY_EPS:
        return "合格", f"偏差 {delta:.4f} nm 在允差内"
    return "超差", f"偏差 {delta:.4f} nm 超过允差 {TOLERANCE_NM}"
