# Geopolitical Risk Data

Dataset et code pour tracer le Geopolitical Risk Daily Index (GPRD).  
Dataset and code for plotting the Geopolitical Risk Daily Index (GPRD).

## Description

Ce repository contient un dataset quotidien d'indices de risque géopolitique et un script Python pour visualiser ces données.  
This repository contains a daily geopolitical risk index dataset and a Python script to visualize this data.

## Fichiers / Files

- `data_gpr_daily_recent_.csv` : Dataset contenant les indices de risque géopolitique quotidiens / Dataset containing daily geopolitical risk indices
- `plot_gpr_index.py` : Script Python pour tracer et analyser les données / Python script to plot and analyze the data
- `requirements.txt` : Dépendances Python requises / Required Python dependencies

## Structure du Dataset / Dataset Structure

Le dataset contient les colonnes suivantes / The dataset contains the following columns:

- `Date` : Date de l'observation / Observation date
- `GPR_Index` : Valeur de l'indice de risque géopolitique / Geopolitical risk index value
- `Country` : Pays ou région / Country or region
- `Event_Category` : Catégorie d'événement (Economic, Political, Military) / Event category
- `Description` : Description de l'événement / Event description

## Installation

```bash
# Cloner le repository / Clone the repository
git clone https://github.com/QuantMerlinLab/geopolitical-risk-data.git
cd geopolitical-risk-data

# Installer les dépendances / Install dependencies
pip install -r requirements.txt
```

## Utilisation / Usage

```bash
# Exécuter le script de visualisation / Run the visualization script
python plot_gpr_index.py
```

Le script génère automatiquement plusieurs graphiques :  
The script automatically generates several plots:

1. **Série temporelle GPR** (`gpr_time_series.png`) : Évolution de l'indice dans le temps avec moyenne mobile / GPR time series with moving average
2. **GPR par catégorie** (`gpr_by_category.png`) : Distribution des indices par catégorie d'événement / GPR distribution by event category
3. **Statistiques GPR** (`gpr_statistics.png`) : Histogrammes et boîtes à moustaches / Histograms and box plots

## Fonctionnalités / Features

- ✅ Chargement automatique des données CSV / Automatic CSV data loading
- ✅ Visualisations interactives et sauvegarde PNG / Interactive visualizations and PNG export
- ✅ Statistiques descriptives détaillées / Detailed descriptive statistics
- ✅ Analyse par catégorie et région / Analysis by category and region
- ✅ Moyennes mobiles et intervalles de confiance / Moving averages and confidence intervals
- ✅ Support bilingue (Français/Anglais) / Bilingual support (French/English)

## Licence / License

MIT License - voir le fichier LICENSE pour plus de détails / see LICENSE file for details.
