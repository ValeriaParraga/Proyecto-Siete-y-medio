create view `lowest_bet` as
select 
player_game_round.player_id, 
min(player_game_round.bet_points) as mpoints
from player_game_round
where player_game_round.bet_points = (select min(player_game_round.bet_points) from player_game_round)
group by player_game_round.player_id; 