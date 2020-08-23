# django_vue

## vue + django
前端使用vue，后端使用django  
这是一个最简单的小例子，可以提供一个参考  
> 并没有使用djangorestframework!  

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
