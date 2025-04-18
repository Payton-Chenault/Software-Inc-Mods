import customtkinter as ctk

class ModCreatorApp:
    def __init__(self, root: ctk.CTk):
        self.root = root
        self._setup_window()
        self._create_sidebar()
        self._create_main_area()

        self.frames = {}
        self.sub_feature_dropdowns = []
        self.create_frames()

        self._create_sidebar_buttons()
        self.show_frame("Software Type")

    def _setup_window(self):
        self.root.geometry("1500x800")
        self.root.title("Software Inc. Mod Creator")
        self.root.resizable(True, True)
        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("red.json")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

    def _create_sidebar(self):
        self.sidebar = ctk.CTkFrame(self.root, width=250, corner_radius=0)
        self.sidebar.grid(row=0, column=0, rowspan=4, sticky="nsew", padx=5, pady=5)
        self.sidebar.grid_rowconfigure(99, weight=1)

        self.sidebar_label = ctk.CTkLabel(
            self.sidebar, text="🧩 Mod Sections", font=ctk.CTkFont(size=22, weight="bold")
        )
        self.sidebar_label.grid(row=0, column=0, padx=20, pady=(25, 10), sticky="ew")

    def _create_main_area(self):
        self.main_frame_container = ctk.CTkFrame(self.root, corner_radius=15)
        self.main_frame_container.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.main_frame_container.grid_rowconfigure(0, weight=1)
        self.main_frame_container.grid_columnconfigure(0, weight=1)

    def _create_sidebar_buttons(self):
        self.buttons = {
            "Software Type": ctk.CTkButton(self.sidebar, text="Software Type", command=lambda: self.show_frame("Software Type")),
            "Spec Features": ctk.CTkButton(self.sidebar, text="Spec Features", command=lambda: self.show_frame("Spec Features")),
            "Sub Features": ctk.CTkButton(self.sidebar, text="Sub Features", command=lambda: self.show_frame("Sub Features")),
            "Export": ctk.CTkButton(self.sidebar, text="Export Mod", command=lambda: self.show_frame("Export")),
        }

        for i, (_, button) in enumerate(self.buttons.items(), start=1):
            button.grid(row=i, column=0, padx=20, pady=5, sticky="ew")

    def create_frames(self):
        self.frames["Software Type"] = self.create_input_frame("Software Type", {
            "Software Name": "Software Name",
            "Description": "Description",
            "Unlock Year": "Year",
            "Random": "Sales Weight (0-1)",
            "Ideal Price": "Price",
            "Optimal Dev Time": "Months",
            "Popularity": "Max Customer Multiplier (0-1)",
            "Retention": "Months",
            "Iterative": "(0-1)",
            "OS Supports": "True, False, or specific os eg Computer",
            "Contract Software": "True False",
            "In House Software": "True False",
            "Name Generator": "File Name",
            "Submarket Name One": "",
            "Submarket Name Two": "",
            "Submarket Name Three": ""
        })
        self.frames["Spec Features"] = self.create_spec_features_frame()
        self.frames["Sub Features"] = self.create_sub_features_frame()
        self.frames["Export"] = self.create_export_frame()

        for frame in self.frames.values():
            frame.grid(row=0, column=0, sticky="nsew")

    def create_input_frame(self, title, fields):
        frame = ctk.CTkFrame(self.main_frame_container, corner_radius=15)

        title_label = ctk.CTkLabel(frame, text=title, font=ctk.CTkFont(size=20, weight="bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(20, 10))

        for i, (label_text, entry_placeholder) in enumerate(fields.items(), start=1):
            ctk.CTkLabel(frame, text=f"{label_text}:", anchor="e", font=ctk.CTkFont(size=14)).grid(
                row=i, column=0, padx=15, pady=5, sticky="e"
            )
            entry = ctk.CTkEntry(frame, placeholder_text=entry_placeholder, width=300)
            entry.grid(row=i, column=1, padx=10, pady=5, sticky="ew")

        frame.grid_columnconfigure(1, weight=1)
        return frame

    def create_spec_features_frame(self):
        frame = ctk.CTkFrame(self.main_frame_container, corner_radius=15)
        ctk.CTkLabel(frame, text="Spec Features", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=(20, 10))

        self.spec_feature_scroll_frame = ctk.CTkScrollableFrame(frame, orientation="horizontal", width=900, height=300)
        self.spec_feature_scroll_frame.pack(padx=10, pady=5, fill="both", expand=True)

        self.spec_feature_rows = []
        self.add_spec_feature_row()

        ctk.CTkButton(frame, text="+", width=30, command=self.add_spec_feature_row).pack(pady=15, anchor="w", padx=20)
        return frame

    def add_spec_feature_row(self):
        row_index = len(self.spec_feature_rows)
        labels = [
            "Name", "Spec", "Description", "Dependencies", "Unlock",
            "DevTime", "Submarkets 1", "Submarket 2", "Submarket 3", "Code Art", "Server", "Optional", "Software Categories"
        ]
        entries = []

        for col, label in enumerate(labels):
            entry = ctk.CTkEntry(self.spec_feature_scroll_frame, placeholder_text=label, width=120)
            entry.grid(row=row_index, column=col, padx=5, pady=2)
            entries.append(entry)

        # Set up name trace for dynamic dropdown update
        entries[0].bind("<FocusOut>", lambda e: self.update_sub_feature_dropdowns())

        self.spec_feature_rows.append(entries)
        self.update_sub_feature_dropdowns()

    def create_sub_features_frame(self):
        frame = ctk.CTkFrame(self.main_frame_container, corner_radius=15)
        ctk.CTkLabel(frame, text="Sub Features", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=(20, 10))

        self.sub_feature_scroll_frame = ctk.CTkScrollableFrame(frame, orientation="horizontal", width=900, height=300)
        self.sub_feature_scroll_frame.pack(padx=10, pady=5, fill="both", expand=True)

        self.sub_feature_rows = []
        ctk.CTkButton(frame, text="+", width=30, command=self.add_sub_feature_row).pack(pady=15, anchor="w", padx=20)

        self.add_sub_feature_row()
        return frame

    def add_sub_feature_row(self):
        row_index = len(self.sub_feature_rows)
        labels = [
            "Name", "Description", "Level", "Unlock", "Dev Time",
            "Submarket 1", "Submarket 2", "Submarket 3", "Code Art", "Server", "Software Categories", "Software Feature"
        ]
        entries = []

        for col, label in enumerate(labels):
            if label == "Level":
                entry = ctk.CTkOptionMenu(self.sub_feature_scroll_frame, values=["1", "2"])
            elif label == "Software Feature":
                entry = ctk.CTkOptionMenu(self.sub_feature_scroll_frame, values=[""])
                self.sub_feature_dropdowns.append(entry)
            else:
                entry = ctk.CTkEntry(self.sub_feature_scroll_frame, placeholder_text=label, width=120)

            entry.grid(row=row_index, column=col, padx=5, pady=2)
            entries.append(entry)

        self.sub_feature_rows.append(entries)
        self.update_sub_feature_dropdowns()

    def update_sub_feature_dropdowns(self):
        feature_names = [row[0].get() for row in self.spec_feature_rows if row[0].get().strip()]
        for dropdown in self.sub_feature_dropdowns:
            dropdown.configure(values=feature_names or [""])

    def create_export_frame(self):
        frame = ctk.CTkFrame(self.main_frame_container, corner_radius=15)
        ctk.CTkLabel(frame, text="Export Mod", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=30)
        ctk.CTkButton(frame, text="Export to File", command=self.export_mod).pack(pady=10)
        return frame

    def export_mod(self):
        print("Exporting mod...")  # Placeholder

    def show_frame(self, name):
        frame = self.frames.get(name)
        if frame:
            frame.tkraise()


if __name__ == "__main__":
    root = ctk.CTk()
    app = ModCreatorApp(root)
    root.mainloop()
