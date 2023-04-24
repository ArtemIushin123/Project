use doctor
alter table Client add Mail Nvarchar(50)
update Client set Mail = 0
alter table Client alter column Mail Nvarchar(50) not null