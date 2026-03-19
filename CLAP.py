import customtkinter as ctk
import requests
import os
import string
import random
import threading

# --- Settings ---
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
CACHE_FILE = "top_10m_passwords.txt"
URL = "https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Passwords/Common-Credentials/Pwdb_top-10000000.txt"

class PasswordApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window Setup
        self.title("CLAP v1.0")
        self.geometry("500x450") 
        self.resizable(False, False)

        # --- Header ---
        self.header_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.header_frame.pack(pady=20, padx=20, fill="x")

        self.label = ctk.CTkLabel(self.header_frame, text="CLAP", font=("Impact", 36), text_color="#1f538d")
        self.label.pack()
        self.sub_label = ctk.CTkLabel(self.header_frame, text="Credential Leak Analysis Program", font=("Roboto", 12))
        self.sub_label.pack()

        # --- Input Area ---
        self.entry = ctk.CTkEntry(self, placeholder_text="Enter password...", width=320, height=40, show="*")
        self.entry.pack(pady=10)

        self.show_pass_var = ctk.BooleanVar(value=False)
        self.show_pass_check = ctk.CTkCheckBox(self, text="Show Plaintext", font=("Roboto", 11),
                                               variable=self.show_pass_var, command=self.toggle_password)
        self.show_pass_check.pack(pady=5)

        # --- Main Controls ---
        self.check_button = ctk.CTkButton(self, text="START ANALYSIS", font=("Roboto", 14, "bold"),
                                          height=45, width=200, fg_color="#1f538d", hover_color="#14375e",
                                          command=self.start_check_thread)
        self.check_button.pack(pady=15)

        # --- Console Toggle ---
        self.details_enabled = ctk.BooleanVar(value=False)
        self.detail_switch = ctk.CTkSwitch(self, text="Live Console Stream(Slower)", font=("Roboto", 12),
                                           variable=self.details_enabled, command=self.toggle_console_view)
        self.detail_switch.pack(pady=10)

        # --- The Console (Hidden by default) ---
        self.console = ctk.CTkTextbox(self, width=460, height=180, font=("Courier", 12), 
                                      text_color="#00FF41", fg_color="#0a0a0a", border_width=1, border_color="#1f538d")

        # --- Dynamic Status Label ---
        self.result_label = ctk.CTkLabel(self, text="STATUS: SYSTEM READY", font=("Roboto", 13, "bold"))
        self.result_label.pack(pady=15)

        # Footer Actions
        self.footer = ctk.CTkFrame(self, fg_color="transparent")
        self.footer.pack(side="bottom", pady=10)
        
        self.gen_btn = ctk.CTkButton(self.footer, text="Generate", width=80, height=24, fg_color="#333", command=self.generate_ui)
        self.gen_btn.pack(side="left", padx=5)
        
        self.clear_btn = ctk.CTkButton(self.footer, text="Wipe Cache", width=80, height=24, fg_color="#333", command=self.clear_cache)
        self.clear_btn.pack(side="left", padx=5)

    def toggle_console_view(self):
        if self.details_enabled.get():
            self.geometry("500x680")
            self.console.pack(pady=10, before=self.result_label)
            self.write_to_console("--- CONSOLE STREAM INITIALIZED ---")
        else:
            self.console.pack_forget()
            self.geometry("500x420")

    def write_to_console(self, message):
        self.console.configure(state="normal")
        self.console.insert("end", f"> {message}\n")
        self.console.see("end")
        self.console.configure(state="disabled")

    def toggle_password(self):
        self.entry.configure(show="" if self.show_pass_var.get() else "*")

    def generate_ui(self):
        pool = string.ascii_letters + string.digits + string.punctuation
        new_p = "".join(random.choice(pool) for _ in range(16))
        self.entry.delete(0, 'end')
        self.entry.insert(0, new_p)
        self.result_label.configure(text="NEW PASSWORD GENERATED", text_color="cyan")
        if self.details_enabled.get():
            self.write_to_console(f"KEY_GEN: {new_p}")

    def clear_cache(self):
        if os.path.exists(CACHE_FILE):
            os.remove(CACHE_FILE)
            self.result_label.configure(text="Cache has been deleted", text_color="orange")
        else:
            self.result_label.configure(text="Cache is empty", text_color="white")

    def start_check_thread(self):
        self.check_button.configure(state="disabled")
        threading.Thread(target=self.check_password, daemon=True).start()

    def check_password(self):
        target = self.entry.get()
        if not target:
            self.result_label.configure(text="ERROR: NO INPUT", text_color="red")
            self.check_button.configure(state="normal")
            return

        # 1. Download Status
        if not os.path.exists(CACHE_FILE):
            self.result_label.configure(text="DOWNLOADING SECLIST WORDLIST...", text_color="yellow")
            self.write_to_console("Requesting external database...")
            try:
                r = requests.get(URL, timeout=30)
                with open(CACHE_FILE, "w", encoding="utf-8") as f: f.write(r.text)
                self.write_to_console("Download complete.")
            except:
                self.result_label.configure(text="CONNECTION FAILED", text_color="red")
                self.check_button.configure(state="normal")
                return

        # 2. Analyzing Status
        self.result_label.configure(text=f"ANALYZING: {target}", text_color="yellow")
        self.write_to_console(f"Running heuristic scan on '{target}'")

        try:
            with open(CACHE_FILE, "r", encoding="utf-8", errors="ignore") as f:
                wordlist = f.read().splitlines()

            found = False
            for i, p in enumerate(wordlist):
                if self.details_enabled.get() and i % 100000 == 0:
                    self.write_to_console(f"COMPARING: {p}")
                
                if p == target:
                    found = True
                    break

            # 3. Final Result & Recommendation
            if found:
                self.write_to_console(f"MATCH FOUND: {target}")
                self.result_label.configure(
                    text="COMPROMISED! (Recomended: Generate a secure password)", 
                    text_color="#ff4444"
                )
            else:
                self.write_to_console("No leaks detected in database.")
                self.result_label.configure(text="STATUS: SAFE", text_color="#44ff44")
            
        except Exception as e:
            self.result_label.configure(text="SYSTEM ERROR", text_color="red")
            self.write_to_console(f"FATAL: {e}")
        
        self.check_button.configure(state="normal")

if __name__ == "__main__":
    app = PasswordApp()
    app.mainloop()