USE TEST
GO
--测试用例表
    IF EXISTS(SELECT 1 FROM SYSOBJECTS WHERE NAME ='TESTCASE')
        DROP TABLE TESTCASE
GO
    CREATE TABLE TESTCASE
    (TESTCASE_ID INTEGER NOT NULL IDENTITY,    --测试用例ID
     CREATE_MAN  INTEGER NOT NULL,             --创建测试用例的人
     TESTCASE_NAME VARCHAR(100)                --测试用例名称
    )
GO

GO
--操作表
    IF EXISTS(SELECT 1 FROM SYSOBJECTS WHERE NAME ='ACTIONS')
        DROP TABLE ACTIONS
GO
    CREATE TABLE ACTIONS
    (ACTIONS_ID            INTEGER NOT NULL IDENTITY,     --操作ID
     TESTCASE_ID           INTEGER NOT NULL,              --测试用例ID
     ACTIONS_TYPE          INTEGER NOT NULL,              --动作类型1.元素操作 2.切换frame/iframe表单 3.切换窗口 4.切换到弹出框
     ELEMENT_SELECT        NVARCHAR(20),                  --定位元素的方法
     ELEMENT_SELECT_KEY    NVARCHAR(20),                  --定位元素所需参数
     ELEMENT_ACTION        INTEGER,                       --元素操作 1.输入值 2.单击 3.下拉选项
     ELEMENT_ACTION_KEY    NVARCHAR(30),                  --元素操作所需参数
     FRAME_TYPE            INTEGER,                       --是否切换到默认表单 1.是 2.否
     FRAME                 NVARCHAR(20),                  --frame/iframe的属性值
     WINDOW_INDEX          INTEGER,                       --使用句柄索引切换窗口 1.初始窗口 2.最新窗口
     ALERT_ACTION          INTEGER,                       --弹出框操作 1.接受 2.拒绝 3.输入值
     ALERT_ACTION_KEY      NVARCHAR(20)                   --弹出框输入值
    )
GO

GO 
DELETE TESTCASE WHERE CREATE_MAN=888
INSERT INTO TESTCASE
VALUES(888,'新建项目成员信息'),(888,'登录退出')

DELETE TESTCASE WHERE TESTCASE_ID=1
INSERT INTO ACTIONS
VALUES(1,1,'id','username',1,'admin',0,'',0,0,''),
      (1,1,'id','password',1,'000000',0,'',0,0,''),
      (1,1,'tag name','button',2,'',0,'',0,0,''),
      (1,2,'','',0,'',2,'topFrame',0,0,''),
      (1,1,'id','mmenu8',2,'',0,'',0,0,''),
      (1,2,'','',0,'',1,'',0,0,''),
      (1,2,'','',0,'',2,'leftFrame',0,0,''),
      (1,2,'','',0,'',2,'leftiframe',0,0,''),
      (1,1,'id','itemTextLink5',2,'',0,'',0,0,''),
      (1,1,'id','itemTextLink9',2,'',0,'',0,0,''),
      (1,2,'','',0,'',1,'',0,0,''),
      (1,2,'','',0,'',2,'content',0,0,''),
      (1,1,'name','btnNew',2,'',0,'',0,0,''),
      (1,3,'','',0,'',0,'',2,0,''),
      (1,1,'name','proj_id',3,'TZ_451',0,'',0,0,''),
      (1,1,'name','coa_id',1,'test0001',0,'',0,0,''),
      (1,1,'name','mem_id_name',3,'8955',0,'',0,0,''),
      (1,1,'name','proj_mem_role',3,'01',0,'',0,0,''),
      (1,1,'name','cont_mode',1,'13888888888',0,'',0,0,''),
      (1,1,'name','reg_person',1,'系统管理员',0,'',0,0,''),
      (1,1,'name','reg_org',1,'金谷信托',0,'',0,0,''),
      (1,1,'name','reg_tm_picker',1,'20200101',0,'',0,0,''),
      (1,1,'name','btnSave',2,'',0,'',0,0,''),
      (1,3,'','',0,'',0,'',1,0,''),
      (1,4,'','',2,'',0,'',0,1,''),
      (1,2,'','',0,'',1,'',0,0,''),
      (1,2,'','',0,'',2,'topFrame',0,0,''),
      (1,1,'link text','退出系统',2,'',0,'',0,0,''),
      (1,4,'','',2,'',0,'',0,1,'')
      
DELETE TESTCASE WHERE TESTCASE_ID=2
INSERT INTO ACTIONS
VALUES(2,1,'id','username',1,'admin',0,'',0,0,''),
      (2,1,'id','password',1,'000000',0,'',0,0,''),
      (2,1,'tag name','button',2,'',0,'',0,0,''),
      (2,2,'','',0,'',2,'topFrame',0,0,''),
      (2,1,'link text','退出系统',2,'',0,'',0,0,''),
      (2,4,'','',2,'',0,'',0,1,'')
GO