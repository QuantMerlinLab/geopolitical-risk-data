# geopolitical-risk-data
Dataset et code pour tracer le Geopolitical Risk Daily Index (GPRD).

## Description
This repository contains tools for visualizing the Geopolitical Risk Daily Index (GPRD) with event annotations. The GPRD tracks geopolitical risk levels over time and correlates them with significant political, military, and economic events.

## Installation
1. Clone this repository
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage
To generate a plot of the GPRD index with events:
```bash
python plot_gprd.py
```

This will:
- Load data from `data_gpr_daily_recent_.csv`
- Create a visualization showing the GPRD index over time
- Highlight significant events with annotations
- Save the plot as `gprd_plot.png`

## Data Format
The CSV file should contain the following columns:
- `date`: Date in YYYY-MM-DD format
- `gprd_index`: Numerical GPRD index value
- `event_type`: Type of event (Political, Military, Economic, etc.) - optional
- `event_description`: Description of the event - optional

## Features
- Time series visualization of GPRD index
- Event annotations with different colors for event types
- Statistical summary in the plot
- High-resolution PNG output suitable for reports and presentations
