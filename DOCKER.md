# Quiz Pengupil - Docker Setup

## 🐳 Running with Docker

### Prerequisites
- Docker Desktop installed
- Docker Compose installed

### Quick Start

1. **Build and run containers:**
   ```bash
   docker-compose up -d
   ```

2. **Access the application:**
   - Web App: http://localhost:8080
   - phpMyAdmin: http://localhost:8081

3. **Stop containers:**
   ```bash
   docker-compose down
   ```

### Container Services

| Service | Port | Description |
|---------|------|-------------|
| web | 8080 | PHP Apache server |
| db | 3307 | MySQL database |
| phpmyadmin | 8081 | Database management |

### Database Connection

The app automatically uses these settings in Docker:
- Host: `db`
- User: `root`
- Password: `root`
- Database: `quiz_pengupil`

Database is auto-imported from `db/quiz_pengupil.sql` on first run.

### Useful Commands

```bash
# Rebuild containers
docker-compose up -d --build

# View logs
docker-compose logs -f web

# Execute command in container
docker-compose exec web bash

# Remove containers and volumes
docker-compose down -v
```

### For Local Development (XAMPP)

If using XAMPP instead of Docker:
1. Use the original `koneksi.php`
2. Access at: http://localhost/quiz-pengupil

### For CI/CD (GitHub Actions)

The GitHub Actions workflow doesn't use Docker - it runs PHP built-in server directly for faster testing.

### Production Deployment

To deploy with Docker:
1. Update environment variables in `docker-compose.yml`
2. Use stronger passwords
3. Consider using Docker secrets
4. Add nginx reverse proxy if needed
