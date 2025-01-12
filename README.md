# Towards a systematic exploration of motif development in Arab-Andalusian Music

Authors: Oriol Colomé i Font & Satyajeet Prabhu  
Affiliation: SMC 2023-24. Universitat Pompeu Fabra.  

## Overview
This repository contains the original code and analysis for exploring motif development in ṭab' Iraq-al-ayam, as described in our research paper. The analysis focuses on identifying and tracking musical motifs across different pieces in the Arab-Andalusian tradition.

## Project Structure
- `scores/`: Contains MusicXML files of the analyzed pieces
  - Includes various forms: Btayhi, Quddam, and Bassit in Iraq-Ajam
  - Color-annotated scores showing identified motifs
- `plots/`: Generated visualizations of motif analysis
- `paper/`: Research paper and related materials
- `notebook.ipynb`: Main analysis notebook

## Setup Instructions
1. Clone this repository
2. Install required dependencies:
```bash
pip install numpy matplotlib music21 pandas
```

## Usage
1. Open `notebook.ipynb` in Jupyter Notebook or JupyterLab
2. The notebook is structured to analyze MusicXML scores from the `scores` folder
3. Generated plots will be saved to the `plots` folder
4. Color-annotated scores can be viewed using Musescore or similar music score editors

## Methodology
The analysis pipeline includes:
- Score parsing using music21
- Motif identification through pattern matching
- Visualization of motif development
- Color annotation of identified patterns

## Results
The plots and annotated scores demonstrate the systematic development of motifs across different pieces in the ṭab' Iraq-al-ayam tradition. Refer to the research paper for detailed interpretation of results.

## Contact
For questions or collaborations, please contact:
- Oriol Colomé i Font: oriol.colome01@estudiant.upf.edu
- Satyajeet Prabhu: satyajeet.prabhu01@estudiant.upf.edu

## License
This project is licensed under the terms included in the LICENSE file.




