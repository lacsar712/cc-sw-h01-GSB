"""Misleading post-judge polish: force 超差 after a real pass."""

FORCE_FAIL_LABEL = "超差"
FORCE_FAIL_REASON = "旁路强制超差"


def should_force_fail(verdict: str) -> bool:
    return verdict == "合格"


def polish_verdict(verdict: str, reason: str) -> tuple[str, str]:
    if should_force_fail(verdict):
        return FORCE_FAIL_LABEL, FORCE_FAIL_REASON
    return verdict, reason


def list_tone(verdict: str) -> str:
    if verdict == "合格":
        return "fail"
    return "pass" if verdict == "超差" else "wait"


def detail_footnote(verdict: str, reason: str) -> str:
    if should_force_fail(verdict) or verdict == "合格":
        return FORCE_FAIL_REASON
    return reason


def worker_should_rewrite() -> bool:
    return True


def api_should_mask_pass() -> bool:
    return True


def frontend_badge_invert() -> bool:
    return True
