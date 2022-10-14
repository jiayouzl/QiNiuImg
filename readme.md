## 效果预览

<img src="http://myimages.25531.com/20220714/iShot_2022-07-14_22.31.26.png" style="zoom:50%;" />

## 程序简介

一个`PySide6/PYQT6`的练手APP，QT真的很强大，慢慢摸索中后续有新的想法也会对该APP进行升级，支持`MacOS`平台。

之前一直用免费图床，跑路了。。。。。得了，还是用收费的云储存吧，稳定还是没的说的。

如使用中碰到任何Bug与建议请至仓库`issue`提交建议。

> Windows与Linux版本后续发布。

### 功能简介
* 参数配置支持保存/读取
* 已支持拖拽文件

### 七牛参数配置获取方式

#### 1. 获取AccessKey与SecretKey

<img src="http://myimages.25531.com/20220715/iShot_2022-07-15_23.04.21.png" style="zoom:35%;" />

#### 2. 获取BucketName与Domain

<img src="http://myimages.25531.com/20220715/iShot_2022-07-15_23.08.24.png" style="zoom:35%;" />

## 开发环境

1. MacBook Pro M1PRO
2. macOS Monterey `12.4`
3. Python `3.9.13`
4. Visual Studio Code And PyCharm 2022.1.3
5. PySide6 And Designer

## 编译环境
* macOS Monterey `12.4` `arm64`
* macOS Monterey `12.4` `Intel 64-bit`

## 下载/安装

- From release: [https://github.com/jiayouzl/QiNiuImg/releases](https://github.com/jiayouzl/QiNiuImg/releases)

## 文件说明
```
.
├── Config                          配置目录
│   └── com.zhenglei.qiniu.plist    配置文件
├── cache                           七牛JSON缓存目录
├── main.py                         程序入口源代码
├── requirements.txt                依赖组件库
├── ui.py                           UI设计PY文件
└── ui.ui                           UI设计Designer文件
```

## License

MIT
