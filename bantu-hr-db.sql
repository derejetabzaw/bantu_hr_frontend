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
drop table personel;

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


create table holiday(
holiday_id int primary key,
hoiday_name varchar(60),
min_unit int, 
unit int,
round_off int, 
symbol_in_report varchar(25)
);
create table MailAlertSetting
(
	alert_id int primary key auto_increment,
    email_sending_server varchar(300),
    server_port Decimal,
    email_account varchar(100),
    pwd varchar(100),
    email_adress varchar(100)
);
create table alarmSetting
(
 alarm_id int primary key auto_increment,
 max_late_days int,
 max_early_leaves int,
 max_number_of_absents int,
 email_sending_frequency varchar(40),
 email_for_attendance boolean,
 approval_alert boolean,
 pop_alert boolean
);