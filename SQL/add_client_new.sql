USE [DOCTOR]
GO
/****** Object:  StoredProcedure [dbo].[add_client]    Script Date: 26.04.2023 10:04:51 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER procedure [dbo].[add_client] @Client_name nvarchar(30), @telephone nvarchar(30), @Mail nvarchar(30) , @Client_city nvarchar(30)
as
INSERT INTO Client(Client_Name, Telephone, Mail, Client_city) values(@Client_name, @telephone, @Mail, @Client_city)