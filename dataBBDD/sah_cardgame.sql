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
-- Table structure for table `cardgame`
--

DROP TABLE IF EXISTS `cardgame`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cardgame` (
  `cardgame_id` int(11) NOT NULL AUTO_INCREMENT,
  `players` tinyint(4) NOT NULL,
  `rounds` tinyint(4) NOT NULL,
  `start_hour` datetime NOT NULL,
  `end_hour` datetime NOT NULL,
  `deck_id` char(3) NOT NULL,
  PRIMARY KEY (`cardgame_id`),
  KEY `deck_id` (`deck_id`),
  CONSTRAINT `cardgame_ibfk_1` FOREIGN KEY (`deck_id`) REFERENCES `deck` (`deck_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7903 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cardgame`
--

LOCK TABLES `cardgame` WRITE;
/*!40000 ALTER TABLE `cardgame` DISABLE KEYS */;
INSERT INTO `cardgame` VALUES (7895,3,5,'2023-01-24 16:37:49','2023-01-24 16:41:28','1'),(7896,4,5,'2023-01-24 17:04:39','2023-01-24 17:05:28','1'),(7897,3,2,'2023-01-24 17:20:52','2023-01-24 17:21:10','1'),(7898,4,5,'2023-01-24 17:28:15','2023-01-24 17:29:02','1'),(7899,3,2,'2023-01-24 18:36:58','2023-01-24 18:41:41','1'),(7900,3,2,'2023-01-24 18:42:50','2023-01-24 18:42:50','1'),(7901,3,2,'2023-01-24 18:42:59','2023-01-24 18:42:59','1'),(7902,3,2,'2023-01-24 23:00:51','2023-01-24 23:02:47','1');
/*!40000 ALTER TABLE `cardgame` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-06 18:16:23
