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
-- Table structure for table `card`
--

DROP TABLE IF EXISTS `card`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `card` (
  `card_id` char(3) NOT NULL,
  `card_name` varchar(25) NOT NULL,
  `card_value` decimal(3,1) NOT NULL,
  `card_priority` tinyint(4) NOT NULL,
  `card_real_value` tinyint(4) NOT NULL,
  `deck_id` char(3) NOT NULL,
  PRIMARY KEY (`card_id`),
  KEY `deck_id` (`deck_id`),
  CONSTRAINT `card_ibfk_1` FOREIGN KEY (`deck_id`) REFERENCES `deck` (`deck_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `card`
--

LOCK TABLES `card` WRITE;
/*!40000 ALTER TABLE `card` DISABLE KEYS */;
INSERT INTO `card` VALUES ('B01','As de Bastos',1.0,1,1,'1'),('B02','Dos de Bastos',2.0,1,2,'1'),('B03','Tres de Bastos',3.0,1,3,'1'),('B04','Cuatro de Bastos',4.0,1,4,'1'),('B05','Cinco de Bastos',5.0,1,5,'1'),('B06','Seis de Bastos',6.0,1,6,'1'),('B07','Siete de Bastos',7.0,1,7,'1'),('B08','Ocho de Bastos',8.0,1,1,'1'),('B09','Nueve de Bastos',9.0,1,1,'1'),('B10','Sota de Bastos',10.0,1,1,'1'),('B11','Caballo de Bastos',11.0,1,1,'1'),('B12','Rey de Bastos',12.0,1,1,'1'),('C01','As de Copas',1.0,3,1,'1'),('C02','Dos de Copas',2.0,3,2,'1'),('C03','Tres de Copas',3.0,3,3,'1'),('C04','Cuatro de Copas',4.0,3,4,'1'),('C05','Cinco de Copas',5.0,3,5,'1'),('C06','Seis de Copas',6.0,3,6,'1'),('C07','Siete de Copas',7.0,3,7,'1'),('C08','Ocho de Copas',8.0,3,1,'1'),('C09','Nueve de Copas',9.0,3,1,'1'),('C10','Sota de Copas',10.0,3,1,'1'),('C11','Caballo de Copas',11.0,3,1,'1'),('C12','Rey de Copas',12.0,3,1,'1'),('D01','As de Diamantes',1.0,4,1,'2'),('D02','Dos de Diamantes',2.0,4,2,'2'),('D03','Tres de Diamantes',3.0,4,3,'2'),('D04','Cuatro de Diamantes',4.0,4,4,'2'),('D05','Cinco de Diamantes',5.0,4,5,'2'),('D06','Seis de Diamantes',6.0,4,6,'2'),('D07','Siete de Diamantes',7.0,4,7,'2'),('D08','Ocho de Diamantes',8.0,4,1,'2'),('D09','Nueve de Diamantes',9.0,4,1,'2'),('D10','Diez de Diamantes',10.0,4,1,'2'),('D11','Jota(J) de Diamantes',11.0,4,1,'2'),('D12','Reina(Q) de Diamantes',12.0,4,1,'2'),('D13','Rey(R) de Diamantes',13.0,4,1,'2'),('E01','As de Espadas',1.0,2,1,'1'),('E02','Dos de Espadas',2.0,2,2,'1'),('E03','Tres de Espadas',3.0,2,3,'1'),('E04','Cuatro de Espadas',4.0,2,4,'1'),('E05','Cinco de Espadas',5.0,2,5,'1'),('E06','Seis de Espadas',6.0,2,6,'1'),('E07','Siete de Espadas',7.0,2,7,'1'),('E08','Ocho de Espadas',8.0,2,1,'1'),('E09','Nueve de Espadas',9.0,2,1,'1'),('E10','Sota de Espadas',10.0,2,1,'1'),('E11','Caballo de Espadas',11.0,2,1,'1'),('E12','Rey de Espadas',12.0,2,1,'1'),('O01','As de Oros',1.0,4,1,'1'),('O02','Dos de Oros',2.0,4,2,'1'),('O03','Tres de Oros',3.0,4,3,'1'),('O04','Cuatro de Oros',4.0,4,4,'1'),('O05','Cinco de Oros',5.0,4,5,'1'),('O06','Seis de Oros',6.0,4,6,'1'),('O07','Siete de Oros',7.0,4,7,'1'),('O08','Ocho de Oros',8.0,4,1,'1'),('O09','Nueve de Oros',9.0,4,1,'1'),('O10','Sota de Oros',10.0,4,1,'1'),('O11','Caballo de Oros',11.0,4,1,'1'),('O12','Rey de Oros',12.0,4,1,'1'),('P01','As de Picas',1.0,2,1,'2'),('P02','Dos de Picas',2.0,2,2,'2'),('P03','Tres de Picas',3.0,2,3,'2'),('P04','Cuatro de Picas',4.0,2,4,'2'),('P05','Cinco de Picas',5.0,2,5,'2'),('P06','Seis de Picas',6.0,2,6,'2'),('P07','Siete de Picas',7.0,2,7,'2'),('P08','Ocho de Picas',8.0,2,1,'2'),('P09','Nueve de Picas',9.0,2,1,'2'),('P10','Diez de Picas',10.0,2,1,'2'),('P11','Jota(J) de Picas',11.0,2,1,'2'),('P12','Reina(Q) de Picas',12.0,2,1,'2'),('P13','Rey(R) de Picas',12.0,2,1,'2'),('T01','As de Tréboles',1.0,1,1,'2'),('T02','Dos de Tréboles',2.0,1,2,'2'),('T03','Tres de Tréboles',3.0,1,3,'2'),('T04','Cuatro de Tréboles',4.0,1,4,'2'),('T05','Cinco de Tréboles',5.0,1,5,'2'),('T06','Seis de Tréboles',6.0,1,6,'2'),('T07','Siete de Tréboles',7.0,1,7,'2'),('T08','Ocho de Tréboles',8.0,1,1,'2'),('T09','Nueve de Tréboles',9.0,1,1,'2'),('T10','Diez de Tréboles',10.0,1,1,'2'),('T11','Jota(J) de Tréboles',11.0,1,1,'2'),('T12','Reina(Q) de Tréboles',12.0,1,1,'2'),('T13','Rey(R) de Tréboles',12.0,1,1,'2'),('Z01','As de Corazones',1.0,3,1,'2'),('Z02','Dos de Corazones',2.0,3,2,'2'),('Z03','Tres de Corazones',3.0,3,3,'2'),('Z04','Cuatro de Corazones',4.0,3,4,'2'),('Z05','Cinco de Corazones',5.0,3,5,'2'),('Z06','Seis de Corazones',6.0,3,6,'2'),('Z07','Siete de Corazones',7.0,3,7,'2'),('Z08','Ocho de Corazones',8.0,3,1,'2'),('Z09','Nueve de Corazones',9.0,3,1,'2'),('Z10','Diez de Corazones',10.0,3,1,'2'),('Z11','Jota(J) de Corazones',11.0,3,1,'2'),('Z12','Reina(Q) de Corazones',12.0,3,1,'2'),('Z13','Rey(R) de Corazones',12.0,3,1,'2');
/*!40000 ALTER TABLE `card` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-06 18:16:21
