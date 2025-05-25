import gradio as gr
from PyPDF2 import PdfMerger
import os
import tempfile

# Gộp PDF theo thứ tự tên file
def merge_pdfs(files, ordered_names):
    merger = PdfMerger()
    file_map = {os.path.basename(f.name): f for f in files}
    for name in ordered_names:
        f = file_map[name]
        merger.append(f.name)
    output_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    merger.write(output_file.name)
    merger.close()
    return output_file.name

# Lấy danh sách tên file ban đầu
def get_file_names(files):
    names = [os.path.basename(f.name) for f in files]
    return gr.update(choices=names, value=names)

# Sắp xếp tên A→Z
def sort_names_asc(files):
    names = sorted([os.path.basename(f.name) for f in files])
    return gr.update(choices=names, value=names)

# Đảo ngược thứ tự file
def reverse_names(files):
    names = [os.path.basename(f.name) for f in files][::-1]
    return gr.update(choices=names, value=names)

with gr.Blocks() as demo:
    gr.Markdown("## 📄 Gộp file PDF với sắp xếp thủ công hoặc tự động")
    gr.Markdown("1. Kéo-thả các file PDF → 2. Sắp xếp lại thủ công hoặc tự động → 3. Nhấn Gộp")

    with gr.Row():
        files_input = gr.File(file_types=[".pdf"], file_count="multiple", label="📂 Chọn hoặc kéo-thả file PDF")
        with gr.Column():
            sort_button = gr.Button("🔼 Sắp xếp theo tên (A→Z)")
            reverse_button = gr.Button("🔽 Đảo ngược thứ tự")

    order_dropdown = gr.Dropdown(choices=[], multiselect=True, label="📑 Sắp xếp thứ tự file PDF", interactive=True)
    merge_button = gr.Button("🔗 Gộp PDF")
    result = gr.File(label="📥 File đã gộp")

    files_input.change(get_file_names, inputs=files_input, outputs=order_dropdown)
    sort_button.click(sort_names_asc, inputs=files_input, outputs=order_dropdown)
    reverse_button.click(reverse_names, inputs=files_input, outputs=order_dropdown)
    merge_button.click(merge_pdfs, inputs=[files_input, order_dropdown], outputs=result)

if __name__ == "__main__":
    demo.launch()
