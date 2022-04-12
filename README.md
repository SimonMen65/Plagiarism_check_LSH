# Plagiarism_check_LSH

## Project Structure
### Data
Include raw data, processed data and processing scripts.
- Under **data/raw** we have the downloaded PAN Plagiarism Corpus 2009 from [Zenodo](https://zenodo.org/record/3250083#.YlXZHTfMITs)  The Orinigal corpus has about 16000 source documents and another 16000 suspicious documents. Now due to llimited calculation power,we develop on 2000 of each first.
- Under **data/processed** we have the processed data where we seperate True Positive and True Negative passages to different folders.
- process.py contains scripts for data processing

