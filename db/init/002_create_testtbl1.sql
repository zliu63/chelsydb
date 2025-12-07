-- Creates table testtbl1 in chelsydb. Ensure you're connected to chelsydb.
\\connect chelsydb
CREATE TABLE IF NOT EXISTS testtbl1 (
  id BIGSERIAL PRIMARY KEY,
  data TEXT NOT NULL
);
