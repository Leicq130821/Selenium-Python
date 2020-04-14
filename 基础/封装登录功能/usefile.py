import codecs
class Openfile:
    def getbrowser(path):
        browser={}
        # file=open(path)
        file=codecs.open(path,'r','utf-8')
        for data in file:
            result=[ele.strip() for ele in data.split('==')]
            browser.update([result])
        return browser
    def getuser(path):
        user=[]
        # file=open(path)
        file=codecs.open(path,'r','utf-8')
        for data in file:
            user_dict={}
            result = [ele.strip() for ele in data.split(' ')]
            for r in result:
                account = [ele.strip() for ele in r.split('=')]
                user_dict.update([account])
            user.append(user_dict)
        return  user