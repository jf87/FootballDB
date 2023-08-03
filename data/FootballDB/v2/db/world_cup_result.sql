create table world_cup_result
(
    year    integer not null
        constraint world_cup_result_world_cup_fk
            references world_cup,
    team_id integer not null
        constraint world_cup_result_national_team_fk
            references national_team,
    prize   varchar(15)
);

alter table world_cup_result
    owner to postgres;

create index world_cup_result_team_id_idx
    on world_cup_result (team_id);

create index world_cup_result_year_idx
    on world_cup_result (year);

grant select on world_cup_result to inode_readonly;

INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1930, 386, 'winner');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1934, 32, 'winner');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1938, 280, 'winner');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1950, 368, 'winner');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1954, 59, 'winner');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1958, 391, 'winner');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1962, 406, 'winner');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1966, 49, 'winner');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1970, 306, 'winner');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1974, 62, 'winner');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1978, 400, 'winner');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1982, 236, 'winner');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1986, 93, 'winner');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1990, 253, 'winner');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1994, 310, 'winner');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1998, 316, 'winner');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (2002, 117, 'winner');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (2006, 149, 'winner');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (2010, 288, 'winner');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (2014, 36, 'winner');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (2018, 438, 'winner');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (2022, 468, 'winner');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1930, 408, 'runner_up');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1934, 178, 'runner_up');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1938, 204, 'runner_up');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1950, 79, 'runner_up');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1954, 421, 'runner_up');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1958, 240, 'runner_up');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1962, 401, 'runner_up');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1966, 388, 'runner_up');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1970, 119, 'runner_up');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1974, 419, 'runner_up');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1978, 396, 'runner_up');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1982, 16, 'runner_up');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1986, 378, 'runner_up');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1990, 170, 'runner_up');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1994, 241, 'runner_up');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1998, 405, 'runner_up');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (2002, 173, 'runner_up');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (2006, 360, 'runner_up');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (2010, 134, 'runner_up');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (2014, 97, 'runner_up');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (2018, 434, 'runner_up');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (2022, 474, 'runner_up');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1930, 98, 'third');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1934, 232, 'third');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1938, 120, 'third');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1950, 13, 'third');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1954, 349, 'third');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1958, 383, 'third');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1962, 372, 'third');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1966, 297, 'third');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1970, 23, 'third');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1974, 282, 'third');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1978, 266, 'third');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1982, 211, 'third');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1986, 367, 'third');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1990, 202, 'third');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1994, 140, 'third');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1998, 203, 'third');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (2002, 128, 'third');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (2006, 376, 'third');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (2010, 330, 'third');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (2014, 175, 'third');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (2018, 430, 'third');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (2022, 482, 'third');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1930, 223, 'fourth');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1934, 196, 'fourth');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1938, 105, 'fourth');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1950, 344, 'fourth');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1954, 183, 'fourth');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1958, 144, 'fourth');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1962, 139, 'fourth');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1966, 48, 'fourth');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1970, 12, 'fourth');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1974, 395, 'fourth');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1978, 43, 'fourth');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1982, 143, 'fourth');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1986, 11, 'fourth');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1990, 246, 'fourth');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1994, 9, 'fourth');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (1998, 425, 'fourth');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (2002, 259, 'fourth');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (2006, 209, 'fourth');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (2010, 351, 'fourth');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (2014, 82, 'fourth');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (2018, 437, 'fourth');
INSERT INTO exp_v2.world_cup_result (year, team_id, prize) VALUES (2022, 483, 'fourth');
