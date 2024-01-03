# PDFConverterPy
pdf 转换器 ：可以转换为excel word,同时可以提取pdf中图片，还可以对pdf 和图片进行预览

## 包文件替换   
    1、converter.py
        替换pdf2docx包converter.py
        添加功能：
            1、converter的运行过程添加到日志框中
    2、tableview.py
        替换tkinter包下的Tableview.py
        添加功能：
            1、tableview的运行过程添加到日志框中
            2、tableview行双击事件，预览功能
            3、tableview右键菜单 增加系统删除文件和使用系统默认程序打开文件
## 打包exe
    转换Excel需要使用jar 需要添加    --data  tabula-1.0.5-jar-with-dependencies.jar;tabula
    （见pdfopr.json 使用auto-py-to-exe导入该文件即可）    

## 详见
    https://www.cnblogs.com/Old-Kang/articles/17932598.html