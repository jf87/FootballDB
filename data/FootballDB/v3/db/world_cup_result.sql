create table world_cup_result
(
    year      integer not null
        constraint world_cup_result_world_cup_fk
            references world_cup,
    team_id   integer not null
        constraint world_cup_result_national_team_fk
            references national_team,
    winner    boolean,
    runner_up boolean,
    third     boolean,
    fourth    boolean
);

alter table world_cup_result
    owner to postgres;

create index world_cup_result_fourth_idx
    on world_cup_result (fourth);

create index world_cup_result_runner_up_idx
    on world_cup_result (runner_up);

create index world_cup_result_team_id_idx
    on world_cup_result (team_id);

create index world_cup_result_third_idx
    on world_cup_result (third);

create index world_cup_result_winner_idx
    on world_cup_result (winner);

create index world_cup_result_year_idx
    on world_cup_result (year);

grant select on world_cup_result to inode_readonly;

INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1930, 386, true, false, false, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1934, 32, true, false, false, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1938, 280, true, false, false, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1950, 368, true, false, false, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1954, 59, true, false, false, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1958, 391, true, false, false, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1962, 406, true, false, false, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1966, 49, true, false, false, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1970, 306, true, false, false, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1974, 62, true, false, false, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1978, 400, true, false, false, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1982, 236, true, false, false, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1986, 93, true, false, false, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1990, 253, true, false, false, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1994, 310, true, false, false, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1998, 316, true, false, false, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (2002, 117, true, false, false, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (2006, 149, true, false, false, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (2010, 288, true, false, false, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (2014, 36, true, false, false, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (2018, 438, true, false, false, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1930, 408, false, true, false, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1934, 178, false, true, false, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1938, 204, false, true, false, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1950, 79, false, true, false, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1954, 421, false, true, false, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1958, 240, false, true, false, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1962, 401, false, true, false, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1966, 388, false, true, false, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1970, 119, false, true, false, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1974, 419, false, true, false, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1978, 396, false, true, false, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1982, 16, false, true, false, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1986, 378, false, true, false, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1990, 170, false, true, false, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1994, 241, false, true, false, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1998, 405, false, true, false, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (2002, 173, false, true, false, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (2006, 360, false, true, false, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (2010, 134, false, true, false, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (2014, 97, false, true, false, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (2018, 434, false, true, false, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1930, 98, false, false, true, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1934, 232, false, false, true, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1938, 120, false, false, true, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1950, 13, false, false, true, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1954, 349, false, false, true, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1958, 383, false, false, true, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1962, 372, false, false, true, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1966, 297, false, false, true, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1970, 23, false, false, true, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1974, 282, false, false, true, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1978, 266, false, false, true, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1982, 211, false, false, true, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1986, 367, false, false, true, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1990, 202, false, false, true, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1994, 140, false, false, true, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1998, 203, false, false, true, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (2002, 128, false, false, true, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (2006, 376, false, false, true, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (2010, 330, false, false, true, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (2014, 175, false, false, true, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (2018, 430, false, false, true, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1930, 223, false, false, false, true);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1934, 196, false, false, false, true);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1938, 105, false, false, false, true);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1950, 344, false, false, false, true);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1954, 183, false, false, false, true);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1958, 144, false, false, false, true);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1962, 139, false, false, false, true);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1966, 48, false, false, false, true);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1970, 12, false, false, false, true);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1974, 395, false, false, false, true);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1978, 43, false, false, false, true);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1982, 143, false, false, false, true);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1986, 11, false, false, false, true);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1990, 246, false, false, false, true);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1994, 9, false, false, false, true);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (1998, 425, false, false, false, true);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (2002, 259, false, false, false, true);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (2006, 209, false, false, false, true);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (2010, 351, false, false, false, true);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (2014, 82, false, false, false, true);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (2018, 437, false, false, false, true);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (2022, 468, true, false, false, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (2022, 474, false, true, false, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (2022, 482, false, false, true, false);
INSERT INTO exp_v3.world_cup_result (year, team_id, winner, runner_up, third, fourth) VALUES (2022, 483, false, false, false, true);
