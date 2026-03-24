LL(1) 文法
SELECT(A->a$\beta$) = {a}
SELECT(A->$\epsilon$) = FOLLOW{A}

![[Pasted image 20260324102359.png]]

![[Pasted image 20260324103506.png]]
![[Pasted image 20260324103527.png]]

## 🧭 计算 FOLLOW 集的三条黄金法则

假设我们要计算非终结符 $B$ 的 FOLLOW 集：

- **法则 1 (起始符特权)：** 如果 $B$ 是文法的开始符号，把输入结束符 `$` 放入 $FOLLOW(B)$ 中。 _(对应图中的：“首先，将 $ 添加到 Follow(E) 中”)_
    
- **法则 2 (看 B 的后面跟着谁)：** 在产生式右部找 $B$。如果存在一个产生式 $A \to \alpha B \beta$（$\beta$ 不是空的）： 就把 $\beta$ 的 FIRST 集合中**除了** $\varepsilon$ **以外**的所有元素，统统放入 $FOLLOW(B)$ 中。 _(白话：B 后面跟着_ $\beta$_，那么_ $\beta$ _能打头的所有终结符，自然就能紧跟在 B 后面)_
    
- **法则 3 (B 在最后，或者后面的东西可以为空)：** 如果存在一个产生式 $A \to \alpha B$（$B$ 在最右边）， **或者**存在 $A \to \alpha B \beta$ 且 $\beta$ 可以推导出 $\varepsilon$（即 $\varepsilon \in FIRST(\beta)$）： 就把 $A$ 的 FOLLOW 集（即 $FOLLOW(A)$）中的所有元素，统统放入 $FOLLOW(B)$ 中。 _(白话：B 后面没东西了，或者后面的东西消失了，那么谁跟着 A，谁也就自然跟着 B)_

