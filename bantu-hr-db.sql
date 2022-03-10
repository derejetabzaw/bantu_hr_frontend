use  `bantu-hr-db`;

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
    image Blob
);

