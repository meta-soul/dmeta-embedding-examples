# DMeta Embedding

## Models

- [Dmeta-embedding-zh](https://huggingface.co/DMetaSoul/Dmeta-embedding-zh), 2024.04.01 发布，参数规模 300M，推理速度提升 30%，精度下降仅 1%
- [Dmeta-embedding-zh-small](https://huggingface.co/DMetaSoul/Dmeta-embedding-zh-small), 2024.02.07 发布，参数规模 400M，获得 MTEB 中文榜第二

目前我们针对开源模型提供了高性能 HTTP API 服务，免除模型本地推理部署的复杂性，真正实现业务场景的开箱即用，现可扫码免费参与内测：

![](./docs/api_qrcode.jpeg)

## Examples

| 示例   | 概述 | 亮点 |
| --- | --- | --- |
| [embed-your-data](./embed-your-data) | 基于豆瓣电影数据的语义检索示例，包括离线索引构建以及在线检索等 | **Langchain/Faiss** 等工具的使用 |
| [Chroma](./Chroma) | Chroma 向量数据库使用 Dmeta-embedding 示例 | **Chroma** 向量数据库、本地/HTTP API 推理方式 |
| [Pinecone](./Pinecone) | Pinecone 向量数据库使用 Dmeta-embedding 示例 | **Pinecone** 向量数据库、本地/HTTP API 推理方式 |
