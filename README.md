# data-science-QS-world-university-rankings

## Project Overview

This repository provides a complete data science pipeline for analyzing the QS World University Rankings 2025 dataset. You will load and preprocess the data, perform exploratory data analysis, visualize key insights, and build regression models to predict overall university scores.

## Folder Structure

```
project-root/
├── data/
│   ├── raw/
│   │   └── qs_rankings_2025.csv
│   └── processed/
│       ├── raw_rankings.csv
│       └── processed_rankings.csv
├── scripts/
│   ├── 01_load_data.py
│   ├── 02_preprocess_data.py
│   ├── 03_exploratory_analysis.py
│   ├── 04_visualization.py
│   └── 05_modeling.py
└── outputs/
    ├── figures/
    ├── tables/
    └── models/
```  

## Usage

1. **Setup the Project:**  
   - Clone the repository.  
   - Ensure you have Python installed.  
   - Install required dependencies using the requirements.txt file.  
   ```bash
   pip install -r requirements.txt
   ```  
2. **Load Raw Data:**  
   ```bash
   python scripts/01_load_data.py
   ```  
3. **Preprocess Data:**  
   ```bash
   python scripts/02_preprocess_data.py
   ```  
4. **Exploratory Analysis:**  
   ```bash
   python scripts/03_exploratory_analysis.py
   ```  
5. **Generate Visualizations:**  
   ```bash
   python scripts/04_visualization.py
   ```  
6. **Train & Evaluate Models:**  
   ```bash
   python scripts/05_modeling.py
   ```  

## Requirements

- Python 3.8 or higher  
- pandas  
- numpy  
- matplotlib  
- scikit-learn  
- joblib  

## Acknowledgments

dataset name: QS World University Rankings 2025  
dataset author: Melissa Monfared  
dataset source: https://www.kaggle.com/datasets/melissamonfared/qs-world-university-rankings-2025