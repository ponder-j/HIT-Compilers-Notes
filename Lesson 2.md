## 2.1 基本概念

串 string：有穷符号序列
长度：|s|
幂运算：$s^0=\epsilon, s^n=s^{n-1}s$ 
字母表：有穷符号集合 $\Sigma$ , $\Sigma^0=\{\epsilon\}, \Sigma^n=\Sigma^{n-1}\Sigma$ ; 乘积、n次幂、正闭包、Kleene 闭包
语言：$\forall L \subseteq \Sigma^*$ 称 L 为 $\Sigma$ 上的一个语言
句子：$\forall x \in L$ 叫做 L 的一个句子

## 2.2 文法定义

$G = (V_T, V_N, P, S)$
terminal, nonterminal
$V_T \cap V_N = \emptyset$ 
产生式 production：$\alpha \rightarrow \beta$ , $\alpha \in (V_T\cap V_N)^+$ 且 $\alpha$ 包含至少一个非终结符
开始符号：表示该文法中最大的语法成分

## 2.3 语言定义

推导 Derivations 与 规约 Reductions

最左推导——最右规约
最右推导——最左规约

句子是不包含非终结符的句型
语言：开始符号推导出的所有句子构成的集合
## 2.4 文法分类

### 0 型文法
无限制文法

### 1 型文法
上下文有关文法（CSG）
$\alpha_1A\alpha_2\rightarrow \alpha_1\beta\alpha_2(\beta\neq \epsilon)$

### 2 型文法
上下文无关文法（CFG）

### 3 型文法
正则语法
右线性文法：$A\rightarrow wB$ 或 $A\rightarrow w$
左线性文法
两者等价

![[Pasted image 20260312090931.png]]


## 2.5 CFG 的语法分析树

分析树忽略了推导的次序
从左到右排列叶子节点：树的产出 / 边缘
每一棵子树的边缘：短语
子树之有父子两代节点：直接短语

二义性文法：一个句子可以生成多个分析树
消除二义性的两个方法：
1. 改文法（会使得文法变得复杂，且无通用的方法）
2. 使用二义性文法+消歧规则

无二义性文法的判定：没有通用算法
无二义性文法的充分条件：
1. 确定性的上下文无关文法是无二义性的
2. LL(k) LR(k) 文法是无二义性的

