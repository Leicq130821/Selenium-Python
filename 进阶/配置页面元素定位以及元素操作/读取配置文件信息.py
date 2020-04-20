import configparser

# 实例化配置文件对象。
config = configparser.ConfigParser()
# 读取配置文件信息。
config.read(r'E:\Selenium-Python\进阶\配置页面元素定位以及元素操作\login.ini')
# 获取配置文件的节点信息，以列表的形式返回。
print(config.sections())
section=config.sections()[0]
# 获取节点下的键，以列表的形式返回。
print(config.options(section))
# 获取节点下的键值对，返回以元组形式的元素组成的列表。
print(config.items(section))
# 获取节点下键对应的值。
print(config.get(section,'username'))