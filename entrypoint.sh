#!/bin/bash
set -e

echo "=========================================="
echo "🚀 Django container starting (SQLite)"
echo "⏰ Time: $(date -Iseconds)"
echo "🖥 Host: $(hostname)"
echo "=========================================="

# ==============================
# Create required directories
# ==============================
echo "📁 Preparing directories..."
mkdir -p /app/static /app/media
chmod -R 755 /app/static /app/media

# ==============================
# Apply migrations
# ==============================
echo "🗄 Making migrations..."
python manage.py makemigrations

echo "🗄 Applying migrations..."
python manage.py migrate

# ==============================
# Create superuser (DEV ONLY)
# ==============================
echo "👤 Creating superuser (if not exists)..."

python manage.py shell << 'EOF'
from django.contrib.auth import get_user_model
User = get_user_model()

if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser(
        username="admin",
        password="admin123",
        email="admin@local.com"
    )
    print("✅ Superuser created: admin / admin123")
else:
    print("ℹ Superuser already exists")
EOF

# ==============================
# Collect static files
# ==============================
echo "🎨 Collecting static files..."
python manage.py collectstatic --noinput

# ==============================
# Start Django server
# ==============================
echo "🚀 Starting Django development server..."
exec python manage.py runserver 0.0.0.0:8000
