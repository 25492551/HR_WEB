#!/usr/bin/env python3
"""
Extract color palette from Name-card.png
This script analyzes the business card image and extracts the main colors
used in the design.
"""

from PIL import Image
import numpy as np
from collections import Counter
import json
from pathlib import Path

def extract_dominant_colors(image_path, num_colors=10):
    """
    Extract dominant colors from an image.
    
    Args:
        image_path: Path to the image file
        num_colors: Number of dominant colors to extract
    
    Returns:
        List of tuples (RGB, count) sorted by frequency
    """
    # Open and convert image to RGB
    img = Image.open(image_path)
    img = img.convert('RGB')
    
    # Resize for faster processing (optional)
    img.thumbnail((500, 500))
    
    # Get all pixels
    pixels = list(img.get_flattened_data())
    
    # Count color frequencies
    color_counts = Counter(pixels)
    
    # Get most common colors
    dominant_colors = color_counts.most_common(num_colors)
    
    return dominant_colors

def rgb_to_hex(rgb):
    """Convert RGB tuple to HEX string."""
    return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}".upper()

def analyze_business_card(image_path):
    """
    Analyze business card and extract key colors.
    
    Returns:
        Dictionary with color information
    """
    print(f"Analyzing image: {image_path}")
    
    # Extract dominant colors
    dominant_colors = extract_dominant_colors(image_path, num_colors=20)
    
    # Convert to more readable format
    color_info = []
    for rgb, count in dominant_colors:
        hex_color = rgb_to_hex(rgb)
        percentage = (count / sum(c[1] for c in dominant_colors)) * 100
        color_info.append({
            'rgb': rgb,
            'hex': hex_color,
            'count': count,
            'percentage': round(percentage, 2)
        })
    
    # Identify key colors (heuristic approach)
    # Look for blue (primary brand color)
    blue_colors = [c for c in color_info if c['rgb'][2] > c['rgb'][0] and c['rgb'][2] > c['rgb'][1] and c['rgb'][2] > 100]
    # Look for white/light colors
    white_colors = [c for c in color_info if sum(c['rgb']) > 600]
    # Look for dark colors (black text)
    black_colors = [c for c in color_info if sum(c['rgb']) < 100]
    # Look for gray/silver colors
    gray_colors = [c for c in color_info if abs(c['rgb'][0] - c['rgb'][1]) < 30 and 
                   abs(c['rgb'][1] - c['rgb'][2]) < 30 and 
                   100 < sum(c['rgb']) < 500]
    
    result = {
        'all_colors': color_info,
        'blue_colors': sorted(blue_colors, key=lambda x: x['count'], reverse=True)[:5],
        'white_colors': sorted(white_colors, key=lambda x: x['count'], reverse=True)[:3],
        'black_colors': sorted(black_colors, key=lambda x: x['count'], reverse=True)[:3],
        'gray_colors': sorted(gray_colors, key=lambda x: x['count'], reverse=True)[:5],
    }
    
    return result

def save_color_palette(color_data, output_path):
    """Save color palette to JSON file."""
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(color_data, f, indent=2, ensure_ascii=False)
    print(f"Color palette saved to: {output_path}")

def print_color_summary(color_data):
    """Print a summary of extracted colors."""
    print("\n" + "="*60)
    print("COLOR PALETTE SUMMARY")
    print("="*60)
    
    print("\n[BLUE] BLUE COLORS (Primary Brand Color):")
    for i, color in enumerate(color_data['blue_colors'], 1):
        print(f"  {i}. {color['hex']} - RGB{color['rgb']} ({color['percentage']}%)")
    
    print("\n[WHITE] WHITE/LIGHT COLORS:")
    for i, color in enumerate(color_data['white_colors'], 1):
        print(f"  {i}. {color['hex']} - RGB{color['rgb']} ({color['percentage']}%)")
    
    print("\n[BLACK] BLACK/DARK COLORS:")
    for i, color in enumerate(color_data['black_colors'], 1):
        print(f"  {i}. {color['hex']} - RGB{color['rgb']} ({color['percentage']}%)")
    
    print("\n[GRAY] GRAY/SILVER COLORS:")
    for i, color in enumerate(color_data['gray_colors'], 1):
        print(f"  {i}. {color['hex']} - RGB{color['rgb']} ({color['percentage']}%)")
    
    print("\n" + "="*60)
    print("RECOMMENDED COLOR PALETTE:")
    print("="*60)
    if color_data['blue_colors']:
        print(f"Primary Blue:   {color_data['blue_colors'][0]['hex']}")
    if color_data['white_colors']:
        print(f"White:          {color_data['white_colors'][0]['hex']}")
    if color_data['black_colors']:
        print(f"Black:          {color_data['black_colors'][0]['hex']}")
    if color_data['gray_colors']:
        print(f"Silver/Gray:    {color_data['gray_colors'][0]['hex']}")
    print("="*60 + "\n")

def main():
    """Main function."""
    # Paths
    project_root = Path(__file__).parent.parent
    image_path = project_root / "01_data" / "Name-card.png"
    output_path = project_root / "01_data" / "color_palette.json"
    
    # Check if image exists
    if not image_path.exists():
        print(f"Error: Image not found at {image_path}")
        return
    
    # Analyze image
    color_data = analyze_business_card(str(image_path))
    
    # Print summary
    print_color_summary(color_data)
    
    # Save to JSON
    save_color_palette(color_data, str(output_path))
    
    print("Color extraction completed!")

if __name__ == "__main__":
    main()
