create table league
(
    league_id   varchar not null
        constraint league_pk
            primary key,
    league_name varchar,
    found_year  integer,
    country     varchar
);

alter table league
    owner to postgres;

create index league_found_year_idx
    on league (found_year);

grant select on league to inode_readonly;

INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q16481773', 'Italian Football Championship', 1898, 'Kingdom of Italy');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q12837728', 'First Professional Football League', 1924, 'Bulgaria');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q21208335', 'Football National Championship', 1898, 'Kingdom of Italy');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q16738482', 'Oberliga Nord (1947–1963)', 1947, 'West Germany');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q16056559', 'South African Premier Division', 1996, 'South Africa');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q235114', 'Super League Greece', 1927, 'Greece');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q182165', 'Russian Premier League', 1992, 'Russia');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q82595', 'Bundesliga', 1963, 'Germany');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q2301428', 'Toppserien', 1984, 'Norway');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q204752', 'Danish Superliga', 1991, 'Denmark');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q275665', 'A Lyga', 1991, 'Lithuania');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q202243', 'Allsvenskan', 1924, 'Sweden');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q235307', 'Serbian SuperLiga', 2006, 'Serbia');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q308798', 'Latvian Higher League', 1927, 'Latvia');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q391006', 'Premier League of Bosnia and Herzegovina', 2000, 'Bosnia and Herzegovina');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q485568', 'Süper Lig', 1956, 'Turkey');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q7074767', 'Oberliga Südwest', 1945, 'West Germany');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q237753', 'Romanian SuperLiga', 1909, 'Romania');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q477309', 'Israeli Premier League', 1999, 'Israel');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q219592', 'Austrian Bundesliga', 1974, 'Austria');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q275005', 'Slovenian PrvaLiga', 1991, 'Slovenia');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q317683', 'Oberliga West (1947-1963)', 1947, 'West Germany');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q317238', 'Oberliga Süd', 1945, 'West Germany');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q1189038', 'Lebanese Premier League', 1933, 'Lebanon');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q155965', 'Cypriot First Division', 1935, 'Cyprus');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q157553', 'DDR-Oberliga', 1948, 'German Democratic Reworld_cup_2023_03_13');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q326859', 'Azerbaijan Premier League', 1992, 'Azerbaijan');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q1522963', 'Gibraltar National League', 1905, 'United Kingdom');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q277945', 'NIFL Premiership', 1890, 'United Kingdom');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q239738', 'Meistriliiga', 1992, 'Estonia');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q255633', 'Saudi Professional League', 1950, 'Saudi Arabia');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q739479', 'Faroe Islands Premier League', 1942, 'Denmark');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q216022', 'Belgian First Division A', 1895, 'Belgium');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q978160', 'Football Superleague of Kosovo', 1945, 'Kosovo');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q167541', 'Eredivisie', 1956, 'Netherlands');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q182994', 'Liga Portugal', 1934, 'Portugal');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q220875', 'Veikkausliiga', 1990, 'Finland');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q1429268', 'Kansallinen Liiga', 1974, 'Finland');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q238113', 'Slovak Super Liga', 1993, 'Slovakia');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q326422', 'Kazakhstan Premier League', 1992, 'Kazakhstan');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q257282', 'Primera Divisió', 1995, 'Andorra');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q13394', 'Ligue 1', 1932, 'France');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q387662', 'Campionato Sammarinese di Calcio', 1985, 'San Marino');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q384531', 'Moldovan National Division', 1992, 'Moldova');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q218555', 'Welsh Premier League', 1992, 'United Kingdom');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q988698', 'Ligue 1 (Ivory Coast)', 1960, 'Ivory Coast');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q647746', 'Algerian Ligue Professionnelle 1', 1962, 'Algeria');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q237181', 'Armenian Premier League', 1992, 'Armenia');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q247788', 'Yemeni League', 1990, 'Yemen');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q276085', 'Nemzeti Bajnokság I', 1901, 'Hungary');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q15804', 'Serie A', 1898, 'Italy');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q3496311', 'Oberliga Berlin', 1946, 'West Germany');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q219007', 'Erovnuli Liga', 1990, 'Georgia');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q44763', 'Ekstraklasa', 1926, 'Poland');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q217016', 'Czech First League', 1993, 'Czech Reworld_cup_2023_03_13');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q271271', 'Montenegrin First League', 2006, 'Montenegro');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q245252', 'Luxembourg National Division', 1910, 'Luxembourg');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q244464', 'Belarusian Premier League', 1992, 'Belarus');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q201671', 'Eliteserien', 1937, 'Norway');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q206073', 'Premier League (Ukraine)', 1991, 'Ukraine');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q210836', 'Besta deild karla', 1912, 'Iceland');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q324867', 'La Liga', 1929, 'Spain');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q9448', 'Premiere League', 1992, 'United Kingdom');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q14377162', 'Scottish Premiership', 2013, 'Scotland');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q202699', 'Swiss Super League', 1897, 'Switzerland');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q210183', 'Albanian Superliga', 1930, 'Albania');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q275189', 'First Macedonian Football League', 1992, 'North Macedonia');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q162604', 'Prva HNL', 1991, 'Croatia');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q831202', 'League of Ireland Premier Division', 1985, 'Reworld_cup_2023_03_13 of Ireland');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q318480', 'Maltese Premier League', 1909, 'Malta');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q219586', 'A-League', 2004, 'Australia');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q206813', 'Campeonato Brasileiro Série A', 1959, 'Brazil');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q850132', 'Elite One', 1961, 'Cameroon');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q25000566', 'Canadian Premier League', 2017, 'Canada');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q1139408', 'Liga Promerica', 1921, 'Costa Rica');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q2289847', 'Liga Pro Betcris', 1957, 'Ecuador');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q794251', 'Ghana Premier League', 1956, 'Ghana');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q194641', 'Persian Gulf Pro League', 2001, 'Iran');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q276445', 'J1 League', 1992, 'Japan');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q764690', 'Liga MX ', 1943, 'Mexico');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q570246', 'Botola Pro 1', 1916, 'Morocco');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q1188284', 'Senegal Premier League', 1966, 'Senegal');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q794235', 'Tunisian Ligue Professionnelle 1', 1907, 'Tunisia');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q18543', 'Major League Soccer', 1993, 'United States');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q287453', 'Uruguayan Primera División', 1900, 'Uruguay');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q209318', 'Chinese Super League', 2004, 'China');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q830826', 'Nigerian Premier League', 1972, 'Nigeria');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q2386334', 'K League 1', 1983, 'South Korea');
INSERT INTO exp_v3.league (league_id, league_name, found_year, country) VALUES ('Q223170', 'Argentine Primera División', 1891, 'Argentina');
