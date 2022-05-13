CREATE TABLE `agenda`.`evento` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `evento` VARCHAR(255) NOT NULL,
  `dia` INT NOT NULL,
  `mes` INT NOT NULL,
  `year` INT NOT NULL,
  PRIMARY KEY (`id`));
