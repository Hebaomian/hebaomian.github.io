window.PUBLICATIONS = [
  {
    id: "tlm-dre", group: "Preprints", topic: "agents", year: 2026, badge: "arXiv '26", visual: "tlm-DRE",
    figure: "assets/publications/tlm-dre.png",
    figureAlt: "Figure 1: overall architecture of tlm-DRE in a single training iteration.",
    figureWidth: 1000, figureHeight: 585,
    title: "Turn-level Multiscale Density Ratio Estimation for LLM Agents",
    authors: ["Zishuo Zhao", "Kai Chen", "Ao Li", "Yuan Liu"],
    venue: "arXiv:2609.16760, 2026",
    url: "https://arxiv.org/abs/2609.16760", pdf: "https://arxiv.org/pdf/2609.16760",
    abstract: "We study preference alignment for multi-turn LLM agents. Turn-level Multiscale Density Ratio Estimation (tlm-DRE) assigns different weights to individual turns and uses asymmetric token-level training to learn from positive and negative trajectories. Experiments cover multi-turn reasoning tasks under both in-domain and out-of-domain conditions.",
    bibtex: "@misc{zhao2026turnlevel,\n  title = {Turn-level Multiscale Density Ratio Estimation for LLM Agents},\n  author = {Zishuo Zhao and Kai Chen and Ao Li and Yuan Liu},\n  year = {2026},\n  eprint = {2609.16760},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n  url = {https://arxiv.org/abs/2609.16760}\n}"
  },
  {
    id: "flex-clip", group: "Preprints", topic: "multimodal", year: 2024, badge: "arXiv '24", visual: "FLEX-CLIP",
    figure: "assets/publications/flex-clip.png",
    figureAlt: "Figure 3: FLEX-CLIP feature extraction, multimodal feature synthesis, and common space projection.",
    figureWidth: 1000, figureHeight: 412,
    title: "FLEX-CLIP: Feature-Level GEneration Network Enhanced CLIP for X-shot Cross-modal Retrieval",
    authors: ["Jingyou Xie", "Jiayi Kuang", "Zhenzhou Lin", "Jiarui Ouyang", "Zishuo Zhao", "Ying Shen"],
    venue: "arXiv:2411.17454, 2024",
    url: "https://arxiv.org/abs/2411.17454", pdf: "https://arxiv.org/pdf/2411.17454",
    abstract: "FLEX-CLIP combines CLIP representations with a feature generation network for few-shot cross-modal retrieval. A multimodal VAE-GAN generates pseudo samples to address data imbalance, while a gated residual network combines CLIP and projected features to reduce feature degradation in new domains.",
    bibtex: "@misc{xie2024flexclip,\n  title = {FLEX-CLIP: Feature-Level GEneration Network Enhanced CLIP for X-shot Cross-modal Retrieval},\n  author = {Jingyou Xie and Jiayi Kuang and Zhenzhou Lin and Jiarui Ouyang and Zishuo Zhao and Ying Shen},\n  year = {2024},\n  eprint = {2411.17454},\n  archivePrefix = {arXiv},\n  url = {https://arxiv.org/abs/2411.17454}\n}"
  },
  {
    id: "sf-absa", group: "Conference Papers", topic: "nlp", year: 2024, badge: "LREC-COLING '24", visual: "SF-ABSA",
    figure: "assets/publications/sf-absa.png",
    figureAlt: "Figure 2: overview of the SF-ABSA framework for source-free domain adaptation.",
    figureWidth: 1000, figureHeight: 390,
    title: "Source-free Domain Adaptation for Aspect-based Sentiment Analysis",
    authors: ["Zishuo Zhao", "Ziyang Ma", "Zhenzhou Lin", "Jingyou Xie", "Yinghui Li", "Ying Shen"],
    venue: "LREC-COLING 2024, pp. 15076–15086",
    url: "https://aclanthology.org/2024.lrec-main.1310/", pdf: "https://aclanthology.org/2024.lrec-main.1310.pdf",
    abstract: "We introduce a source-free domain adaptation framework for aspect-based sentiment analysis. Only model parameters are transferred between domains, without access to source data during adaptation. Feature-based adaptation and pseudo-label learning support transfer to unlabeled target domains, with evaluation on four benchmarks.",
    bibtex: "@inproceedings{zhao-etal-2024-source,\n  title = {Source-free Domain Adaptation for Aspect-based Sentiment Analysis},\n  author = {Zhao, Zishuo and Ma, Ziyang and Lin, Zhenzhou and Xie, Jingyou and Li, Yinghui and Shen, Ying},\n  booktitle = {Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024)},\n  year = {2024},\n  pages = {15076--15086},\n  publisher = {ELRA and ICCL},\n  url = {https://aclanthology.org/2024.lrec-main.1310/}\n}"
  },
  {
    id: "sf-qa", group: "Conference Papers", topic: "nlp", year: 2023, badge: "ICASSP '23", visual: "SF-QA",
    title: "Source-Free Unsupervised Domain Adaptation for Question Answering",
    authors: ["Zishuo Zhao", "Yuexiang Xie", "Jingyou Xie", "Zhenzhou Lin", "Yaliang Li", "Ying Shen"],
    venue: "IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2023",
    url: "https://ieeexplore.ieee.org/abstract/document/10095248",
    summary: "Research on adapting question answering models to target domains without access to source-domain training data.",
    bibtex: "@inproceedings{zhao2023sourcefree,\n  title = {Source-Free Unsupervised Domain Adaptation for Question Answering},\n  author = {Zishuo Zhao and Yuexiang Xie and Jingyou Xie and Zhenzhou Lin and Yaliang Li and Ying Shen},\n  booktitle = {ICASSP 2023 - 2023 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)},\n  year = {2023},\n  pages = {1--5},\n  url = {https://ieeexplore.ieee.org/abstract/document/10095248}\n}"
  },
  {
    id: "htens", group: "Conference Papers", topic: "knowledge", year: 2023, badge: "SIGIR '23", visual: "HTENS",
    title: "Hierarchical Type Enhanced Negative Sampling for Knowledge Graph Embedding",
    authors: ["Zhenzhou Lin", "Zishuo Zhao", "Jingyou Xie", "Ying Shen"],
    venue: "ACM SIGIR 2023, pp. 2047–2051",
    url: "https://doi.org/10.1145/3539618.3591996",
    summary: "Research on using hierarchical entity type information to improve negative sampling for knowledge graph embeddings.",
    bibtex: "@inproceedings{lin2023hierarchical,\n  title = {Hierarchical Type Enhanced Negative Sampling for Knowledge Graph Embedding},\n  author = {Zhenzhou Lin and Zishuo Zhao and Jingyou Xie and Ying Shen},\n  booktitle = {Proceedings of the 46th International ACM SIGIR Conference on Research and Development in Information Retrieval},\n  year = {2023},\n  pages = {2047--2051},\n  doi = {10.1145/3539618.3591996}\n}"
  },
  {
    id: "mgl", group: "Conference Papers", topic: "multimodal", year: 2023, badge: "SDM '23", visual: "MGL",
    title: "Multimodal Graph Learning for Cross-Modal Retrieval",
    authors: ["Jingyou Xie", "Zishuo Zhao", "Zhenzhou Lin", "Ying Shen"],
    venue: "SIAM International Conference on Data Mining (SDM), 2023, pp. 145–153",
    url: "https://doi.org/10.1137/1.9781611977653.ch17",
    abstract: "We propose a graph-based framework for cross-modal retrieval that captures correlations within multimodal data. A graph construction algorithm, modality-shared projection, co-attention, and gated fusion combine complementary information. Graph sampling extends the approach to larger-scale scenarios.",
    bibtex: "@inproceedings{xie2023multimodal,\n  title = {Multimodal Graph Learning for Cross-Modal Retrieval},\n  author = {Jingyou Xie and Zishuo Zhao and Zhenzhou Lin and Ying Shen},\n  booktitle = {Proceedings of the 2023 SIAM International Conference on Data Mining (SDM)},\n  year = {2023},\n  pages = {145--153},\n  doi = {10.1137/1.9781611977653.ch17}\n}"
  }
];
