import sys
import random
import re
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QFormLayout,
    QLabel, QLineEdit, QCheckBox, QPushButton, QStackedLayout,
    QFrame, QScrollArea, QGridLayout
)
from PyQt5.QtCore import Qt

class LowballGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('LOW - Lowballer\'s Optimal Workflow')
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.resize(700, 380)
        self.move(40, 40)
        self.setStyleSheet("""
            QWidget { 
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                            stop:0 #1f1f1f, stop:1 #2e2e2e);
                border: 2px solid #000;
                border-radius: 10px;
            }
            QLabel#title { 
                color: #b3b3b3;
                font: bold 22px 'Consolas';
            }
            QLabel { 
                color: #dddddd;
                font: 12px 'Consolas';
            }
            QLineEdit { 
                background: #101010;
                color: #dddddd;
                padding: 6px;
                border: 1px solid #7d8282;
                border-radius: 4px;
                font: 12px 'Consolas';
            }
            QPushButton { 
                background: #7d8282;
                color: dddddd;
                border: 1px solid #7d8282;
                border-radius: 6px;
                padding: 10px 16px;
                font: bold 12px 'Consolas';
            }
            QPushButton:hover { 
                background: #9ca1a1;
            }
            QCheckBox { 
                color: #7d8282;
                font: 12px 'Consolas';
            }
        """)

        self.stacked = QStackedLayout(self)
        self.init_input_page()
        self.init_result_page()

    def init_input_page(self):
        page = QFrame()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(18)

        title = QLabel('Lowball Message Generator', objectName='title')
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        form = QFormLayout()
        self.purse_input = QLineEdit(); self.purse_input.setPlaceholderText('Default: 200m')
        self.min_input = QLineEdit(); self.min_input.setPlaceholderText('Default: 25m')
        form.addRow(' Purse: ', self.purse_input)
        form.addRow(' Min: ', self.min_input)
        layout.addLayout(form)

        cb_layout = QGridLayout()
        cb_layout.setAlignment(Qt.AlignCenter)
        self.checkboxes = []
        labels = ['No Attributes', 'No Dyes', 'No Minions', 'Lvl 100 Pets']
        for i, label in enumerate(labels):
            cb = QCheckBox(label)
            cb_layout.addWidget(cb, i // 2, i % 2)
            self.checkboxes.append(cb)
        layout.addLayout(cb_layout)

        layout.addStretch()
        buttons = QHBoxLayout()
        buttons.addStretch()
        gen_btn = QPushButton('Generate Messages')
        quit_btn = QPushButton('Quit')
        gen_btn.clicked.connect(self.generate_messages)
        quit_btn.clicked.connect(QApplication.instance().quit)
        buttons.addWidget(gen_btn)
        buttons.addWidget(quit_btn)
        buttons.addStretch()
        layout.addLayout(buttons)

        self.stacked.addWidget(page)

    def init_result_page(self):
        page = QFrame()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(20, 20, 20, 20)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.container = QFrame()
        self.message_layout = QVBoxLayout(self.container)
        self.message_layout.setSpacing(10)

        self.copy_buttons = []
        self.message_edits = []

        for _ in range(5):
            row = QHBoxLayout()
            copy_btn = QPushButton('Copy')
            copy_btn.setFixedWidth(80)
            line = QLineEdit()
            line.setReadOnly(True)
            line.setCursorPosition(0)
            line.setAlignment(Qt.AlignLeft)

            def make_handler(btn, edit):
                return lambda: self.copy_to_clipboard(btn, edit)

            copy_btn.clicked.connect(make_handler(copy_btn, line))

            row.addWidget(copy_btn)
            row.addWidget(line)

            self.copy_buttons.append(copy_btn)
            self.message_edits.append(line)
            self.message_layout.addLayout(row)

        self.scroll_area.setWidget(self.container)
        layout.addWidget(self.scroll_area)

        nav_buttons = QHBoxLayout()
        self.back_btn = QPushButton('Back')
        self.more_btn = QPushButton('More')

        self.back_btn.clicked.connect(self.go_back)
        self.more_btn.clicked.connect(self.generate_messages)

        nav_buttons.addStretch()
        nav_buttons.addWidget(self.back_btn)
        nav_buttons.addWidget(self.more_btn)
        nav_buttons.addStretch()

        layout.addLayout(nav_buttons)
        self.stacked.addWidget(page)

    def copy_to_clipboard(self, button, line_edit):
        QApplication.clipboard().setText(line_edit.text())
        button.setText("✓")

    def go_back(self):
        for btn in self.copy_buttons:
            btn.setText("Copy")
        self.stacked.setCurrentIndex(0)

    def parse_amount(self, text):
        match = re.match(r"([0-9]+(?:\.[0-9]+)?)([kmb]?)", text.lower().strip())
        if not match:
            return None
        num, suffix = float(match.group(1)), match.group(2)
        return int(num * {'': 1, 'k': 1e3, 'm': 1e6, 'b': 1e9}[suffix])

    def generate_messages(self):
        purse_raw = self.purse_input.text() or "200m"
        min_raw = self.min_input.text() or "25m"
        purse = self.parse_amount(purse_raw)
        minimum = self.parse_amount(min_raw)
        if purse is None or minimum is None:
            return

        for btn in self.copy_buttons:
            btn.setText("Copy")

        flags = [cb.text() for cb in self.checkboxes if cb.isChecked()]
        flag_strs = {
            "bar": " | ".join(flags),
            "dash": " - ".join(flags),
            "slash": " / ".join(flags),
            "plus": " + ".join(flags),
            "dot": " • ".join(flags),
            "space": " ".join(flags),
        }

        if flags:
            templates = [
                f"LOWBALLING {purse_raw} | Min: {min_raw} | {flag_strs['bar']} | VISIT ME",
                f"LOWBALLING {purse_raw} → Min Value: {min_raw} → No: {flag_strs['dash']} → Come now!",
                f"LOWBALLING {purse_raw} Purse | Min Price: {min_raw} | Conditions: {flag_strs['plus']} | /visit",
                f"LOWBALLING {purse_raw} with items worth {min_raw}+ | {flag_strs['slash']} | VISIT MY ISLAND",
                f"LOWBALLING {purse_raw} - Taking {min_raw}+ items - Skipping: {flag_strs['bar']} - Trade quick!",
                f"LOWBALLING {purse_raw} – Min {min_raw} – Avoiding: {flag_strs['dot']} – Let’s go!",
                f"LOWBALLING {purse_raw} | Accepting {min_raw}+ value only | Skipping {flag_strs['space']} | /visit",
                f"LOWBALLING {purse_raw} Purse → {min_raw}+ item value → No {flag_strs['bar']} → Come by now!",
            ]
        else:
            templates = [
                f"LOWBALLING {purse_raw} | Min: {min_raw} | VISIT ME",
                f"LOWBALLING {purse_raw} → Min Value: {min_raw} → Come now!",
                f"LOWBALLING {purse_raw} Purse | Min Price: {min_raw} | /visit",
                f"LOWBALLING {purse_raw} with items worth {min_raw}+ | VISIT MY ISLAND",
                f"LOWBALLING {purse_raw} - Taking items priced {min_raw}+ - Fair offers!",
                f"LOWBALLING {purse_raw} – Need {min_raw}+ gear – Come trade now!",
                f"LOWBALLING {purse_raw} Purse → Looking for {min_raw}+ items → Visit!",
                f"LOWBALLING {purse_raw} | Only {min_raw}+ items | Fast deals, /visit!",
            ]

        extras = ["", "!", " — fast trades", " — visit now", " — don't miss it", " — quick deals", " — no junk pls"]
        selected = set()
        while len(selected) < 5:
            selected.add(random.choice(templates) + random.choice(extras))

        for line_edit, message in zip(self.message_edits, list(selected)):
            line_edit.setText(message)
            line_edit.setCursorPosition(0)

        self.stacked.setCurrentIndex(1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LowballGenerator()
    window.show()
    sys.exit(app.exec_())
