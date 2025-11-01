import tkinter as tk
from tkinter import messagebox

# ======================
# Step 1. 获取作息时间
# ======================
def get_sleep_schedule():
    """弹窗询问用户睡眠与起床时间，并返回结果"""
    def on_submit():
        wake = wake_entry.get().strip()
        sleep = sleep_entry.get().strip()

        if not wake or not sleep:
            messagebox.showerror("错误", "请填写完整的起床和睡觉时间！")
            return
        
        # 简单校验格式
        if ":" not in wake or ":" not in sleep:
            messagebox.showerror("错误", "时间格式应为 HH:MM，例如 07:30")
            return

        # 保存结果到全局变量或文件
        global user_schedule
        user_schedule = {"wake_time": wake, "sleep_time": sleep}

        messagebox.showinfo("成功", f"起床时间：{wake}\n睡觉时间：{sleep}")
        root.destroy()

    # 创建主窗口
    root = tk.Tk()
    root.title("作息时间设置")
    root.geometry("320x250")

    tk.Label(root, text="请输入每日起床与睡觉时间", font=("微软雅黑", 12, "bold")).pack(pady=10)
    
    tk.Label(root, text="注意使用英文冒号").pack()
    tk.Label(root, text="起床时间 (如 07:30)：").pack()
    wake_entry = tk.Entry(root)
    wake_entry.pack(pady=5)

    tk.Label(root, text="睡觉时间 (如 23:30)：").pack()
    sleep_entry = tk.Entry(root)
    sleep_entry.pack(pady=5)

    tk.Button(root, text="确认", command=on_submit, bg="#4CAF50", fg="white").pack(pady=15)

    root.mainloop()

# ======================
# 调用函数
# ======================
if __name__ == "__main__":
    get_sleep_schedule()
    print("用户作息时间：", user_schedule)


