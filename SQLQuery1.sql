CREATE DATABASE Sales;
use Sales;

CREATE TABLE DimRegion(
	id_region int identity(1,1) primary key,
	region_name varchar(255)
);

CREATE TABLE DimCountry(
	id_country int identity(1,1) primary key,
	country varchar(255) null
);

CREATE TABLE DimItemType(
	id_type int identity(1,1) primary key,
	item_type varchar(255) null
);

CREATE TABLE DimPriority(
	id_priority int identity primary key,
	priority varchar(2) null,
	description varchar(255) null
);

CREATE TABLE DimMetode(
	id_metode int identity(1,1) primary key,
	metode varchar(20) null
);

CREATE TABLE FactSales(
	id int identity(1,1) primary key,
	id_region int null,
	id_country int null,
	id_type int null,
	id_priority int null,
	id_metode int null,
	order_year int null,
	ship_year int null,
	unit_sold int null,
	unit_price float null,
	FOREIGN KEY (id_region) REFERENCES DimRegion(id_region) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (id_country) REFERENCES DimCountry(id_country) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (id_type) REFERENCES DimItemType(id_type) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (id_priority) REFERENCES DimPriority(id_priority) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (id_metode) REFERENCES DimMetode(id_metode) ON DELETE CASCADE ON UPDATE CASCADE
);

UPDATE DimPriority
SET description = 'Medium'
WHERE id_priority = 1;

UPDATE DimPriority
SET description = 'Cheap'
WHERE id_priority = 2;

UPDATE DimPriority
SET description = 'Large'
WHERE id_priority = 3;

UPDATE DimPriority
SET description = 'High'
WHERE id_priority = 4;

INSERT INTO DimMetode VALUES('Offline'),('Online');

DELETE FROM DimItemType where item_type = '';

SELECT * FROM DimRegion;
SELECT * FROM DimCountry;
SELECT * FROM DimItemType;
SELECT * FROM DimPriority;
SELECT * FROM DimMetode;
SELECT * FROM FactSales;

DROP TABLE DimRegion;
DROP TABLE DimCountry;
DROP TABLE DimItemType;
DROP TABLE DimPriority;
DROP TABLE DimMetode;
DROP TABLE FactSales;

DELETE FROM FactSales;