# FootballDB Dataset

- `v1` contains the SQL scripts to create the v1 database in [`./v1/db/`](./v1/db/)
- `v2` contains the SQL scripts to create the v2 database in [`./v2/db/`](./v2/db/)
- `v3` contains the SQL scripts to create the v3 database in [`./v3/db/`](./v3/db/)

Each folder also contains the train and test (dev) data in different splits (100, 200, 300) to train the NL-to-SQL systems in [`../../src/train`](../../src/train/).
For the v3 data model, we further provide an additional labeled set of 859 NL-SQL pairs.
