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
-- Table structure for table `stud_details`
--

DROP TABLE IF EXISTS `stud_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stud_details` (
  `username` varchar(20) DEFAULT NULL,
  `Email_id` varchar(50) NOT NULL,
  PRIMARY KEY (`Email_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stud_details`
--

LOCK TABLES `stud_details` WRITE;
/*!40000 ALTER TABLE `stud_details` DISABLE KEYS */;
INSERT INTO `stud_details` VALUES ('ishanteee','123@gmail.com'),('789','789'),('850','850'),('741','852'),('12365','963'),('741','9636'),('852','96388'),('987','987'),('7415','98745'),('abab','abab@gmail.com'),('lklklko0ikl','fnfnu@'),('klklkll','hihihi'),('ishanthj','iiiisss@gmail.com'),('ishant3','ishant@78'),('ishant','ishant123@gmail.com'),('ishant@03','ishantrambhad@gmail.c'),('ishant','ishantrambhad@gmail.com'),('jgthfh','jlljuyt'),('mnmn','kmkm'),('mnmn','kmkm.'),('ioiop','lklklnn'),('no','nin'),('n','nin22'),('n','njik'),('opo','opo'),('poi','poi'),('opop','popoo'),('ishant','qwer@gmail.com'),('okmn','yui');
/*!40000 ALTER TABLE `stud_details` ENABLE KEYS */;
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
