import pyodbc

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=DESKTOP-83CBCMC;"
    "DATABASE=TESTDB;"
    "UID=sa;"
    "PWD=xxx"
)
cursor = conn.cursor()


# MSSQL CREATE TABLE
# USE [TestDB]
# GO
# ****** Object:  Table [dbo].[TESTTABLE]    Script Date: 2021/1/21 上午 09:53:09 ******/
# SET ANSI_NULLS ON
# GO

# SET QUOTED_IDENTIFIER ON
# GO

# CREATE TABLE [dbo].[TESTTABLE](
# 	[ID] [int] IDENTITY(1,1) NOT NULL,
# 	[USER_NAME] [nvarchar](20) NULL,
# 	[USER_PHONE] [nvarchar](20) NULL,
# 	[USER_MAIL] [nvarchar](20) NULL,
# 	[USER_ADD] [nvarchar](20) NULL,
# 	[USER_DATETIME] [nvarchar](15) NULL,
#  CONSTRAINT [PK_TESTTABLE] PRIMARY KEY CLUSTERED
# (
# 	[ID] ASC
# )WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
# ) ON [PRIMARY]
# GO
