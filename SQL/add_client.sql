USE [DOCTOR]
GO
/****** Object:  StoredProcedure [dbo].[add_client]    Script Date: 24.04.2023 18:22:53 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER procedure [dbo].[add_client]
as
INSERT INTO Client(Client_Name, Telephone, Mail) values('TestUser', '123456', 'Емае')
