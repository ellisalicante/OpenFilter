# OpenFilter: A Framework to Democratize Research Access to Social Media AR Filters

This repo contains the official PyTorch implementation and benchmark datasets of our NeurIPS 2022 paper  - **OpenFilter: A Framework to Democratize Research Access to Social Media AR Filters**. [[`arXiv`]([https://arxiv.org/abs/2106.04990])] [[`OpenReview`]([https://openreview.net/forum?id=ZKy2X3dgPA]))] [[`slides`]([.github/slides.pdf](http://users.ntua.gr/psomasbill/OpenFilter_NeurIPS2022_slides.pdf))] [[`poster`]([.github/poster.pdf](http://users.ntua.gr/psomasbill/OpenFilter_NeurIPS2022_poster.pdf))]

<div align="center">
  <img width="80%" alt="OpenFilter dataset illustration" src=".github/openfilter.PNG">
</div>

## OpenFilter: the framework
Most of the AR filters available on social media platforms can only be applied in real-time on selfie images captured from the camera. Hence, it is challenging to carry out quantitative and systematic research on such filters. OpenFilter fulfills such a need by enabling the application of AR filters on publicly available datasets of faces. 

Please find more information [in this folder](https://github.com/ellisalicante/OpenFilter/tree/main/OpenFilter).

## Beautified datasets
Through OpenFilter, we have beautified two datasets (FairBeauty and B-LFW), available [online](https://fairbeauty.z6.web.core.windows.net/).

Please find more information [in this folder](https://github.com/ellisalicante/OpenFilter/tree/main/Datasets).

## License and attribution
The framework and the datasets are part of a scientific paper currently under review for the 36th Conference on Neural Information Processing Systems (NeurIPS 2022) Track on Datasets and Benchmarks, under the title "OpenFilter: A Framework to Democratize Research
Access to Social Media AR Filters", by Piera Riccio, Bill Psomas, Francesco Galati, Francisco Escolano, Thomas Hofmann and Nuria Oliver.

**OpenFilter** is a flexible open framework to apply AR filters available in social media platforms on existing, publicly available large collections of images. We share this framework to provide the research community and practitioners with easier access to any AR filter available on social media, and to perform novel research in this emerging and culturally relevant field. We strongly discourage controversial and unethical uses of our framework and datasets. We acknowledge that, while the development of some applications could be appealing from a technical and scientific perspective, the subject matter of this work has a profound sociological and cultural component, which should not be ignored. As a consequence, we opt for protecting the general public from any consequence of this research, and thus share our datasets with exclusively a non-commercial license. The datasets **FairBeauty** and **B-LFW** are distributed under the [CC-BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) license agreement, which allows sharing and re-adaptation for non-commercial purposes and redistribution under the same license. The code for **OpenFilter** is shared under a dual license. For non-commercial purposes, the [GNU General Public License, version 2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html) applies. Users interested in using the code for commercial purposes are asked to contact the authors for an explicit authorization. The authors will evaluate the ethical implications for each case.

## Citation
If you find this repository useful, please consider giving a star :star: and citation:
```
@article{riccio2022openfilter,
  title={OpenFilter: a framework to democratize research access to social media AR filters},
  author={Riccio, Piera and Psomas, Bill and Galati, Francesco and Escolano, Francisco and Hofmann, Thomas and Oliver, Nuria},
  journal={Advances in Neural Information Processing Systems},
  volume={35},
  pages={12491--12503},
  year={2022}
}
```
