import torch
from diffusers import DiffusionPipeline
from diffusers.utils import export_to_video
import ipywidgets as widgets
from IPython.display import display, HTML
import time
import shutil
import base64

# Function to generate video based on prompt
def generate_video(prompt, progress_bar, status_text, spinner):
    try:
        spinner.layout.display = 'block'
        status_text.value = "Generating video, please wait..."
        progress_bar.value = 0

        # Load pipeline
        pipe = DiffusionPipeline.from_pretrained("damo-vilab/text-to-video-ms-1.7b", torch_dtype=torch.float16, variant="fp16")
        pipe.enable_model_cpu_offload()
        pipe.enable_vae_slicing()  # Memory optimization

        # Simulate progress
        for i in range(1, 21):
            time.sleep(0.1)
            progress_bar.value = i * 5

        # Generate video
        video_frames = pipe(prompt, num_frames=64).frames[0]
        video_path = export_to_video(video_frames)

        # Move to fixed path
        final_path = '/content/generated_video.mp4'
        shutil.move(video_path, final_path)

        # Encode video for inline playback
        with open(final_path, "rb") as f:
            encoded_video = base64.b64encode(f.read()).decode()

        spinner.layout.display = 'none'
        status_text.value = "Video ready. Playing below..."

        video_html = f"""
        <video width="640" height="480" controls>
            <source src="data:video/mp4;base64,{encoded_video}" type="video/mp4">
            Your browser does not support the video tag.
        </video>
        """
        display(HTML(video_html))

    except Exception as e:
        spinner.layout.display = 'none'
        status_text.value = f"Error: {str(e)}"
        status_text.style = {'color': 'red'}

# Widgets
prompt_input = widgets.Text(
    value="Darth Vader surfing a wave",
    description="Enter Prompt:",
    layout=widgets.Layout(width='100%', height='40px', margin='10px 0')
)

generate_button = widgets.Button(
    description="Generate Video",
    layout=widgets.Layout(width='100%', height='50px', margin='20px 0'),
    style={'button_color': '#FF5722', 'font_weight': 'bold'}
)

progress_bar = widgets.IntProgress(
    value=0, min=0, max=100, step=5,
    description='Progress:',
    layout=widgets.Layout(width='100%', margin='20px 0')
)

spinner = widgets.HTML(
    value="<i class='fa fa-spinner fa-spin' style='font-size: 24px'></i>",
    layout=widgets.Layout(display='none', width='100%', height='40px')
)

status_text = widgets.Label(
    value="",
    layout=widgets.Layout(width='100%', margin='10px 0')
)

container = widgets.VBox([
    widgets.HTML("<h2 style='text-align:center; color: #FF5722;'>Text to Video Generator</h2>"),
    prompt_input,
    generate_button,
    progress_bar,
    spinner,
    status_text
])

# Button behavior
def on_button_click(b):
    generate_button.disabled = True
    generate_video(prompt_input.value, progress_bar, status_text, spinner)
    generate_button.disabled = False

generate_button.on_click(on_button_click)

# Inject style and display UI
style_html = """
<style>
    .widget-label { font-weight: bold; font-size: 16px; }
    .widget-button { background-color: #FF5722; color: white; border-radius: 6px; }
</style>
"""
display(HTML(style_html))
display(container)
