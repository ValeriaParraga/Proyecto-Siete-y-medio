-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: dbvad.mysql.database.azure.com    Database: sah
-- ------------------------------------------------------
-- Server version	5.7.39-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Temporary view structure for view `highest_bet`
--

DROP TABLE IF EXISTS `highest_bet`;
/*!50001 DROP VIEW IF EXISTS `highest_bet`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `highest_bet` AS SELECT 
 1 AS `player_id`,
 1 AS `maxPoints`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `avg_bet_per_game`
--

DROP TABLE IF EXISTS `avg_bet_per_game`;
/*!50001 DROP VIEW IF EXISTS `avg_bet_per_game`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `avg_bet_per_game` AS SELECT 
 1 AS `cardgame_id`,
 1 AS `avgBetPoints`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `6_alt`
--

DROP TABLE IF EXISTS `6_alt`;
/*!50001 DROP VIEW IF EXISTS `6_alt`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `6_alt` AS SELECT 
 1 AS `identiﬁcador_partida`,
 1 AS `rondas_ganadas_banca`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `avg_bets_1st_round`
--

DROP TABLE IF EXISTS `avg_bets_1st_round`;
/*!50001 DROP VIEW IF EXISTS `avg_bets_1st_round`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `avg_bets_1st_round` AS SELECT 
 1 AS `cardgame_id`,
 1 AS `abp`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `lowest_bet`
--

DROP TABLE IF EXISTS `lowest_bet`;
/*!50001 DROP VIEW IF EXISTS `lowest_bet`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `lowest_bet` AS SELECT 
 1 AS `player_id`,
 1 AS `mpoints`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `ranking`
--

DROP TABLE IF EXISTS `ranking`;
/*!50001 DROP VIEW IF EXISTS `ranking`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `ranking` AS SELECT 
 1 AS `player_id`,
 1 AS `earningpoints`,
 1 AS `gamesplayed`,
 1 AS `minutesplayed`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `banks_in_game`
--

DROP TABLE IF EXISTS `banks_in_game`;
/*!50001 DROP VIEW IF EXISTS `banks_in_game`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `banks_in_game` AS SELECT 
 1 AS `cardgame_id`,
 1 AS `banks`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `ej10`
--

DROP TABLE IF EXISTS `ej10`;
/*!50001 DROP VIEW IF EXISTS `ej10`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `ej10` AS SELECT 
 1 AS `cardgame_id`,
 1 AS `avgpoints`,
 1 AS `maxnum`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `highest_bet`
--

/*!50001 DROP VIEW IF EXISTS `highest_bet`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`GPVAD`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `highest_bet` AS select `player_game_round`.`player_id` AS `player_id`,max(`player_game_round`.`bet_points`) AS `maxPoints` from `player_game_round` where (`player_game_round`.`bet_points` = (select max(`player_game_round`.`bet_points`) from `player_game_round`)) group by `player_game_round`.`player_id` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `avg_bet_per_game`
--

/*!50001 DROP VIEW IF EXISTS `avg_bet_per_game`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`GPVAD`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `avg_bet_per_game` AS select `player_game_round`.`cardgame_id` AS `cardgame_id`,avg(`player_game_round`.`bet_points`) AS `avgBetPoints` from `player_game_round` group by `player_game_round`.`cardgame_id` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `6_alt`
--

/*!50001 DROP VIEW IF EXISTS `6_alt`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`GPVAD`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `6_alt` AS select `pgr`.`cardgame_id` AS `identiﬁcador_partida`,sum((case when (`tbl_sibank`.`points_j` > `tbl_nobank`.`max_points_j`) then 1 when (`tbl_sibank`.`points_j` < `tbl_nobank`.`max_points_j`) then 0 end)) AS `rondas_ganadas_banca` from ((`sah`.`player_game_round` `pgr` join (select `pgr`.`cardgame_id` AS `cardgame_id`,`pgr`.`round_num` AS `round_num`,max(`tblint`.`points_j`) AS `max_points_j` from (`sah`.`player_game_round` `pgr` join (select `pgr`.`cardgame_id` AS `cardgame_id`,`pgr`.`round_num` AS `round_num`,`pgr`.`player_id` AS `player_id`,sum((`pgr`.`starting_round_points` + `pgr`.`ending_round_points`)) AS `points_j` from `sah`.`player_game_round` `pgr` where (`pgr`.`is_bank` = 0) group by `pgr`.`cardgame_id`,`pgr`.`round_num`,`pgr`.`player_id`) `tblint` on(((`tblint`.`cardgame_id` = `pgr`.`cardgame_id`) and (`tblint`.`round_num` = `pgr`.`round_num`)))) where (`pgr`.`is_bank` = 0) group by `pgr`.`cardgame_id`,`pgr`.`round_num`) `tbl_nobank` on(((`tbl_nobank`.`cardgame_id` = `pgr`.`cardgame_id`) and (`tbl_nobank`.`round_num` = `pgr`.`round_num`)))) join (select `pgr`.`cardgame_id` AS `cardgame_id`,`pgr`.`round_num` AS `round_num`,`pgr`.`player_id` AS `player_id`,sum((`pgr`.`starting_round_points` + `pgr`.`ending_round_points`)) AS `points_j` from `sah`.`player_game_round` `pgr` where (`pgr`.`is_bank` = 1) group by `pgr`.`cardgame_id`,`pgr`.`round_num`,`pgr`.`player_id`) `tbl_sibank` on(((`tbl_sibank`.`cardgame_id` = `pgr`.`cardgame_id`) and (`tbl_sibank`.`round_num` = `pgr`.`round_num`)))) where (`pgr`.`is_bank` = 1) group by `pgr`.`cardgame_id` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `avg_bets_1st_round`
--

/*!50001 DROP VIEW IF EXISTS `avg_bets_1st_round`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`GPVAD`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `avg_bets_1st_round` AS select `player_game_round`.`cardgame_id` AS `cardgame_id`,avg(`player_game_round`.`bet_points`) AS `abp` from `player_game_round` where (`player_game_round`.`round_num` = 0) group by `player_game_round`.`cardgame_id` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `lowest_bet`
--

/*!50001 DROP VIEW IF EXISTS `lowest_bet`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`GPVAD`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `lowest_bet` AS select `player_game_round`.`player_id` AS `player_id`,min(`player_game_round`.`bet_points`) AS `mpoints` from `player_game_round` where (`player_game_round`.`bet_points` = (select min(`player_game_round`.`bet_points`) from `player_game_round`)) group by `player_game_round`.`player_id` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `ranking`
--

/*!50001 DROP VIEW IF EXISTS `ranking`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`GPVAD`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `ranking` AS select `g`.`player_id` AS `player_id`,sum((`g`.`ending_points` - `g`.`starting_points`)) AS `earningpoints`,count(distinct `c`.`cardgame_id`) AS `gamesplayed`,sum(((((hour(`c`.`end_hour`) - hour(`c`.`start_hour`)) * 60) + (minute(`c`.`end_hour`) - minute(`c`.`start_hour`))) + ((second(`c`.`end_hour`) - second(`c`.`start_hour`)) / 60))) AS `minutesplayed` from (`cardgame` `c` join `player_game` `g`) where (`c`.`cardgame_id` = `g`.`cardgame_id`) group by `g`.`player_id` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `banks_in_game`
--

/*!50001 DROP VIEW IF EXISTS `banks_in_game`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`GPVAD`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `banks_in_game` AS select `player_game_round`.`cardgame_id` AS `cardgame_id`,sum(`player_game_round`.`is_bank`) AS `banks` from `player_game_round` group by `player_game_round`.`cardgame_id` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `ej10`
--

/*!50001 DROP VIEW IF EXISTS `ej10`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`GPVAD`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `ej10` AS select `player_game_round`.`cardgame_id` AS `cardgame_id`,avg(`player_game_round`.`bet_points`) AS `avgpoints`,max(`player_game_round`.`round_num`) AS `maxnum` from `player_game_round` group by `player_game_round`.`cardgame_id` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-06 18:16:29
