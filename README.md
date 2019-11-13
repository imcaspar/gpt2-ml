![gpt2-ml](./.github/logo.png)
## **GPT2** for **M**ultiple **L**anguages

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/imcaspar/gpt2-ml/blob/master/pretrained_model_demo.ipynb)
[![GitHub](https://img.shields.io/github/license/imcaspar/gpt2-ml)](https://github.com/imcaspar/gpt2-ml)
[![GitHub All Releases](https://img.shields.io/github/downloads/imcaspar/gpt2-ml/total)](https://github.com/imcaspar/gpt2-ml/releases)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/imcaspar/gpt2-ml/issues)
[![GitHub stars](https://img.shields.io/github/stars/imcaspar/gpt2-ml?style=social)](https://github.com/imcaspar/gpt2-ml)
[![Twitter Follow](https://img.shields.io/twitter/follow/imcaspar?style=social)](https://twitter.com/intent/follow?screen_name=imcaspar)

[**中文说明**](./README_CN.md) | [**English**](./README.md)

- [x] Simplified GPT2 train scripts（based on Grover, supporting TPUs）
- [x] Ported bert tokenizer，multilingual corpus compatible
- [x] 1.5B GPT2 pretrained Chinese model ( ~15G corpus, 10w steps )
- [x] Batteries-included Colab demo [#](https://github.com/imcaspar/gpt2-ml#google-colab)
- [ ] 1.5B GPT2 pretrained Chinese model ( ~50G corpus, 100w steps )


## Pretrained Model
1.5B GPT2 pretrained Chinese model [**[Google Drive]**](https://drive.google.com/open?id=1n_5-tgPpQ1gqbyLPbP1PwiFi2eo7SWw_)

Corpus from [THUCNews](http://thuctc.thunlp.org/#%E4%B8%AD%E6%96%87%E6%96%87%E6%9C%AC%E5%88%86%E7%B1%BB%E6%95%B0%E6%8D%AE%E9%9B%86THUCNews) and [nlp_chinese_corpus](https://github.com/brightmart/nlp_chinese_corpus)

Using [Cloud TPU Pod v3-256](https://cloud.google.com/tpu/docs/types-zones#types) to train 10w steps

![loss](./.github/loss.png)


## Google Colab
With just 3 clicks (not including Colab auth process), the 1.5B pretrained Chinese model demo is ready to go：

[**[Colab Notebook]**](https://colab.research.google.com/github/imcaspar/gpt2-ml/blob/master/pretrained_model_demo.ipynb)

<img src="./.github/demo.png" width="640">

## Train

## Disclaimer
The contents in this repository are for academic research purpose, and we do not provide any conclusive remarks.

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