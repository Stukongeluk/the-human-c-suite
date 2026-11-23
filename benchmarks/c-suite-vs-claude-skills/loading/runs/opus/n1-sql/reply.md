Here's the query in PostgreSQL:

```sql
SELECT
    date_trunc('month', created_at)::date AS month,
    SUM(amount)                           AS revenue
FROM orders
GROUP BY date_trunc('month', created_at)
ORDER BY month;
```

This truncates each `created_at` to the first day of its month, groups on that value and sums `amount`. You get one row per month, oldest first, for example `2026-01-01 | 48250.00`.

**Other databases.** Only the month expression changes:

| Database   | Month expression                                    |
|------------|-----------------------------------------------------|
| MySQL      | `DATE_FORMAT(created_at, '%Y-%m-01')`               |
| SQL Server | `DATEFROMPARTS(YEAR(created_at), MONTH(created_at), 1)` (or `DATETRUNC(month, created_at)` on 2022+) |
| SQLite     | `strftime('%Y-%m', created_at)`                     |
| BigQuery   | `DATE_TRUNC(DATE(created_at), MONTH)`               |
| Snowflake  | `DATE_TRUNC('month', created_at)`                   |

**Things to check:**

- **Months with no orders don't show up.** If you need every month listed with a 0, join against a generated month series. In PostgreSQL:

  ```sql
  SELECT
      m.month::date                 AS month,
      COALESCE(SUM(o.amount), 0)    AS revenue
  FROM generate_series(
           date_trunc('month', (SELECT MIN(created_at) FROM orders)),
           date_trunc('month', (SELECT MAX(created_at) FROM orders)),
           interval '1 month'
       ) AS m(month)
  LEFT JOIN orders o
         ON o.created_at >= m.month
        AND o.created_at <  m.month + interval '1 month'
  GROUP BY m.month
  ORDER BY m.month;
  ```

- **Time zones.** If `created_at` is stored in UTC (`timestamptz`), orders placed late on the last day of a month in your local time can fall into the next month. To group by local months, convert first, for example `date_trunc('month', created_at AT TIME ZONE 'America/New_York')`, using your own zone.
- **Filtering a date range.** Filter on the raw column so an index on `created_at` can still be used:

  ```sql
  WHERE created_at >= '2026-01-01' AND created_at < '2027-01-01'
  ```

- **What counts as revenue.** This sums every row in `orders`. If the table also holds cancelled or refunded orders, or test orders, filter those out before you rely on the totals.
