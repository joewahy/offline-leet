"""Stops a solution that uses too much memory.

setrlimit is not enforced on macOS, so a watchdog thread polls the process's
peak resident memory instead. Over the limit, it interrupts the running case
with MemoryLimitExceeded. If the code swallows that, or never returns to the
interpreter, the process exits at twice the limit.
"""
import contextlib
import os
import resource
import signal
import sys
import threading
import time

LIMIT = 1 << 30  # bytes. The biggest test inputs need well under 100 MB.
POLL = 0.01  # seconds

_armed = threading.Event()


class MemoryLimitExceeded(MemoryError):
    pass


def peak_rss():
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return peak if sys.platform == "darwin" else peak * 1024


def _message(limit):
    return f"memory limit exceeded ({limit >> 20} MB)"


def _on_signal(signum, frame):
    if _armed.is_set():
        _armed.clear()
        raise MemoryLimitExceeded(_message(LIMIT))


def _watch(main_thread, limit):
    while True:
        time.sleep(POLL)
        used = peak_rss()
        if used > 2 * limit:
            os.write(2, f"Your code used too much memory and was stopped ({_message(limit)}).\n".encode())
            os._exit(137)
        if used > limit and _armed.is_set():
            signal.pthread_kill(main_thread, signal.SIGUSR1)


def start(limit=LIMIT):
    """Start watching the current process. Call once, from the main thread."""
    global LIMIT
    LIMIT = limit
    signal.signal(signal.SIGUSR1, _on_signal)
    threading.Thread(target=_watch, args=(threading.get_ident(), limit), daemon=True).start()


@contextlib.contextmanager
def guard():
    """Let the watchdog interrupt the code inside this block."""
    _armed.set()
    try:
        yield
    finally:
        _armed.clear()
