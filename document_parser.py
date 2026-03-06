import os
from typing import Optional, Dict, Any
import PyPDF2
from docx import Document
from pathlib import Path
import re


class DocumentParser:
    """Parser for various document formats"""

    @staticmethod
    def extract_text_from_pdf(file_path: str) -> str:
        """Extract text from PDF file"""
        try:
            with open(file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text() + "\n"
                return text.strip()
        except Exception as e:
            raise Exception(f"Error reading PDF file: {str(e)}")

    @staticmethod
    def extract_text_from_docx(file_path: str) -> str:
        """Extract text from Word document"""
        try:
            doc = Document(file_path)
            text = ""
            for paragraph in doc.paragraphs:
                text += paragraph.text + "\n"
            return text.strip()
        except Exception as e:
            raise Exception(f"Error reading Word document: {str(e)}")

    @staticmethod
    def extract_text_from_txt(file_path: str) -> str:
        """Extract text from text file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read().strip()
        except Exception as e:
            raise Exception(f"Error reading text file: {str(e)}")

    @staticmethod
    def extract_text_from_tex(file_path: str) -> str:
        """Extract readable text from LaTeX file by stripping commands"""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            # Remove comments
            content = re.sub(r'%.*$', '', content, flags=re.MULTILINE)
            # Remove preamble (everything before \begin{document})
            match = re.search(r'\\begin\{document\}', content)
            if match:
                content = content[match.end():]
            content = re.sub(r'\\end\{document\}', '', content)
            # Remove common LaTeX commands but keep their text arguments
            content = re.sub(r'\\(?:textbf|textit|emph|underline|href\{[^}]*\})\{([^}]*)\}', r'\1', content)
            content = re.sub(r'\\(?:LARGE|Large|large|small|tiny|huge|Huge|bfseries|scshape)\b', '', content)
            # Remove environments
            content = re.sub(r'\\begin\{[^}]*\}(?:\[[^\]]*\])?', '', content)
            content = re.sub(r'\\end\{[^}]*\}', '', content)
            # Remove other commands
            content = re.sub(r'\\(?:vspace|hfill|hspace|titlerule|titleformat|titlespacing|setlength|pagestyle|definecolor|hypersetup|usepackage|newcommand)\b[^\\]*?(?=\n|\\)', '', content)
            content = re.sub(r'\\(?:section|subsection)\*?\{([^}]*)\}', r'\n\1\n', content)
            content = re.sub(r'\\resumeitem\{([^}]*)\}', r'- \1', content)
            content = re.sub(r'\\item\[?[^\]]*\]?', '- ', content)
            # Clean up remaining LaTeX artifacts
            content = re.sub(r'\\\$', '$', content)
            content = re.sub(r'\\[a-zA-Z]+\*?(?:\{[^}]*\})?', '', content)
            content = re.sub(r'[{}]', '', content)
            content = re.sub(r'\$\\vert\$', '|', content)
            content = re.sub(r'\\,', ' ', content)
            content = re.sub(r'\\\\', '\n', content)
            content = re.sub(r'~', ' ', content)
            # Clean up whitespace
            content = re.sub(r'\n{3,}', '\n\n', content)
            content = re.sub(r'[ \t]+', ' ', content)
            return content.strip()
        except Exception as e:
            raise Exception(f"Error reading LaTeX file: {str(e)}")

    @staticmethod
    def parse_document(file_path: str) -> str:
        """Parse document based on file extension"""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        file_extension = Path(file_path).suffix.lower()

        if file_extension == '.pdf':
            return DocumentParser.extract_text_from_pdf(file_path)
        elif file_extension == '.docx':
            return DocumentParser.extract_text_from_docx(file_path)
        elif file_extension == '.tex':
            return DocumentParser.extract_text_from_tex(file_path)
        elif file_extension in ['.txt', '.md']:
            return DocumentParser.extract_text_from_txt(file_path)
        else:
            raise ValueError(f"Unsupported file format: {file_extension}")


class ResumeParser:
    """Specialized parser for resume analysis"""

    def __init__(self):
        self.document_parser = DocumentParser()

    def parse_resume(self, file_path: str) -> Dict[str, Any]:
        """Parse resume and extract structured information"""
        text = self.document_parser.parse_document(file_path)

        # Basic information extraction using regex patterns
        parsed_data = {
            'raw_text': text,
            'sections': self._extract_sections(text),
            'contact_info': self._extract_contact_info(text),
            'skills': self._extract_skills(text),
            'education': self._extract_education(text),
            'experience': self._extract_experience(text)
        }

        return parsed_data

    def _extract_sections(self, text: str) -> Dict[str, str]:
        """Extract different sections from resume"""
        sections = {}

        # Common section headers
        section_patterns = {
            'summary': r'(?i)^(summary|profile|objective|about)\s*$',
            'experience': r'(?i)^(experience|employment|work history|professional experience)\s*$',
            'education': r'(?i)^(education|academic|qualifications)\s*$',
            'skills': r'(?i)^(skills|competencies|technical skills|expertise)\s*$',
            'projects': r'(?i)^(projects|portfolio)\s*$',
            'certifications': r'(?i)^(certifications?|certificates|licenses)\s*$',
            'achievements': r'(?i)^(achievements|awards|honors|accomplishments)\s*$',
            'open_source': r'(?i)^(open\s*source|contributions?)\s*$',
            'writing': r'(?i)^(writing|publications?|blog)\s*$',
        }

        lines = text.split('\n')
        current_section = None
        section_content = []

        for line in lines:
            line = line.strip()
            if not line:
                continue

            # Check if line is a section header
            matched = False
            for section_name, pattern in section_patterns.items():
                if re.search(pattern, line):
                    if current_section and section_content:
                        sections[current_section] = '\n'.join(section_content)
                    current_section = section_name
                    section_content = []
                    matched = True
                    break

            if not matched and current_section:
                section_content.append(line)

        # Add the last section
        if current_section and section_content:
            sections[current_section] = '\n'.join(section_content)

        return sections

    def _extract_contact_info(self, text: str) -> Dict[str, str]:
        """Extract contact information"""
        contact_info = {}

        # Email pattern
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        email_match = re.search(email_pattern, text)
        if email_match:
            contact_info['email'] = email_match.group()

        # Phone pattern
        phone_pattern = r'(\+?1?[-.\s]?)?\(?([0-9]{3})\)?[-.\s]?([0-9]{3})[-.\s]?([0-9]{4})'
        phone_match = re.search(phone_pattern, text)
        if phone_match:
            contact_info['phone'] = phone_match.group()

        # LinkedIn pattern
        linkedin_pattern = r'linkedin\.com/in/[\w-]+'
        linkedin_match = re.search(linkedin_pattern, text, re.IGNORECASE)
        if linkedin_match:
            contact_info['linkedin'] = linkedin_match.group()

        # GitHub pattern
        github_pattern = r'github\.com/[\w-]+'
        github_match = re.search(github_pattern, text, re.IGNORECASE)
        if github_match:
            contact_info['github'] = github_match.group()

        return contact_info

    def _extract_skills(self, text: str) -> list:
        """Extract skills from resume using word-boundary matching"""
        common_skills = [
            # Languages
            'Python', 'R', 'SQL', 'TypeScript', 'JavaScript', 'Solidity',
            # ML / AI
            'TensorFlow', 'TensorFlow.js', 'PyTorch', 'Scikit-learn', 'XGBoost',
            'Deep Learning', 'NLP', 'Computer Vision', 'YOLOv8', 'COCO-SSD',
            # Data
            'Pandas', 'NumPy', 'Power BI', 'Tableau', 'Statistical Analysis',
            'Time Series Forecasting',
            # Web3
            'Ethereum', 'Smart Contracts', 'Blockchain Analytics',
            'Web3.js', 'Ethers.js',
            # Infrastructure
            'Docker', 'Git', 'AWS', 'PostgreSQL', 'Redis',
            'React', 'Node.js', 'FastAPI', 'Tailwind CSS',
            # Autonomy
            'MAVLink', 'PX4', 'ArduPilot', 'Sensor Fusion', 'EKF',
            # General
            'Machine Learning', 'Data Science', 'Project Management',
            'Agile', 'Scrum', 'Leadership', 'Communication',
        ]

        found_skills = []
        for skill in common_skills:
            # Use word-boundary matching to avoid false positives
            pattern = r'(?<![a-zA-Z])' + re.escape(skill) + r'(?![a-zA-Z])'
            if re.search(pattern, text, re.IGNORECASE):
                found_skills.append(skill)

        return found_skills

    def _extract_education(self, text: str) -> list:
        """Extract education information"""
        education = []

        # Degree patterns
        degree_patterns = [
            r'(?i)\b(bachelor|b\.?s\.?|b\.?a\.?)\b',
            r'(?i)\b(master|m\.?s\.?|m\.?a\.?|mba)\b',
            r'(?i)\b(ph\.?d\.?|doctorate|doctoral)\b',
            r'(?i)\b(associate|a\.?s\.?)\b',
            r'(?i)\b(diploma)\b',
        ]

        lines = text.split('\n')
        for line in lines:
            for pattern in degree_patterns:
                if re.search(pattern, line):
                    education.append(line.strip())
                    break

        return education

    def _extract_experience(self, text: str) -> list:
        """Extract work experience"""
        experience = []

        # Look for job titles and company patterns
        job_patterns = [
            r'(?i)\b(engineer|developer|manager|analyst|director|consultant|specialist)\b',
            r'(?i)\b(founder|auditor|scientist|architect|lead|principal|staff)\b',
        ]

        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if 10 < len(line) < 100:
                for pattern in job_patterns:
                    if re.search(pattern, line):
                        experience.append(line)
                        break

        return experience
