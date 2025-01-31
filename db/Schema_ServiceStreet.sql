USE [ServiceStreet]
GO
/****** Object:  Table [dbo].[BranchesGa]    Script Date: 2025-01-31 11:29:57 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[BranchesGa](
	[branchID] [int] NOT NULL,
	[locationCode] [nvarchar](50) NOT NULL,
	[branchNumber] [nvarchar](5) NULL,
	[branchName] [nvarchar](100) NULL,
	[address] [nvarchar](255) NULL,
	[address2] [nvarchar](255) NULL,
	[address3] [nvarchar](255) NULL,
	[city] [nvarchar](100) NULL,
	[postalCode] [nvarchar](10) NULL,
	[province] [nvarchar](100) NULL,
	[geoUrl] [nvarchar](500) NULL,
PRIMARY KEY CLUSTERED 
(
	[branchID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[IncidentClosed]    Script Date: 2025-01-31 11:29:57 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[IncidentClosed](
	[incidentID] [int] NOT NULL,
	[incidentNumber] [nvarchar](50) NULL,
	[state] [nvarchar](50) NULL,
	[shortDescription] [nvarchar](max) NULL,
	[description] [nvarchar](max) NULL,
	[location] [nvarchar](100) NULL,
	[openedAt] [datetime] NULL,
	[userEnd] [nvarchar](100) NULL,
	[assignedTo] [nvarchar](100) NULL,
	[assignmentDate] [datetime] NULL,
	[resolutionDate] [datetime] NULL,
	[assignmentGroup] [nvarchar](100) NULL,
	[assignedRead] [bit] NULL,
	[assignedReadTime] [datetime] NULL,
	[lastModification] [datetime] NULL,
PRIMARY KEY CLUSTERED 
(
	[incidentID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY],
UNIQUE NONCLUSTERED 
(
	[incidentNumber] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[IncidentGa]    Script Date: 2025-01-31 11:29:57 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[IncidentGa](
	[incidentID] [int] IDENTITY(1,1) NOT NULL,
	[incidentNumber] [nvarchar](50) NULL,
	[state] [nvarchar](50) NULL,
	[shortDescription] [nvarchar](max) NULL,
	[description] [nvarchar](max) NULL,
	[location] [nvarchar](100) NULL,
	[openedAt] [datetime] NULL,
	[userEnd] [nvarchar](100) NULL,
	[assignedTo] [nvarchar](100) NULL,
	[assignmentDate] [datetime] NULL,
	[resolutionDate] [datetime] NULL,
	[assignmentGroup] [nvarchar](100) NULL,
	[assignedRead] [bit] NULL,
	[assignedReadTime] [datetime] NULL,
	[lastModification] [datetime] NULL,
PRIMARY KEY CLUSTERED 
(
	[incidentID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY],
UNIQUE NONCLUSTERED 
(
	[incidentNumber] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[IncidentNotes]    Script Date: 2025-01-31 11:29:57 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[IncidentNotes](
	[NoteID] [int] IDENTITY(1,1) NOT NULL,
	[IncidentNumber] [nvarchar](50) NOT NULL,
	[NoteText] [nvarchar](max) NOT NULL,
	[CreatedBy] [nvarchar](255) NOT NULL,
	[CreatedAt] [datetime] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[NoteID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[IncidentOpen]    Script Date: 2025-01-31 11:29:57 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[IncidentOpen](
	[incidentID] [int] NOT NULL,
	[incidentNumber] [nvarchar](50) NULL,
	[state] [nvarchar](50) NULL,
	[shortDescription] [nvarchar](max) NULL,
	[description] [nvarchar](max) NULL,
	[location] [nvarchar](100) NULL,
	[openedAt] [datetime] NULL,
	[userEnd] [nvarchar](100) NULL,
	[assignedTo] [nvarchar](100) NULL,
	[assignmentDate] [datetime] NULL,
	[resolutionDate] [datetime] NULL,
	[assignmentGroup] [nvarchar](100) NULL,
	[assignedRead] [bit] NULL,
	[assignedReadTime] [datetime] NULL,
	[lastModification] [datetime] NULL,
PRIMARY KEY CLUSTERED 
(
	[incidentID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY],
UNIQUE NONCLUSTERED 
(
	[incidentNumber] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[IncidentStatus]    Script Date: 2025-01-31 11:29:57 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[IncidentStatus](
	[StatusID] [int] IDENTITY(1,1) NOT NULL,
	[StatusName] [nvarchar](50) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[StatusID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY],
UNIQUE NONCLUSTERED 
(
	[StatusName] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[SocialMediaUsers]    Script Date: 2025-01-31 11:29:57 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[SocialMediaUsers](
	[UserID] [int] IDENTITY(1,1) NOT NULL,
	[GoogleID] [varchar](255) NULL,
	[Email] [varchar](255) NOT NULL,
	[FullName] [varchar](255) NULL,
	[ProfilePictureURL] [varchar](500) NULL,
	[PasswordHash] [varchar](255) NULL,
	[AccessToken] [text] NULL,
	[RefreshToken] [text] NULL,
	[CreatedAt] [datetime] NULL,
	[LastLoginAt] [datetime] NULL,
PRIMARY KEY CLUSTERED 
(
	[UserID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY],
UNIQUE NONCLUSTERED 
(
	[GoogleID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY],
UNIQUE NONCLUSTERED 
(
	[Email] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
ALTER TABLE [dbo].[IncidentClosed] ADD  DEFAULT ((0)) FOR [assignedRead]
GO
ALTER TABLE [dbo].[IncidentClosed] ADD  DEFAULT (getdate()) FOR [lastModification]
GO
ALTER TABLE [dbo].[IncidentGa] ADD  DEFAULT ((0)) FOR [assignedRead]
GO
ALTER TABLE [dbo].[IncidentGa] ADD  DEFAULT (getdate()) FOR [lastModification]
GO
ALTER TABLE [dbo].[IncidentNotes] ADD  DEFAULT (getdate()) FOR [CreatedAt]
GO
ALTER TABLE [dbo].[IncidentOpen] ADD  DEFAULT ((0)) FOR [assignedRead]
GO
ALTER TABLE [dbo].[IncidentOpen] ADD  DEFAULT (getdate()) FOR [lastModification]
GO
ALTER TABLE [dbo].[SocialMediaUsers] ADD  DEFAULT (getdate()) FOR [CreatedAt]
GO
ALTER TABLE [dbo].[SocialMediaUsers] ADD  DEFAULT (getdate()) FOR [LastLoginAt]
GO
/****** Object:  StoredProcedure [dbo].[AssignAndMoveIncident]    Script Date: 2025-01-31 11:29:57 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[AssignAndMoveIncident]
    @incidentNumber NVARCHAR(50), -- Número del incidente
    @userID NVARCHAR(100)         -- ID del usuario a asignar
AS
BEGIN
    SET NOCOUNT ON;

    -- Verificar si el registro existe en IncidentGa con el estado 'Nuevo'
    IF EXISTS (SELECT 1 FROM IncidentGa WHERE incidentNumber = @incidentNumber AND state = 'Nuevo')
    BEGIN
        -- Mover el registro a la tabla IncidentOpen
        INSERT INTO IncidentOpen (incidentID, incidentNumber, state, shortDescription, description, location, openedAt, userEnd, assignedTo, assignmentDate, resolutionDate, assignmentGroup)
        SELECT incidentID, incidentNumber, 'En curso', shortDescription, description, location, openedAt, userEnd, @userID, CURRENT_TIMESTAMP, resolutionDate, assignmentGroup
        FROM IncidentGa
        WHERE incidentNumber = @incidentNumber AND state = 'Nuevo';

        -- Eliminar el registro de la tabla IncidentGa
        DELETE FROM IncidentGa
        WHERE incidentNumber = @incidentNumber AND state = 'Nuevo';
    END
    ELSE
    BEGIN
        -- Si no se encuentra el registro, lanzar un error
        RAISERROR ('No se encontró un registro con el número de incidente especificado y estado "Nuevo".', 16, 1);
    END
END;
GO
/****** Object:  StoredProcedure [dbo].[MoveClosedOrResolvedIncidents]    Script Date: 2025-01-31 11:29:57 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[MoveClosedOrResolvedIncidents]
AS
BEGIN
    SET NOCOUNT ON;

    -- Mover registros de IncidentGa a IncidentCloses
    INSERT INTO IncidentClosed (incidentID, incidentNumber, state, shortDescription, description, location, openedAt, userEnd, assignedTo, assignmentDate, resolutionDate, assignmentGroup)
    SELECT incidentID, incidentNumber, state, shortDescription, description, location, openedAt, userEnd, assignedTo, assignmentDate, resolutionDate, assignmentGroup
    FROM IncidentGa
    WHERE state IN ('Cerrado', 'Resuelto');

    -- Eliminar los registros movidos de IncidentGa
    DELETE FROM IncidentGa
    WHERE state IN ('Cerrado', 'Resuelto');
END;
GO
/****** Object:  StoredProcedure [dbo].[UpdateIncidentStatusAndAddNote]    Script Date: 2025-01-31 11:29:57 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- Crear el Stored Procedure
CREATE PROCEDURE [dbo].[UpdateIncidentStatusAndAddNote]
    @incidentNumber NVARCHAR(50), -- Número del incidente
    @newStatus NVARCHAR(50),     -- Nuevo estado (Resuelto o En espera)
    @noteText NVARCHAR(MAX),     -- Texto de la nota
    @userID NVARCHAR(100)        -- Usuario que crea la nota
AS
BEGIN
    SET NOCOUNT ON;

    -- Validar que el nuevo estado sea 'Resuelto' o 'En espera'
    IF @newStatus NOT IN ('Resuelto', 'En espera', 'En curso', 'Cerrado')
    BEGIN
        RAISERROR ('El estado proporcionado no es válido. Solo se permiten los estados "Resuelto" o "En espera".', 16, 1);
        RETURN;
    END

    -- Validar que el incidente exista en IncidentOpen
    IF NOT EXISTS (SELECT 1 FROM IncidentOpen WHERE incidentNumber = @incidentNumber)
    BEGIN
        RAISERROR ('El incidente proporcionado no existe en la tabla IncidentOpen.', 16, 1);
        RETURN;
    END

    -- Actualizar el estado del incidente
    UPDATE IncidentOpen
    SET state = @newStatus
    WHERE incidentNumber = @incidentNumber;

    -- Insertar la nota en la tabla IncidentNotes
    INSERT INTO IncidentNotes (IncidentNumber, NoteText, CreatedBy, CreatedAt)
    VALUES (@incidentNumber, @noteText, @userID, GETDATE());

    PRINT 'El estado del incidente se actualizó correctamente y la nota fue agregada.';
END;
GO
