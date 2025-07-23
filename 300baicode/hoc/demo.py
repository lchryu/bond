import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Máy Tính Đơn Giản")
        self.window.geometry("300x400")
        self.window.resizable(False, False)
        
        # Biến lưu trữ
        self.current = "0"
        self.previous = ""
        self.operation = ""
        self.should_reset = False
        
        self.create_display()
        self.create_buttons()
        
    def create_display(self):
        # Màn hình hiển thị
        self.display_frame = tk.Frame(self.window, bg='black', height=80)
        self.display_frame.pack(fill='x', padx=5, pady=5)
        
        self.display = tk.Label(
            self.display_frame, 
            text=self.current,
            font=('Arial', 20, 'bold'),
            fg='white',
            bg='black',
            anchor='e',
            padx=10
        )
        self.display.pack(fill='both', expand=True)
        
    def create_buttons(self):
        # Frame chứa các nút
        button_frame = tk.Frame(self.window)
        button_frame.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Định nghĩa các nút
        buttons = [
            ['C', '±', '%', '÷'],
            ['7', '8', '9', '×'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=']
        ]
        
        # Màu sắc cho các loại nút
        colors = {
            'number': {'bg': '#333333', 'fg': 'white'},
            'operator': {'bg': '#ff9500', 'fg': 'white'},
            'function': {'bg': '#a6a6a6', 'fg': 'black'},
            'equals': {'bg': '#ff9500', 'fg': 'white'}
        }
        
        for i, row in enumerate(buttons):
            for j, btn_text in enumerate(row):
                if btn_text == '0':
                    # Nút 0 chiếm 2 cột
                    btn = tk.Button(
                        button_frame,
                        text=btn_text,
                        font=('Arial', 18, 'bold'),
                        command=lambda t=btn_text: self.button_click(t),
                        **colors['number']
                    )
                    btn.grid(row=i, column=j, columnspan=2, sticky='nsew', padx=1, pady=1)
                else:
                    # Xác định màu nút
                    if btn_text.isdigit() or btn_text == '.':
                        color = colors['number']
                    elif btn_text in ['C', '±', '%']:
                        color = colors['function']
                    elif btn_text == '=':
                        color = colors['equals']
                    else:
                        color = colors['operator']
                    
                    btn = tk.Button(
                        button_frame,
                        text=btn_text,
                        font=('Arial', 18, 'bold'),
                        command=lambda t=btn_text: self.button_click(t),
                        **color
                    )
                    # Nút = chiếm 2 hàng
                    if btn_text == '=':
                        btn.grid(row=i, column=j, rowspan=2, sticky='nsew', padx=1, pady=1)
                    else:
                        btn.grid(row=i, column=j, sticky='nsew', padx=1, pady=1)
        
        # Cấu hình grid
        for i in range(5):
            button_frame.grid_rowconfigure(i, weight=1)
        for j in range(4):
            button_frame.grid_columnconfigure(j, weight=1)
    
    def button_click(self, char):
        if char.isdigit():
            self.input_number(char)
        elif char == '.':
            self.input_decimal()
        elif char in ['÷', '×', '-', '+']:
            self.input_operation(char)
        elif char == '=':
            self.calculate()
        elif char == 'C':
            self.clear()
        elif char == '±':
            self.toggle_sign()
        elif char == '%':
            self.percentage()
    
    def input_number(self, num):
        if self.should_reset:
            self.current = "0"
            self.should_reset = False
            
        if self.current == "0":
            self.current = num
        else:
            self.current += num
        self.update_display()
    
    def input_decimal(self):
        if self.should_reset:
            self.current = "0"
            self.should_reset = False
            
        if '.' not in self.current:
            self.current += '.'
        self.update_display()
    
    def input_operation(self, op):
        if self.operation and not self.should_reset:
            self.calculate()
        
        self.previous = self.current
        self.operation = op
        self.should_reset = True
    
    def calculate(self):
        if not self.operation or not self.previous:
            return
            
        try:
            prev = float(self.previous)
            curr = float(self.current)
            
            if self.operation == '+':
                result = prev + curr
            elif self.operation == '-':
                result = prev - curr
            elif self.operation == '×':
                result = prev * curr
            elif self.operation == '÷':
                if curr == 0:
                    messagebox.showerror("Lỗi", "Không thể chia cho 0!")
                    return
                result = prev / curr
            
            # Làm tròn kết quả
            if result == int(result):
                self.current = str(int(result))
            else:
                self.current = str(round(result, 8))
            
            self.operation = ""
            self.previous = ""
            self.should_reset = True
            self.update_display()
            
        except Exception as e:
            messagebox.showerror("Lỗi", "Phép tính không hợp lệ!")
            self.clear()
    
    def clear(self):
        self.current = "0"
        self.previous = ""
        self.operation = ""
        self.should_reset = False
        self.update_display()
    
    def toggle_sign(self):
        if self.current != "0":
            if self.current.startswith('-'):
                self.current = self.current[1:]
            else:
                self.current = '-' + self.current
        self.update_display()
    
    def percentage(self):
        try:
            result = float(self.current) / 100
            if result == int(result):
                self.current = str(int(result))
            else:
                self.current = str(result)
            self.update_display()
        except:
            pass
    
    def update_display(self):
        # Giới hạn độ dài hiển thị
        display_text = self.current
        if len(display_text) > 12:
            display_text = display_text[:12]
        self.display.config(text=display_text)
    
    def run(self):
        # Bắt sự kiện phím
        self.window.bind('<Key>', self.key_press)
        self.window.focus_set()
        self.window.mainloop()
    
    def key_press(self, event):
        key = event.char
        if key.isdigit() or key in ['+', '-', '.', '=']:
            if key == '=':
                self.button_click('=')
            else:
                self.button_click(key)
        elif key in ['*', 'x', 'X']:
            self.button_click('×')
        elif key in ['/', ':']:
            self.button_click('÷')
        elif key in ['\r', '\n']:  # Enter
            self.button_click('=')
        elif key in ['\x08', '\x7f']:  # Backspace, Delete
            self.button_click('C')

if __name__ == "__main__":
    calc = Calculator()
    calc.run()