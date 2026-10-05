@echo off
title MedMultiSync Healthcare AI Launcher
echo =======================================================
echo Starting MedMultiSync Multimodal Healthcare App...
echo =======================================================
start http://localhost:7860
uv run --with torch --with torchvision --with gradio --with pillow --with numpy python app.py
pause
