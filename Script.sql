CREATE TABLE drug (
	id int AUTO_INCREMENT PRIMARY KEY,
	main_name VARCHAR(50)
);

CREATE TABLE mechanism (
	id int AUTO_INCREMENT PRIMARY KEY,
	name varchar(50)
);

CREATE TABLE drug_mechanism (
	id int AUTO_INCREMENT PRIMARY KEY,
	drug_id INT,
	mechanism_id INT,
	FOREIGN KEY (drug_id) REFERENCES drug(id),
	FOREIGN KEY (mechanism_id) REFERENCES mechanism(id)
);

create table entity (
	id int AUTO_INCREMENT PRIMARY KEY,
	type_id int,
	entity_id int,
	name varchar(50),
	FOREIGN KEY (type_id) REFERENCES entity_type(id) 
);

create table entity_type(
	id int AUTO_INCREMENT PRIMARY KEY,
	type_name VARCHAR(50)
);

# Seed entity type values
INSERT INTO entity_type VALUES (NULL, "drug");
INSERT INTO entity_type VALUES (NULL, "mechanism");

# Seed drugs, mechanism, and entities

# no mechanisms for prednisone
INSERT INTO drug VALUES (1, "Prednisone");
INSERT INTO entity VALUES (NULL, 1, 1, "Prednisone");

# Cyclophosphamide
INSERT INTO drug VALUES (2, "Cyclophosphamide");
INSERT INTO entity VALUES (NULL, 1, 2, "Cyclophosphamide");
INSERT INTO mechanism VALUES (1, "LGALS1 Edxpression Inhibitors");
INSERT INTO entity VALUES (NULL, 2, 1, "LGALS1 Expression Inhibitors");
INSERT INTO mechanism VALUES (2, "BCL2 Edxpression Inhibitors");
INSERT INTO entity VALUES (NULL, 2, 2, "BCL2 Edxpression Inhibitors");
INSERT INTO drug_mechanism VALUES (1, 2, 1);
INSERT INTO drug_mechanism VALUES (NULL, 2, 2);

