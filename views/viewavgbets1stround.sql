use sah;
CREATE VIEW `avg_bets_1st_round` AS 
SELECT cardgame_id, avg(bet_points) as abp
FROM player_game_round
where round_num = 0
group by cardgame_id