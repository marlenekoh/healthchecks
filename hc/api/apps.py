from __future__ import annotations

from collections.abc import Sequence
from typing import Any

from django.apps import AppConfig
from django.conf import settings
from django.core.checks import Warning, register


class ApiConfig(AppConfig):
    name = "hc.api"


@register()
def settings_check(
    app_configs: Sequence[AppConfig] | None,
    databases: Sequence[str] | None,
    **kwargs: dict[str, Any],
) -> list[Warning]:
    items = []

    site_root_parts = settings.SITE_ROOT.split("://")
    if site_root_parts[0] not in ("http", "https"):
        items.append(
            Warning(
                "Invalid settings.SITE_ROOT value",
                hint="SITE_ROOT should start with either http:// or https://",
                id="hc.api.E001",
            )
        )
    return items
