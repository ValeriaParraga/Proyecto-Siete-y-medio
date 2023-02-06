use sah;
-- 4. 1 SELECTS:
select player_id, earningpoints, gamesplayed, minutesplayed 
from ranking 
order by earningpoints desc;
-- 4.2 SELECT:
select player_id, earningpoints, gamesplayed, minutesplayed 
from ranking 
order by gamesplayed desc;
-- 4.3 SELECT:
select player_id, earningpoints, gamesplayed, minutesplayed 
from ranking 
order by minutesplayed desc;