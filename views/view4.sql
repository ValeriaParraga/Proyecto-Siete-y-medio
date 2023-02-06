USE sah;
CREATE VIEW sah.ranking AS
 SELECT 
        g.player_id AS player_id,
        SUM((g.ending_points - g.starting_points)) AS earningpoints,
        COUNT(DISTINCT c.cardgame_id) AS gamesplayed,
        SUM(((((HOUR(c.end_hour) - HOUR(c.start_hour)) * 60) + (MINUTE(c.end_hour) - MINUTE(c.start_hour))) + ((SECOND(c.end_hour) - SECOND(c.start_hour)) / 60))) AS minutesplayed
    FROM
        (sah.cardgame c
        JOIN sah.player_game g)
    WHERE
        (c.cardgame_id = g.cardgame_id)
    GROUP BY g.player_id