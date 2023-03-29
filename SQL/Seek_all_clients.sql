use DOCTOR

create procedure Seek_all_clients
as
Select Client.Client_Name from TimeTable
inner join Client on TimeTable.ClientId = Client.Id

exec Seek_all_clients