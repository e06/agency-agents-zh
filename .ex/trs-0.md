codebuddy sdk文档: https://www.codebuddy.ai/docs/zh/cli/sdk-python

生成python代码，实现项目文档翻译的功能.

递归遍历当前目录下所有的.md文档，
过滤掉"*_zh.md"文件, 过滤掉"CODEBUDDY.md"
忽略掉".ex", ".ev"下的文件

对于这些文档，执行如下操作
 - 文档作为输入文件名，输出路径是输入文件名".md"替换为"_zh.md", 
   也就是给文件名添加_zh后缀.
 - 是用codebuddy做如下操作, prompt为
   ```
   将{输入文件名} 全文翻译成中文，保存在{输出文件名} 中.
   尽量保持markdown结构.
   注意保留所有的代码块，不需要翻译.
   ```
每次翻译一个文件
