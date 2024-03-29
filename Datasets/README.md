# Beautified Datasets

Our beautified datasets are available [online](https://fairbeauty.z6.web.core.windows.net/).

## FairBeauty
FairBeauty is a beautified version of the [FairFace dataset](https://github.com/joojs/fairface), a dataset promoting algorithmic fairness in Computer Vision systems. The choice of this dataset is motivated by its focus on diversity and our will to be representative of the population of Instagram, without biasing the results. Eight popular, AR beauty filters are applied on equal portions of the original dataset.

![Filters example.](assets/filters_example.png)

The image above is an example of the eight different beauty filters applied to the left-most image from the FairFace dataset. From left to right and top to bottom: filter 0 "pretty" by herusugiarta; filter 1 "hari beauty" by hariani; filter 2 "Just Baby" by blondinochkavika; filter 3 "Shiny Foxy"; filter 4 "Caramel Macchiato" and filter 5 "Cute baby face" by sasha_soul_art; filter 6 "Baby_cute_face_" by anya__ilicheva; filter 7 "big city life" by triutra.

The AR beauty filters detect the position of the faces in an original image and super-impose digital content to modify the original facial features. As these filters apply the same transformation to the facial features of all faces, we hypothesize that they homogenize facial aesthetics making the beautified faces more similar to each other. To determine the homogenization of the filtered faces, we consider different face verification models, i.e. DeepFace, VGG-Face, Facenet, CurricularFace, MagFace and ElasticFace. The code for these experiments are available in the folders **deepface_vggface_facenet**, **curricularface**, **elasticface** and **magface**.


## B-LFW
B-LFW is a beautified version of the LFW (Labeled Faces in the Wild) dataset, a public benchmark dataset for face verification, designed for studying and evaluating unconstrained face recognition systems. We have beautified [LFW aligned at 112x112 pixels](https://github.com/ZhaoJ9014/face.evoLVe), using the same eight popular Instagram beauty filters, using different filters on different images from the same individuals.

The analysis of the B-LFW dataset may lead to new insights on understanding the impact of such filters on face recognition, particularly when no explicit occlusion is applied. We evaluate the performance of three state-of-the-art models (CurricularFace, ElasticFace and MagFace) on face recognition both on each single beauty filter (applied to LFW) and on the B-LFW dataset (in which different beauty filters are applied on different images of the same individual). The code for these experiments is available in folders **curricularface**, **elasticface** and **magface**.


## License and attribution
The framework and the datasets are part of a scientific paper currently under review for the 36th Conference on Neural Information Processing Systems (NeurIPS 2022) Track on Datasets and Benchmarks, under the title "OpenFilter: A Framework to Democratize Research Access to Social Media AR Filters", by Piera Riccio, Bill Psomas, Francesco Galati, Francisco Escolano, Thomas Hofmann and Nuria Oliver.

**OpenFilter** is a flexible open framework to apply AR filters available in social media platforms on existing, publicly available large collections of images. We share this framework to provide the research community and practitioners with easier access to any AR filter available on social media, and to perform novel research in this emerging and culturally relevant field. We strongly discourage controversial and unethical uses of our framework and datasets. We acknowledge that, while the development of some applications could be appealing from a technical and scientific perspective, the subject matter of this work has a profound sociological and cultural component, which should not be ignored. As a consequence, we opt for protecting the general public from any consequence of this research, and thus share our datasets with exclusively a non-commercial license. The datasets **FairBeauty** and **B-LFW** are distributed under the [CC-BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) license agreement, which allows sharing and re-adaptation for non-commercial purposes and redistribution under the same license. The code for **OpenFilter** is shared under a dual license. For non-commercial purposes, the [GNU General Public License, version 2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html) applies. Users interested in using the code for commercial purposes are asked to contact the authors for an explicit authorization. The authors will evaluate the ethical implications for each case.

