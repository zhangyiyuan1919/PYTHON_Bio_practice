#=== 从FASTA格式文件中阅读数据
def readFile(filePath):
    """读取数据返回一个列表"""
    with open(filePath,'r')as f:
        return [l.strip() for l in f.readlines()]

#===清理数据
#===处理数据，让其易于处理
#===执行工具处理数据
#===收集数据
