# Embed Your Data

## 1. 背景
在这里我们实现一个基于 Langchain + Faiss + DMeta Embedding 搭建的向量数据库，作为演示我们采用豆瓣的电影数据，为了减少对环境的依赖，我们建议您采用 API 的方式建立向量数据库。

## 2. 环境安装

### 2.1 Python 软件包依赖安装
```shell
conda create -n demo python=3.10
conda activate demo
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## 3. 数据集准备

### 3.1 豆瓣电影数据
使用 [Moviedata-10M](http://moviedata.csuldw.com/) 中提供的数据集中的 movie.csv。


### 3.2 解析数据
我们从豆瓣电影数据中抽取电影名称、电影故事情节、电影演员、电影导演、电影国家和地区，组成一段描写电影的文字
```shell
cd data/
python parse_movies.py
head movie_desc-10m.txt -n 1000 > movie_desc-1k.txt
```

## 4. 建立 Faiss 向量数据库
为了方便演示，我们这里只使用豆瓣电影数据的前 1000 条，减少因为测试带来的计算资源。

### 4.1 使用 API 模式建立向量数据库
首次运行，需要填写我们的 [API 申请表](https://dmetasoul.feishu.cn/share/base/form/shrcnu7mN1BDwKFfgGXG9Rb1yDf)。申请完 API Key 之后将其放入 `.env` 文件:

``` configuration
DMETA_API_KEY=sk-******************
```

之后可以运行脚本:
```shell
python dump_vec_faiss api
```

### 4.2 使用本地模型建立向量数据库
首次运行，需要从 HuggingFace 上下载我们的模型 [checkpoint](https://huggingface.co/DMetaSoul/Dmeta-embedding-zh)
```shell
python dump_vec_fass local
```

## 5. 验证 Faiss 索引
加载上一步中建立的索引，在终端输入查询，进行向量检索

```
python search_vec_faiss.py
```

## 6. 联系我们
使用过程中存在问题，您可以通过有效联系我们：zhongh@dmetasoul.com, xiaowenbin@dmetasoul.com, sunkai@dmetasoul.com，可以在 HuggingFace [讨论区](https://huggingface.co/DMetaSoul/Dmeta-embedding-zh/discussions) 留言，也可以在 GitHub 上提相关的 issue。欢迎关注我们的微信群:


<p align="center">
   <img height="500" alt="数元灵-AIGC-交流群" src="https://huggingface.co/DMetaSoul/Dmeta-embedding-zh/resolve/main/weixin.jpeg">
</p>
