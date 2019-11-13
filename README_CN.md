![gpt2-ml](./.github/logo.png)
## **GPT2** for **M**ultiple **L**anguages

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/imcaspar/gpt2-ml/blob/master/pretrained_model_demo.ipynb)
[![GitHub](https://img.shields.io/github/license/imcaspar/gpt2-ml)](https://github.com/imcaspar/gpt2-ml)
[![GitHub All Releases](https://img.shields.io/github/downloads/imcaspar/gpt2-ml/total)](https://github.com/imcaspar/gpt2-ml/releases)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/imcaspar/gpt2-ml/issues)
[![GitHub stars](https://img.shields.io/github/stars/imcaspar/gpt2-ml?style=social)](https://github.com/imcaspar/gpt2-ml)
[![Twitter Follow](https://img.shields.io/twitter/follow/imcaspar?style=social)](https://twitter.com/intent/follow?screen_name=imcaspar)

[**中文说明**](./README_CN.md) | [**English**](./README.md)

- [x] 简化整理 GPT2 训练代码（based on Grover, supporting TPUs）
- [x] 移植 bert tokenizer，添加多语言支持
- [x] 15亿参数 GPT2 中文预训练模型( 15G 语料，训练 10w 步 )
- [x] 开箱即用的模型生成效果 demo [#](https://github.com/imcaspar/gpt2-ml#google-colab)
- [ ] 15亿参数 GPT2 中文预训练模型( 50G 语料，训练 100w 步 ，**预计 12 月初发布**)


## 预训练模型
15 亿参数中文预训练模型 [**[Google Drive 下载]**](https://drive.google.com/open?id=1n_5-tgPpQ1gqbyLPbP1PwiFi2eo7SWw_)

训练语料来自 [THUCNews](http://thuctc.thunlp.org/#%E4%B8%AD%E6%96%87%E6%96%87%E6%9C%AC%E5%88%86%E7%B1%BB%E6%95%B0%E6%8D%AE%E9%9B%86THUCNews) 以及 [nlp_chinese_corpus](https://github.com/brightmart/nlp_chinese_corpus)，清洗后总文本量约 15G 

使用 [Cloud TPU Pod v3-256](https://cloud.google.com/tpu/docs/types-zones#types) 训练 10w 步

![loss](./.github/loss.png)


## Google Colab
只需三次鼠标点击（不包括 Colab 授权流程），体验 15 亿参数中文预训练模型生成效果：

[**[Colab Notebook]**](https://colab.research.google.com/github/imcaspar/gpt2-ml/blob/master/pretrained_model_demo.ipynb)

<img src="./.github/demo.png" width="640">

## 训练

## 免责声明
该项目中的内容仅供技术研究参考，不作为任何结论性依据。

## Citing

```
@misc{GPT2-ML,
  author = {Zhibo Zhang},
  title = {GPT2-ML: GPT-2 for Multiple Languages},
  year = {2019},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/imcaspar/gpt2-ml}},
}
```

## Reference
https://github.com/google-research/bert

https://github.com/rowanz/grover

Research supported with Cloud TPUs from Google's TensorFlow Research Cloud (TFRC)