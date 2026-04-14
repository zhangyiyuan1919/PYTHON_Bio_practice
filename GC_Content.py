#===读取FASTA文件
#===清理文件数据，使数据便于使用toolkit
#===结果输出为新的字典保存

#定义读取文件读取函数
def readFile(filePath):
    """读取文件并形成一个列表"""
    with open(filePath, 'r') as f:
        return [l.strip() for l in f.readlines()] #清理 l.strip()去掉每行开头和结尾的空白、换行符、空格
#GC计算工具
def gc_content(seq):
    """GC含量读取工具"""
    return round(
        ((seq.count('C') + seq.count('G')) / len(seq) * 100), 6)

#===清理数据形式易于使用GC计算工具

#读取存储文件为一个列表
FASTAFile=readFile("gc_content.txt") #注意文件放在同级文件夹下面，则直接读取文件

#读取存储为一个字典+数据
FASTADict={}

#存储为目前的序列名
FASTALabel=""

for line in FASTAFile:
    if '>' in line:  #，如果这一行包含 >，说明它是序列名
        FASTALabel = line
        FASTADict[FASTALabel] = ""
    else:
        FASTADict[FASTALabel] += line

print(FASTADict)

#使用字典推导生成一个包含GC内容的新字典，生物信息学解析 FASTA 最经典、最常用的写法
RESULTDict = {key: gc_content(value) for (key, value) in FASTADict.items()}

print(RESULTDict)

#查找新字典values（）中的最大值
MaxGCKey = max(RESULTDict, key=RESULTDict.get) #传入键，返回对应的值

print(f'{MaxGCKey[1:]}\n{RESULTDict[MaxGCKey]}')

