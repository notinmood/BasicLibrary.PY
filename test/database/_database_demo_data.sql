/*
 Navicat MySQL Data Transfer

 Source Server         : local
 Source Server Type    : MySQL
 Source Server Version : 50723
 Source Host           : localhost:3306
 Source Schema         : mydemo

 Target Server Type    : MySQL
 Target Server Version : 50723
 File Encoding         : 65001

 Date: 27/12/2021 22:46:59
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for tmp_user
-- ----------------------------
DROP TABLE IF EXISTS `tmp_user`;
CREATE TABLE `tmp_user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `birthday` datetime NULL DEFAULT NULL,
  `postcode` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 12 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of tmp_user
-- ----------------------------
INSERT INTO `tmp_user` VALUES (1, 'zhangsan', '2021-12-24 09:07:05', 266000);
INSERT INTO `tmp_user` VALUES (4, 'lisi', '2021-12-15 09:07:26', 277521);
INSERT INTO `tmp_user` VALUES (10, 'zhangsan', '2021-12-24 09:07:05', 266000);
INSERT INTO `tmp_user` VALUES (11, 'hah', '2021-12-22 10:07:47', 303333);

SET FOREIGN_KEY_CHECKS = 1;
