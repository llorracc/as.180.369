import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for script execution
import matplotlib.pyplot as plt
import numpy as np
import os

# Ensure presentation_images directory exists
os.makedirs('presentation_images', exist_ok=True)

# ============================================================================
# Chart 1: BNPL GMV Growth (Bars)
# ============================================================================
# Data: BNPL GMV Growth (in billions USD) - US Market
# Source: Consumer Financial Protection Bureau (CFPB) Market Trends Report (2022)
years_gmv = [2019, 2020, 2021, 2022]
gmv_values = [2.0, 8.0, 24.2, 34.0]  # CFPB data: $2B (2019), $24.2B (2021), $34B (2022)

fig1, ax1 = plt.subplots(figsize=(12, 7))
color_gmv = '#3498db'

bars = ax1.bar(years_gmv, gmv_values, width=0.6, color=color_gmv, alpha=0.7, 
               edgecolor='#2980b9', linewidth=1.5, zorder=3)

ax1.set_xlabel('Year', fontsize=14, fontweight='bold', labelpad=12)
ax1.set_ylabel('BNPL GMV (Billions USD)', fontsize=13, fontweight='bold', labelpad=12)
ax1.tick_params(axis='y', labelsize=11)
ax1.tick_params(axis='x', labelsize=11)
ax1.grid(True, alpha=0.3, linestyle='--', linewidth=0.8, zorder=0)
ax1.set_axisbelow(True)

# Add value labels on bars
for year, val in zip(years_gmv, gmv_values):
    ax1.text(year, val, f'${val:.1f}B', ha='center', va='bottom', 
             fontsize=11, fontweight='bold', color='#2c3e50', zorder=4)

ax1.set_title('BNPL Gross Merchandise Value Growth (US Market)', 
              fontsize=16, fontweight='bold', pad=20)
ax1.set_xlim(2018.5, 2022.5)
ax1.set_xticks(years_gmv)

plt.tight_layout()
plt.subplots_adjust(bottom=0.15)  # Make room for source below plot

# Add source citation well outside the plot area
fig1.text(0.99, 0.01, 'Source: CFPB Market Trends Report (2022)', 
         ha='right', va='bottom',
         fontsize=9, style='italic', color='#7f8c8d',
         transform=fig1.transFigure)
output_path1 = 'presentation_images/bnpl_gmv_growth_chart.png'
plt.savefig(output_path1, dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
plt.close()  # Close figure to free memory
print(f"✓ Generated: {output_path1}")

# ============================================================================
# Chart 2: Klarna Valuation (Line with Decline Annotation)
# ============================================================================
# Klarna brand colors: #FFA8CD (pink) and #0B051D (dark navy)

# Data: Klarna Valuation (in billions USD)
years_val = [2019, 2020, 2021, 2022, 2023, 2024, 2025]
valuation_values = [5.5, 10.6, 46.0, 6.7, 7.0, 8.0, 13.5]  # Peak at $46B in 2021, IPO at $13-14B in 2025

# Create figure with refined styling
fig2, ax2 = plt.subplots(figsize=(14, 8))
fig2.patch.set_facecolor('white')

# Klarna brand colors
klarna_pink = '#FFA8CD'
klarna_navy = '#0B051D'

# Plot main line with Klarna pink - solid points
line = ax2.plot(years_val, valuation_values, color=klarna_pink, linewidth=4.5, 
                marker='o', markersize=12, markerfacecolor=klarna_pink, 
                markeredgewidth=0, 
                zorder=4, alpha=0.9)

# Styling
ax2.set_xlabel('Year', fontsize=15, fontweight='bold', labelpad=15, color=klarna_navy)
ax2.set_ylabel('Klarna Valuation (Billions USD)', fontsize=15, fontweight='bold', 
               labelpad=15, color=klarna_navy)
ax2.tick_params(axis='y', labelsize=12, colors=klarna_navy)
ax2.tick_params(axis='x', labelsize=12, colors=klarna_navy)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['left'].set_color(klarna_navy)
ax2.spines['bottom'].set_color(klarna_navy)
ax2.spines['left'].set_linewidth(1.5)
ax2.spines['bottom'].set_linewidth(1.5)

# Refined grid
ax2.grid(True, alpha=0.2, linestyle='--', linewidth=0.8, color=klarna_navy, zorder=0)
ax2.set_axisbelow(True)

# Find peak and IPO points
peak_idx = years_val.index(2021)
peak_val = valuation_values[peak_idx]
ipo_idx = years_val.index(2025)
ipo_val = valuation_values[ipo_idx]

# Calculate decline percentage
decline_pct = ((peak_val - ipo_val) / peak_val) * 100

# Add value labels for ALL years - consistent fonts, centralized, all with same styling
# Adjust y-position slightly to ensure boxes fully cover circular markers
ipo_text_obj = None  # Store IPO text object for arrow connection
for year, val in zip(years_val, valuation_values):
    if year == 2021:  # Peak
        label_text = '$46.0B'
        va_pos = 'bottom'
        y_offset = -0.8  # Downward offset for bottom-aligned labels
    elif year == 2025:  # IPO
        label_text = 'IPO: $13.5B'
        va_pos = 'top'
        y_offset = 0.2  # Upward offset for IPO label
    else:  # All other years
        label_text = f'${val:.1f}B'
        va_pos = 'bottom'
        y_offset = -0.8  # Downward offset for bottom-aligned labels
    
    text_obj = ax2.text(year, val + y_offset, label_text, 
             ha='center', va=va_pos,
             fontsize=11, fontweight='bold', color=klarna_navy,
             bbox=dict(boxstyle='round,pad=0.4', facecolor='white', alpha=0.95, 
                      edgecolor=klarna_pink, linewidth=1.5),
             zorder=5)
    
    # Store IPO text object for arrow connection
    if year == 2025:
        ipo_text_obj = text_obj

# Decline percentage - positioned directly above/left of IPO point
# Position it to the left and slightly above the IPO point (2025, ipo_val)
bbox_props = dict(boxstyle='round,pad=0.6', facecolor=klarna_pink, edgecolor=klarna_pink, 
                  linewidth=1.5, alpha=0.75)

# Position annotation to the left and above the IPO point
annotation_x = 2024.3  # Slightly left of IPO year (2025)
annotation_y = ipo_val + 3.0  # Above the IPO value (moved up slightly)

decline_text = ax2.text(annotation_x, annotation_y, f'{decline_pct:.0f}% decline', 
         fontsize=11, fontweight='bold', style='italic', color=klarna_navy,
         bbox=bbox_props,
         ha='left', va='bottom',
         zorder=6)

# Title with Klarna styling
ax2.set_title('Klarna Valuation: Peak to IPO', 
              fontsize=18, fontweight='bold', pad=25, color=klarna_navy)

# Set limits and ticks
ax2.set_xlim(2018.5, 2025.5)
ax2.set_xticks(years_val)
ax2.set_ylim(0, max(valuation_values) * 1.15)

# Add arrow connecting "71% decline" to IPO label
# Now that limits are set, we can get accurate bounding boxes
fig2.canvas.draw()
renderer = fig2.canvas.get_renderer()

# Get bounding boxes in display coordinates, then transform to data coordinates
decline_bbox = decline_text.get_window_extent(renderer=renderer)
decline_bbox_data = decline_bbox.transformed(ax2.transData.inverted())

if ipo_text_obj:
    ipo_bbox = ipo_text_obj.get_window_extent(renderer=renderer)
    ipo_bbox_data = ipo_bbox.transformed(ax2.transData.inverted())
    
    # Calculate exact edge positions - use the bounding box edges directly
    # Arrow start: right edge of decline box, at bottom-right corner
    arrow_start_x = decline_bbox_data.x1  # Right edge
    # Position at the very bottom - almost exactly at bottom edge
    arrow_start_y = decline_bbox_data.y0 + (decline_bbox_data.y1 - decline_bbox_data.y0) * 0.05  
    
    # Arrow end: left edge of IPO box, top edge (top-left corner)  
    arrow_end_x = ipo_bbox_data.x0  # Left edge
    arrow_end_y = ipo_bbox_data.y1  # Top edge
    
    # Shorten the arrow by moving start point slightly inward from the edge
    # Calculate offsets to move start point inward (left from right edge)
    x_range = ax2.get_xlim()[1] - ax2.get_xlim()[0]
    
    # Small inward offset to shorten arrow and ensure it touches the edge
    # Move left (decrease x) slightly from right edge
    offset_x = x_range * 0.05  # Leftward offset to shorten arrow
    
    arrow_start_x_adj = arrow_start_x - offset_x  # Move left (inward) - shortens arrow
    arrow_start_y_adj = arrow_start_y  # Keep y position (slightly down from top)
    
    # Draw arrow using annotate with dashed line style (断联的那种), no bold
    ax2.annotate('',
                 xy=(arrow_end_x, arrow_end_y),  # End: left-top edge of IPO box
                 xytext=(arrow_start_x_adj, arrow_start_y_adj),  # Start: adjusted to be at visible edge
                 arrowprops=dict(arrowstyle='->',
                               lw=1.5,  # Thinner line (no bold)
                               color=klarna_navy,
                               alpha=0.8,
                               shrinkA=0,  # No extension at start
                               shrinkB=0,  # No extension at end
                               linestyle='--'),  # Dashed line (断联)
                 zorder=5)

plt.tight_layout()
plt.subplots_adjust(bottom=0.15)  # Make room for source below plot

# Add source citation well outside the plot area
fig2.text(0.99, 0.01, 'Source: Klarna public filings & news reports', 
         ha='right', va='bottom',
         fontsize=9, style='italic', color=klarna_navy, alpha=0.7,
         transform=fig2.transFigure)
output_path2 = 'presentation_images/klarna_valuation_chart.png'
plt.savefig(output_path2, dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
plt.close()  # Close figure to free memory
print(f"✓ Generated: {output_path2}")
print("\n✓ All charts generated successfully!")


