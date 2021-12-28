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

 Date: 28/12/2021 11:11:25
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
  `email` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `class` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `score` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 12 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of tmp_user
-- ----------------------------
INSERT INTO `tmp_user` VALUES (1, 'zhangsan', '2021-12-24 09:07:05', '266000@sina.com', '一', 66);
INSERT INTO `tmp_user` VALUES (2, 'lisi', '2021-12-15 09:07:26', '277521@qq.com', '三', 93);
INSERT INTO `tmp_user` VALUES (3, 'zhangsan', '2021-12-24 09:07:05', 'aa@qq.com', '二', 88);
INSERT INTO `tmp_user` VALUES (4, 'hah', '2021-12-22 10:07:47', 'wps@foxmail.com', '一', 97);

SET FOREIGN_KEY_CHECKS = 1;
