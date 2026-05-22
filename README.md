# SATURN 🪐
**Sentiment Analysis Tool for User Review on Network**

## 📖 Overview
SATURN is a research-focused Natural Language Processing (NLP) project designed to perform comparative sentiment analysis on user-generated feedback, such as product reviews and social media comments. 

The primary goal of this project is to evaluate and compare the contextual understanding, sentiment classification accuracy, and overall performance of traditional lexicon-based models versus advanced transformer-based architectures.

## 🎯 Research Objectives
* **Comparative Analysis:** Evaluate the differences in contextual interpretation, semantic representation, and classification robustness across different NLP approaches.
* **Model Benchmarking:** Assess accuracy and performance metrics on real-world, user-generated review datasets.
* **Lexicon vs. Transformer:** Understand the practical trade-offs between speed/simplicity (lexicon) and deep contextual understanding (transformers).

## 🧠 Models Evaluated
This project conducts a head-to-head comparison of three distinct sentiment analysis models:
1.  **VADER (Valence Aware Dictionary and sEntiment Reasoner):** A traditional, lexicon and rule-based sentiment analysis tool specifically tuned for sentiments expressed in social media.
2.  **BERT (Bidirectional Encoder Representations from Transformers):** A transformer-based machine learning technique for NLP pre-training developed by Google, allowing for deep bidirectional context.
3.  **RoBERTa (Robustly Optimized BERT Pretraining Approach):** An optimized method for pretraining NLP systems that improves upon BERT's architecture for enhanced semantic representation and accuracy.

## 📁 Repository Structure
```text
saturn_fe/
├── data/                       # Directory containing sample datasets (Amazon, Instagram)
├── data_exploration.ipynb      # Jupyter notebook for EDA, preprocessing, and testing
├── saturn.py                   # Main script executing the sentiment analysis models
├── .gitignore                  # Specifies intentionally untracked files to ignore
└── README.md                   # Project documentation
