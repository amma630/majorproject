# 🧠 Text-to-Video Generator 🎥

This project is a **Text-to-Video Generator** that allows users to generate short AI-generated videos by providing a simple text prompt. It uses the [Hugging Face `diffusers`](https://github.com/huggingface/diffusers) library and the `damo-vilab/text-to-video-ms-1.7b` model to convert text into video.

## 🚀 Features

* 📜 User-friendly text prompt input
* 🔄 Progress bar with spinner animation
* 🎞️ Generates videos using pre-trained diffusion models
* 📺 Displays the generated video inline in Jupyter Notebook
* ⚙️ Utilizes CPU offloading and VAE slicing for optimized performance
## 🛠️ Technologies Used
* Python 🐍
* [Diffusers (Hugging Face)](https://huggingface.co/docs/diffusers/)
* PyTorch
* IPyWidgets
* Jupyter Notebook
* Base64 for inline video rendering
## 📦 Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/text-to-video-generator.git
   cd text-to-video-generator
   ```

2. **Install dependencies:**

   ```bash
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118  # or cpu-only
   pip install diffusers transformers accelerate ipywidgets
   ```

3. **Enable widgets in Jupyter Notebook (if not already):**

   ```bash
   jupyter nbextension enable --py widgetsnbextension

## 📋 Usage

1. **Open the Jupyter Notebook:**

   ```bash
   jupyter notebook
   ```

2. **Run the Notebook Cell**

   * Type your **prompt** (e.g., `a robot dancing on the moon`)
   * Click on **Generate Video**
   * Watch the magic happen ✨

---

## 📁 Project Structure

```text
.
├── text_to_video.ipynb      # Main notebook file
├── README.md                # Project documentation
```

---

## 📌 Notes

* This notebook is best run on a GPU-enabled environment (e.g., Google Colab).
* The generated video is temporarily saved to `/content/generated_video.mp4`.

---

## 📸 Sample Prompt

**Prompt:** `A panda riding a bicycle in Times Square`
**Output:** *(Displayed inline as an MP4 video)*

---

## 📄 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---

## 🙋‍♂️ Author

"Illingi Sriman Vara Prasad ","tanniru Sravani","peddalodi Nithin ","Akuthota soumya"
*Contributions, suggestions, and feedback are welcome!*

