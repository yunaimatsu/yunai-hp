import { Pool } from 'pg';

const pool = new Pool({
  user: 'your-db-user',
  host: 'your-db-host',
  database: 'your-database-name',
  password: 'your-db-password',
  port: 5432,
});

interface QueryResult<T> {
  rows: T[];
}

export default {
  query: <T>(text: string, params?: any[]): Promise<QueryResult<T>> => pool.query(text, params),
};
