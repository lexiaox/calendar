import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd

def choose_excel_file():
    """弹出文件选择框，读取 Excel 文件并显示部分内容"""
    file_path = filedialog.askopenfilename(
        title="请选择课程表文件",
        filetypes=[("Excel 文件", "*.xlsx *.xls")]
    )

    if not file_path:
        messagebox.showwarning("提示", "未选择文件。")
        return

    try:
        # 读取 Excel
        df = pd.read_excel(file_path)

        # 显示前几行内容
        print("\n==== 成功读取课程表 ====")
        print(df.head())

        messagebox.showinfo("成功", f"成功读取文件：\n{file_path}\n\n前5行已打印到控制台！")

        return df

    except Exception as e:
        messagebox.showerror("错误", f"读取文件失败：\n{e}")
        return None

# ============== 测试窗口 ==============
if __name__ == "__main__":
    root = tk.Tk()
    root.title("课程表导入")
    root.geometry("300x200")

    tk.Label(root, text="请选择 Excel 格式的课程表：", font=("微软雅黑", 11)).pack(pady=20)
    tk.Button(root, text="上传文件", command=choose_excel_file, bg="#2196F3", fg="white").pack(pady=10)

    root.mainloop()
