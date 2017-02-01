# Meizitu - 練習透過 Scrapy 下載圖片

回想一下小時候怎麼學會騎單車的？
學騎單車最快的方式不是詳看使用說明、不是理解機械構造，表演獨輪特技或是製作單車不是我們的目的。
學會騎車最快的方式是立馬跨上單車 JUST DO IT，透過遊戲過程完成一個不完美但有趣的結果 - 坐在單車上，享受微風輕拂、觀賞時速20的風景。

Python Scrapy 裡面很多學問，但不一定對現在的我都有用，不如找個有趣的主題，快速的、粗淺的認識這個工具。
爬圖這個題目有趣，尤其爬的是美女圖，BJ4。

## 觀察網站

## 建立專案
```shell
scrapy startproject myproject
cd myproject
scrapy genspider meizitu www.meizitu.com
```

## Item
src: [items.py](myproject/myproject/items.py)

## Spider
src: [meizitu.py](myproject/myproject/spiders/meizitu.py)

## Setting
src: [settings.py](myproject/myproject/settings.py)

## Pipeline
src: [pipelines.py](myproject/myproject/pipelines.py)

---
## 參考
- [Scrapy 1.0 文档](http://scrapy-chs.readthedocs.io/zh_CN/1.0/index.html)
