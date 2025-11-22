# Edu-Master Docker Deployment Guide

## Quick Start

### Build and run with Docker Compose:

```bash
cd /path/to/edu-master

# Build the image
docker-compose build

# Start the services
docker-compose up -d

# Run migrations (first time only)
docker-compose exec web python manage.py migrate

# Create superuser (first time only)
docker-compose exec web python manage.py createsuperuser
```

The app will be available at:
- **Web**: http://localhost:80 (via Nginx)
- **Django (direct)**: http://localhost:8000

---

## What's Included

### Services:
1. **web** - Django application running with Gunicorn
2. **nginx** - Reverse proxy and static file server
3. **db** - Placeholder (using SQLite by default)

### Features:
- ✅ Production-ready Gunicorn WSGI server
- ✅ Nginx reverse proxy with gzip compression
- ✅ Static file and media serving
- ✅ Docker volumes for persistence
- ✅ Docker network isolation
- ✅ Automatic migrations on startup

---

## Useful Commands

```bash
# View logs
docker-compose logs -f web

# Stop services
docker-compose down

# Remove everything (including volumes)
docker-compose down -v

# Rebuild image
docker-compose build --no-cache

# Access Django shell
docker-compose exec web python manage.py shell

# Collect static files
docker-compose exec web python manage.py collectstatic --noinput
```

---

## Production Checklist

Before deploying to production:

- [ ] Update `SECRET_KEY` in `docker-compose.yml`
- [ ] Set `DEBUG=False` in environment
- [ ] Update `ALLOWED_HOSTS` with your domain
- [ ] Use PostgreSQL instead of SQLite (uncomment db service in compose file)
- [ ] Set up environment variables properly (use `.env` file)
- [ ] Configure domain/SSL with Nginx
- [ ] Set up backups for media and database
- [ ] Monitor logs and performance

---

## Optional: Use PostgreSQL

Uncomment the `db` service in `docker-compose.yml` and update the web service environment:

```yaml
environment:
  - DATABASE_URL=postgresql://edu_user:edu_password@db:5432/edu_master
```

Then rebuild and restart:

```bash
docker-compose up -d --build
```

---

## Deployment to Cloud

### For AWS/DigitalOcean/etc:

1. Push your code to a repository (GitHub)
2. SSH into your server
3. Clone the repo
4. Install Docker and Docker Compose
5. Run: `docker-compose up -d`
6. Set up domain with DNS and SSL (Certbot + Nginx)

### Example for DigitalOcean:
```bash
# SSH into droplet
ssh root@your_server_ip

# Clone repo
git clone https://github.com/yourusername/edu-master.git
cd edu-master

# Install Docker (if needed)
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Start services
sudo docker-compose up -d

# View status
sudo docker-compose ps
```

---

## Notes

- Current setup uses SQLite for simplicity
- Media and static files are persisted in Docker volumes
- All data persists after container restart
- Use environment variables for sensitive data in production
