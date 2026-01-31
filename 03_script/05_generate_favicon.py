"""
Generate favicon.png from svg.svg
Converts SVG logo to PNG favicon (32x32, 64x64, 128x128, 256x256)

Note: This script requires Cairo system library on Windows, which can be complex to install.
Alternative: Use online tools like https://convertio.co/svg-png/ or https://cloudconvert.com/svg-to-png
"""

import os
from pathlib import Path

# Paths
project_root = Path(__file__).parent.parent
svg_path = project_root / "01_data" / "svg.svg"
output_dir = project_root / "public" / "images"
output_dir.mkdir(parents=True, exist_ok=True)

# Favicon sizes (standard sizes)
favicon_sizes = [32, 64, 128, 256]

def print_manual_instructions():
    """Print manual conversion instructions"""
    print("\n" + "="*70)
    print("MANUAL CONVERSION INSTRUCTIONS")
    print("="*70)
    print(f"\nSource SVG: {svg_path}")
    print(f"Output directory: {output_dir}\n")
    print("Option 1: Online Tools (Recommended)")
    print("- Visit: https://convertio.co/svg-png/")
    print("- Or: https://cloudconvert.com/svg-to-png")
    print("- Upload the SVG file")
    print("- Set output size to 32x32px for favicon.png")
    print("- Download and save to:", output_dir / "favicon.png")
    print("\nOption 2: Using Inkscape (if installed)")
    print(f'  inkscape "{svg_path}" --export-filename="{output_dir / "favicon.png"}" --export-width=32 --export-height=32')
    print("\nOption 3: Using ImageMagick (if installed)")
    print(f'  magick "{svg_path}" -resize 32x32 "{output_dir / "favicon.png"}"')
    print("\n" + "="*70)

def create_favicon_placeholder():
    """Create a simple placeholder favicon using basic method"""
    try:
        from PIL import Image, ImageDraw
        
        # Create a simple colored square as placeholder
        # This is a temporary solution until proper SVG conversion is available
        img = Image.new('RGB', (32, 32), color='#2565b2')  # Using brand blue color
        draw = ImageDraw.Draw(img)
        
        # Draw a simple geometric shape (placeholder)
        draw.ellipse([8, 8, 24, 24], fill='#efeff1', outline='#b9bbbc', width=2)
        
        favicon_path = output_dir / "favicon.png"
        img.save(favicon_path, 'PNG')
        print(f"[OK] Created placeholder favicon: {favicon_path}")
        print("  Note: This is a placeholder. Please replace with actual logo conversion.")
        return favicon_path
    except ImportError:
        print("Pillow not available for placeholder creation.")
        return None

if __name__ == "__main__":
    print("Favicon Generation from SVG")
    print("="*70)
    print(f"Source: {svg_path}")
    print(f"Output directory: {output_dir}\n")
    
    if not svg_path.exists():
        print(f"Error: SVG file not found at {svg_path}")
        exit(1)
    
    # Try to use available libraries
    conversion_success = False
    
    # Try cairosvg first
    try:
        import cairosvg
        print("Using cairosvg...")
        
        # Generate main favicon (32x32)
        main_favicon = output_dir / "favicon.png"
        cairosvg.svg2png(
            url=str(svg_path),
            write_to=str(main_favicon),
            output_width=32,
            output_height=32
        )
        print(f"[OK] Generated: {main_favicon} (32x32px)")
        
        # Generate additional sizes
        for size in favicon_sizes:
            output_path = output_dir / f"favicon-{size}x{size}.png"
            cairosvg.svg2png(
                url=str(svg_path),
                write_to=str(output_path),
                output_width=size,
                output_height=size
            )
            print(f"[OK] Generated: {output_path} ({size}x{size}px)")
        
        conversion_success = True
    except (ImportError, OSError) as e:
        print(f"cairosvg not available: {e}")
    
    # Try svglib + reportlab
    if not conversion_success:
        try:
            from svglib.svglib import svg2rlg
            from reportlab.graphics import renderPM
            print("Using svglib + reportlab...")
            
            drawing = svg2rlg(str(svg_path))
            if drawing:
                # Generate main favicon (32x32)
                main_favicon = output_dir / "favicon.png"
                drawing.width = 32
                drawing.height = 32
                scale = 32 / max(drawing.width, drawing.height)
                drawing.scale(scale, scale)
                renderPM.drawToFile(drawing, str(main_favicon), fmt='PNG', dpi=72)
                print(f"[OK] Generated: {main_favicon} (32x32px)")
                
                # Generate additional sizes
                for size in favicon_sizes:
                    output_path = output_dir / f"favicon-{size}x{size}.png"
                    drawing = svg2rlg(str(svg_path))
                    if drawing:
                        drawing.width = size
                        drawing.height = size
                        scale = size / max(drawing.width, drawing.height)
                        drawing.scale(scale, scale)
                        renderPM.drawToFile(drawing, str(output_path), fmt='PNG', dpi=72)
                        print(f"[OK] Generated: {output_path} ({size}x{size}px)")
                
                conversion_success = True
        except (ImportError, OSError) as e:
            print(f"svglib + reportlab not available: {e}")
    
    if not conversion_success:
        print("\n[WARNING] Automatic conversion not available (Cairo library required)")
        print_manual_instructions()
        
        # Create placeholder as fallback
        print("\nCreating placeholder favicon...")
        create_favicon_placeholder()
    else:
        print("\n[OK] Favicon generation complete!")
        print(f"\nGenerated files in: {output_dir}")
        print("- favicon.png (32x32px - main favicon)")
        for size in favicon_sizes:
            print(f"- favicon-{size}x{size}.png")
