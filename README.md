# NLP Final Project

This repository contains the final project for the Natural Language Processing (NLP) course (COSC 426) at Colgate University, developed by Emmett Hintz, James Njoroge, and Kayla Mistica.

## Project Overview

Our project focuses on analyzing English Premier League (EPL) data to predict team performance metrics using NLP techniques. We aim to extract insights from historical data and apply machine learning models to forecast future outcomes.

## Repository Structure

- `configs/`: Configuration files for model training and evaluation.
- `predictions/`: Output files containing model predictions.
- `scripts/`: Python scripts for data processing, model training, and evaluation.
- `data.zip`: Compressed file containing raw datasets used in the project.
- `english-premier-league-standings.zip`: Compressed file with EPL standings data from 1993 to 2024.
- `pl-tables-1993-2024.csv`: CSV file with EPL standings data.
- `process_data2.ipynb`: Jupyter Notebook for data preprocessing and exploration.
- `train_data.tsv`, `test_data.tsv`, `validation_data.tsv`: Tab-separated files for training, testing, and validation datasets.
- `metrics-analysis.md`: Documentation of the evaluation metrics used and their analysis.
- `pre-processing.md`: Documentation detailing the data preprocessing steps.
- `NLP Final Project Proposal - Kayla_James_Emmett.pdf`: Project proposal outlining objectives, methodology, and expected outcomes.

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.6 or higher
- Jupyter Notebook

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/James-Njoroge/nlp-final.git
   cd nlp-final
   ```

2. **Set up the data:**

   - Unzip `data.zip` and `english-premier-league-standings.zip` into the appropriate directories.
   - Ensure that the CSV and TSV files are in the correct paths as expected by the scripts.

## Usage

### Data Preprocessing

Utilize the `process_data2.ipynb` notebook to preprocess the raw data. This step includes cleaning, normalization, and feature extraction necessary for model training.

### Model Training

Execute the scripts in the `scripts/` directory to train the predictive models. Configuration files in the `configs/` directory can be adjusted to modify training parameters.

### Evaluation

After training, evaluate the models using the validation and test datasets. Refer to `metrics-analysis.md` for details on the evaluation metrics and their interpretations.

## Results

The `predictions/` directory contains the output predictions from our models. Detailed analysis and discussion of these results are documented in `metrics-analysis.md`.

## Contributors

- Emmett Hintz
- James Njoroge
- Kayla Mistica

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgments

We extend our gratitude to Professor Grusha Prasad and Professor Forrest Davis for guidance throughout the course.
