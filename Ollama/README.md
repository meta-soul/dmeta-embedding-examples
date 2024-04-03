# Ollama Generate Embeddings

Ollama 本地私有部署，支持拉取 `gguf` 格式 embedding 模型，进而在本地通过 <http://localhost:11434/api/embeddings> 接口来获取文本向量。

## 模型

目前我们已将 Dmeta-Embedding 系列模型导出如下：

- [Dmeta-embedding-zh](https://ollama.com/shaw/dmeta-embedding-zh)，400M 参数规模，2024.02 在 MTEB 排名第二
- [Dmeta-embedding-zh-small](https://ollama.com/shaw/dmeta-embedding-zh-small)，300M 参数规模，推理速度提升 30%
- [Dmeta-embedding-zh-q4](https://ollama.com/shaw/dmeta-embedding-zh-q4)，400M 对应 int4 量化版
- [Dmeta-embedding-zh-small-q4](https://ollama.com/shaw/dmeta-embedding-zh-small-q4)，300M 对应 int4 量化版

## 用法

具体用法以 Dmeta-embedding-zh 为例：

1）拉取模型到本地

```
ollama pull shaw/dmeta-embedding-zh
```

2）通过 API 获取文本向量

```
curl http://localhost:11434/api/embeddings -d '{
  "model": "shaw/dmeta-embedding-zh",
  "prompt": "天空是灰色的"
}'
```
