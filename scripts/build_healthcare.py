"""Build the 'Multimodal-AI-in-Healthcare' presentation deck."""

import sys
from pathlib import Path

# Add scripts directory to path so 'deck' can be imported
sys.path.insert(0, str(Path(__file__).resolve().parent))

from pptx import Presentation
from pptx.util import Inches

from deck import slides_healthcare

OUT = Path(__file__).resolve().parents[1] / "Multimodal-AI-in-Healthcare.pptx"

BUILDERS = [
    slides_healthcare.slide_title,
    slides_healthcare.slide_roadmap,
    slides_healthcare.slide_clinical_imperative,
    slides_healthcare.slide_modality_spectrum,
    slides_healthcare.slide_fusion_paradigms,
    slides_healthcare.slide_cross_attention_arch,
    slides_healthcare.slide_foundation_models,
    slides_healthcare.slide_clinical_workflows,
    slides_healthcare.slide_technical_challenges,
    slides_healthcare.slide_explainability_ieee,
    slides_healthcare.slide_medmultisync_demo,
    slides_healthcare.slide_ieee_literature,
    slides_healthcare.slide_future_gmai,
    slides_healthcare.slide_conclusion_qa,
]


def main():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    for i, fn in enumerate(BUILDERS, 1):
        print(f"Building slide {i:02d}: {fn.__name__}...")
        fn(prs)

    prs.core_properties.title = "Multimodal AI in Healthcare"
    prs.core_properties.author = "Bezaleel Paul N"
    prs.core_properties.subject = "IEEE Seminar on Multimodal Diagnostics, Cross-Attention & Precision Medicine"
    prs.save(OUT)
    print(f"\nSuccessfully wrote presentation to:\n{OUT}\nTotal slides: {len(prs.slides)}")


if __name__ == "__main__":
    main()
