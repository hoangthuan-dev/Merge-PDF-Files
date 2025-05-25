import gradio as gr
from PyPDF2 import PdfMerger
import os
import tempfile

# Gộp PDF theo thứ tự tên file
def merge_pdfs(files, ordered_names):
    merger = PdfMerger()

    # Tạo mapping từ tên file sang file object
    file_map = {os.path.basename(f.name): f for f in files}

    for name in ordered_names:
        f = file_map[name]
        merger.append(f.name)

    # Ghi file kết quả
    output_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    merger.write(output_file.name)
    merger.close()
    return output_file.name

# Lấy danh sách tên file
def get_file_names(files):
    names = [os.path.basename(f.name) for f in files]
    return gr.update(choices=names, value=names)

with gr.Blocks() as demo:
    gr.Markdown("## 📄 Gộp file PDF với sắp xếp thủ công")
    gr.Markdown("1. Kéo-thả các file PDF → 2. Sắp xếp lại thứ tự → 3. Nhấn Gộp")

    files_input = gr.File(file_types=[".pdf"], file_count="multiple", label="📂 Chọn hoặc kéo-thả file PDF")
    order_dropdown = gr.Dropdown(choices=[], multiselect=True, label="📑 Sắp xếp thứ tự file PDF", interactive=True)
    merge_button = gr.Button("🔗 Gộp PDF")
    result = gr.File(label="📥 File đã gộp")

    files_input.change(get_file_names, inputs=files_input, outputs=order_dropdown)
    merge_button.click(merge_pdfs, inputs=[files_input, order_dropdown], outputs=result)

if __name__ == "__main__":
    demo.launch()
