# 第三次学习作业——对javascript的学习

## 1.javascript是什么

​     javascript是一款开发者而生的编程语言，在世界上享有极高的知名度和使用率，JavaScript 是一个脚本语言。它是一个轻量级，但功能强大的编程语言。、

## 2.基本语法

1.**字符串字面量**

​    可以使用单引号或双引号:“ “， ‘ ’ 

2.**基本运算符**

   这点和c语言中语法基本相同，加减乘除依次为”+ - * / "

3.**数组（Array）字面量** 定义一个数组：

   [40, 100, 1, 5, 25, 10]

**对象（Object）字面量** 定义一个对象：

​    {firstName:"John", lastName:"Doe", age:50, eyeColor:"blue"}

**函数（Function）字面量** 定义一个函数：

​    function myFunction(a, b) { return a * b;}

4.**javascript变量**

   在编程语言中，变量用于存储数据值。JavaScript 使用关键字 **var** 来定义变量， 使用等号来为变量赋值：

5.**javascript关键字**、

   JavaScript 关键字用于标识要执行的操作。和其他任何编程语言一样，JavaScript 保留了一些关键字为自己所用。

**var** 关键字告诉浏览器创建一个新的变量

6.**打印语句**

console.log()可以在控制台打印括号中的内容

### 注意点

​    JavaScript 对大小写是敏感的。当编写 JavaScript 语句时，请留意是否关闭大小写切换键。

   函数 **getElementById** 与 **getElementbyID** 是不同的。同样，变量 **myVariable** 与 **MyVariable** 也是不同的。

​    JavaScript 语句是发给浏览器的命令。

​    命令的作用是告诉浏览器要做的事情。

   下面的 JavaScript 语句向 id="demo" 的 HTML 元素输出文本 "你好 Dolly" ：

 **实例**

​      document.getElementById("demo").innerHTML = "你好 Dolly";

**分号** ;

分号用于分隔 JavaScript 语句。

通常我们在每条可执行的语句结尾添加分号。

使用分号的另一用处是在一行中编写多条语句。

**代码块**

JavaScript 可以分批地组合起来。代码块以左花括号开始，以右花括号结束。代码块的作用是一并地执行语句序列。

**关于数据类型**

​     **js中的数据类型是动态数据类型，不用定义数据类型**

**错误处理**

​      **try{}   catch{}**

try访问一个未知的变量，catch接受错误信息然后存储起来



## 个人感想

​      javascript是一款功能强大的编程语言，在经过一段时间的学习后，我觉得它与c语言十分的类似，但它也有许多出众的优点，比如let是动态数据类型所以免去了c语言要提前定义数据类型的麻烦之处。还有使用js时一定要注意关注点分离，使用不同的代码块使代码更加清晰。其他像分支语句，条件语句，运算符号......都与c语言有异曲同工之处。



