/*
SQLyog Enterprise - MySQL GUI v7.02 
MySQL - 5.0.22-community-nt : Database - news
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`news` /*!40100 DEFAULT CHARACTER SET gb2312 COLLATE gb2312_bin */;

USE `news`;

/*Table structure for table `article` */

DROP TABLE IF EXISTS `article`;

CREATE TABLE `article` (
  `id` int(11) NOT NULL auto_increment,
  `title` varchar(255) collate gb2312_bin default NULL,
  `author` varchar(20) collate gb2312_bin default NULL,
  `content` text collate gb2312_bin,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=gb2312 COLLATE=gb2312_bin;

/*Data for the table `article` */

insert  into `article`(`id`,`title`,`author`,`content`) values (2,'a','b','c'),(3,'hello','taotao','hello my name is zhaozhantao');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
