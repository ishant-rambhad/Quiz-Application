-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: db_quiz
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Table structure for table `registration_tb`
--

DROP TABLE IF EXISTS `registration_tb`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `registration_tb` (
  `SrNo` int NOT NULL AUTO_INCREMENT,
  `USERNAME` varchar(30) NOT NULL,
  `EMAIL` varchar(30) NOT NULL,
  `GENDER` enum('Male','Female') DEFAULT NULL,
  `PASSWORD` varchar(30) DEFAULT NULL,
  `RECHACK_PASS` varchar(30) DEFAULT NULL,
  `IMAGE` blob,
  UNIQUE KEY `SrNo` (`SrNo`),
  CONSTRAINT `registration_tb_chk_1` CHECK (((`Gender` = _utf8mb4'Male') or (`Gender` = _utf8mb4'Female')))
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registration_tb`
--

LOCK TABLES `registration_tb` WRITE;
/*!40000 ALTER TABLE `registration_tb` DISABLE KEYS */;
INSERT INTO `registration_tb` VALUES (1,'ishant','ishantrambhad@gmail.com','Male','ishant','ishant',_binary 'D:quiz contestlogo.jpg'),(2,'qwertyu','asdfghj','Male','sdfg','sdfg',NULL),(3,'qwert','asdfg','Male','sdf','sdf',NULL),(4,'qasdfghj','asdfghj','Male','mn','mn',NULL),(5,'qasdfghj','asdfghj','Male','mn','mn',NULL),(6,'qwerty','asdfghj','Male','nm','nm',NULL),(7,'qwertyuiop','sdfghjkl','Male','nn','nn',NULL),(8,'raj','raj@gmail.com','Male','sd','sd',NULL),(9,'prathmesh','prathmesh@gmail.com','Male','mn','mn',NULL),(10,'ashawini','ashu@gmail.com','Female','123','123',NULL),(11,'123','123','Male','123','123',NULL),(12,'ishant1234','ishant@gmai.com','Male','123','123',NULL),(13,'4741','wertyu','Male','asd','asd',NULL),(14,'1','1','Male','1','1',NULL),(15,'ishant12345','ishant223@gmail.com','Male','123','123',NULL);
/*!40000 ALTER TABLE `registration_tb` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-02 19:36:48
