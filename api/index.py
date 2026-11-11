import os
import sys
from pathlib import Path

# Add project root to sys.path so 'portfolio' and 'portfolio_project' can be resolved
BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')

import django
django.setup()

from django.core.management import call_command
from django.core.wsgi import get_wsgi_application

# Auto-migrate and seed in /tmp when running on Vercel with SQLite
if os.environ.get('VERCEL') == '1' and 'DATABASE_URL' not in os.environ:
    db_file = Path('/tmp/db.sqlite3')
    if not db_file.exists():
        try:
            call_command('migrate', interactive=False, verbosity=0)
            call_command('seed_portfolio', interactive=False, verbosity=0)
        except Exception as err:
            print(f"[Vercel] Database initialization notice: {err}")

application = get_wsgi_application()
app = application
handler = application
