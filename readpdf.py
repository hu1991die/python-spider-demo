#coding=utf-8
# Created by feizi at 2017/2/10

# 导入开发包
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from urllib.request import urlopen

# 打开文档对象,使用二进制的读模式进行读取（读取本地pdf资源文件）
# fp = open("resources/naacl06-shinyama.pdf", "rb")

# 读取远程pdf资源文件
fp = urlopen("http://www.tencent.com/zh-cn/articles/8003251479983154.pdf")

# 创建一个与PDF文档相关联的解释器
parser = PDFParser(fp)

# 创建一个pdf文档对象存储文档结构
doc = PDFDocument(parser)

# 将文档解释器与文档对象相关联
parser.set_document(doc)
doc.set_parser(parser)

# 初始化文档
doc.initialize("")

# 创建一个PDF资源管理器
resource = PDFResourceManager()

# 创建一个参数分析器
laParams = LAParams()

# 创建一个聚合器
device = PDFPageAggregator(resource, laparams=laParams)

# 创建一个PDF页面内容解释器
interpreter = PDFPageInterpreter(resource, device=device)

# 使用文档对象从页面中读取内容
for page in doc.get_pages():
    # 使用页面解释器来读取
    interpreter.process_page(page=page)

    # 使用聚合器来获取内容
    layout = device.get_result()

    for out in layout:
        # 判断是否有get_text()属性
        if hasattr(out, "get_text"):
            print(out.get_text())