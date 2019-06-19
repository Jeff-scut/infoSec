CREATE TABLE IF NOT EXISTS `teacherInfo`(
	`id` INT NOT NULL AUTO_INCREMENT,
	`name` CHAR(20),
	`type` CHAR(20),
	`url` TEXT,
	`recordTime` DATETIME,
	PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `scanInfo`(
	`id` INT NOT NULL AUTO_INCREMENT,
	`ip` CHAR(20),
	`port` INT,
	`state` CHAR(10),
	`createTime` DATETIME,
	PRIMARY KEY (`id`)
);