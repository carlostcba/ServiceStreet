USE ServiceStreet;
GO

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='sucursales_ga' AND xtype='U')
CREATE TABLE sucursales_ga (
    id INT IDENTITY(1,1) PRIMARY KEY,
    location_code NVARCHAR(50) NOT NULL,
    branch_number INT NULL,
    branch_name NVARCHAR(100) NULL,
    address NVARCHAR(255) NULL,
    city NVARCHAR(100) NULL,
    postal_code NVARCHAR(10) NULL,
    province NVARCHAR(100) NULL,
    geo_url NVARCHAR(500) NULL
);
GO
