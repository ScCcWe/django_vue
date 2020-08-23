# django_vue
本项目参考自https://cloud.tencent.com/developer/article/1005607    
原项目给出的部分代码和流程已经过时，这里更新了它们，例如axios，以及vue工程的创建  
axios在vue中的使用可以参考https://blog.csdn.net/qq_41115965/article/details/80780264  
vue工程的创建可以参考https://www.cnblogs.com/blcorder/p/12015715.html  
当然，上述给出的网站是针对vue小白的(比如我这种，完全不懂vue，只是想用vue)，会vue的人可以完全忽视  

## vue + django
前端使用@vue/cli 4.4.6，后端使用django2.2.15  
这是一个最简单的小例子，可以提供一个参考，当然，也只能提供一个参考😓...  
> 本项目并没有使用djangorestframework!，如果你想看一下djangorestframwork是如何使用的，那么请去别处吧    

## 项目django环境说明
本项目在win中创建，运行，下面的创建方式也都是win中。

### 使用pipenv
使用`pipenv install --dev`创建项目的django环境   
使用`pipenv shell`进入虚拟环境

### 使用pip + virtualvenv
> 如果使用这种方式，建议在pycharm中鼠标点击来创建虚拟环境  
> 如果你非要键入命令，你可以尝试百度一下，然后自行创建  

首先创建一个虚拟环境
然后输入`$ pip install -r requirements.txt`创建项目的django环境

## 项目vue环境说明
vue中使用了axios，element-ui  
使用`$ npm install`来创建vue环境  
使用`$ npm run serve`来运行vue
