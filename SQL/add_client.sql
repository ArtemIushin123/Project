USE [DOCTOR]
GO
/****** Object:  StoredProcedure [dbo].[add_client]    Script Date: 24.04.2023 21:49:09 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER procedure [dbo].[add_client]
as
INSERT INTO Client(Client_Name, Telephone, Client_city, Mail) values('TestUser', '123456','spb', 'Емае')