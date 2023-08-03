create table world_cup
(
    year           integer not null
        constraint world_cup_pk
            primary key,
    venue          varchar,
    goals_scored   integer,
    qualified_team integer,
    matches_played integer,
    attendance     integer,
    winner         integer
        constraint world_cup_national_team_winner_team_id_fk
            references national_team,
    runner_up      integer
        constraint world_cup_national_team_runner_up_team_id_fk
            references national_team,
    third          integer
        constraint world_cup_national_team_third_team_id_fk
            references national_team,
    fourth         integer
        constraint world_cup_national_team_fourth_team_id_fk
            references national_team
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

INSERT INTO exp_v1.world_cup (year, venue, goals_scored, qualified_team, matches_played, attendance, winner, runner_up, third, fourth) VALUES (2022, 'Qatar', 172, 32, 64, 3404252, 468, 474, 482, 483);
INSERT INTO exp_v1.world_cup (year, venue, goals_scored, qualified_team, matches_played, attendance, winner, runner_up, third, fourth) VALUES (1994, 'USA', 141, 24, 52, 3587538, 310, 241, 140, 9);
INSERT INTO exp_v1.world_cup (year, venue, goals_scored, qualified_team, matches_played, attendance, winner, runner_up, third, fourth) VALUES (1986, 'Mexico', 132, 24, 52, 2394031, 93, 378, 367, 11);
INSERT INTO exp_v1.world_cup (year, venue, goals_scored, qualified_team, matches_played, attendance, winner, runner_up, third, fourth) VALUES (1970, 'Mexico', 95, 16, 32, 1603975, 306, 119, 23, 12);
INSERT INTO exp_v1.world_cup (year, venue, goals_scored, qualified_team, matches_played, attendance, winner, runner_up, third, fourth) VALUES (1978, 'Argentina', 102, 16, 38, 1545791, 400, 396, 266, 43);
INSERT INTO exp_v1.world_cup (year, venue, goals_scored, qualified_team, matches_played, attendance, winner, runner_up, third, fourth) VALUES (1966, 'England', 89, 16, 32, 1563135, 49, 388, 297, 48);
INSERT INTO exp_v1.world_cup (year, venue, goals_scored, qualified_team, matches_played, attendance, winner, runner_up, third, fourth) VALUES (2014, 'Brazil', 171, 32, 64, 3386810, 36, 97, 175, 82);
INSERT INTO exp_v1.world_cup (year, venue, goals_scored, qualified_team, matches_played, attendance, winner, runner_up, third, fourth) VALUES (1938, 'France', 84, 15, 18, 375700, 280, 204, 120, 105);
INSERT INTO exp_v1.world_cup (year, venue, goals_scored, qualified_team, matches_played, attendance, winner, runner_up, third, fourth) VALUES (1962, 'Chile', 89, 16, 32, 893172, 406, 401, 372, 139);
INSERT INTO exp_v1.world_cup (year, venue, goals_scored, qualified_team, matches_played, attendance, winner, runner_up, third, fourth) VALUES (1982, 'Spain', 146, 24, 52, 2109723, 236, 16, 211, 143);
INSERT INTO exp_v1.world_cup (year, venue, goals_scored, qualified_team, matches_played, attendance, winner, runner_up, third, fourth) VALUES (1954, 'Switzerland', 140, 16, 26, 768607, 59, 421, 349, 183);
INSERT INTO exp_v1.world_cup (year, venue, goals_scored, qualified_team, matches_played, attendance, winner, runner_up, third, fourth) VALUES (1934, 'Italy', 70, 16, 17, 363000, 32, 178, 232, 196);
INSERT INTO exp_v1.world_cup (year, venue, goals_scored, qualified_team, matches_played, attendance, winner, runner_up, third, fourth) VALUES (2006, 'Germany', 147, 32, 64, 3359439, 149, 360, 376, 209);
INSERT INTO exp_v1.world_cup (year, venue, goals_scored, qualified_team, matches_played, attendance, winner, runner_up, third, fourth) VALUES (1930, 'Uruguay', 70, 13, 18, 590549, 386, 408, 98, 223);
INSERT INTO exp_v1.world_cup (year, venue, goals_scored, qualified_team, matches_played, attendance, winner, runner_up, third, fourth) VALUES (1990, 'Italy', 115, 24, 52, 2516215, 253, 170, 202, 246);
INSERT INTO exp_v1.world_cup (year, venue, goals_scored, qualified_team, matches_played, attendance, winner, runner_up, third, fourth) VALUES (2002, 'Korea/Japan', 161, 32, 64, 2705197, 117, 173, 128, 259);
INSERT INTO exp_v1.world_cup (year, venue, goals_scored, qualified_team, matches_played, attendance, winner, runner_up, third, fourth) VALUES (1950, 'Brazil', 88, 13, 22, 1045246, 368, 79, 13, 344);
INSERT INTO exp_v1.world_cup (year, venue, goals_scored, qualified_team, matches_played, attendance, winner, runner_up, third, fourth) VALUES (2010, 'South Africa', 145, 32, 64, 3178856, 288, 134, 330, 351);
INSERT INTO exp_v1.world_cup (year, venue, goals_scored, qualified_team, matches_played, attendance, winner, runner_up, third, fourth) VALUES (1974, 'Germany', 97, 16, 38, 1865753, 62, 419, 282, 395);
INSERT INTO exp_v1.world_cup (year, venue, goals_scored, qualified_team, matches_played, attendance, winner, runner_up, third, fourth) VALUES (1998, 'France', 171, 32, 64, 2785100, 316, 405, 203, 425);
INSERT INTO exp_v1.world_cup (year, venue, goals_scored, qualified_team, matches_played, attendance, winner, runner_up, third, fourth) VALUES (2018, 'Russia', 169, 32, 64, 3031768, 438, 434, 430, 437);
INSERT INTO exp_v1.world_cup (year, venue, goals_scored, qualified_team, matches_played, attendance, winner, runner_up, third, fourth) VALUES (1958, 'Sweden', 126, 16, 35, 819810, 391, 240, 383, 144);
