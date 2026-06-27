"""
Shared evidence JSON helpers — stdlib only (no jsonschema dependency).
"""

from __future__ import annotations

import json
import re
from datetime import date, datetime
from pathlib import Path
from typing import Any

SCHEMA_VERSION = "1.0"
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
DATETIME_RE = re.compile(
    r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})?$"
)
INVESTIGATION_ID_RE = re.compile(r"^Investigation_\d{4}-\d{2}-\d{2}$")
SHA256_RE = re.compile(r"^[a-f0-9]{64}$")

OS_FAMILIES = frozenset({"windows", "macos", "linux", "unknown"})
PHASE_NAMES = frozenset(
    {
        "documentation",
        "scanning",
        "inspection",
        "network_check",
        "decision",
        "handoff",
        "closed",
    }
)
FILE_STATUSES = frozenset(
    {"documented", "quarantined", "cleared", "escalated", "monitoring"}
)
EXPOSURE_TYPES = frozenset({"email", "password", "phone", "other"})


class ValidationError(Exception):
    def __init__(self, errors: list[str]) -> None:
        self.errors = errors
        super().__init__("\n".join(errors))


def new_evidence_document(date_stamp: str, os_family: str = "unknown") -> dict[str, Any]:
    if not DATE_RE.match(date_stamp):
        raise ValueError(f"Invalid date stamp: {date_stamp!r}")
    if os_family not in OS_FAMILIES:
        os_family = "unknown"
    return {
        "schema_version": SCHEMA_VERSION,
        "investigation": {
            "id": f"Investigation_{date_stamp}",
            "started_at": date_stamp,
            "investigator": "self",
            "os": {"family": os_family, "version": "", "framework": "minimal-tools-v1.1"},
            "phase": 0,
            "phase_name": "documentation",
            "situation_summary": "",
        },
        "system": {
            "system_time_verified": None,
            "system_time_was_correct": None,
            "system_time_corrected": False,
        },
        "files": [],
        "sessions": [],
        "escalation": {"recommended": False, "criteria_met": [], "notes": ""},
        "breach_checks": [],
        "artifacts": {"screenshots": [], "network_captures": [], "tool_exports": []},
    }


def load_evidence(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as fh:
        data = json.load(fh)
    if not isinstance(data, dict):
        raise ValidationError(["Root must be a JSON object."])
    return data


def _require(obj: Any, path: str, errors: list[str]) -> bool:
    if obj is None:
        errors.append(f"Missing required field: {path}")
        return False
    return True


def _check_type(value: Any, expected: str, path: str, errors: list[str]) -> None:
    if expected == "string" and not isinstance(value, str):
        errors.append(f"{path}: expected string, got {type(value).__name__}")
    elif expected == "integer" and not isinstance(value, int):
        errors.append(f"{path}: expected integer, got {type(value).__name__}")
    elif expected == "boolean" and not isinstance(value, bool):
        errors.append(f"{path}: expected boolean, got {type(value).__name__}")
    elif expected == "array" and not isinstance(value, list):
        errors.append(f"{path}: expected array, got {type(value).__name__}")
    elif expected == "object" and not isinstance(value, dict):
        errors.append(f"{path}: expected object, got {type(value).__name__}")


def validate_evidence(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []

    if data.get("schema_version") != SCHEMA_VERSION:
        errors.append(f"schema_version must be {SCHEMA_VERSION!r}.")

    inv = data.get("investigation")
    if not _require(inv, "investigation", errors) or not isinstance(inv, dict):
        return errors

    for key in ("id", "started_at", "os", "phase", "phase_name"):
        _require(inv.get(key), f"investigation.{key}", errors)

    if isinstance(inv.get("id"), str) and not INVESTIGATION_ID_RE.match(inv["id"]):
        errors.append("investigation.id must match Investigation_YYYY-MM-DD.")

    if isinstance(inv.get("started_at"), str) and not DATE_RE.match(inv["started_at"]):
        errors.append("investigation.started_at must be YYYY-MM-DD.")

    os_obj = inv.get("os")
    if isinstance(os_obj, dict):
        fam = os_obj.get("family")
        if fam not in OS_FAMILIES:
            errors.append(f"investigation.os.family must be one of {sorted(OS_FAMILIES)}.")
    else:
        errors.append("investigation.os must be an object.")

    phase = inv.get("phase")
    if isinstance(phase, int) and not (0 <= phase <= 6):
        errors.append("investigation.phase must be 0–6.")

    pname = inv.get("phase_name")
    if pname not in PHASE_NAMES:
        errors.append(f"investigation.phase_name must be one of {sorted(PHASE_NAMES)}.")

    files = data.get("files")
    if not _require(files, "files", errors) or not isinstance(files, list):
        return errors

    for i, entry in enumerate(files):
        prefix = f"files[{i}]"
        if not isinstance(entry, dict):
            errors.append(f"{prefix}: must be an object.")
            continue
        if not entry.get("path"):
            errors.append(f"{prefix}.path: required non-empty string.")
        status = entry.get("status")
        if status not in FILE_STATUSES:
            errors.append(f"{prefix}.status must be one of {sorted(FILE_STATUSES)}.")
        sha = entry.get("sha256")
        if isinstance(sha, str) and sha and not SHA256_RE.match(sha):
            errors.append(f"{prefix}.sha256: must be 64 lowercase hex chars or null.")
        for ts_key in ("created", "modified", "accessed"):
            ts = entry.get(ts_key)
            if isinstance(ts, str) and ts and not DATETIME_RE.match(ts):
                errors.append(f"{prefix}.{ts_key}: use ISO-8601 date-time.")

    artifacts = data.get("artifacts")
    if not _require(artifacts, "artifacts", errors) or not isinstance(artifacts, dict):
        return errors
    for key in ("screenshots", "network_captures", "tool_exports"):
        val = artifacts.get(key)
        if not isinstance(val, list):
            errors.append(f"artifacts.{key} must be an array.")

    sessions = data.get("sessions", [])
    if not isinstance(sessions, list):
        errors.append("sessions must be an array.")
    else:
        for i, sess in enumerate(sessions):
            if not isinstance(sess, dict):
                errors.append(f"sessions[{i}]: must be an object.")
                continue
            for req in ("at", "phase", "summary"):
                if req not in sess:
                    errors.append(f"sessions[{i}].{req}: required.")

    breach_checks = data.get("breach_checks", [])
    if isinstance(breach_checks, list):
        for i, chk in enumerate(breach_checks):
            if not isinstance(chk, dict):
                errors.append(f"breach_checks[{i}]: must be an object.")
                continue
            if not chk.get("checked_at") or not DATE_RE.match(str(chk["checked_at"])):
                errors.append(f"breach_checks[{i}].checked_at: required YYYY-MM-DD.")
            if not chk.get("account"):
                errors.append(f"breach_checks[{i}].account: required.")
            for exp in chk.get("exposure_types", []):
                if exp not in EXPOSURE_TYPES:
                    errors.append(
                        f"breach_checks[{i}].exposure_types: invalid value {exp!r}."
                    )

    return errors


def assert_valid(data: dict[str, Any]) -> None:
    errors = validate_evidence(data)
    if errors:
        raise ValidationError(errors)


def iso_now() -> str:
    return datetime.now().astimezone().replace(microsecond=0).isoformat()


def today_stamp() -> str:
    return date.today().isoformat()