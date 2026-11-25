# SQL_more_queries

More MySQL: users and privileges, constraints (`NOT NULL`, `DEFAULT`,
`UNIQUE`, `PRIMARY KEY`, `AUTO_INCREMENT`, `FOREIGN KEY`), subqueries and
joins (`INNER JOIN`, `LEFT JOIN`) with `GROUP BY` and `ORDER BY`.

## Usage

```
cat 1-create_user.sql | mysql -hlocalhost -uroot -p
cat 10-genre_id_by_show.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
```

The `hbtn_0d_tvshows` dump must be imported before tasks 10 to 16.

## Files

| File | Description |
| --- | --- |
| `0-privileges.sql` | Lists the privileges of `user_0d_1` and `user_0d_2` |
| `1-create_user.sql` | Creates `user_0d_1` with all privileges |
| `2-create_read_user.sql` | Creates `hbtn_0d_2` and `user_0d_2` with `SELECT` only |
| `3-force_name.sql` | Table `force_name` with a `NOT NULL` name |
| `4-never_empty.sql` | Table `id_not_null` with a default id of 1 |
| `5-unique_id.sql` | Table `unique_id` with a unique id |
| `6-states.sql` | Database `hbtn_0d_usa` and table `states` |
| `7-cities.sql` | Table `cities` with a foreign key to `states` |
| `8-cities_of_california_subquery.sql` | Cities of California, with a subquery |
| `9-cities_by_state_join.sql` | All cities with their state name |
| `10-genre_id_by_show.sql` | Shows that have at least one genre |
| `11-genre_id_all_shows.sql` | All shows, `NULL` when there is no genre |
| `12-no_genre.sql` | Shows without a genre |
| `13-count_shows_by_genre.sql` | Number of shows for each genre |
| `14-my_genres.sql` | Genres of the show Dexter |
| `15-comedy_only.sql` | All Comedy shows |
| `16-shows_by_genre.sql` | All shows with their genres |
