---
title: Merge PDF Files
emoji: 📄
colorFrom: yellow
colorTo: red
sdk: gradio
sdk_version: 5.31.0
app_file: app.py
license: mit
pinned: false
---


---


# 📄 PDF Merger App - Gộp file PDF theo thứ tự kéo-thả

Ứng dụng web giúp bạn **gộp nhiều file PDF lại thành một** theo **thứ tự bạn tự chọn bằng thao tác kéo-thả trực quan**, không cần cài đặt gì phức tạp.

[![🤗 Hugging Face Spaces](https://img.shields.io/badge/Deploy-HuggingFace-blue?logo=huggingface&style=flat)](https://huggingface.co/spaces/your-username/pdf-merger-drag-drop)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![Gradio](https://img.shields.io/badge/Gradio-4.x-orange?logo=gradio)](https://gradio.app)

---

## 🧠 Tính năng nổi bật

- ✅ **Upload nhiều file PDF**
- ✅ **Click-Chọn để sắp xếp thứ tự**
- ✅ **Gộp thành một file PDF liền mạch**
- ✅ **Không phụ thuộc vào tên file (1.pdf, part_1.pdf,...)**
- ✅ **Giao diện tiếng Việt, dễ dùng**
- ✅ **Có thể deploy trên Hugging Face Spaces hoặc chạy offline**

---

## 🚀 Demo online (nếu có)

🔗 [Dùng thử ngay trên Hugging Face Spaces »](https://huggingface.co/spaces/hoangthuandev/Merge-PDF-Files)

---

## 🖥️ Cài đặt & chạy cục bộ (Local)

### 1. Cài đặt Python

Yêu cầu Python >= 3.8

### 2. Cài thư viện cần thiết

````markdown

```bash
pip install gradio PyPDF2
````

### 3. Chạy ứng dụng

```bash
python app.py
```

Truy cập ứng dụng tại `http://127.0.0.1:7860`

---

## 🗂️ Cấu trúc dự án

```
📁 Merge-PDF-Files/
│
├── app.py              # Mã nguồn chính (Gradio UI + PyPDF2 merge logic)
├── README.md           # File mô tả dự án
├── requirements.txt    # Danh sách thư viện cần cài (nếu dùng Hugging Face)
```

---

## 📦 requirements.txt (nếu cần)

```txt
gradio
PyPDF2
```

---

## 🧩 Kỹ thuật sử dụng

* ✅ **Gradio UI**: xây dựng giao diện web thân thiện
* ✅ **JavaScript (SortableJS)**: hỗ trợ kéo-thả sắp xếp thứ tự
* ✅ **PyPDF2**: gộp file PDF từ nhiều nguồn

---

## 🤝 Giấy Phép

Dự án này sử dụng **MIT License**.  
Bạn có thể sử dụng, chỉnh sửa hoặc chia sẻ thoải mái!

---

## 👤 Tác Giả

**Hoàng Thuận DEV**
🌐 Website: [hoangthuan.dev](https://hoangthuan.dev)
📫 [Email hoặc GitHub](https://github.com/hoangthuan-dev)

---

## 💡 Đóng Góp

Mọi ý tưởng đóng góp, chỉnh sửa hoặc cải tiến tính năng đều được chào đón!  
Bạn có thể giúp cải thiện thuật toán nhận dạng nhãn hoặc hỗ trợ ngôn ngữ khác nếu muốn.

---
