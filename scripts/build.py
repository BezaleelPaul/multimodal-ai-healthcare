"""Build the 'AI in Software Design & Engineering' deck."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from pptx import Presentation
from pptx.util import Inches

from deck import slides_ai, slides_end, slides_open, slides_ops, slides_uml

OUT = Path(__file__).resolve().parents[1] / "AI-in-Software-Design-and-Engineering.pptx"

BUILDERS = [
    slides_open.slide_title,
    slides_open.slide_roadmap,
    slides_open.slide_traditional,
    slides_open.slide_uml_toolkit,
    slides_uml.slide_usecase_class,
    slides_uml.slide_sequence_activity,
    slides_uml.slide_state_machine,
    slides_uml.slide_component_deployment,
    slides_ai.slide_ai_shift,
    slides_ai.slide_ml_lifecycle,
    slides_ai.slide_ml_pipeline,
    slides_ai.slide_ai_architecture,
    slides_ai.slide_model_eval,
    slides_ops.slide_mlops,
    slides_ops.slide_feedback,
    slides_ops.slide_genai,
    slides_ops.slide_rag,
    slides_ops.slide_testing,
    slides_ops.slide_responsible,
    slides_end.slide_compare,
    slides_end.slide_grand,
    slides_end.slide_close,
]


def main():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    for fn in BUILDERS:
        fn(prs)
    prs.core_properties.title = "AI in Software Design & Engineering"
    prs.core_properties.author = "Bezaleel Paul N"
    prs.core_properties.subject = "From UML to AI / MLOps"
    prs.save(OUT)
    print(f"wrote {OUT}  ({len(prs.slides.__iter__.__self__._sldIdLst)} slides)")


if __name__ == "__main__":
    main()
