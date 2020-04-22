USE TEST
GO
    DELETE ELEMENT WHERE FUNCTION_PAGE_ID=1
    INSERT INTO ELEMENT
    VALUES (1,'用户名','id','username',1,'admin'),
           (1,'密码','name','password',1,'000000'),
           (1,'登录按钮','tag name','button',2,'')
GO