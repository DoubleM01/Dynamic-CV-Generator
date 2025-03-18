import tkinter as tk
from tkinter import filedialog, ttk
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import json

# Functions
## back up json for futrther editing
def save_backup(data):
    file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[["JSON files", "*.json"]])
    if file_path:
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
        status_label.config(text=f"Backup saved at {file_path}", fg="green")

def load_backup():
    file_path = filedialog.askopenfilename(defaultextension=".json", filetypes=[["JSON files", "*.json"]])
    if file_path:
        with open(file_path, "r") as file:
            data = json.load(file)
        name_entry.delete(0, tk.END)
        name_entry.insert(0, data["name"])
        email_entry.delete(0, tk.END)
        email_entry.insert(0, data["email"])
        phone_entry.delete(0, tk.END)
        phone_entry.insert(0, data["phone"])
        address_entry.delete(0, tk.END)
        address_entry.insert(0, data["address"])
        linkedin_entry.delete(0, tk.END)
        linkedin_entry.insert(0, data["linkedin"])
        github_entry.delete(0, tk.END)
        github_entry.insert(0, data["github"])
        profile_text.delete("1.0", tk.END)
        profile_text.insert(tk.END, data["profile_summary"])
        skills_text.delete("1.0", tk.END)
        skills_text.insert(tk.END, data["skills"])
        education_text.delete("1.0", tk.END)
        education_text.insert(tk.END, data["education"])
        certificates_text.delete("1.0", tk.END)
        certificates_text.insert(tk.END, data["certificates"])
        for i, exp in enumerate(data["experiences"]):
            experience_entries[i]["job"].delete(0, tk.END)
            experience_entries[i]["job"].insert(0, exp[0])
            experience_entries[i]["company"].delete(0, tk.END)
            experience_entries[i]["company"].insert(0, exp[1])
            experience_entries[i]["location"].delete(0, tk.END)
            experience_entries[i]["location"].insert(0, exp[2])
            experience_entries[i]["date"].delete(0, tk.END)
            experience_entries[i]["date"].insert(0, exp[3])
            experience_entries[i]["summary"].delete("1.0", tk.END)
            experience_entries[i]["summary"].insert(tk.END, exp[4])
        for i, proj in enumerate(data["projects"]):
            project_entries[i]["title"].delete(0, tk.END)
            project_entries[i]["title"].insert(0, proj[0])
            project_entries[i]["description"].delete("1.0", tk.END)
            project_entries[i]["description"].insert(tk.END, proj[1])
            
        status_label.config(text=f"Backup loaded successfully from {file_path}", fg="green")

def prepare_pdf(file_path, data:dict):
    # init 
    doc = SimpleDocTemplate(file_path, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()

    # Title
    elements.append(Paragraph(f"<b><font-size: 20px color: blue{data['name']}</font>  </b>", styles["Title"]))
    elements.append(Spacer(1, 12))

    # Personal Information
    elements.append(Paragraph("<b>Personal Information</b>", styles["Heading2"]))
    elements.append(Paragraph(f"Name: {data['name']}", styles["BodyText"]))
    elements.append(Paragraph(f"Email: {data['email']}", styles["BodyText"]))
    elements.append(Paragraph(f"Phone: {data['phone']}", styles["BodyText"]))
    elements.append(Paragraph(f"Address: {data['address']}", styles["BodyText"]))
    if data["linkedin"]:
        elements.append(Paragraph(f"LinkedIn: {data['linkedin']}", styles["BodyText"]))
    if data["github"]:
        elements.append(Paragraph(f"GitHub: {data['github']}", styles["BodyText"]))
    elements.append(Spacer(1, 12))

    # Profile Summary
    elements.append(Paragraph("<b>Profile Summary</b>", styles["Heading2"]))
    elements.append(Paragraph(data["profile_summary"], styles["BodyText"]))
    elements.append(Spacer(1, 12))

    # Experience
    elements.append(Paragraph("<b>Experience</b>", styles["Heading2"]))
    for job_title, company, location, date, summary in data["experiences"]:
        elements.append(Paragraph(f"<b>{job_title}</b>", styles["Heading3"]))
        elements.append(Paragraph(f"<i>{company} | {location} | {date}</i>", styles["BodyText"]))
        elements.append(Paragraph(summary, styles["BodyText"]))
        elements.append(Spacer(1, 12))
    
    # skills
    elements.append(Paragraph("<b>Skills</b>", styles["Heading2"]))
    for skill in data["skills"].split("\n"):
        elements.append(Paragraph(f"• {skill.strip()}", styles["BodyText"]))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph("<b>Education</b>", styles["Heading2"]))
    
    # Education
    for edu in data["education"].split("\n"):
        elements.append(Paragraph(f"• {edu.strip()}", styles["BodyText"]))
    elements.append(Spacer(1, 12))

    # Certificates
    elements.append(Paragraph("<b>Certificates</b>", styles["Heading2"]))
    for cert in data["certificates"].split("\n"):
        elements.append(Paragraph(f"• {cert.strip()}", styles["BodyText"]))

    # Build PDF
    doc.build(elements)
    
def generate_cv():
    # Get user input
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    address = address_entry.get()
    linkedin = linkedin_entry.get().strip()
    github = github_entry.get().strip()
    profile_summary = profile_text.get("1.0", tk.END).strip()
    skills = skills_text.get("1.0", tk.END).strip()
    education = education_text.get("1.0", tk.END).strip()
    certificates = certificates_text.get("1.0", tk.END).strip()
    
    # Experience Data
    experiences = []
    for exp in experience_entries:
        job_title = exp["job"].get()
        company = exp["company"].get()
        location = exp["location"].get()
        date = exp["date"].get()
        summary = exp["summary"].get("1.0", tk.END).strip()
        
        if job_title and company:
            experiences.append((job_title, company, location, date, summary))
    
    # Projects Data
    projects = []
    for proj in project_entries:
        project_title = proj["title"].get()
        project_description = proj["description"].get("1.0", tk.END).strip()
        
        if project_title:
            projects.append((project_title, project_description))

    # Ask user for save location
    file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[["PDF files", "*.pdf"]])
    if not file_path:
        return

    data = {
        "name": name,
        "email": email,
        "phone": phone,
        "address": address,
        "linkedin": linkedin,
        "github": github,
        "profile_summary": profile_summary,
        "skills": skills,
        "education": education,
        "certificates": certificates,
        "experiences": experiences,
        "projects": projects,}
    prepare_pdf(file_path, data)
    status_label.config(text=f"CV saved successfully at {file_path}", fg="green")

# GUI Setup
root = tk.Tk()
root.title("Dynamic CV Generator")
root.geometry("600x700")

canvas_frame = tk.Canvas(root)
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas_frame.yview)
scrollable_frame = ttk.Frame(canvas_frame)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas_frame.configure(
        scrollregion=canvas_frame.bbox("all")
    )
)

canvas_window = canvas_frame.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas_frame.configure(yscrollcommand=scrollbar.set)

# Labels and Entry Fields
tk.Label(scrollable_frame, text="Full Name:").pack()
name_entry = tk.Entry(scrollable_frame, width=50)
name_entry.pack()

tk.Label(scrollable_frame, text="Email:").pack()
email_entry = tk.Entry(scrollable_frame, width=50)
email_entry.pack()

tk.Label(scrollable_frame, text="Phone:").pack()
phone_entry = tk.Entry(scrollable_frame, width=50)
phone_entry.pack()

tk.Label(scrollable_frame, text="Address:").pack()
address_entry = tk.Entry(scrollable_frame, width=50)
address_entry.pack()

tk.Label(scrollable_frame, text="LinkedIn:").pack()
linkedin_entry = tk.Entry(scrollable_frame, width=50)
linkedin_entry.pack()

tk.Label(scrollable_frame, text="GitHub:").pack()
github_entry = tk.Entry(scrollable_frame, width=50)
github_entry.pack()

tk.Label(scrollable_frame, text="Profile Summary:").pack()
profile_text = tk.Text(scrollable_frame, width=50, height=3)
profile_text.pack()

tk.Label(scrollable_frame, text="Experience:").pack()
experience_entries = []
for _ in range(3):
    frame = tk.Frame(scrollable_frame)
    frame.pack()
    tk.Label(frame, text="Job Title:").grid(row=0, column=0)
    job_entry = tk.Entry(frame, width=30)
    job_entry.grid(row=0, column=1)
    tk.Label(frame, text="Company:").grid(row=1, column=0)
    company_entry = tk.Entry(frame, width=30)
    company_entry.grid(row=1, column=1)
    tk.Label(frame, text="Location:").grid(row=2, column=0)
    location_entry = tk.Entry(frame, width=30)
    location_entry.grid(row=2, column=1)
    tk.Label(frame, text="Date:").grid(row=3, column=0)
    date_entry = tk.Entry(frame, width=30)
    date_entry.grid(row=3, column=1)
    tk.Label(frame, text="Summary:").grid(row=4, column=0)
    summary_text = tk.Text(frame, width=40, height=3)
    summary_text.grid(row=4, column=1)
    experience_entries.append({"job": job_entry, "company": company_entry, "location": location_entry, "date": date_entry, "summary": summary_text})

canvas_frame.pack(side="left", fill="both", expand=True)




canvas_frame.pack(side="left", fill="both", expand=True)
tk.Label(scrollable_frame, text="Skills:").pack()
skills_text = tk.Text(scrollable_frame, width=50, height=3)
skills_text.pack()

tk.Label(scrollable_frame, text="Education:").pack()
education_text = tk.Text(scrollable_frame, width=50, height=3)
education_text.pack()

tk.Label(scrollable_frame, text="Certificates:").pack()
certificates_text = tk.Text(scrollable_frame, width=50, height=3)
certificates_text.pack()
# project_entries
tk.Label(scrollable_frame, text="Projects:").pack()
project_entries = []
for _ in range(3):
    frame = tk.Frame(scrollable_frame)
    frame.pack()
    tk.Label(frame, text="Title:").grid(row=0, column=0)
    title_entry = tk.Entry(frame, width=30)
    title_entry.grid(row=0, column=1)
    tk.Label(frame, text="Description:").grid(row=1, column=0)
    description_text = tk.Text(frame, width=40, height=3)
    description_text.grid(row=1, column=1)
    project_entries.append({"title": title_entry, "description": description_text})
# Generate CV Button
generate_button = tk.Button(scrollable_frame, text="Generate CV", command=generate_cv, bg="blue", fg="white")
generate_button.pack(pady=10)

# Backup and Load Buttons
ButtonFrame = tk.Frame(scrollable_frame)
ButtonFrame.pack()
backup_button = tk.Button(ButtonFrame, text="Save Backup", command=lambda: save_backup({
    "name": name_entry.get(),
    "email": email_entry.get(),
    "phone": phone_entry.get(),
    "address": address_entry.get(),
    "linkedin": linkedin_entry.get(),
    "github": github_entry.get(),
    "profile_summary": profile_text.get("1.0", tk.END),
    "skills": skills_text.get("1.0", tk.END),
    "education": education_text.get("1.0", tk.END),
    "certificates": certificates_text.get("1.0", tk.END),
    "experiences": [(exp["job"].get(), exp["company"].get(), exp["location"].get(), exp["date"].get(), exp["summary"].get("1.0", tk.END)) for exp in experience_entries],
    "projects": [(proj["title"].get(), proj["description"].get("1.0", tk.END)) for proj in project_entries]
}))
backup_button.pack(side="left")

load_backup_button = tk.Button(ButtonFrame, text="Load Backup", command=load_backup, bg="green", fg="white")
load_backup_button.pack(side="right")

# Status Label
status_label = tk.Label(scrollable_frame, text="", fg="red")
status_label.pack()
scrollbar.pack(side="right", fill="y")
root.mainloop()



