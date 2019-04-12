/*
Navicat MySQL Data Transfer

Source Server         : local
Source Server Version : 50724
Source Host           : localhost:3306
Source Database       : practice

Target Server Type    : MYSQL
Target Server Version : 50724
File Encoding         : 65001

Date: 2019-04-12 16:48:48
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for morders
-- ----------------------------
DROP TABLE IF EXISTS `morders`;
CREATE TABLE `morders` (
  `O_Id` int(11) NOT NULL,
  `OrderDate` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `OrderPrice` decimal(10,2) DEFAULT NULL,
  `Customer` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`O_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of morders
-- ----------------------------
INSERT INTO `morders` VALUES ('1', '2008-12-29 00:00:00', '1000.00', 'Bush');
INSERT INTO `morders` VALUES ('2', '2008-11-23 00:00:00', '1600.00', 'Carter');
INSERT INTO `morders` VALUES ('3', '2008-10-05 00:00:00', '700.00', 'Bush');
INSERT INTO `morders` VALUES ('4', '2008-09-28 00:00:00', '300.00', 'Bush');
INSERT INTO `morders` VALUES ('5', '2008-08-06 00:00:00', '2000.00', 'Adams');
INSERT INTO `morders` VALUES ('6', '2008-07-21 00:00:00', '100.00', 'Carter');

-- ----------------------------
-- Table structure for norders
-- ----------------------------
DROP TABLE IF EXISTS `norders`;
CREATE TABLE `norders` (
  `Id_O` int(11) NOT NULL,
  `OrderNo` int(11) DEFAULT NULL,
  `Id_P` int(11) DEFAULT NULL,
  PRIMARY KEY (`Id_O`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of norders
-- ----------------------------
INSERT INTO `norders` VALUES ('1', '77895', '3');
INSERT INTO `norders` VALUES ('2', '44678', '3');
INSERT INTO `norders` VALUES ('3', '22456', '1');
INSERT INTO `norders` VALUES ('4', '24562', '1');
INSERT INTO `norders` VALUES ('5', '34764', '65');

-- ----------------------------
-- Table structure for npersons
-- ----------------------------
DROP TABLE IF EXISTS `npersons`;
CREATE TABLE `npersons` (
  `Id_P` int(11) NOT NULL,
  `LastName` varchar(255) DEFAULT NULL,
  `FirstName` varchar(255) DEFAULT NULL,
  `Address` varchar(255) DEFAULT NULL,
  `City` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Id_P`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of npersons
-- ----------------------------
INSERT INTO `npersons` VALUES ('1', 'Adams', 'John', 'Oxford Street', 'London');
INSERT INTO `npersons` VALUES ('2', 'Bush', 'George', 'Fifth Avenue', 'New York');
INSERT INTO `npersons` VALUES ('3', 'Carter', 'Thomas', 'Changan Street', 'Beijing');

-- ----------------------------
-- Table structure for orders
-- ----------------------------
DROP TABLE IF EXISTS `orders`;
CREATE TABLE `orders` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Company` varchar(255) DEFAULT NULL,
  `OrderNumber` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of orders
-- ----------------------------
INSERT INTO `orders` VALUES ('1', 'IBM', '3532');
INSERT INTO `orders` VALUES ('2', 'W3School', '2356');
INSERT INTO `orders` VALUES ('3', 'Apple', '4698');
INSERT INTO `orders` VALUES ('4', 'W3School', '6953');

-- ----------------------------
-- Table structure for persons
-- ----------------------------
DROP TABLE IF EXISTS `persons`;
CREATE TABLE `persons` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `LastName` varchar(255) DEFAULT NULL,
  `FirstName` varchar(255) DEFAULT NULL,
  `Address` varchar(255) DEFAULT NULL,
  `City` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of persons
-- ----------------------------
INSERT INTO `persons` VALUES ('1', 'Adams', 'John', 'Oxford Street', 'London');
INSERT INTO `persons` VALUES ('2', 'Bush', 'news', 'Fifth Avenue', 'Nanjing');
INSERT INTO `persons` VALUES ('3', 'Carter', 'Thomas', 'Changan Street', 'Beijing');
INSERT INTO `persons` VALUES ('20', 'Gates', 'Bill', 'xuanwumen 10', 'Beijing');
