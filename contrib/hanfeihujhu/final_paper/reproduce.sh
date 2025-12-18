#!/usr/bin/env bash
set -euo pipefail

# Always run from the repo root
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

APPENDIX_NOTEBOOK="08_appendix.ipynb"

if [[ ! -f "$APPENDIX_NOTEBOOK" ]]; then
  echo "Appendix notebook not found: $APPENDIX_NOTEBOOK" >&2
  exit 1
fi

echo "Executing appendix notebook…"
jupyter nbconvert \
  --to notebook \
  --execute \
  --inplace \
  --ExecutePreprocessor.timeout=600 \
  "$APPENDIX_NOTEBOOK"

echo "Building paper with MyST…"
myst build --pdf

echo "Done."