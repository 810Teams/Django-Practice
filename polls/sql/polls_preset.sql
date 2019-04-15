# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 127.0.0.1 (MySQL 5.7.18)
# Database: webpro-practice
# Generation Time: 2019-03-27 15:42:23 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table polls_choice
# ------------------------------------------------------------

DROP TABLE IF EXISTS `polls_choice`;

CREATE TABLE `polls_choice` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `text` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `value` int(11) NOT NULL,
  `question_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `polls_choice_question_id_c5b4b260_fk_polls_question_id` (`question_id`),
  CONSTRAINT `polls_choice_question_id_c5b4b260_fk_polls_question_id` FOREIGN KEY (`question_id`) REFERENCES `polls_question` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

LOCK TABLES `polls_choice` WRITE;
/*!40000 ALTER TABLE `polls_choice` DISABLE KEYS */;

INSERT INTO `polls_choice` (`id`, `text`, `value`, `question_id`)
VALUES
	(1,'น่าเบื่อมาก',1,1),
	(2,'ค่อนข้างน่าเบื่อ',2,1),
	(3,'เฉยๆ',3,1),
	(4,'ค่อนข้างสนุก',4,1),
	(5,'สนุกมากๆ',5,1),
	(6,'ไม่รู้เรื่องเลย',1,2),
	(7,'รู้เรื่องนิดหน่อย',2,2),
	(8,'เฉยๆ',3,2),
	(9,'เรียนรู้เรื่อง',4,2),
	(10,'เรียนเข้าใจมากๆ',5,2),
	(11,'เครื่องช้ามาก',1,3),
	(12,'เครื่องค่อนข้างช้า',2,3),
	(13,'เฉยๆ',3,3),
	(14,'เครื่องเร็ว',4,3),
	(15,'เครื่องเร็วมากๆ',5,3),
	(16,'ง่ายมากๆ',1,4),
	(17,'ค่อนข้างง่าย',2,4),
	(18,'เฉยๆ',3,4),
	(19,'ค่อนข้างยาก',4,4),
	(20,'ยากมากๆ',5,4),
	(21,'ง่ายมากๆ',1,5),
	(22,'ค่อนข้างง่าย',2,5),
	(23,'เฉยๆ',3,5),
	(24,'ค่อนข้างยาก',4,5),
	(25,'ยากมากๆ',5,5),
	(26,'ง่ายมากๆ',1,6),
	(27,'ค่อนข้างง่าย',2,6),
	(28,'เฉยๆ',3,6),
	(29,'ค่อนข้างยาก',4,6),
	(30,'ยากมากๆ',5,6),
	(31,'ง่ายมากๆ',1,7),
	(32,'ค่อนข้างง่าย',2,7),
	(33,'เฉยๆ',3,7),
	(34,'ค่อนข้างยาก',4,7),
	(35,'ยากมากๆ',5,7),
	(36,'ง่ายมากๆ',1,8),
	(37,'ค่อนข้างง่าย',2,8),
	(38,'เฉยๆ',3,8),
	(39,'ค่อนข้างยาก',4,8),
	(40,'ยากมากๆ',5,8),
	(41,'ง่ายมากๆ',1,9),
	(42,'ค่อนข้างง่าย',2,9),
	(43,'เฉยๆ',3,9),
	(44,'ค่อนข้างยาก',4,9),
	(45,'ยากมากๆ',5,9),
	(46,'ไม่ชอบเลย',1,10),
	(47,'ค่อนข้างไม่ชอบ',2,10),
	(48,'เฉยๆ',3,10),
	(49,'ค่อนข้างชอบ',4,10),
	(50,'ชอบมากๆ',5,10),
	(51,'ไม่ชอบเลย',1,11),
	(52,'ค่อนข้างไม่ชอบ',2,11),
	(53,'เฉยๆ',3,11),
	(54,'ค่อนข้างชอบ',4,11),
	(55,'ชอบมากๆ',5,11),
	(56,'ไม่ชอบเลย',1,12),
	(57,'ค่อนข้างไม่ชอบ',2,12),
	(58,'เฉยๆ',3,12),
	(59,'ค่อนข้างชอบ',4,12),
	(60,'ชอบมากๆ',5,12),
	(61,'A',1,13),
	(62,'B+',2,13),
	(63,'B',3,13),
	(64,'C+',4,13),
	(65,'C',5,13),
	(66,'D+',6,13),
	(67,'D',7,13),
	(68,'F',8,13);

/*!40000 ALTER TABLE `polls_choice` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table polls_poll
# ------------------------------------------------------------

DROP TABLE IF EXISTS `polls_poll`;

CREATE TABLE `polls_poll` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `del_flag` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

LOCK TABLES `polls_poll` WRITE;
/*!40000 ALTER TABLE `polls_poll` DISABLE KEYS */;

INSERT INTO `polls_poll` (`id`, `title`, `start_date`, `end_date`, `del_flag`)
VALUES
	(1,'การสอนวิชา Web Programming',NULL,NULL,0),
	(2,'การสอนวิชา Web Programming',NULL,NULL,0),
	(3,'ความยากข้อสอบ mid-term',NULL,NULL,0),
	(4,'อาหารที่ชอบ',NULL,NULL,0),
	(5,'เกรดวิชา Web Pro ที่คิดว่าจะได้',NULL,NULL,0);

/*!40000 ALTER TABLE `polls_poll` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table polls_question
# ------------------------------------------------------------

DROP TABLE IF EXISTS `polls_question`;

CREATE TABLE `polls_question` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `text` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `type` varchar(2) COLLATE utf8mb4_unicode_ci NOT NULL,
  `poll_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `polls_question_poll_id_b6ace2e1_fk_polls_poll_id` (`poll_id`),
  CONSTRAINT `polls_question_poll_id_b6ace2e1_fk_polls_poll_id` FOREIGN KEY (`poll_id`) REFERENCES `polls_poll` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

LOCK TABLES `polls_question` WRITE;
/*!40000 ALTER TABLE `polls_question` DISABLE KEYS */;

INSERT INTO `polls_question` (`id`, `text`, `type`, `poll_id`)
VALUES
	(1,'อาจารย์บัณฑิตสอนน่าเบื่อไหม','01',2),
	(2,'นักศึกษาเรียนรู้เรื่องหรือไม่','01',2),
	(3,'เครื่องคอมพิวเตอร์ใช้งานดีหรือไม่','01',2),
	(4,'ข้อ 1','01',3),
	(5,'ข้อ 2','01',3),
	(6,'ข้อ 3','01',3),
	(7,'ข้อ 4','01',3),
	(8,'ข้อ 5','01',3),
	(9,'ข้อ 6','01',3),
	(10,'พิซซ่า','01',4),
	(11,'ไก่ทอด','01',4),
	(12,'แฮมเบอร์เกอร์','01',4),
	(13,'เกรดที่คิดว่าจะได้','01',5);

/*!40000 ALTER TABLE `polls_question` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;