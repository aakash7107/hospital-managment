-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: aakash
-- ------------------------------------------------------
-- Server version	8.0.21

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
-- Table structure for table `admin_reg`
--

DROP TABLE IF EXISTS `admin_reg`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin_reg` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `contact` varchar(20) DEFAULT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_reg`
--

LOCK TABLES `admin_reg` WRITE;
/*!40000 ALTER TABLE `admin_reg` DISABLE KEYS */;
INSERT INTO `admin_reg` VALUES (1,'aakash bhujel','aakashbhujel.ab@gmail.com','9863215864','aakash','aakash@10'),(2,'aakash bhujel','aakashbhujel.ab@gmail.com','9863215864','aakash','aakash@10'),(3,'aakash bhujel','aakashbhujel.ab@gmail.com','9863215864','aakash','aakash@10'),(4,'fsdf','dgdsg','ege','app','11'),(5,'sostika','uu','6786767','sos','11'),(6,'sandesh','ajds2423432','32423','san','11'),(7,'fdgdfsd','w','e','w','ew'),(8,'1','1','1','1','1'),(9,'re','eerer','rer','sa','ghjg'),(10,'sdf','ads','dsad','sad','da'),(11,'sdf','ads','dsad','sad','da'),(12,'sdf','ads','dsad','sad','da'),(13,'ad','dsad','dsad','df','df'),(14,'ad','dsad','dsad','aa','df'),(15,'sad','sfsa','saf','ss','ss'),(16,'fdg','gdg','dfg','11','11'),(17,'dfds','dsfsd','fdsf','h','h'),(18,'sdas','sad','sfs','ap','ap'),(19,'rh','gdfg','gfdn','n','n'),(20,'fdgd','dgdfg','fdgf','v','v'),(21,'sad','dsad','sd','c','c'),(22,'ada','das','sad','r','r'),(23,'dsg','gdg','dfg','q','q'),(24,'FDG','GDFG','DFG','B','B'),(25,'ef','fsf','ff','f','f'),(26,'gd','dgd','dg','u','u'),(27,'gd','dgd','dg','y','u'),(28,'sgtse','sgfs','sgsdg','s','s'),(29,'rg','gdfg','gf','x','x');
/*!40000 ALTER TABLE `admin_reg` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-09-04 10:10:11
