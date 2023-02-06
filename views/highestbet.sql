create view `highest_bet` as
select 
player_game_round.player_id, 
max(player_game_round.bet_points) as maxPoints
from player_game_round
where player_game_round.bet_points = (select max(player_game_round.bet_points) from player_game_round)
group by player_game_round.player_id; 