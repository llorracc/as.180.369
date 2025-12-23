#!/usr/bin/env bash
# reproduce.sh
#
# Reproduce the MyST paper PDF:
#   The_California_Environmental_Quality_Act__CEQA__and_Housing_Prices.pdf
#
# Usage (from the project root, where myst.yml lives):
#   bash reproduce.sh
#
# Notes:
# - Requires: Python 3, and a LaTeX toolchain with `latexmk` on PATH.
# - Output will be written to: ./The_California_Environmental_Quality_Act__CEQA__and_Housing_Prices.pdf

set -euo pipefail

# -------- Config --------
PDF_NAME="The_California_Environmental_Quality_Act__CEQA__and_Housing_Prices.pdf"
VENV_DIR="${VENV_DIR:-.venv}"
PYTHON_BIN="${PYTHON_BIN:-python3}"

# -------- Helpers --------
err() { echo "ERROR: $*" >&2; exit 1; }
info() { echo "==> $*"; }

# -------- Sanity checks --------
[[ -f "myst.yml" ]] || err "myst.yml not found. Run this script from your project root."

if ! command -v "$PYTHON_BIN" >/dev/null 2>&1; then
  err "Python not found (expected '$PYTHON_BIN'). Install Python 3 and try again."
fi

# LaTeX required for PDF builds
if ! command -v latexmk >/dev/null 2>&1; then
  cat >&2 <<'EOF'
ERROR: latexmk not found (required for MyST PDF builds).

Install a LaTeX distribution and ensure latexmk is on PATH.

macOS common fix after installing MacTeX/BasicTeX:
  echo 'export PATH="/Library/TeX/texbin:$PATH"' >> ~/.zprofile
  source ~/.zprofile

Then confirm:
  latexmk -v
EOF
  exit 1
fi

# -------- Python env --------
info "Using Python: $($PYTHON_BIN --version)"
if [[ ! -d "$VENV_DIR" ]]; then
  info "Creating virtual environment at $VENV_DIR"
  "$PYTHON_BIN" -m venv "$VENV_DIR"
fi

# shellcheck disable=SC1091
source "$VENV_DIR/bin/activate"

info "Upgrading pip tooling"
python -m pip install --upgrade pip setuptools wheel >/dev/null

# If you have pinned deps, prefer them.
if [[ -f "requirements.txt" ]]; then
  info "Installing dependencies from requirements.txt"
  pip install -r requirements.txt
else
  info "Installing MyST build tooling (mystmd) + notebook runtime"
  pip install "mystmd>=1.0.0" jupyter nbformat nbclient ipykernel
fi

# Confirm myst CLI exists
command -v myst >/dev/null 2>&1 || err "myst CLI not found after install. Try: pip install mystmd"

info "MyST version: $(myst --version 2>/dev/null || true)"
info "LaTeX (latexmk): $(latexmk -v | head -n 1)"

# -------- Build --------
info "Cleaning previous build artifacts"
rm -rf _build

info "Building PDF with MyST"
myst build --pdf

# MyST typically writes PDFs into _build/exports. Locate the newest pdf.
info "Locating built PDF"
BUILT_PDF="$(find _build -type f -name '*.pdf' -print 2>/dev/null | head -n 1 || true)"

# Prefer the export name if present
if [[ -f "_build/exports/CEQAPaper.pdf" ]]; then
  BUILT_PDF="_build/exports/CEQAPaper.pdf"
elif [[ -f "_build/exports/CEQAPaper.pdf" ]]; then
  BUILT_PDF="_build/exports/CEQAPaper.pdf"
fi

# If multiple PDFs exist, try to pick the most recent
if [[ -z "${BUILT_PDF:-}" ]]; then
  BUILT_PDF="$(find _build -type f -name '*.pdf' -print0 2>/dev/null | xargs -0 ls -t 2>/dev/null | head -n 1 || true)"
fi

[[ -n "${BUILT_PDF:-}" && -f "$BUILT_PDF" ]] || err "No PDF found in _build. The build may have failed—re-run: myst build --pdf -v"

# Copy/rename to the requested final filename in project root
info "Copying output to ./${PDF_NAME}"
cp -f "$BUILT_PDF" "./${PDF_NAME}"

info "Done."
info "Generated: ./${PDF_NAME}"
