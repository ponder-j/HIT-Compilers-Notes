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


## 2.5 CFG 的语法分析树

