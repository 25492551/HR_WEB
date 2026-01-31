"""
Convert PNG to SVG by embedding PNG as base64 image
"""
import base64
from pathlib import Path

# Paths
project_root = Path(__file__).parent.parent
png_path = project_root / "public" / "images" / "renewal" / "gazelle_11.png"
svg_path = project_root / "public" / "images" / "renewal" / "gazelle_11.svg"

def png_to_svg(png_path: Path, svg_path: Path) -> None:
    """Convert PNG to SVG by embedding as base64"""
    # Read PNG file
    with open(png_path, "rb") as f:
        png_data = f.read()
    
    # Encode to base64
    base64_data = base64.b64encode(png_data).decode("ascii")
    
    # Get image dimensions (we'll use a reasonable default or read from file)
    # For now, we'll create a responsive SVG that scales
    svg_content = f'''<svg width="100%" height="100%" viewBox="0 0 1024 1536" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<image width="100%" height="100%" xlink:href="data:image/png;base64,{base64_data}"/>
</svg>'''
    
    # Write SVG file
    svg_path.parent.mkdir(parents=True, exist_ok=True)
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    
    print(f"Converted: {png_path.name} -> {svg_path.name}")

if __name__ == "__main__":
    if not png_path.exists():
        print(f"Error: PNG file not found: {png_path}")
    else:
        png_to_svg(png_path, svg_path)
        print(f"SVG created at: {svg_path}")
