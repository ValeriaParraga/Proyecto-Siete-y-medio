
create view `avg_bet_per_game` as
select player_game_round.cardgame_id, avg(player_game_round.bet_points) as avgBetPoints
from player_game_round
group by cardgame_id;
SELECT * FROM sah.avg_bet_per_game;