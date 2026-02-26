"""
Extract header logo and favicon from files/logo_master.png.
Layout (1024x1024): top = large dark logo, bottom-left = white logo, bottom-right = circular icon.
We use BOTTOM-LEFT (white on black): make black transparent, then invert → black logo on transparent
for header (good contrast on cream). Footer uses same file + CSS invert for white on charcoal.
"""
from PIL import Image
import os

SRC = "files/logo_master.png"
OUT_DIR = "."
FILES_DIR = "files"

def make_black_transparent(img, threshold=30):
    """Set alpha to 0 for pixels at or below threshold (black/near-black)."""
    data = img.getdata()
    out = []
    for item in data:
        if len(item) == 4:
            r, g, b, a = item
        else:
            r, g, b = item[:3]
            a = 255
        if r <= threshold and g <= threshold and b <= threshold:
            out.append((r, g, b, 0))
        else:
            out.append((r, g, b, a))
    img.putdata(out)
    return img

def invert_rgb_keep_alpha(img):
    """Invert RGB, keep alpha unchanged (white→black, transparent stays transparent)."""
    from PIL import ImageChops
    r, g, b, a = img.split()
    rgb_inv = ImageChops.invert(Image.merge("RGB", (r, g, b)))
    r2, g2, b2 = rgb_inv.split()
    return Image.merge("RGBA", (r2, g2, b2, a))

def main():
    im = Image.open(SRC).convert("RGBA")
    w, h = im.size
    half = h // 2

    # --- Header logo: bottom-left (white on black). Black→transparent, then invert → black on transparent. ---
    bottom_left = im.crop((0, half, half, h))
    bottom_left = make_black_transparent(bottom_left)
    bottom_left = invert_rgb_keep_alpha(bottom_left)
    logo_path = os.path.join(FILES_DIR, "logo.png")
    os.makedirs(FILES_DIR, exist_ok=True)
    bottom_left.save(logo_path, "PNG")
    print("Saved", logo_path)

    # --- Favicon: bottom-right circular icon. Crop and resize. ---
    right = im.crop((half, half, w, h))
    # Resize for favicon.ico (16, 32, 48 for sharper look on high-DPI)
    icon_16 = right.resize((16, 16), Image.Resampling.LANCZOS)
    icon_32 = right.resize((32, 32), Image.Resampling.LANCZOS)
    icon_48 = right.resize((48, 48), Image.Resampling.LANCZOS)
    favicon_path = "favicon.ico"
    icon_16.save(favicon_path, format="ICO", append_images=[icon_32, icon_48], sizes=[(16, 16), (32, 32), (48, 48)])
    print("Saved", favicon_path)

    # Optional: 32x32 PNG and apple-touch 180x180
    icon_32.save(os.path.join(FILES_DIR, "favicon-32x32.png"), "PNG")
    icon_180 = right.resize((180, 180), Image.Resampling.LANCZOS)
    icon_180.save(os.path.join(FILES_DIR, "apple-touch-icon.png"), "PNG")
    print("Saved files/favicon-32x32.png, files/apple-touch-icon.png")

if __name__ == "__main__":
    main()
