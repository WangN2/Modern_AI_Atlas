"""Centralized path configuration for the Modern AI Atlas Generator.

All paths are derived from ROOT_DIR, which is the project root directory.
"""

from __future__ import annotations

from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

EXPORT_DIR = ROOT_DIR / "export"
ASSET_DIR = ROOT_DIR / "assets"
THEME_DIR = ROOT_DIR / "assets" / "themes"
KNOWLEDGE_DIR = ROOT_DIR / "knowledge"

# Atlas definitions live alongside the knowledge base
ATLAS_DIR = ROOT_DIR / "atlas"
