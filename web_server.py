"""Lightweight standalone web server for MedMultiSync.
Uses Python's built-in http.server - starts instantly with zero external web framework dependencies.
Serves interactive diagnostic UI at http://localhost:8000.
"""

import io
import json
import base64
from pathlib import Path
from http.server import HTTPServer, BaseHTTPRequestHandler
from PIL import Image

from medmultisync.model import ClinicalDiagnosticEngine
from medmultisync.data_presets import CLINICAL_PRESETS

print("Initializing MedMultiSync Diagnostic Engine...")
engine = ClinicalDiagnosticEngine()
print("Engine ready!")

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MedMultiSync - Multimodal Healthcare AI</title>
    <style>
        :root {
            --bg: #0B132B;
            --panel: #141E3C;
            --panel2: #1A2647;
            --border: #2C3C6B;
            --cyan: #00B4D8;
            --sky: #4CC9F0;
            --emerald: #34D399;
            --amber: #FBBF24;
            --rose: #FB7185;
            --white: #F8FAFC;
            --muted: #CBD5E1;
            --dim: #94A3B8;
        }
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background: var(--bg); color: var(--white); padding: 24px; line-height: 1.5; }
        .container { max-width: 1300px; margin: 0 auto; }
        header { border-bottom: 2px solid var(--border); padding-bottom: 16px; margin-bottom: 24px; }
        .tag { display: inline-block; background: rgba(0,180,216,0.15); border: 1px solid var(--cyan); color: var(--cyan); font-size: 11px; font-weight: 700; padding: 3px 10px; border-radius: 99px; text-transform: uppercase; margin-bottom: 8px; letter-spacing: 1px; }
        h1 { font-size: 26px; color: var(--white); margin-bottom: 6px; }
        .sub { color: var(--sky); font-size: 14px; }
        .meta { color: var(--dim); font-size: 12px; margin-top: 4px; }
        .presets { display: flex; gap: 10px; margin-bottom: 20px; flex-wrap: wrap; }
        .preset-btn { background: var(--panel2); border: 1px solid var(--border); color: var(--white); padding: 10px 16px; border-radius: 8px; cursor: pointer; font-size: 13px; font-weight: 600; transition: all 0.2s; }
        .preset-btn:hover { border-color: var(--cyan); background: rgba(0,180,216,0.1); }
        .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; }
        .card { background: var(--panel); border: 1px solid var(--border); border-radius: 12px; padding: 20px; }
        .card h2 { font-size: 17px; margin-bottom: 16px; color: var(--sky); border-bottom: 1px solid var(--border); padding-bottom: 8px; }
        .form-group { margin-bottom: 14px; }
        label { display: block; font-size: 12px; font-weight: 600; color: var(--dim); margin-bottom: 6px; text-transform: uppercase; letter-spacing: 0.5px; }
        .vitals-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
        input[type="number"], textarea, select { width: 100%; background: var(--panel2); border: 1px solid var(--border); color: var(--white); padding: 9px 12px; border-radius: 6px; font-size: 13px; outline: none; }
        input[type="number"]:focus, textarea:focus { border-color: var(--cyan); }
        textarea { resize: vertical; min-height: 85px; }
        .btn-diagnose { width: 100%; background: linear-gradient(135deg, #00B4D8, #4CC9F0); border: none; color: #0B132B; font-weight: 700; font-size: 15px; padding: 12px; border-radius: 8px; cursor: pointer; margin-top: 16px; transition: opacity 0.2s; }
        .btn-diagnose:hover { opacity: 0.9; }
        .preview-box { width: 100%; height: 240px; background: #000; border: 1px dashed var(--border); border-radius: 8px; display: flex; align-items: center; justify-content: center; overflow: hidden; margin-bottom: 12px; }
        .preview-box img { max-width: 100%; max-height: 100%; object-fit: contain; }
        .prob-bar { margin-bottom: 12px; }
        .prob-header { display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 4px; }
        .bar-bg { width: 100%; height: 8px; background: var(--panel2); border-radius: 4px; overflow: hidden; }
        .bar-fill { height: 100%; background: var(--cyan); border-radius: 4px; transition: width 0.4s; }
        .bar-fill.highlight { background: var(--emerald); }
        .attrib-table { width: 100%; border-collapse: collapse; margin: 12px 0; font-size: 12px; }
        .attrib-table th, .attrib-table td { padding: 8px; border: 1px solid var(--border); text-align: left; }
        .attrib-table th { background: var(--panel2); color: var(--sky); }
        .report-box { background: var(--panel2); border-left: 3px solid var(--cyan); padding: 14px; border-radius: 6px; font-size: 12.5px; white-space: pre-wrap; color: var(--muted); max-height: 300px; overflow-y: auto; }
        .alert-badge { display: inline-block; background: rgba(251,113,133,0.2); border: 1px solid var(--rose); color: var(--rose); font-size: 11px; padding: 2px 8px; border-radius: 4px; margin-right: 6px; margin-bottom: 4px; font-weight: 600; }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <div class="tag">IEEE Seminar · Multimodal Deep Learning</div>
            <h1>🩺 MedMultiSync: Clinical Decision Support System</h1>
            <div class="sub">Cross-Modal Attention Fusing Medical Imaging, EHR Vitals, and Physician Notes</div>
            <div class="meta">Presenter: Bezaleel Paul N · B.Tech CSE · Grounded in IEEE JBHI & Nature Medicine</div>
        </header>

        <div class="presets">
            <span style="font-size: 13px; font-weight: 600; align-self: center; color: var(--dim); margin-right: 4px;">⚡ Quick Presets:</span>
            <button class="preset-btn" onclick="loadCase('Bacterial Pneumonia')">📋 Case 1: Bacterial Pneumonia</button>
            <button class="preset-btn" onclick="loadCase('Cardiomegaly')">🫀 Case 2: Cardiomegaly / Heart Failure</button>
            <button class="preset-btn" onclick="loadCase('Atelectasis')">🫁 Case 3: Bibasilar Atelectasis</button>
            <button class="preset-btn" onclick="loadCase('Normal Baseline')">🩺 Case 4: Normal Healthy Screening</button>
        </div>

        <div class="grid">
            <!-- Left: Inputs -->
            <div class="card">
                <h2>📥 1. Patient Input Modalities</h2>
                <div class="form-group">
                    <label>Modality 1: Chest Radiograph (X-Ray)</label>
                    <div class="preview-box">
                        <img id="input-img" src="" alt="Chest X-Ray">
                    </div>
                    <input type="file" id="file-input" accept="image/*" onchange="handleFileUpload(event)">
                </div>

                <div class="form-group">
                    <label>Modality 2: EHR Vitals & Lab Biomarkers</label>
                    <div class="vitals-grid">
                        <div><label>Age (years)</label><input type="number" id="v-age" value="64"></div>
                        <div><label>Heart Rate (bpm)</label><input type="number" id="v-hr" value="108"></div>
                        <div><label>Resp Rate (/min)</label><input type="number" id="v-rr" value="26"></div>
                        <div><label>SpO2 Saturation (%)</label><input type="number" id="v-spo2" value="91"></div>
                        <div><label>Body Temp (°C)</label><input type="number" id="v-temp" value="39.2" step="0.1"></div>
                        <div><label>Systolic BP (mmHg)</label><input type="number" id="v-bp" value="118"></div>
                        <div><label>WBC (x10³/µL)</label><input type="number" id="v-wbc" value="16.4" step="0.1"></div>
                    </div>
                </div>

                <div class="form-group">
                    <label>Modality 3: Physician Narrative / Chief Complaint</label>
                    <textarea id="notes-text" placeholder="Patient symptoms, auscultation, clinical history..."></textarea>
                </div>

                <button class="btn-diagnose" onclick="runDiagnosis()">🔬 Run Multimodal Diagnostic Assessment</button>
            </div>

            <!-- Right: Outputs -->
            <div class="card">
                <h2>📊 2. Diagnostic Probabilities & Explainability</h2>
                
                <div style="margin-bottom: 16px;">
                    <div style="font-size: 12px; color: var(--dim); text-transform: uppercase; font-weight: 600; margin-bottom: 4px;">Primary Consensus Verdict:</div>
                    <div id="verdict-banner" style="font-size: 20px; font-weight: 700; color: var(--emerald);">Awaiting Assessment...</div>
                    <div id="alerts-container" style="margin-top: 8px;"></div>
                </div>

                <div id="prob-container" style="margin-bottom: 20px;"></div>

                <div class="form-group">
                    <label>Grad-CAM Anatomical Saliency Heatmap (Visual Grounding)</label>
                    <div class="preview-box">
                        <img id="cam-img" src="" alt="Grad-CAM Saliency Overlay">
                    </div>
                </div>

                <div class="form-group">
                    <label>Modality Attribution Decomposition (Cross-Modal Attention Gating)</label>
                    <table class="attrib-table">
                        <thead><tr><th>Modality</th><th>Contribution</th><th>Role</th></tr></thead>
                        <tbody id="attrib-tbody"></tbody>
                    </table>
                </div>

                <div class="form-group">
                    <label>Automated Clinical Impression Report (SOAP Format)</label>
                    <div class="report-box" id="report-text">Report will generate after running diagnostics.</div>
                </div>
            </div>
        </div>
    </div>

    <script>
        let currentImageBase64 = "";

        async function loadCase(caseKey) {
            const res = await fetch('/api/preset?case=' + encodeURIComponent(caseKey));
            const data = await res.json();
            document.getElementById('input-img').src = 'data:image/png;base64,' + data.image_base64;
            currentImageBase64 = data.image_base64;
            document.getElementById('v-age').value = data.vitals.age;
            document.getElementById('v-hr').value = data.vitals.heart_rate;
            document.getElementById('v-rr').value = data.vitals.resp_rate;
            document.getElementById('v-spo2').value = data.vitals.spo2;
            document.getElementById('v-temp').value = data.vitals.temp_c;
            document.getElementById('v-bp').value = data.vitals.systolic_bp;
            document.getElementById('v-wbc').value = data.vitals.wbc;
            document.getElementById('notes-text').value = data.notes;
            runDiagnosis();
        }

        function handleFileUpload(event) {
            const file = event.target.files[0];
            if (!file) return;
            const reader = new FileReader();
            reader.onload = function(e) {
                currentImageBase64 = e.target.result.split(',')[1];
                document.getElementById('input-img').src = e.target.result;
            };
            reader.readAsDataURL(file);
        }

        async function runDiagnosis() {
            const payload = {
                image_base64: currentImageBase64,
                vitals: {
                    age: parseFloat(document.getElementById('v-age').value) || 55,
                    heart_rate: parseFloat(document.getElementById('v-hr').value) || 75,
                    resp_rate: parseFloat(document.getElementById('v-rr').value) || 16,
                    spo2: parseFloat(document.getElementById('v-spo2').value) || 98,
                    temp_c: parseFloat(document.getElementById('v-temp').value) || 37.0,
                    systolic_bp: parseFloat(document.getElementById('v-bp').value) || 120,
                    wbc: parseFloat(document.getElementById('v-wbc').value) || 7.5
                },
                notes: document.getElementById('notes-text').value
            };

            document.getElementById('verdict-banner').innerText = "Analyzing multimodal tensors...";
            const res = await fetch('/api/diagnose', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(payload)
            });
            const data = await res.json();

            // Verdict
            document.getElementById('verdict-banner').innerHTML = `${data.prediction.toUpperCase()} <span style="font-size:15px; color:var(--sky);">(${(data.confidence * 100).toFixed(1)}% confidence)</span>`;
            
            // Alerts
            const alertsDiv = document.getElementById('alerts-container');
            alertsDiv.innerHTML = '';
            for (const [k, v] of Object.entries(data.clinical_alerts)) {
                alertsDiv.innerHTML += `<span class="alert-badge">⚠️ ${k}: ${v}</span>`;
            }

            // Probabilities
            const probDiv = document.getElementById('prob-container');
            probDiv.innerHTML = '';
            for (const [cls, p] of Object.entries(data.probabilities)) {
                const pct = (p * 100).toFixed(1);
                const isTop = cls === data.prediction;
                probDiv.innerHTML += `
                    <div class="prob-bar">
                        <div class="prob-header"><span>${isTop ? '🟢 ' : ''}<b>${cls}</b></span><span>${pct}%</span></div>
                        <div class="bar-bg"><div class="bar-fill ${isTop ? 'highlight' : ''}" style="width: ${pct}%;"></div></div>
                    </div>`;
            }

            // GradCAM
            document.getElementById('cam-img').src = 'data:image/png;base64,' + data.gradcam_base64;

            // Attribution
            const tbody = document.getElementById('attrib-tbody');
            tbody.innerHTML = `
                <tr><td>🩻 <b>Medical Imaging</b></td><td><b>${data.modality_attribution['Medical Imaging']}%</b></td><td>Spatial Feature Extraction (Grad-CAM)</td></tr>
                <tr><td>📈 <b>EHR Vitals & Labs</b></td><td><b>${data.modality_attribution['EHR Vitals & Labs']}%</b></td><td>Physiological z-score scaling</td></tr>
                <tr><td>📝 <b>Clinical Notes</b></td><td><b>${data.modality_attribution['Clinical Notes / Symptoms']}%</b></td><td>Symptom keyword grounding</td></tr>
            `;

            // Report
            document.getElementById('report-text').innerText = data.clinical_report;
        }

        // Auto-load case 1 on start
        window.onload = () => loadCase('Bacterial Pneumonia');
    </script>
</body>
</html>
"""


class MedRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path.startswith("/index"):
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(HTML_TEMPLATE.encode("utf-8"))
        elif self.path.startswith("/api/preset"):
            # Parse case query parameter
            import urllib.parse
            query = urllib.parse.urlparse(self.path).query
            params = urllib.parse.parse_qs(query)
            case_name = params.get("case", ["Bacterial Pneumonia"])[0]

            preset = CLINICAL_PRESETS.get(case_name, CLINICAL_PRESETS["Bacterial Pneumonia"])
            img = Image.open(preset["image_path"])
            buf = io.BytesIO()
            img.save(buf, format="PNG")
            b64_img = base64.b64encode(buf.getvalue()).decode("utf-8")

            res = {
                "name": preset["name"],
                "vitals": preset["vitals"],
                "notes": preset["notes"],
                "image_base64": b64_img,
            }
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(res).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == "/api/diagnose":
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length)
            data = json.loads(body.decode("utf-8"))

            b64_img = data.get("image_base64", "")
            if b64_img:
                img_bytes = base64.b64decode(b64_img)
                pil_img = Image.open(io.BytesIO(img_bytes))
            else:
                pil_img = Image.open(Path("samples/case_normal.png"))

            vitals = data.get("vitals", {})
            notes = data.get("notes", "")

            result = engine.diagnose(pil_img, vitals, notes)

            # Convert GradCAM numpy array to base64 PNG
            cam_pil = Image.fromarray(result["gradcam_image"])
            cam_buf = io.BytesIO()
            cam_pil.save(cam_buf, format="PNG")
            cam_b64 = base64.b64encode(cam_buf.getvalue()).decode("utf-8")

            res = {
                "prediction": result["prediction"],
                "confidence": result["confidence"],
                "probabilities": result["probabilities"],
                "gradcam_base64": cam_b64,
                "modality_attribution": result["modality_attribution"],
                "clinical_alerts": result["clinical_alerts"],
                "clinical_report": result["clinical_report"],
            }
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(res).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()


def run_server(port=5055):
    for p in [port, 5056, 5057]:
        try:
            server_address = ("127.0.0.1", p)
            httpd = HTTPServer(server_address, MedRequestHandler)
            print("\n" + "=" * 55)
            print("MedMultiSync Standalone Web App running at:")
            print(f"-> http://localhost:{p}")
            print(f"-> http://127.0.0.1:{p}")
            print("=" * 55 + "\n", flush=True)
            httpd.serve_forever()
            break
        except OSError:
            continue


if __name__ == "__main__":
    run_server()
