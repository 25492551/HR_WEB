"""
Export images and code from Figma design file using Figma API.

This script allows you to:
1. Export images from Figma nodes
2. Get CSS/styling information
3. Batch export multiple nodes

Requirements:
- Figma Personal Access Token (set in .env file as FIGMA_ACCESS_TOKEN)
- File Key from Figma URL
- Node IDs to export

Usage:
    python 03_script/07_export_figma_assets.py

Configuration:
    - Set FIGMA_ACCESS_TOKEN in .env file or environment variable
    - Update FILE_KEY and NODE_IDS in the script
"""

import os
import json
import requests
from pathlib import Path
from typing import List, Dict, Optional
from urllib.parse import urlparse, parse_qs

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
OUTPUT_DIR = PROJECT_ROOT / "public" / "images" / "figma"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Figma API configuration
FIGMA_API_BASE = "https://api.figma.com/v1"

# Get access token from environment variable or .env file
def get_access_token() -> str:
    """Get Figma access token from environment or .env file."""
    # Try environment variable first
    token = os.getenv("FIGMA_ACCESS_TOKEN")
    if token:
        return token
    
    # Try .env file
    env_file = PROJECT_ROOT / ".env"
    if env_file.exists():
        with open(env_file, "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("FIGMA_ACCESS_TOKEN="):
                    return line.split("=", 1)[1].strip().strip('"').strip("'")
    
    raise ValueError(
        "FIGMA_ACCESS_TOKEN not found. "
        "Please set it in .env file or environment variable.\n"
        "Get your token from: https://www.figma.com/settings"
    )


def extract_file_key_from_url(url: str) -> str:
    """Extract file key from Figma URL."""
    # URL format: https://www.figma.com/file/{FILE_KEY}/파일명
    # or: https://www.figma.com/design/{FILE_KEY}/파일명
    parsed = urlparse(url)
    path_parts = parsed.path.strip("/").split("/")
    
    if len(path_parts) >= 2 and path_parts[0] in ["file", "design"]:
        return path_parts[1]
    
    raise ValueError(f"Could not extract file key from URL: {url}")


def extract_node_ids_from_url(url: str) -> List[str]:
    """Extract node IDs from Figma URL query parameters."""
    parsed = urlparse(url)
    query_params = parse_qs(parsed.query)
    
    node_ids = []
    if "node-id" in query_params:
        # node-id format: "15-6" or "15:6"
        node_id_str = query_params["node-id"][0]
        # Convert "-" to ":" if needed
        node_id = node_id_str.replace("-", ":")
        node_ids.append(node_id)
    
    return node_ids


def get_file_info(access_token: str, file_key: str) -> Dict:
    """Get Figma file information."""
    url = f"{FIGMA_API_BASE}/files/{file_key}"
    headers = {"X-Figma-Token": access_token}
    
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    return response.json()


def get_node_info(access_token: str, file_key: str, node_ids: List[str]) -> Dict:
    """Get information about specific nodes."""
    url = f"{FIGMA_API_BASE}/files/{file_key}/nodes"
    headers = {"X-Figma-Token": access_token}
    params = {"ids": ",".join(node_ids)}
    
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    
    return response.json()


def export_images(
    access_token: str,
    file_key: str,
    node_ids: List[str],
    format: str = "png",
    scale: int = 2,
    output_dir: Path = OUTPUT_DIR
) -> List[str]:
    """
    Export images from Figma nodes.
    
    Args:
        access_token: Figma Personal Access Token
        file_key: Figma file key
        node_ids: List of node IDs to export
        format: Image format (png, jpg, svg, pdf)
        scale: Image scale (1, 2, 3, 4)
        output_dir: Output directory for images
    
    Returns:
        List of exported file paths
    """
    url = f"{FIGMA_API_BASE}/images/{file_key}"
    headers = {"X-Figma-Token": access_token}
    params = {
        "ids": ",".join(node_ids),
        "format": format,
        "scale": scale
    }
    
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    
    data = response.json()
    exported_files = []
    
    if "images" in data:
        for node_id, image_url in data["images"].items():
            if image_url:
                # Download image
                img_response = requests.get(image_url)
                img_response.raise_for_status()
                
                # Save image
                filename = f"node-{node_id.replace(':', '-')}.{format}"
                filepath = output_dir / filename
                
                with open(filepath, "wb") as f:
                    f.write(img_response.content)
                
                exported_files.append(str(filepath))
                print(f"✓ Exported: {filepath}")
            else:
                print(f"⚠ No image URL for node: {node_id}")
    
    return exported_files


def get_css_info(node_data: Dict) -> Dict:
    """Extract CSS-relevant information from node data."""
    css_info = {
        "width": None,
        "height": None,
        "background_color": None,
        "border_radius": None,
        "font_family": None,
        "font_size": None,
        "font_weight": None,
        "color": None,
        "padding": None,
        "margin": None
    }
    
    # This is a simplified extraction
    # Full implementation would require parsing the Figma node structure
    # which is complex and varies by node type
    
    return css_info


def save_node_info(node_data: Dict, output_dir: Path = OUTPUT_DIR):
    """Save node information as JSON for reference."""
    info_file = output_dir / "node_info.json"
    
    with open(info_file, "w", encoding="utf-8") as f:
        json.dump(node_data, f, indent=2, ensure_ascii=False)
    
    print(f"✓ Saved node info: {info_file}")


def main():
    """Main function to export Figma assets."""
    print("=" * 70)
    print("Figma Assets Exporter")
    print("=" * 70)
    
    # Configuration
    # Update these values based on your Figma file
    FIGMA_URL = "https://www.figma.com/design/bhZp6s1IGjzeTuYV7UQbTs/바이오_랜딩페이지?node-id=15-6&t=lEYCRbLj2WstN0NR-0"
    
    # Or set directly:
    # FILE_KEY = "bhZp6s1IGjzeTuYV7UQbTs"
    # NODE_IDS = ["15:6"]  # Add more node IDs as needed
    
    try:
        # Get access token
        print("\n1. Getting access token...")
        access_token = get_access_token()
        print("✓ Access token found")
        
        # Extract file key and node IDs from URL
        print("\n2. Extracting file information from URL...")
        file_key = extract_file_key_from_url(FIGMA_URL)
        node_ids = extract_node_ids_from_url(FIGMA_URL)
        
        if not node_ids:
            print("⚠ No node IDs found in URL. Using default node ID.")
            node_ids = ["15:6"]  # Default from URL
        
        print(f"✓ File Key: {file_key}")
        print(f"✓ Node IDs: {node_ids}")
        
        # Get file info
        print("\n3. Fetching file information...")
        file_info = get_file_info(access_token, file_key)
        print(f"✓ File name: {file_info.get('name', 'Unknown')}")
        
        # Get node info
        print("\n4. Fetching node information...")
        node_info = get_node_info(access_token, file_key, node_ids)
        save_node_info(node_info, OUTPUT_DIR)
        
        # Export images
        print("\n5. Exporting images...")
        exported_files = export_images(
            access_token,
            file_key,
            node_ids,
            format="png",
            scale=2,
            output_dir=OUTPUT_DIR
        )
        
        print(f"\n✓ Successfully exported {len(exported_files)} image(s)")
        print(f"✓ Output directory: {OUTPUT_DIR}")
        
        # Instructions for manual export
        print("\n" + "=" * 70)
        print("ADDITIONAL OPTIONS")
        print("=" * 70)
        print("\nTo export more nodes:")
        print("1. Open Figma and select the elements you want to export")
        print("2. Copy the node ID from the URL or use the API")
        print("3. Add node IDs to the NODE_IDS list in this script")
        print("4. Run the script again")
        print("\nTo get CSS code:")
        print("1. Open Figma in Dev Mode")
        print("2. Select elements and copy CSS code from the right panel")
        print("3. Or use Figma plugins like 'Figma to Code'")
        
    except requests.exceptions.HTTPError as e:
        print(f"\n✗ HTTP Error: {e}")
        if e.response.status_code == 403:
            print("  → Check if your access token is valid")
            print("  → Make sure you have access to this Figma file")
        elif e.response.status_code == 404:
            print("  → Check if the file key and node IDs are correct")
    except ValueError as e:
        print(f"\n✗ Error: {e}")
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
