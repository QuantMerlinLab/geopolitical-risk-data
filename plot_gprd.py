#!/usr/bin/env python3
"""
Geopolitical Risk Daily Index (GPRD) Plotting Tool

This script loads the GPRD data from CSV file and creates visualizations
showing the index over time with event annotations.
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import numpy as np

def load_gprd_data(filename='data_gpr_daily_recent_.csv'):
    """
    Load GPRD data from CSV file.
    
    Args:
        filename (str): Path to the CSV file containing GPRD data
        
    Returns:
        pandas.DataFrame: Loaded and processed GPRD data
    """
    try:
        # Load the CSV data
        df = pd.read_csv(filename)
        
        # Convert date column to datetime
        df['date'] = pd.to_datetime(df['date'])
        
        # Sort by date to ensure proper ordering
        df = df.sort_values('date').reset_index(drop=True)
        
        print(f"Successfully loaded {len(df)} records from {filename}")
        print(f"Date range: {df['date'].min()} to {df['date'].max()}")
        
        return df
        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def plot_gprd_with_events(df, save_plot=True, show_plot=True):
    """
    Create a plot of the GPRD index with event annotations.
    
    Args:
        df (pandas.DataFrame): GPRD data
        save_plot (bool): Whether to save the plot to file
        show_plot (bool): Whether to display the plot
    """
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # Plot the GPRD index line
    ax.plot(df['date'], df['gprd_index'], 
            linewidth=2, color='navy', alpha=0.8, label='GPRD Index')
    
    # Fill area under the curve for better visualization
    ax.fill_between(df['date'], df['gprd_index'], alpha=0.3, color='lightblue')
    
    # Add event markers and annotations
    events_df = df[df['event_type'].notna() & (df['event_type'] != '')]
    
    if not events_df.empty:
        # Define colors for different event types
        event_colors = {
            'Political': 'red',
            'Military': 'darkred', 
            'Economic': 'green',
            'Diplomatic': 'blue',
            'Social': 'orange'
        }
        
        for _, event in events_df.iterrows():
            event_color = event_colors.get(event['event_type'], 'purple')
            
            # Add vertical line for event
            ax.axvline(x=event['date'], color=event_color, 
                      linestyle='--', alpha=0.7, linewidth=1.5)
            
            # Add event marker
            ax.scatter(event['date'], event['gprd_index'], 
                      color=event_color, s=100, zorder=5, 
                      marker='o', edgecolors='white', linewidth=2)
            
            # Add event annotation
            ax.annotate(f"{event['event_type']}: {event['event_description']}", 
                       xy=(event['date'], event['gprd_index']),
                       xytext=(10, 20), textcoords='offset points',
                       bbox=dict(boxstyle='round,pad=0.3', 
                                facecolor=event_color, alpha=0.7),
                       arrowprops=dict(arrowstyle='->', 
                                     connectionstyle='arc3,rad=0'),
                       fontsize=9, color='white', weight='bold')
    
    # Customize the plot
    ax.set_xlabel('Date', fontsize=12, weight='bold')
    ax.set_ylabel('GPRD Index', fontsize=12, weight='bold')
    ax.set_title('Geopolitical Risk Daily Index (GPRD) with Events', 
                fontsize=16, weight='bold', pad=20)
    
    # Format x-axis dates
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha='right')
    
    # Add grid for better readability
    ax.grid(True, alpha=0.3, linestyle='-', linewidth=0.5)
    
    # Add legend
    if not events_df.empty:
        # Create legend handles for event types
        legend_elements = [plt.Line2D([0], [0], color='navy', linewidth=2, label='GPRD Index')]
        
        for event_type in events_df['event_type'].unique():
            if event_type and event_type != '':
                color = event_colors.get(event_type, 'purple')
                legend_elements.append(
                    plt.Line2D([0], [0], marker='o', color='w', 
                              markerfacecolor=color, markersize=8, 
                              label=f'{event_type} Event')
                )
        
        ax.legend(handles=legend_elements, loc='upper left', framealpha=0.9)
    else:
        ax.legend()
    
    # Adjust layout to prevent label cutoff
    plt.tight_layout()
    
    # Add statistics text box
    stats_text = f"""Statistics:
    Max GPRD: {df['gprd_index'].max():.2f}
    Min GPRD: {df['gprd_index'].min():.2f}
    Mean GPRD: {df['gprd_index'].mean():.2f}
    Events: {len(events_df)}"""
    
    ax.text(0.02, 0.98, stats_text, transform=ax.transAxes, 
            verticalalignment='top', bbox=dict(boxstyle='round', 
            facecolor='white', alpha=0.8), fontsize=10)
    
    # Save plot if requested
    if save_plot:
        plt.savefig('gprd_plot.png', dpi=300, bbox_inches='tight')
        print("Plot saved as 'gprd_plot.png'")
    
    # Show plot if requested
    if show_plot:
        plt.show()
    
    return fig, ax

def main():
    """Main function to load data and create plot."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Plot Geopolitical Risk Daily Index (GPRD) with events')
    parser.add_argument('--input', '-i', default='data_gpr_daily_recent_.csv',
                        help='Input CSV file (default: data_gpr_daily_recent_.csv)')
    parser.add_argument('--output', '-o', default='gprd_plot.png',
                        help='Output plot file (default: gprd_plot.png)')
    parser.add_argument('--show', action='store_true',
                        help='Display the plot in addition to saving it')
    
    args = parser.parse_args()
    
    print(f"Loading GPRD data from {args.input} and creating visualization...")
    
    # Load the data
    df = load_gprd_data(args.input)
    
    if df is not None:
        # Create the plot
        fig, ax = plot_gprd_with_events(df, save_plot=True, show_plot=args.show)
        
        # Save with custom filename if specified
        if args.output != 'gprd_plot.png':
            plt.savefig(args.output, dpi=300, bbox_inches='tight')
            print(f"Plot saved as '{args.output}'")
        
        # Print summary information
        print("\nData Summary:")
        print(f"Total records: {len(df)}")
        print(f"Date range: {df['date'].min().strftime('%Y-%m-%d')} to {df['date'].max().strftime('%Y-%m-%d')}")
        print(f"GPRD Index range: {df['gprd_index'].min():.2f} - {df['gprd_index'].max():.2f}")
        
        # Count events by type
        events_df = df[df['event_type'].notna() & (df['event_type'] != '')]
        if not events_df.empty:
            print("\nEvents by type:")
            event_counts = events_df['event_type'].value_counts()
            for event_type, count in event_counts.items():
                print(f"  {event_type}: {count}")
        
        print("\nVisualization completed successfully!")
    else:
        print("Failed to load data. Please check the CSV file.")

if __name__ == "__main__":
    main()