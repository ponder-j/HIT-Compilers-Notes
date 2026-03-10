编译的主要任务：**翻译**和**优化**（代码规模小，执行速度快）

源程序 $\longrightarrow$ **预处理器** $\longrightarrow$ 经过预处理的源程序 $\longrightarrow$ **编译器** $\longrightarrow$ 汇编语言程序 $\longrightarrow$ **汇编器** $\longrightarrow$ 可重定位的机器代码 $\longrightarrow$ **链接器/加载器** $\longrightarrow$ 目标机器代码

## 1.2 编译系统的结构

1. 识别单词 —— 词法分析（前端）
2. 分析语法 —— 语法分析（前端）
3. 语义分析、中间代码生成（前端）
4. 机器无关代码优化
5. 目标代码生成（后端）
6. 机器相关代码优化（后端）

前端：源语言相关、目标代码无关
后端：目标代码相关

编码力度越大，语法分析越简单，语义分析越复杂

**词法分析**
input：源代码
output：token: <种别码， 属性值>

**语法分析**
input：词法单元序列
output：语法分析树

