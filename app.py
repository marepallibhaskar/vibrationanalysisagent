import gradio as gr
from orchestrator import Orchestrator

orc = Orchestrator(
    agents_file="config/agents.yaml",
    tools_file="config/tools.yaml",
    tasks_file="config/tasks.yaml",
    pipeline_file="config/pipeline.yaml"
)

def analyze(file, fs, rpm, design_doc, query):
    context = {
        "file_path": file.name,
        "fs": fs if fs else None,
        "rpm": rpm if rpm else None,
        "design_doc_path": design_doc.name if design_doc else None
    }
    results = orc.run_pipeline(context)

    if query:
        if "dominant frequency" in query.lower():
            return f"Dominant frequency: {results['fft_result']['dominant_freq']} Hz"
        elif "fault" in query.lower():
            return f"Detected fault: {results['fault_report']['fault']} (Confidence {results['fault_report']['confidence']:.2f})"
        else:
            return f"Results: {results}"
    else:
        return f"Detected fault: {results['fault_report']['fault']} (Confidence {results['fault_report']['confidence']:.2f})"

iface = gr.Interface(
    fn=analyze,
    inputs=[
        gr.File(label="Upload Vibration File"),
        gr.Number(label="Sampling Frequency (Hz)", value=10000),
        gr.Number(label="RPM (optional)"),
        gr.File(label="Upload Design Document (optional)"),
        gr.Textbox(label="Ask a question about the analysis")
    ],
    outputs="text",
    title="Autonomous Vibration Analyst Crew"
)

iface.launch()
