create database `bantu-hr-db`;

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
insert into areas values
(1,"443","atlas","bole","new office");
select*from areas;
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

create table machine
(
	machineNumber int NOT NULL auto_increment,
	deviceName varchar(45),
    serialNumber varchar(15),
    ipAddress varchar(17),
    portNumber int,
    macAddress varchar(17),
    PRIMARY KEY (machineNumber)
);

create table personel
(
	personel_id varchar(10) primary key,
    devicePersonel_id int,
    Gender varchar(6) null,
    Department varchar(45) null,
    Employee_type varchar(45) null,
    Employment_date date null,
    full_name varchar(45) null,
    job_title varchar(45) null,
    paygrade double null,
    image longblob null,
    fingerprint int default 0
)
select current_date();
create table Department
(
		Department_id int primary key auto_increment,
        Department_name varchar(60),
        Parent_Department varchar(60)
);
insert into Department values (1,"web dev","IT");
select *from Department;
select Department_name from Department;
select Department_name from Department WHERE Parent_Department = "IT";
drop table Department;
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
round_off boolean, 
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
create table attendance_log
(
	attendance_id int primary key auto_increment,
    devicepersonel int,
    full_name varchar(50),
    check_date date,
    check_in time,
    check_out time,
    worked_hours time
);
drop table attendance_log;
select *from attendance_log;

	

