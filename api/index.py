import os
import sys
import shutil
from pathlib import Path

# Add project root to sys.path so 'portfolio' and 'portfolio_project' can be resolved
BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

# Ensure Vercel serverless environment flag is set
os.environ.setdefault('VERCEL', '1')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')

# Copy pre-seeded database into writable /tmp directory if needed
tmp_db = Path('/tmp/db.sqlite3')
seed_db = BASE_DIR / 'portfolio' / 'seed_data.sqlite3'
if not tmp_db.exists() or tmp_db.stat().st_size == 0:
    if seed_db.exists():
        try:
            shutil.copyfile(seed_db, tmp_db)
        except Exception as e:
            print(f"[Vercel] Error copying seed DB to /tmp: {e}")

import django
django.setup()

from django.core.management import call_command
from django.core.wsgi import get_wsgi_application

# Secondary safeguard: verify database has data
try:
    from portfolio.models import Skill, Project
    if Skill.objects.count() == 0 or Project.objects.count() == 0:
        call_command('migrate', interactive=False, verbosity=0)
        call_command('seed_portfolio', interactive=False, verbosity=0)
except Exception as err:
    print(f"[Vercel] Secondary DB setup notice: {err}")

application = get_wsgi_application()
app = application
handler = application
