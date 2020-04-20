IF NOT EXISTS(SELECT 1 FROM DICTPARAM WHERE FUNCTION_ID = 1)BEGIN
    INSERT INTO DICTPARAM
    VALUES (1,'登录系统','用户名','id','username',1,'admin'),
           (1,'登录系统','密码','name','password',1,'000000'),
           (1,'登录系统','登录按钮','tag name','button',2,'')
END