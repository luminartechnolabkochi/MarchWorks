# Trying again to generate the PDF with the "Ground Rent Paid" date (20th April) included

from fpdf import FPDF

# Data
members = [
    [1, 'surej', 'paid', 80, 0, 0],
    [2, 'sajay', 'paid', 80, 0, 0],
    [3, 'anoopeattan', 'paid', 80, 0, 0],
    [4, 'sandeepattan', 'paid', 80, 0, 0],
    [5, 'rahul', 'paid', 80, 0, 0],
    [6, 'suneesh', 'paid', 80, 0, 0],
    [7, 'vyshak', 'paid', 80, 0, 0],
    [8, 'kuttucheattan', 'paid', 80, 0, 0],
    [9, 'aneeshettan', 'paid', 100, 0, 0],
    [10, 'vyshnav', 'paid', 80, 0, 0],
    [11, 'ajaydas', 'not paid', 80, 2, 140]
]

summary = {
    "Total Received": 820,
    "Previous Balance": 250,
    "Grand Total": 1070,
    "Ground Rent Paid": 600,
    "Current Balance": 470
}

# PDF class
class CustomPDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, 'Payment Report', 0, 1, 'C')
        self.ln(5)

    def section_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(2)

    def table_header(self, headers):
        self.set_font('Arial', 'B', 10)
        for header in headers:
            self.cell(32, 8, header, border=1)
        self.ln()

    def table_row(self, data, is_unpaid=False):
        self.set_font('Arial', '', 10)
        if is_unpaid:
            self.set_fill_color(255, 0, 0)  # Red background
        else:
            self.set_fill_color(255, 255, 255)  # White background
        for item in data:
            self.cell(32, 8, str(item), border=1, fill=True)
        self.ln()

# Generate PDF
pdf = CustomPDF()
pdf.add_page()

# Player Contribution Section
pdf.section_title('Player Contribution')
pdf.table_header(['#', 'Name', 'Status', 'Amount', 'Pending Count', 'Pending Amount'])
for member in members:
    is_unpaid = member[2].lower() == 'not paid'
    pdf.table_row(member, is_unpaid=is_unpaid)

# Expenses Section
pdf.ln(10)
pdf.section_title('Expenses')
pdf.set_font('Arial', '', 12)
pdf.cell(0, 10, f'Ground Rent Paid: {summary["Ground Rent Paid"]} (on 20th April)', ln=True)

# Summary Section
pdf.ln(10)
pdf.section_title('Summary')
pdf.set_font('Arial', '', 12)
pdf.cell(0, 10, f'Total Received: {summary["Total Received"]}', ln=True)
pdf.cell(0, 10, f'Previous Balance: {summary["Previous Balance"]}', ln=True)
pdf.cell(0, 10, f'Grand Total: {summary["Grand Total"]}', ln=True)
pdf.cell(0, 10, f'Current Balance: {summary["Current Balance"]}', ln=True)

# Save PDF
output_pdf_path = './payment_report_20th_april.pdf'
pdf.output(output_pdf_path)

output_pdf_path
