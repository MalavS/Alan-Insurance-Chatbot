import tkinter as tk
from tkinter import messagebox

class AlanChatbot:
    def __init__(self, root):
        self.root = root
        self.root.title("🤖 Alan Insurance Advisor")
        self.root.geometry("950x750")
        self.root.configure(bg='#0f172a')
        self.root.resizable(False, False)
        
        self.current_step = "welcome"
        self.user_data = {}
        self.setup_ui()
    
    def setup_ui(self):
        # Header
        header = tk.Frame(self.root, bg='#1e293b', height=120)
        header.pack(fill=tk.X, pady=(0, 30))
        header.pack_propagate(False)
        
        title = tk.Label(header, text="🤖 Alan Insurance Advisor", 
                        font=('Segoe UI', 28, 'bold'), bg='#1e293b', fg='#60a5fa')
        title.pack(pady=25)
        
        subtitle = tk.Label(header, text="AI-Powered Bear & Marmot Plan Recommendations", 
                           font=('Segoe UI', 14), bg='#1e293b', fg='#cbd5e1')
        subtitle.pack(pady=(0, 15))
        
        # Main container
        main_frame = tk.Frame(self.root, bg='#0f172a')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=50, pady=20)
        
        # Result display
        self.result_frame = tk.Frame(main_frame, bg='#1e293b', relief=tk.RAISED, bd=2)
        self.result_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 30))
        
        self.result_title = tk.Label(self.result_frame, text="", font=('Segoe UI', 16, 'bold'), 
                                   bg='#1e293b', fg='#f8fafc')
        self.result_title.pack(pady=20)
        
        self.result_text = tk.Label(self.result_frame, text="", font=('Segoe UI', 12), 
                                  bg='#1e293b', fg='#e2e8f0', wraplength=750, justify=tk.LEFT)
        self.result_text.pack(pady=10, padx=30)
        
        # Buttons frame
        self.btn_frame = tk.Frame(main_frame, bg='#0f172a')
        self.btn_frame.pack(pady=20)
    
    def show_welcome(self):
        self.current_step = "welcome"
        self.result_title.config(text="🏥 Welcome to Alan Insurance!")
        self.result_text.config(text="""Choose your situation below for instant AI-powered recommendations:

**Individual Plans:**
• Bear - Basic coverage (Rx, dental, paramedical, vision)
• Marmot - Comprehensive (everything + semi-private rooms)

**Business Group Plans:**
• 20% cheaper than brokers
• Instant digital enrollment
• Perfect for Canadian SMBs (1-500 employees)

**Built by Malav Shah | Alan Internship Q3**""")
        
        self.show_main_buttons()
    
    def show_main_buttons(self):
        for widget in self.btn_frame.winfo_children():
            widget.destroy()
        
        # Row 1: Individual
        row1 = tk.Frame(self.btn_frame, bg='#0f172a')
        row1.pack(pady=15)
        
        tk.Button(row1, text="👤 Individual\n(Employed)", command=lambda: self.individual("employed"),
                 bg='#3b82f6', fg='white', font=('Segoe UI', 14, 'bold'), 
                 relief=tk.FLAT, padx=50, pady=20, height=3).pack(side=tk.LEFT, padx=20)
        tk.Button(row1, text="👤 Individual\n(Self-Employed)", command=lambda: self.individual("self-employed"),
                 bg='#06b6d4', fg='white', font=('Segoe UI', 14, 'bold'), 
                 relief=tk.FLAT, padx=50, pady=20, height=3).pack(side=tk.LEFT, padx=20)
        
        # Row 2: Business
        row2 = tk.Frame(self.btn_frame, bg='#0f172a')
        row2.pack(pady=15)
        
        tk.Button(row2, text="🏢 Small Business\n(1-49 employees)", command=lambda: self.business(25),
                 bg='#10b981', fg='white', font=('Segoe UI', 14, 'bold'), 
                 relief=tk.FLAT, padx=50, pady=20, height=3).pack(side=tk.LEFT, padx=20)
        tk.Button(row2, text="🏢 Mid-Size\n(50-500 employees)", command=lambda: self.business(150),
                 bg='#f59e0b', fg='white', font=('Segoe UI', 14, 'bold'), 
                 relief=tk.FLAT, padx=50, pady=20, height=3).pack(side=tk.LEFT, padx=20)
        
        # Custom
        tk.Button(self.btn_frame, text="⚙️ Custom\nEmployee Count", command=self.show_custom,
                 bg='#8b5cf6', fg='white', font=('Segoe UI', 14, 'bold'), 
                 relief=tk.FLAT, padx=60, pady=20, height=3).pack(pady=20)
    
    def individual(self, status):
        self.current_step = "individual"
        
        if status == "employed":
            self.result_title.config(text="👤 Individual (Employed)", fg='#3b82f6')
            self.result_text.config(text="""**🎯 PERFECT MATCH: ALAN MARMOT PLAN**

✅ **Comprehensive Coverage**
• Prescription drugs + paramedical (physio, massage, chiro)  
• Dental (checkups, cleanings, major procedures)
• Vision coverage + prescription glasses
• Semi-private hospital accommodation

✅ **Why Marmot for employed individuals:**
• Higher coverage limits than Bear
• Perfect for comprehensive family protection
• Fast app-based reimbursements

📅 **Next: Book your Marmot demo call today!**""")
        else:
            self.result_title.config(text="👤 Individual (Self-Employed)", fg='#06b6d4')
            self.result_text.config(text="""**🎯 PERFECT MATCH: ALAN BEAR PLAN**

✅ **Essential Coverage**
• Prescription drugs
• Paramedical (physio, massage, chiro)  
• Dental (checkups, cleanings)
• Vision coverage

✅ **Why Bear for self-employed:**
• Affordable monthly premiums
• No employment restrictions
• Instant digital enrollment

📅 **Next: Get your Bear plan quote instantly!**""")
        
        self.show_action_buttons()
    
    def business(self, employees):
        self.current_step = "business"
        
        if employees <= 49:
            self.result_title.config(text=f"🏢 Small Business ({employees} employees)", fg='#10b981')
            self.result_text.config(text="""**🎯 PERFECT MATCH: ALAN BEAR GROUP PLAN**

✅ **Group Benefits (1-49 employees)**
• Prescription drugs, paramedical, dental
• Vision coverage for all employees
• 20% CHEAPER than traditional brokers

✅ **Why Bear Group Plan:**
• Instant online enrollment (no brokers!)
• Flexible monthly payments
• Perfect for Canadian tech startups & SMBs

💰 **Save 20% vs brokers + zero paperwork**

📅 **Next: Book your group demo today!**""")
        else:
            self.result_title.config(text=f"🏢 Mid-Size Business ({employees} employees)", fg='#f59e0b')
            self.result_text.config(text="""**🎯 PERFECT MATCH: ALAN MARMOT GROUP PLAN**

✅ **Enhanced Group Benefits (50-500 employees)**
• Everything in Bear + higher limits
• Semi-private hospital rooms
• Customizable coverage options

✅ **Why Marmot Group:**
• Perfect for growing Canadian companies
• Comprehensive employee benefits package
• 20% savings vs traditional brokers

💰 **Enterprise-grade coverage at SMB prices**

📅 **Next: Schedule your custom group quote!**""")
        
        self.show_action_buttons()
    
    def show_custom(self):
        self.current_step = "custom"
        for widget in self.btn_frame.winfo_children():
            widget.destroy()
        
        tk.Label(self.btn_frame, text="🏢 Enter your employee count (1-500):", 
                font=('Segoe UI', 16, 'bold'), bg='#0f172a', fg='#f1f5f9').pack(pady=30)
        
        entry_frame = tk.Frame(self.btn_frame, bg='#0f172a')
        entry_frame.pack(pady=20)
        
        self.emp_entry = tk.Entry(entry_frame, font=('Segoe UI', 18), width=8, 
                                 justify=tk.CENTER, relief=tk.FLAT, bg='#1e293b', fg='#f1f5f9')
        self.emp_entry.pack(pady=10)
        self.emp_entry.insert(0, "25")
        
        tk.Button(self.btn_frame, text="🎯 Get My AI Recommendation", command=self.process_custom,
                 bg='#ef4444', fg='white', font=('Segoe UI', 16, 'bold'), 
                 relief=tk.FLAT, padx=60, pady=20, height=3).pack(pady=30)
        
        tk.Button(self.btn_frame, text="← Back to Main Menu", command=self.show_welcome,
                 bg='#6b7280', fg='white', font=('Segoe UI', 14, 'bold'), 
                 relief=tk.FLAT, padx=50, pady=15).pack(pady=10)
    
    def process_custom(self):
        try:
            employees = int(self.emp_entry.get())
            if 1 <= employees <= 500:
                self.business(employees)
            else:
                messagebox.showerror("Invalid Input", "Please enter 1-500 employees")
        except:
            messagebox.showerror("Invalid Input", "Please enter a valid number")
    
    def show_action_buttons(self):
        for widget in self.btn_frame.winfo_children():
            widget.destroy()
        
        tk.Button(self.btn_frame, text="📅 Book Demo Call", 
                 command=lambda: messagebox.showinfo("Success", "Demo booked! Sales team will contact you within 24h."),
                 bg='#10b981', fg='white', font=('Segoe UI', 14, 'bold'), 
                 relief=tk.FLAT, padx=60, pady=20, height=3).pack(pady=15)
        
        tk.Button(self.btn_frame, text="🔄 New Recommendation", command=self.show_welcome,
                 bg='#3b82f6', fg='white', font=('Segoe UI', 14, 'bold'), 
                 relief=tk.FLAT, padx=60, pady=20, height=3).pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = AlanChatbot(root)
    app.show_welcome()
    root.mainloop()
