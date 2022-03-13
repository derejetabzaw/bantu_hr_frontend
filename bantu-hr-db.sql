use  `bantu-hr-db`;

create table areas
(
	areaId int NOT NULL,
    areaCode varchar(3),
    areaName varchar(45),
    parentArea varchar(45),
    remarks varchar(45),
	PRIMARY KEY (areaId)
);

create table device
(
	deviceId int NOT NULL,
	deviceName varchar(45),
    serialNumber varchar(15),
    ipAddress varchar(35),
    portNumber int,
    areaId int,
    PRIMARY KEY (deviceID),
    FOREIGN KEY (areaId) REFERENCES areas (areaId)
);

create table personel
(
	personel_id int primary key,
    Gender varchar(6),
    Department varchar(45),
    Employee_type varchar(45),
    Employemnet_date date,
    pasword varchar(255),
    first_name varchar(45),
    last_name varchar(45),
    job_title varchar(45),
    paygrade double,
    image Blob,
    deviceId int,
    FOREIGN KEY (deviceId) REFERENCES device(deviceID)
);
