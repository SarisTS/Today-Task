import json
from fpdf import FPDF

with open('statement.json') as f:
    data = json.load(f)

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "Credit Card Statement", ln=True, align="C")
        self.ln(10)

pdf = PDF()
pdf.add_page()

# Card holder and details
pdf.set_font("Arial", size=12)
pdf.cell(0, 10, f"Card Holder: {data['card_holder']}", ln=True)
pdf.cell(0, 10, f"Card Number: {data['card_number']}", ln=True)
pdf.cell(0, 10, f"Statement Date: {data['statement_date']}", ln=True)
pdf.ln(10)

# Transaction table header
pdf.set_font("Arial", "B", 12)
pdf.cell(40, 10, "Date", border=1)
pdf.cell(100, 10, "Description", border=1)
pdf.cell(40, 10, "Amount", border=1, ln=True)

# Transaction rows
pdf.set_font("Arial", "", 12)
for txn in data['transactions']:
    pdf.cell(40, 10, txn["date"], border=1)
    pdf.cell(100, 10, txn["description"], border=1)
    pdf.cell(40, 10, f"${txn['amount']:.2f}", border=1, ln=True)

pdf.ln(10)
pdf.set_font("Arial", "B", 12)
pdf.cell(0, 10, f"Total Due: ${data['total_due']:.2f}", ln=True)

# Save the PDF
pdf.output("credit_card_statement.pdf")
