from fpdf import FPDF


def create_resume(name, email, phone, skills, education, projects, experience):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, "RESUME", ln=True, align="C")

    pdf.ln(10)

    pdf.cell(200, 10, f"Name: {name}", ln=True)

    pdf.cell(200, 10, f"Email: {email}", ln=True)

    pdf.cell(200, 10, f"Phone: {phone}", ln=True)


    pdf.ln(5)

    pdf.cell(200, 10, "Skills:", ln=True)

    pdf.multi_cell(0, 10, skills)


    pdf.cell(200, 10, "Education:", ln=True)

    pdf.multi_cell(0, 10, education)


    pdf.cell(200, 10, "Projects:", ln=True)

    pdf.multi_cell(0, 10, projects)


    pdf.cell(200, 10, "Experience:", ln=True)

    pdf.multi_cell(0, 10, experience)


    file_name = "AI_Generated_Resume.pdf"

    pdf.output(file_name)

    return file_name