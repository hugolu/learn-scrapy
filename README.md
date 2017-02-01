# Learn Scrapy

## Scrapy 架構
![](http://scrapy-chs.readthedocs.io/zh_CN/1.0/_images/scrapy_architecture.png)

元件 | 描述
---|---
Scrapy Engine | 引擎负责控制数据流在系统中所有组件中流动，并在相应动作发生时触发事件。
Scheduler (调度器) | 调度器从引擎接受request并将他们入队，以便之后引擎请求他们时提供给引擎。
Downloader (下载器) | 下载器负责获取页面数据并提供给引擎，而后提供给spider。
Spiders | Spider是Scrapy用户编写用于分析response并提取item(即获取到的item)或额外跟进的URL的类。 每个spider负责处理一个特定(或一些)网站。
Item Pipeline | Item Pipeline负责处理被spider提取出来的item。典型的处理有清理、 验证及持久化(例如存取到数据库中)。 
Downloader middlewares (下载器中间件) | 下载器中间件是在引擎及下载器之间的特定钩子(specific hook)，处理Downloader传递给引擎的response。 其提供了一个简便的机制，通过插入自定义代码来扩展Scrapy功能。
Spider middlewares (Spider中间件) | Spider中间件是在引擎及Spider之间的特定钩子(specific hook)，处理spider的输入(response)和输出(items及requests)。 其提供了一个简便的机制，通过插入自定义代码来扩展Scrapy功能。

## Data flow 数据流

Scrapy中的数据流由执行引擎控制，其过程如下:

1. 引擎打开一个网站，找到处理该网站的Spider并向该spider请求第一个要爬取的URL(s)。
2. 引擎从Spider中获取到第一个要爬取的URL并在调度器以Request调度。
3. 引擎向调度器请求下一个要爬取的URL。
4. 调度器返回下一个要爬取的URL给引擎，引擎将URL通过下载中间件转发给下载器。 [request]
5. 一旦页面下载完毕，下载器生成一个该页面的Response，并将其通过下载中间件发送给引擎。 [response]
6. 引擎从下载器中接收到Response并通过Spider中间件发送给Spider处理。
7. Spider处理Response并返回爬取到的Item及(跟进的)新的Request给引擎。
8. 引擎将爬取到的Item给Item Pipeline，将Request给调度器。
9. (从第二步)重复直到调度器中没有更多地request，引擎关闭该网站。
