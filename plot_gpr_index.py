#!/usr/bin/env python3
"""
Script pour tracer le Geopolitical Risk Daily Index (GPRD)
Script to plot the Geopolitical Risk Daily Index (GPRD)
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import seaborn as sns
import numpy as np
import os

def load_data(filename="data_gpr_daily_recent_.csv"):
    """
    Charge les données du fichier CSV
    Load data from CSV file
    """
    try:
        # Ensure we're working with the correct path
        script_dir = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.join(script_dir, filename)
        
        df = pd.read_csv(filepath)
        df['Date'] = pd.to_datetime(df['Date'])
        df = df.sort_values('Date')
        return df
    except FileNotFoundError:
        print(f"Erreur: Le fichier {filename} n'a pas été trouvé.")
        print(f"Error: File {filename} not found.")
        return None
    except Exception as e:
        print(f"Erreur lors du chargement des données: {e}")
        print(f"Error loading data: {e}")
        return None

def plot_gpr_time_series(df, save_plot=True):
    """
    Trace la série temporelle de l'indice GPR
    Plot GPR index time series
    """
    plt.figure(figsize=(12, 8))
    
    # Plot main time series
    plt.plot(df['Date'], df['GPR_Index'], linewidth=2, color='darkred', alpha=0.8)
    
    # Add moving average
    df['MA_7'] = df['GPR_Index'].rolling(window=7).mean()
    plt.plot(df['Date'], df['MA_7'], linewidth=2, color='blue', alpha=0.7, 
             linestyle='--', label='Moyenne mobile 7 jours / 7-day MA')
    
    plt.title('Geopolitical Risk Daily Index (GPRD)', fontsize=16, fontweight='bold')
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Indice GPR / GPR Index', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    # Format x-axis
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    
    if save_plot:
        plt.savefig('gpr_time_series.png', dpi=300, bbox_inches='tight')
        print("Graphique sauvegardé: gpr_time_series.png")
        print("Plot saved: gpr_time_series.png")
    
    plt.show()

def plot_gpr_by_category(df, save_plot=True):
    """
    Trace l'indice GPR par catégorie d'événement
    Plot GPR index by event category
    """
    plt.figure(figsize=(14, 8))
    
    categories = df['Event_Category'].unique()
    colors = sns.color_palette("Set2", len(categories))
    
    for i, category in enumerate(categories):
        category_data = df[df['Event_Category'] == category]
        plt.scatter(category_data['Date'], category_data['GPR_Index'], 
                   label=category, alpha=0.7, s=50, color=colors[i])
    
    plt.title('Indice GPR par Catégorie d\'Événement / GPR Index by Event Category', 
              fontsize=16, fontweight='bold')
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Indice GPR / GPR Index', fontsize=12)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, alpha=0.3)
    
    # Format x-axis
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    
    if save_plot:
        plt.savefig('gpr_by_category.png', dpi=300, bbox_inches='tight')
        print("Graphique sauvegardé: gpr_by_category.png")
        print("Plot saved: gpr_by_category.png")
    
    plt.show()

def plot_gpr_statistics(df, save_plot=True):
    """
    Affiche les statistiques de l'indice GPR
    Display GPR index statistics
    """
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
    
    # Histogram
    ax1.hist(df['GPR_Index'], bins=20, alpha=0.7, color='darkred', edgecolor='black')
    ax1.set_title('Distribution de l\'Indice GPR / GPR Index Distribution')
    ax1.set_xlabel('Indice GPR / GPR Index')
    ax1.set_ylabel('Fréquence / Frequency')
    ax1.grid(True, alpha=0.3)
    
    # Box plot by category
    df.boxplot(column='GPR_Index', by='Event_Category', ax=ax2)
    ax2.set_title('GPR par Catégorie / GPR by Category')
    ax2.set_xlabel('Catégorie d\'Événement / Event Category')
    ax2.set_ylabel('Indice GPR / GPR Index')
    
    # Box plot by country
    df.boxplot(column='GPR_Index', by='Country', ax=ax3)
    ax3.set_title('GPR par Pays/Région / GPR by Country/Region')
    ax3.set_xlabel('Pays/Région / Country/Region')
    ax3.set_ylabel('Indice GPR / GPR Index')
    ax3.tick_params(axis='x', rotation=45)
    
    # Time series with confidence interval
    daily_stats = df.groupby('Date')['GPR_Index'].agg(['mean', 'std']).reset_index()
    ax4.plot(daily_stats['Date'], daily_stats['mean'], color='darkred', linewidth=2)
    ax4.fill_between(daily_stats['Date'], 
                     daily_stats['mean'] - daily_stats['std'],
                     daily_stats['mean'] + daily_stats['std'],
                     alpha=0.3, color='darkred')
    ax4.set_title('GPR avec Intervalle de Confiance / GPR with Confidence Interval')
    ax4.set_xlabel('Date')
    ax4.set_ylabel('Indice GPR / GPR Index')
    ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    if save_plot:
        plt.savefig('gpr_statistics.png', dpi=300, bbox_inches='tight')
        print("Graphique sauvegardé: gpr_statistics.png")
        print("Plot saved: gpr_statistics.png")
    
    plt.show()

def print_summary_statistics(df):
    """
    Affiche les statistiques résumées
    Print summary statistics
    """
    print("\n" + "="*60)
    print("STATISTIQUES RÉSUMÉES / SUMMARY STATISTICS")
    print("="*60)
    
    print(f"Période: {df['Date'].min().strftime('%Y-%m-%d')} à {df['Date'].max().strftime('%Y-%m-%d')}")
    print(f"Period: {df['Date'].min().strftime('%Y-%m-%d')} to {df['Date'].max().strftime('%Y-%m-%d')}")
    
    print(f"\nNombre total d'observations / Total observations: {len(df)}")
    
    print(f"\nIndice GPR moyen / Average GPR Index: {df['GPR_Index'].mean():.2f}")
    print(f"Écart-type / Standard deviation: {df['GPR_Index'].std():.2f}")
    print(f"Minimum: {df['GPR_Index'].min():.2f}")
    print(f"Maximum: {df['GPR_Index'].max():.2f}")
    print(f"Médiane / Median: {df['GPR_Index'].median():.2f}")
    
    print("\nRépartition par catégorie / Distribution by category:")
    print(df['Event_Category'].value_counts())
    
    print("\nRépartition par pays/région / Distribution by country/region:")
    print(df['Country'].value_counts())
    
    print("\n" + "="*60)

def main():
    """
    Fonction principale
    Main function
    """
    print("Chargement des données GPR...")
    print("Loading GPR data...")
    
    # Load data
    df = load_data()
    if df is None:
        return
    
    print(f"Données chargées avec succès: {len(df)} observations")
    print(f"Data loaded successfully: {len(df)} observations")
    
    # Print summary statistics
    print_summary_statistics(df)
    
    # Create plots
    print("\nCréation des graphiques...")
    print("Creating plots...")
    
    plot_gpr_time_series(df)
    plot_gpr_by_category(df)
    plot_gpr_statistics(df)
    
    print("\nAnalyse terminée!")
    print("Analysis completed!")

if __name__ == "__main__":
    main()