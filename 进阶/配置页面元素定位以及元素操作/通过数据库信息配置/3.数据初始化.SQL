USE TEST
GO
    DELETE ELEMENTPARAM WHERE PAGE_ID=1
    INSERT INTO ELEMENTPARAM
    VALUES (1,'登录系统','用户名','id','username',1,'admin'),
           (1,'登录系统','密码','name','password',1,'000000'),
           (1,'登录系统','登录按钮','tag name','button',2,'')
GO