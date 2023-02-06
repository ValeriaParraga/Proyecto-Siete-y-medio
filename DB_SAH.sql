drop database if exists sah;
create database if not exists sah;
use sah;
create table player(
player_id varchar(25) primary key,
player_name varchar(40) not null,
player_risk TINYINT not null,
human TINYINT(1) not null
);

create table deck(
deck_id char(3) Primary Key,
deck_name varchar(25) not null
);
create table card(
card_id char(3) Primary Key,
card_name varchar(25) not null,
card_value DECIMAL(3,1) not null,
card_priority TINYINT not null,
card_real_value TINYINT not null,
deck_id char(3) not null,
foreign key(deck_id) references deck(deck_id)
);
create table cardgame(
cardgame_id int auto_increment Primary KEY,
players tinyint not null,
rounds tinyint not null,
start_hour DATETIME not null,
end_hour DATETIME not null,
deck_id char(3) not null,
foreign key (deck_id) references deck(deck_id)
);
create table player_game(
cardgame_id int not null,
player_id varchar(25),
foreign key (cardgame_id) references cardgame(cardgame_id),
foreign key (player_id) references player(player_id),
Primary key(cardgame_id, player_id),
initial_card_id char(3) not null,
foreign key(initial_card_id) references card(card_id),
starting_points TINYINT not null,
ending_points TINYINT not null
);
create table player_game_round(
round_num int,
cardgame_id int not null,
player_id varchar(25),
constraint card_game_player_id foreign key (cardgame_id, player_id) references player_game(cardgame_id, player_id),
Primary key(round_num, cardgame_id, player_id),
is_bank tinyint not null,
bet_points TINYINT not null,
card_value decimal(4,1) not null,
starting_round_points TINYINT not null,
ending_round_points TINYINT not null
);