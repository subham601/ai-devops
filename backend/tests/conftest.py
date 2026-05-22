import sys
from pathlib import Path

# Ensure "app" package (backend/app) is importable when running pytest from
# repo root.
BACKEND_DIR = Path(__file__).resolve().parents[1]  # /repo/backend
if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))
