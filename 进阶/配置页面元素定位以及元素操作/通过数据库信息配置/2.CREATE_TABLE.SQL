USE TEST

GO
--模块表
IF EXISTS (SELECT 1 FROM SYSOBJECTS WHERE NAME ='MOUDLE')
    DROP TABLE MOUDLE
GO
    CREATE TABLE MOUDLE
    (MOUDLE_ID             INTEGER NOT NULL IDENTITY PRIMARY KEY,--模块ID
     MOUDLE_NAME           NVARCHAR(20),                         --模块名称
     FRAME_NAME            NVARCHAR(20),                         --模块所在表单
     ELEMENT_SELECT        NVARCHAR(20),                         --定位模块的方法
     ELEMENT_SELECT_KEY    NVARCHAR(20),                         --定位模块所需参数
     ELEMENT_ACTION        INTEGER,                              --模块操作 1.单击
     ELEMENT_ACTION_KEY    NVARCHAR(30)                          --模块操作所需参数
    )
GO

GO
--父菜单表
IF EXISTS (SELECT 1 FROM SYSOBJECTS WHERE NAME ='PARENT_MENU')
    DROP TABLE PARENT_MENU
GO
    CREATE TABLE PARENT_MENU
    (PARENT_MENU_ID        INTEGER NOT NULL IDENTITY PRIMARY KEY,    --父菜单ID
     PARENT_MENU_NAME      NVARCHAR(20),                             --父菜单名称
     MOUDLE_ID             INTEGER NOT NULL,                         --父菜单所属模块ID
     FRAME_NAME            NVARCHAR(20),                             --父菜单所在表单
     ELEMENT_SELECT        NVARCHAR(20),                             --定位父菜单的方法
     ELEMENT_SELECT_KEY    NVARCHAR(20),                             --定位父菜单所需参数
     ELEMENT_ACTION        INTEGER,                                  --父菜单操作 1.单击
     ELEMENT_ACTION_KEY    NVARCHAR(30),                             --父菜单操作所需参数
     )
GO

GO
--子菜单表
IF EXISTS (SELECT 1 FROM SYSOBJECTS WHERE NAME ='CHILD_MENU')
    DROP TABLE CHILD_MENU
GO
    CREATE TABLE CHILD_MENU
    (CHILD_MENU_ID             INTEGER NOT NULL IDENTITY PRIMARY KEY,    --子菜单ID
     CHILD_MENU_NAME           NVARCHAR(20),                             --子菜单名称
     PARENT_MENU_ID            INTEGER NOT NULL,                         --所属父菜单ID
     FRAME_NAME                NVARCHAR(20),                             --子菜单所在表单
     ELEMENT_SELECT            NVARCHAR(20),                             --定位子菜单的方法
     ELEMENT_SELECT_KEY        NVARCHAR(20),                             --定位子菜单所需参数
     ELEMENT_ACTION            INTEGER,                                  --子菜单操作 1.单击
     ELEMENT_ACTION_KEY        NVARCHAR(30),                             --子菜单操作所需参数
    )
GO


GO
--子菜单功能表
IF EXISTS (SELECT 1 FROM SYSOBJECTS WHERE NAME ='CHILD_FUNCTION')
    DROP TABLE CHILD_FUNCTION
GO
    CREATE TABLE CHILD_FUNCTION
    (CHILD_FUNCTION_ID         INTEGER NOT NULL IDENTITY PRIMARY KEY,    --子菜单功能ID
     CHILD_FUNCTION_TYPE       INTEGER NOT NULL,                         --子菜单功能按钮操作类型 1.先点击按钮跳转至页面操作 2.页面上选择数据后再操作
     CHILD_FUNCTION_NAME       NVARCHAR(20),                             --子菜单功能名称
     CHILD_MENU_ID             INTEGER NOT NULL,                         --所属子菜单ID
     FRAME_NAME                NVARCHAR(20),                             --子菜单功能按钮所在表单
     ELEMENT_SELECT            NVARCHAR(20),                             --定位子菜单功能按钮的方法
     ELEMENT_SELECT_KEY        NVARCHAR(20),                             --定位子菜单功能按钮所需参数
     ELEMENT_ACTION            INTEGER,                                  --子菜单功能按钮操作 1.单击
     ELEMENT_ACTION_KEY        NVARCHAR(30),                             --子菜单功能按钮操作所需参数
    )
GO


GO
--子菜单功能页面表
IF EXISTS (SELECT 1 FROM SYSOBJECTS WHERE NAME ='FUNCTION_PAGE')
    DROP TABLE FUNCTION_PAGE
GO
    CREATE TABLE FUNCTION_PAGE
    (FUNCTION_PAGE_ID          INTEGER NOT NULL IDENTITY PRIMARY KEY,    --子菜单功能页面ID
     CHILD_FUNCTION_ID         INTEGER NOT NULL,                         --子菜单功能ID
     FRAME_NAME                NVARCHAR(20),                             --子菜单功能页面所在表单
     FUNCTION_PAGE_URL         NVARCHAR(30),                             --页面URL
    )
GO


GO
--页面元素表
IF EXISTS(SELECT 1 FROM SYSOBJECTS WHERE NAME='ELEMENT')
    DROP TABLE ELEMENT
GO
    CREATE TABLE ELEMENT
    (ELEMENT_ID               INTEGER NOT NULL IDENTITY PRIMARY KEY,    --页面元素ID
     FUNCTION_PAGE_ID         INTEGER,                                  --子菜单功能页面ID
     ELEMENT_NAME             NVARCHAR(20),                             --元素名称
     ELEMENT_SELECT           NVARCHAR(20),                             --定位元素的方法
     ELEMENT_SELECT_KEY       NVARCHAR(20),                             --定位元素所需参数
     ELEMENT_ACTION           INTEGER,                                  --元素操作 1:输入值 2:单击 3.下拉选项
     ELEMENT_ACTION_KEY       NVARCHAR(30)                              --元素操作所需参数
    )
GO
--动作表