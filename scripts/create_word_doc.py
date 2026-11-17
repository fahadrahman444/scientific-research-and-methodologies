import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

doc = docx.Document()

# Document Title
title = doc.add_heading('How XGBoost Works in Our Research', level=0)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER

subtitle = doc.add_paragraph('A Simple, Minimal & Plain-English Guide for Presentation & Viva Defense')
subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
subtitle.runs[0].font.italic = True
subtitle.runs[0].font.size = Pt(11)

doc.add_paragraph()

# Section 1
doc.add_heading('1. The Big Picture: What is XGBoost?', level=1)
p1 = doc.add_paragraph(
    'XGBoost stands for eXtreme Gradient Boosting. Think of it as a team of 180 students working together on an exam:\n\n'
    '• Student 1 (Tree 1): Makes a first guess at crop yield. It gets some things right, but makes a few mistakes.\n'
    '• Student 2 (Tree 2): Does NOT start from scratch. It looks only at the mistakes of Student 1 and tries to fix them.\n'
    '• Student 3 (Tree 3): Looks at what Student 1 and 2 still got wrong, and fixes that.\n'
    '• This chain continues 180 times in a row (n_estimators = 180).\n\n'
    'By the end, all small corrections are combined into one highly accurate final prediction. This sequential learning process is called Boosting.'
)

# Section 2
doc.add_heading('2. How Does a Single Tree Work on Our Weather Data?', level=1)
p2 = doc.add_paragraph(
    'In our model, a tree is simply a chain of YES or NO questions about the weather in Bangladesh:\n\n'
    'Question 1: Were there 12.5 or more Heat Stress Days (>= 35°C) this year?\n'
    '   --> YES: Rice flowers were heat-shocked! Subtract 220 kg/ha from yield.\n'
    '   --> NO: Go to Question 2.\n\n'
    'Question 2: Was there a 3-month drought (SPI-3 < -1.0)?\n'
    '   --> YES: Subtract 140 kg/ha from yield.\n'
    '   --> NO: Add +95 kg/ha (favorable harvest conditions).\n\n'
    'Because decision trees split data using sharp cutoffs, they naturally capture biological tipping points that linear formulas miss completely.'
)

# Section 3
doc.add_heading('3. What Makes XGBoost "Extreme" & Superior?', level=1)
p3 = doc.add_paragraph(
    '1. Focuses on the Hardest Years (Gradient Descent):\n'
    'If the model makes a large error on a sudden flood or cyclone year, the next tree specifically works to correct that exact error.\n\n'
    '2. Small, Steady Steps (Learning Rate = 0.06):\n'
    'Each tree only contributes 6% of its opinion. This prevents the model from overreacting to single extreme events.\n\n'
    '3. Built-in Brakes (Max Depth = 5 & Regularization):\n'
    'Each tree is capped at 5 questions deep. This prevents the model from memorizing noise (overfitting) and ensures it learns genuine biological rules.'
)

# Section 4
doc.add_heading('4. Why XGBoost Won Over Other Models', level=1)
table = doc.add_table(rows=1, cols=3)
table.style = 'Light Shading Accent 1'
hdr_cells = table.rows[0].cells
hdr_cells[0].text = 'Model Architecture'
hdr_cells[1].text = 'Test R² Score'
hdr_cells[2].text = 'Why It Won / Lost'

rows_data = [
    ('Linear Ridge Regression', '0.812', 'Failed because it assumes crop yield responds in a straight line; cannot capture 35°C heat tipping point.'),
    ('Random Forest', '0.895', 'Built trees independently in parallel; does not learn sequentially from previous mistakes.'),
    ('PyTorch LSTM', '0.918', 'Deep neural networks require huge datasets; on 15 years of tabular numbers, tree ensembles are more robust.'),
    ('XGBoost (WINNER)', '0.941', 'Highest accuracy (98.65%, MAPE 1.35%) because it sequentially corrects errors and handles sharp biological thresholds.')
]

for model, r2, reason in rows_data:
    row_cells = table.add_row().cells
    row_cells[0].text = model
    row_cells[1].text = r2
    row_cells[2].text = reason

doc.add_paragraph()

# Section 5
doc.add_heading('5. The 20-Second Presentation Summary', level=1)
p5 = doc.add_paragraph(
    'If your examiner asks: "How does XGBoost work in your paper?", say this:\n\n'
    '"XGBoost builds an ensemble of 180 small decision trees in a sequence. Rather than predicting independently, each tree focuses exclusively on correcting the prediction errors made by the previous trees. By splitting data on simple YES/NO questions (such as whether heat stress days crossed 12.5 days), it captures non-linear biological thresholds that straight-line regression models completely miss."'
)
p5.runs[0].font.italic = True

doc.save('docs/HOW_XGBOOST_WORKS_EASY_GUIDE.docx')
print('Word document saved successfully to docs/HOW_XGBOOST_WORKS_EASY_GUIDE.docx')
