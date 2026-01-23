"""
Generate logo assets from 01_data/Name-card.png without modifying the source.

Outputs (written to public/images):
  - logo-mark.png     (512x512, circular alpha mask)
  - favicon.png       (64x64, circular alpha mask)

Also prints a base64 data URI payload for embedding into favicon.svg.

Notes:
  - This script intentionally crops from the LEFT half of the name card to avoid the right blue card.
  - Cropping is based on detecting the blue circular region (simple color threshold) and computing its bounding box.
"""

from __future__ import annotations

import base64
import io
import os
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "01_data" / "Name-card.png"
OUT_DIR = ROOT / "public" / "images"


def _find_blue_circle_bbox_left_half(rgb: Image.Image) -> tuple[int, int, int, int]:
    """Return bounding box (x0,y0,x1,y1) of the blue circle within the left half."""
    w, h = rgb.size
    left = rgb.crop((0, 0, w // 2, h))
    arr = np.array(left, dtype=np.uint8)

    r = arr[:, :, 0].astype(np.int16)
    g = arr[:, :, 1].astype(np.int16)
    b = arr[:, :, 2].astype(np.int16)

    # Blue-ish pixels: strong blue channel, relatively lower red/green.
    mask = (b > 110) & (r < 140) & (g < 170) & ((b - r) > 40) & ((b - g) > 20)

    ys, xs = np.where(mask)
    if xs.size == 0 or ys.size == 0:
        raise RuntimeError("Failed to detect blue circle region from Name-card.png (threshold too strict).")

    x0, x1 = int(xs.min()), int(xs.max() + 1)
    y0, y1 = int(ys.min()), int(ys.max() + 1)
    return x0, y0, x1, y1


def _square_crop(rgb: Image.Image, bbox: tuple[int, int, int, int], pad_ratio: float = 0.06) -> Image.Image:
    """Crop a padded square around bbox."""
    x0, y0, x1, y1 = bbox
    bw, bh = x1 - x0, y1 - y0
    cx, cy = x0 + bw / 2.0, y0 + bh / 2.0
    size = max(bw, bh) * (1.0 + pad_ratio * 2.0)

    half = size / 2.0
    sx0, sy0 = int(round(cx - half)), int(round(cy - half))
    sx1, sy1 = int(round(cx + half)), int(round(cy + half))

    # Clamp to image bounds
    sx0 = max(0, sx0)
    sy0 = max(0, sy0)
    sx1 = min(rgb.size[0], sx1)
    sy1 = min(rgb.size[1], sy1)

    return rgb.crop((sx0, sy0, sx1, sy1))


def _detect_blue_bbox(rgb: Image.Image) -> tuple[int, int, int, int]:
    """Detect blue-ish pixels bbox in the given image."""
    arr = np.array(rgb, dtype=np.uint8)

    r = arr[:, :, 0].astype(np.int16)
    g = arr[:, :, 1].astype(np.int16)
    b = arr[:, :, 2].astype(np.int16)

    # Same heuristic as _find_blue_circle_bbox_left_half, but without assuming a specific region.
    mask = (b > 110) & (r < 140) & (g < 170) & ((b - r) > 40) & ((b - g) > 20)
    ys, xs = np.where(mask)
    if xs.size == 0 or ys.size == 0:
        raise RuntimeError("Failed to detect blue region (no pixels matched threshold).")

    x0, x1 = int(xs.min()), int(xs.max() + 1)
    y0, y1 = int(ys.min()), int(ys.max() + 1)
    return x0, y0, x1, y1


def _detect_blue_circle_center_radius(rgb: Image.Image) -> tuple[float, float, float]:
    """Detect the center (cx, cy) and radius of the blue circle."""
    arr = np.array(rgb, dtype=np.uint8)
    
    r = arr[:, :, 0].astype(np.int16)
    g = arr[:, :, 1].astype(np.int16)
    b = arr[:, :, 2].astype(np.int16)
    
    # Blue-ish pixels: strong blue channel, relatively lower red/green.
    mask = (b > 110) & (r < 140) & (g < 170) & ((b - r) > 40) & ((b - g) > 20)
    
    ys, xs = np.where(mask)
    if xs.size == 0 or ys.size == 0:
        raise RuntimeError("Failed to detect blue circle (no pixels matched threshold).")
    
    # Calculate center as centroid of blue pixels
    cx = float(xs.mean())
    cy = float(ys.mean())
    
    # Calculate radius as max distance from center to blue pixel
    distances = np.sqrt((xs - cx) ** 2 + (ys - cy) ** 2)
    radius = float(distances.max())
    
    return cx, cy, radius


def _apply_circle_alpha(img: Image.Image) -> Image.Image:
    """Apply alpha mask - only pure white background becomes transparent, preserve silver antelope color."""
    rgba = img.convert("RGBA")
    w, h = rgba.size
    
    # Convert to numpy for easier processing
    arr = np.array(rgba)
    r, g, b = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2]
    
    # Detect pure WHITE background only (very high threshold to preserve silver)
    # Silver antelope has RGB values typically in 180-220 range, so threshold must be higher
    white_mask = (r > 245) & (g > 245) & (b > 245)
    
    # Create alpha channel: 0 (transparent) for pure white, 255 (opaque) for everything else
    # This preserves silver antelope (which has lower RGB values than white)
    alpha = np.where(white_mask, 0, 255).astype(np.uint8)
    
    rgba_arr = arr.copy()
    rgba_arr[:, :, 3] = alpha
    
    return Image.fromarray(rgba_arr, mode="RGBA")


def _save_png(img: Image.Image, path: Path, size: int) -> None:
    out = img.resize((size, size), Image.Resampling.LANCZOS)
    path.parent.mkdir(parents=True, exist_ok=True)
    out.save(path, format="PNG", optimize=True)


def _png_base64(img: Image.Image, size: int) -> str:
    out = img.resize((size, size), Image.Resampling.LANCZOS)
    buf = io.BytesIO()
    out.save(buf, format="PNG", optimize=True)
    return base64.b64encode(buf.getvalue()).decode("ascii")


def main() -> None:
    if not SRC.exists():
        raise FileNotFoundError(f"Source not found: {SRC}")

    rgb = Image.open(SRC).convert("RGB")
    w, h = rgb.size
    left = rgb.crop((0, 0, w // 2, h))

    # Pass 1: detect and crop around the blue circle on the left half.
    bbox1 = _detect_blue_bbox(left)
    crop1 = _square_crop(left, bbox=bbox1, pad_ratio=0.05)

    # Pass 2: refine detection inside crop and add extra padding for horn tips.
    bbox2 = _detect_blue_bbox(crop1)
    # Increased padding to ensure horn vertices are fully included
    crop2 = _square_crop(crop1, bbox=bbox2, pad_ratio=0.06)

    # Pass 3: CUT - Remove text below by cropping to blue circle bottom boundary
    # Detect blue circle bottom edge and crop everything below it
    bbox3 = _detect_blue_bbox(crop2)
    _, y0_blue, _, y1_blue = bbox3
    # Crop to remove text below blue circle (add small padding below blue circle)
    crop3 = crop2.crop((0, 0, crop2.size[0], y1_blue + int(crop2.size[1] * 0.05)))

    mark = _apply_circle_alpha(crop3)

    _save_png(mark, OUT_DIR / "logo-mark.png", size=512)
    _save_png(mark, OUT_DIR / "favicon.png", size=64)

    b64 = _png_base64(mark, size=64)
    print(b64)


if __name__ == "__main__":
    # Ensure deterministic output directory behavior in some IDE runs.
    os.chdir(ROOT)
    main()

