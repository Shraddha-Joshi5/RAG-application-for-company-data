"""Shared model-name resolution for agent modules."""

from __future__ import annotations

import os

DEFAULT_MODEL = "openai:gpt-4.1"


def env_model(*names: str, default: str = DEFAULT_MODEL) -> str:
    """Return the first non-empty env var, or *default*."""
    for name in names:
        value = os.environ.get(name)
        if value and value.strip():
            return value.strip()
    return default