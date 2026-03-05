# Lab Deployment

1. Install docker from [docker.com](https://docs.docker.com/desktop/setup/install/windows-install/)
2. Run:
   ```sh
   cp .env.example .env
   cd ./Lab && docker-compose up --build -d
   ```

## Access

- Blog: http://localhost:8000