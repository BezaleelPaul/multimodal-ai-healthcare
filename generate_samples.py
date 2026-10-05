"""Generate realistic synthetic chest X-ray images for demonstration presets.
Creates anatomical structures: thoracic cage, clavicles, ribs, cardiac silhouette,
diaphragmatic domes, and condition-specific opacities/features.
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter
import numpy as np

SAMPLES_DIR = Path(__file__).resolve().parent / "samples"
SAMPLES_DIR.mkdir(parents=True, exist_ok=True)


def _base_chest_xray(width=512, height=512):
    """Draw a base radiograph with anatomical chest structures."""
    # Dark lung background (air is radiolucent = dark)
    img = Image.new("L", (width, height), color=25)
    draw = ImageDraw.Draw(img)

    # Soft tissue mantle & thoracic wall (surrounding soft tissue is grey)
    draw.rectangle([0, 0, width, height], fill=30)
    # Lung fields (two large elliptical dark regions)
    # Left lung (patient's right - left of image)
    draw.ellipse([80, 90, 230, 420], fill=15)
    # Right lung (patient's left - right of image)
    draw.ellipse([270, 90, 425, 420], fill=15)

    # Mediastinum & Spine (dense white/grey down center)
    draw.rectangle([210, 40, 290, 470], fill=140)

    # Clavicles (bilateral upper bars)
    draw.line([70, 95, 230, 85], fill=175, width=12)
    draw.line([430, 95, 270, 85], fill=175, width=12)

    # Posterior & Anterior Ribs (curved arches across lungs)
    for y_offset in range(120, 390, 38):
        # Patient right
        draw.arc([60, y_offset, 250, y_offset + 55], start=180, end=360, fill=85, width=7)
        # Patient left
        draw.arc([250, y_offset, 440, y_offset + 55], start=180, end=360, fill=85, width=7)

    # Diaphragmatic Domes (bright curved lower boundary)
    draw.pieslice([60, 370, 250, 490], start=180, end=360, fill=180)
    draw.pieslice([255, 385, 445, 505], start=180, end=360, fill=170)

    # Normal Cardiac Silhouette (covers center-left, typical CTR ~ 0.45)
    draw.chord([190, 250, 330, 425], start=45, end=225, fill=160)

    # Blur to simulate radiographic scatter & tissue density gradients
    img = img.filter(ImageFilter.GaussianBlur(radius=7))
    return img


def make_normal_case():
    img = _base_chest_xray()
    # Add subtle pulmonary vascular markings
    draw = ImageDraw.Draw(img)
    draw.line([220, 210, 160, 260], fill=55, width=3)
    draw.line([220, 220, 150, 310], fill=50, width=2)
    draw.line([280, 210, 340, 260], fill=55, width=3)
    draw.line([280, 220, 350, 310], fill=50, width=2)
    img = img.filter(ImageFilter.GaussianBlur(radius=3))
    out_path = SAMPLES_DIR / "case_normal.png"
    img.save(out_path)
    return out_path


def make_pneumonia_case():
    img = _base_chest_xray()
    # Right lower lobe consolidation (dense radio-opaque cloudy infiltration)
    draw = ImageDraw.Draw(img)
    # Dense patchy consolidation in left image quadrant (patient right lower lobe)
    for _ in range(5):
        draw.ellipse([110, 270, 230, 390], fill=155)
    # Air bronchogram hints (dark branching within dense white area)
    draw.line([160, 280, 140, 340], fill=60, width=3)
    draw.line([160, 310, 185, 360], fill=60, width=2)
    img = img.filter(ImageFilter.GaussianBlur(radius=6))
    out_path = SAMPLES_DIR / "case_pneumonia.png"
    img.save(out_path)
    return out_path


def make_cardiomegaly_case():
    img = _base_chest_xray()
    draw = ImageDraw.Draw(img)
    # Massive cardiac enlargement (Cardiothoracic ratio > 0.60)
    # Extends noticeably into patient's left hemithorax
    draw.ellipse([160, 230, 385, 435], fill=175)
    # Prominent aortic knob and pulmonary vascular engorgement (cephalization)
    draw.ellipse([215, 120, 285, 185], fill=165)
    draw.line([275, 180, 360, 150], fill=95, width=4)
    draw.line([215, 180, 130, 150], fill=95, width=4)
    img = img.filter(ImageFilter.GaussianBlur(radius=6))
    out_path = SAMPLES_DIR / "case_cardiomegaly.png"
    img.save(out_path)
    return out_path


def make_atelectasis_case():
    img = _base_chest_xray()
    draw = ImageDraw.Draw(img)
    # Linear plate-like / discoid atelectasis bands in bibasilar lung bases
    draw.line([100, 360, 220, 375], fill=145, width=8)
    draw.line([95, 340, 195, 350], fill=135, width=6)
    draw.line([280, 365, 400, 380], fill=140, width=7)
    # Slight elevation of hemidiaphragm due to volume loss
    draw.pieslice([60, 350, 240, 470], start=180, end=360, fill=185)
    img = img.filter(ImageFilter.GaussianBlur(radius=5))
    out_path = SAMPLES_DIR / "case_atelectasis.png"
    img.save(out_path)
    return out_path


def main():
    p1 = make_normal_case()
    p2 = make_pneumonia_case()
    p3 = make_cardiomegaly_case()
    p4 = make_atelectasis_case()
    print("Generated clinical chest X-ray samples:")
    for p in [p1, p2, p3, p4]:
        print(f" - {p.name} ({p.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
