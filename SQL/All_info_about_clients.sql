create procedure All_info_about_clients
as
Select Client.Client_Name, Client.Telephone, Client.Client_city from TimeTable
inner join Client on TimeTable.ClientId = Client.Id

exec All_info_about_clients