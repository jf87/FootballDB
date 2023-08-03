create table world_cup
(
    year           integer not null
        constraint world_cup_pk
            primary key,
    venue          varchar,
    goals_scored   integer,
    qualified_team integer,
    matches_played integer,
    attendance     integer
);

alter table world_cup
    owner to postgres;

create index world_cup_attendance_idx
    on world_cup (attendance);

create index world_cup_goals_scored_idx
    on world_cup (goals_scored);

create index world_cup_matches_played_idx
    on world_cup (matches_played);

create index world_cup_qualified_team_idx
    on world_cup (qualified_team);

create index world_cup_year_idx
    on world_cup (year);

grant select on world_cup to inode_readonly;

INSERT INTO exp_v3.world_cup (year, venue, goals_scored, qualified_team, matches_played, attendance) VALUES (1930, 'Uruguay', 70, 13, 18, 590549);
INSERT INTO exp_v3.world_cup (year, venue, goals_scored, qualified_team, matches_played, attendance) VALUES (1934, 'Italy', 70, 16, 17, 363000);
INSERT INTO exp_v3.world_cup (year, venue, goals_scored, qualified_team, matches_played, attendance) VALUES (1938, 'France', 84, 15, 18, 375700);
INSERT INTO exp_v3.world_cup (year, venue, goals_scored, qualified_team, matches_played, attendance) VALUES (1950, 'Brazil', 88, 13, 22, 1045246);
INSERT INTO exp_v3.world_cup (year, venue, goals_scored, qualified_team, matches_played, attendance) VALUES (1954, 'Switzerland', 140, 16, 26, 768607);
INSERT INTO exp_v3.world_cup (year, venue, goals_scored, qualified_team, matches_played, attendance) VALUES (1958, 'Sweden', 126, 16, 35, 819810);
INSERT INTO exp_v3.world_cup (year, venue, goals_scored, qualified_team, matches_played, attendance) VALUES (1962, 'Chile', 89, 16, 32, 893172);
INSERT INTO exp_v3.world_cup (year, venue, goals_scored, qualified_team, matches_played, attendance) VALUES (1966, 'England', 89, 16, 32, 1563135);
INSERT INTO exp_v3.world_cup (year, venue, goals_scored, qualified_team, matches_played, attendance) VALUES (1970, 'Mexico', 95, 16, 32, 1603975);
INSERT INTO exp_v3.world_cup (year, venue, goals_scored, qualified_team, matches_played, attendance) VALUES (1974, 'Germany', 97, 16, 38, 1865753);
INSERT INTO exp_v3.world_cup (year, venue, goals_scored, qualified_team, matches_played, attendance) VALUES (1978, 'Argentina', 102, 16, 38, 1545791);
INSERT INTO exp_v3.world_cup (year, venue, goals_scored, qualified_team, matches_played, attendance) VALUES (1982, 'Spain', 146, 24, 52, 2109723);
INSERT INTO exp_v3.world_cup (year, venue, goals_scored, qualified_team, matches_played, attendance) VALUES (1986, 'Mexico', 132, 24, 52, 2394031);
INSERT INTO exp_v3.world_cup (year, venue, goals_scored, qualified_team, matches_played, attendance) VALUES (1990, 'Italy', 115, 24, 52, 2516215);
INSERT INTO exp_v3.world_cup (year, venue, goals_scored, qualified_team, matches_played, attendance) VALUES (1994, 'USA', 141, 24, 52, 3587538);
INSERT INTO exp_v3.world_cup (year, venue, goals_scored, qualified_team, matches_played, attendance) VALUES (1998, 'France', 171, 32, 64, 2785100);
INSERT INTO exp_v3.world_cup (year, venue, goals_scored, qualified_team, matches_played, attendance) VALUES (2002, 'Korea/Japan', 161, 32, 64, 2705197);
INSERT INTO exp_v3.world_cup (year, venue, goals_scored, qualified_team, matches_played, attendance) VALUES (2006, 'Germany', 147, 32, 64, 3359439);
INSERT INTO exp_v3.world_cup (year, venue, goals_scored, qualified_team, matches_played, attendance) VALUES (2010, 'South Africa', 145, 32, 64, 3178856);
INSERT INTO exp_v3.world_cup (year, venue, goals_scored, qualified_team, matches_played, attendance) VALUES (2014, 'Brazil', 171, 32, 64, 3386810);
INSERT INTO exp_v3.world_cup (year, venue, goals_scored, qualified_team, matches_played, attendance) VALUES (2018, 'Russia', 169, 32, 64, 3031768);
INSERT INTO exp_v3.world_cup (year, venue, goals_scored, qualified_team, matches_played, attendance) VALUES (2022, 'Qatar', 172, 32, 64, 3404252);
