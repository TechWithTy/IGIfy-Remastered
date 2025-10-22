from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Dict, Optional

from instagrapi.exceptions import (
    BadPassword,
    ChallengeRequired,
    ClientBadRequestError,
    ClientForbiddenError,
    ClientGraphqlError,
    ClientLoginRequired,
    ClientNotFoundError,
    ClientThrottledError,
    FeedbackRequired,
    HashtagNotFound,
    LoginRequired,
    PleaseWaitFewMinutes,
    PrivateError,
)


@dataclass
class ExceptionOutcome:
    action: str  # 'retry', 'wait', 'cooldown', 'skip', 'relogin', 'stop', 'raise', 'retry_later'
    wait_seconds: int = 0
    message: str = ""
    error: Optional[BaseException] = None


def classify_exception(e: BaseException) -> ExceptionOutcome:
    """
    Classify common instagrapi exceptions into high-level outcomes IGFI can act upon.
    """
    if isinstance(e, (PleaseWaitFewMinutes, ClientThrottledError)):
        return ExceptionOutcome(action="wait", wait_seconds=60, message=str(e), error=e)
    if isinstance(e, FeedbackRequired):
        # action blocked; backing off more aggressively
        return ExceptionOutcome(action="cooldown", wait_seconds=12 * 60 * 60, message=str(e), error=e)
    if isinstance(e, (LoginRequired, ClientLoginRequired, BadPassword)):
        return ExceptionOutcome(action="relogin", wait_seconds=0, message=str(e), error=e)
    if isinstance(e, ChallengeRequired):
        return ExceptionOutcome(action="stop", message="Challenge required — manual action needed", error=e)
    if isinstance(e, HashtagNotFound):
        return ExceptionOutcome(action="skip", message="Hashtag not found", error=e)
    if isinstance(e, (ClientNotFoundError, ClientForbiddenError)):
        return ExceptionOutcome(action="retry_later", wait_seconds=5 * 60, message=str(e), error=e)
    if isinstance(e, (ClientBadRequestError, ClientGraphqlError, PrivateError)):
        return ExceptionOutcome(action="retry", wait_seconds=5, message=str(e), error=e)
    return ExceptionOutcome(action="raise", message=str(e), error=e)


def run_with_handling(func: Callable[..., Any], *args, **kwargs) -> Dict[str, Any]:
    """
    Execute callable and return a structured result.

    Returns dict with keys:
    - 'ok': bool
    - 'value': any (if ok)
    - 'outcome': ExceptionOutcome (if not ok)
    """
    try:
        value = func(*args, **kwargs)
        return {"ok": True, "value": value}
    except BaseException as e:  # noqa: BLE001
        outcome = classify_exception(e)
        return {"ok": False, "outcome": outcome}

