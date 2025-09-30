#!/usr/bin/env python3
"""
Example usage of the GPRD plotting functions.

This script demonstrates how to use the plot_gprd module programmatically.
"""

from plot_gprd import load_gprd_data, plot_gprd_with_events

def main():
    """Example of using the GPRD plotting functions programmatically."""
    
    print("Example: Loading and plotting GPRD data programmatically")
    print("=" * 60)
    
    # Load the data
    data = load_gprd_data('data_gpr_daily_recent_.csv')
    
    if data is not None:
        # Create a custom plot
        fig, ax = plot_gprd_with_events(
            data, 
            save_plot=True, 
            show_plot=False
        )
        
        # You can further customize the plot here if needed
        ax.set_title('Custom GPRD Analysis - Example')
        
        # Save with a different name
        fig.savefig('example_gprd_plot.png', dpi=300, bbox_inches='tight')
        print("Custom plot saved as 'example_gprd_plot.png'")
        
        # Display some custom analysis
        print(f"\nCustom Analysis:")
        print(f"Volatility (std dev): {data['gprd_index'].std():.3f}")
        print(f"High risk days (>3.0): {len(data[data['gprd_index'] > 3.0])}")
        print(f"Low risk days (<2.0): {len(data[data['gprd_index'] < 2.0])}")
        
    else:
        print("Error: Could not load data")

if __name__ == "__main__":
    main()