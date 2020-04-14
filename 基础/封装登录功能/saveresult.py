import time
class SaveResult():
    def savesuccess(loginfo):
        name='测试成功'+time.strftime('%Y_%m_%d_%H_%M_%S')
        filepath=r"E:\test\%s.text"%name
        file=open(filepath,mode='w')
        file.write(loginfo)
        file.close()
    def savefail(loginfo):
        name='测试失败'+time.strftime('%Y_%m_%d_%H_%M_%S')
        filepath=r"E:\test\%s.text"%name
        file=open(filepath,mode='w')
        file.write(loginfo)
        file.close()