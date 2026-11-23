Here is a query that sums revenue per month (PostgreSQL syntax):

```sql
SELECT
    DATE_TRUNC('month', created_at) AS month,
    SUM(amount)                     AS revenue
FROM orders
GROUP BY DATE_TRUNC('month', created_at)
ORDER BY month;
```

Dialect variants:

```sql
-- MySQL / MariaDB
SELECT DATE_FORMAT(created_at, '%Y-%m-01') AS month, SUM(amount) AS revenue
FROM orders
GROUP BY month
ORDER BY month;

-- SQL Server
SELECT DATEFROMPARTS(YEAR(created_at), MONTH(created_at), 1) AS month,
       SUM(amount) AS revenue
FROM orders
GROUP BY DATEFROMPARTS(YEAR(created_at), MONTH(created_at), 1)
ORDER BY month;

-- SQLite
SELECT strftime('%Y-%m', created_at) AS month, SUM(amount) AS revenue
FROM orders
GROUP BY month
ORDER BY month;
```

Notes:
- Months with no orders will not appear. If you need them, join against a generated calendar of months.
- If `created_at` is a timestamp with time zone, truncation uses the session time zone. Convert first if you want a specific one, e.g. `DATE_TRUNC('month', created_at AT TIME ZONE 'Europe/Amsterdam')`.
- Add a `WHERE` clause if you need to exclude cancelled or refunded orders, which this table does not show.
