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
<<<<<<< HEAD

create table Department
(
		Department_id int primary key,
        Department_name varchar(60),
        Parent_Department varchar(60)
);

create table Approver
(
	Approver_id int primary key,
    Approver_type varchar(40),
    image blob
);

create table Position
(
	position_id int primary key,
    Deparment varchar(60),
    parent_position varchar(60),
    Position varchar(60),
    position_numner int,
    approved boolean
);

create table area 
(
	area_id int primary key,
    area_code varchar(100),
    Area_name varchar(60),
    parent_area varchar(60),
    remarks text
);
create table Device
(
	Device_id int primary key,
    Device_name varchar(100),
    Serial_number bigint,
    ip_address varchar(32),
    port_number int,
    Area varchar (60)
);
=======
>>>>>>> 74e92ac196fc42cad21db1bfbb6279d56be7d246
