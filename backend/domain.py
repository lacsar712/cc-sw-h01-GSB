TOLERANCE_NM = 0.08


def judge(nominal: float, measured: float) -> tuple[str, str]:
    # 输入按 0.01 nm 步进，先归一化到 1e-6 消除浮点表示误差，
    # 保证偏差恰好 0.08 nm 的压线样条稳定判为合格。
    delta = round(abs(measured - nominal), 6)
    if delta <= TOLERANCE_NM:
        return "合格", f"偏差 {delta:.4f} nm 在允差内"
    return "超差", f"偏差 {delta:.4f} nm 超过允差 {TOLERANCE_NM}"
