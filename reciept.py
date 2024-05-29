from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Receipt', align='C', ln=True)
        self.cell(0, 10, '', ln=True)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def generate_receipt(customer_name, items_purchased, total_amount, receipt_number, output_path):
    pdf = PDF()
    pdf.add_page()

    # Set font
    pdf.set_font("Arial", size=12)

    # Add receipt details
    pdf.cell(200, 10, txt="Receipt Number: " + receipt_number, ln=True)
    pdf.cell(200, 10, txt="Customer Name: " + customer_name, ln=True)
    pdf.cell(200, 10, txt="Items Purchased:", ln=True)
    for item in items_purchased:
        pdf.cell(200, 10, txt="- " + item, ln=True)
    pdf.cell(200, 10, txt="Total Amount: ${:.2f}".format(total_amount), ln=True)

    # Save the PDF
    pdf.output(output_path)

# Example usage
customer_name = "Ayla Ki"
items_purchased = ["Ramen", "Loreal shampoo", "Detan facemask"]
total_amount = 100.50
receipt_number = "070605"
output_path = "receipt.pdf"
generate_receipt(customer_name, items_purchased, total_amount, receipt_number, output_path)
