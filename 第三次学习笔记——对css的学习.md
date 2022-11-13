   # 第三次学习笔记——对css的学习

## 1. css的作用

​    css主要起到对网页润色的效果，html和css是不可分割的两部分，如果说html是整个网页的骨架那么css就是皮肤，因为css的加入网页才能变得多姿多彩。

## 2.css的基本知识

### 两种选择器

**id 选择器**

id 选择器可以为标有特定 id 的 HTML 元素指定特定的样式。

HTML元素以id属性来设置id选择器,CSS 中 id 选择器以 "#" 来定义。

以下的样式规则应用于元素属性 id="para1":

**class 选择器**

class 选择器用于描述一组元素的样式，class 选择器有别于id选择器，class可以在多个元素中使用。

class 选择器在 HTML 中以 class 属性表示, 在 CSS 中，类选择器以一个点 **.** 号显示：

在以下的例子中，所有拥有 center 类的 HTML 元素均为居中。



----



·**CSS 背景**



CSS 背景属性用于定义HTML元素的背景。

CSS 属性定义背景效果:

- background-color

- background-image

- background-repeat

- background-attachment

- background-position

  

  **背景图像**

  background-image 属性描述了元素的背景图像.

  默认情况下，背景图像进行平铺重复显示，以覆盖整个元素实体.

---

**css文字**

文本颜色

颜色属性被用来设置文字的颜色。

颜色是通过CSS最经常的指定：

- 十六进制值 - 如: **＃FF0000**
- 一个RGB值 - 如: **RGB(255,0,0)**
- 颜色的名称 - 如: **red**

**字体大小**

font-size 属性设置文本的大小。

能否管理文字的大小，在网页设计中是非常重要的。但是，你不能通过调整字体大小使段落看上去像标题，或者使标题看上去像段落。

请务必使用正确的HTML标签，就<h1> - <h6>表示标题和<p>表示段落：

字体大小的值可以是绝对或相对的大小。

绝对大小：

- 设置一个指定大小的文本
- 不允许用户在所有浏览器中改变文本大小
- 确定了输出的物理尺寸时绝对大小很有用

相对大小：

- 相对于周围的元素来设置大小
- 允许用户在浏览器中改变文字大小

### 盒子模型

在 CSS 中我们广泛地使用两种“盒子” —— **块级盒子** (**block box**) 和 **内联盒子** (**inline box**)。这两种盒子会在**页面流**（page flow）和元素之间的关系方面表现出不同的行为：

一个被定义成块级的（block）盒子会表现出以下行为：

- 盒子会在内联的方向上扩展并占据父容器在该方向上的所有可用空间，在绝大数情况下意味着盒子会和父容器一样宽
- 每个盒子都会换行
- [`width`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/width) 和 [`height`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/height) 属性可以发挥作用
- 内边距（padding）, 外边距（margin）和 边框（border）会将其他元素从当前盒子周围“推开”

除非特殊指定，诸如标题 (`<h1>`等) 和段落 (`<p>`) 默认情况下都是块级的盒子。

如果一个盒子对外显示为 `inline`，那么他的行为如下：

- 盒子不会产生换行。
- [`width`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/width) 和 [`height`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/height) 属性将不起作用。
- 垂直方向的内边距、外边距以及边框会被应用但是不会把其他处于 `inline` 状态的盒子推开。
- 水平方向的内边距、外边距以及边框会被应用且会把其他处于 `inline` 状态的盒子推开。

用做链接的 `<a>` 元素、 `<span>`、 `<em>` 以及 `<strong>` 都是默认处于 `inline` 状态的。

我们通过对盒子[`display`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/display) 属性的设置，比如 `inline` 或者 `block` ，来控制盒子的外部显示类型。





