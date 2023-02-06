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
-- Table structure for table `player_game`
--

DROP TABLE IF EXISTS `player_game`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `player_game` (
  `cardgame_id` int(11) NOT NULL,
  `player_id` varchar(25) NOT NULL,
  `initial_card_id` char(3) NOT NULL,
  `starting_points` tinyint(4) NOT NULL,
  `ending_points` tinyint(4) NOT NULL,
  PRIMARY KEY (`cardgame_id`,`player_id`),
  KEY `player_id` (`player_id`),
  KEY `initial_card_id` (`initial_card_id`),
  CONSTRAINT `player_game_ibfk_1` FOREIGN KEY (`cardgame_id`) REFERENCES `cardgame` (`cardgame_id`),
  CONSTRAINT `player_game_ibfk_2` FOREIGN KEY (`player_id`) REFERENCES `player` (`player_id`),
  CONSTRAINT `player_game_ibfk_3` FOREIGN KEY (`initial_card_id`) REFERENCES `card` (`card_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `player_game`
--

LOCK TABLES `player_game` WRITE;
/*!40000 ALTER TABLE `player_game` DISABLE KEYS */;
INSERT INTO `player_game` VALUES (7895,'33630431S','O07',20,46),(7895,'58389700Z','O02',20,8),(7895,'78630946H','O05',20,1),(7897,'78630946H','O10',20,46),(7897,'80605450H','B09',20,7),(7897,'99798303S','E05',20,7),(7898,'41017571S','O09',20,5),(7898,'50719737E','O06',20,1),(7898,'84347707Z','O07',20,15),(7898,'99798303S','O05',20,16),(7899,'33630431S','C03',20,29),(7899,'58389700Z','E01',20,34),(7899,'99798303S','C05',20,14),(7900,'33630431S','C01',20,20),(7900,'58389700Z','E02',20,20),(7900,'99798303S','O06',20,20),(7901,'33630431S','B06',20,20),(7901,'58389700Z','O12',20,20),(7901,'99798303S','E07',20,20);
/*!40000 ALTER TABLE `player_game` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-06 18:16:24
