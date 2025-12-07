# chelsydb

Infrastructure code for chelsydb, focusing on PostgreSQL and environment provisioning.

## Structure
- `terraform/` — infra as code (DB instance, networking, security groups)
- `ansible/` — optional host/config management
- `db/init/` — seed/init SQL scripts
- `db/backup-restore/` — backup/restore scripts
- `environments/` — env-specific vars (dev/stage/prod)
- `scripts/` — CI/CD helpers, health checks
- `docker-compose.yml` — local dev DB

## Quick start (local dev DB)
- Ensure Docker is running.
- `docker-compose up -d` to start PostgreSQL for local development.
- Apply Terraform for cloud resources when ready: `terraform init && terraform apply` (with env tfvars).

## How to run chelsydb (local dev)

1) Start Postgres via docker-compose
   cd chelsydb
   docker-compose up -d

   - Container name: chelsydb-postgres
   - Port: 5432 -> localhost:5432
   - Default creds: testuser / testpass
   - Init scripts: db/init/*.sql (creates chelsydb and testtbl1)

2) Verify database
   docker exec -it chelsydb-postgres psql -U testuser -d chelsydb -c '\dt'
   docker exec -it chelsydb-postgres psql -U testuser -d chelsydb -c 'SELECT * FROM testtbl1;'

3) Use the Python accessor
   python -m venv .venv
   source .venv/bin/activate
   pip install -e .
   python -c "from chelsydb import insert_data, fetch_data; i=insert_data('hello'); print(fetch_data(i))"

4) Stop / clean
   docker-compose down          # keeps data volume
   docker-compose down -v       # removes data volume (drop data)
