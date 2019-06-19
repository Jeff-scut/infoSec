CREATE TABLE IF NOT EXISTS `teacherInfo`(
	`id` INT NOT NULL AUTO_INCREMENT,
	`name` CHAR(20),
	`type` CHAR(20),
	`url` TEXT,
	`recordTime` DATETIME,
	PRIMARY KEY (`id`)
);