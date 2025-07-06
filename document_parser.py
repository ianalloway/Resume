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
    def parse_document(file_path: str) -> str:
        """Parse document based on file extension"""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        file_extension = Path(file_path).suffix.lower()
        
        if file_extension == '.pdf':
            return DocumentParser.extract_text_from_pdf(file_path)
        elif file_extension == '.docx':
            return DocumentParser.extract_text_from_docx(file_path)
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
            'summary': r'(?i)(summary|profile|objective|about)',
            'experience': r'(?i)(experience|employment|work history|professional experience)',
            'education': r'(?i)(education|academic|qualifications)',
            'skills': r'(?i)(skills|competencies|technical skills|expertise)',
            'projects': r'(?i)(projects|portfolio)',
            'certifications': r'(?i)(certifications|certificates|licenses)',
            'achievements': r'(?i)(achievements|awards|honors|accomplishments)'
        }
        
        lines = text.split('\n')
        current_section = None
        section_content = []
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            # Check if line is a section header
            for section_name, pattern in section_patterns.items():
                if re.search(pattern, line) and len(line) < 50:
                    if current_section and section_content:
                        sections[current_section] = '\n'.join(section_content)
                    current_section = section_name
                    section_content = []
                    break
            else:
                if current_section:
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
        
        return contact_info
    
    def _extract_skills(self, text: str) -> list:
        """Extract skills from resume"""
        # This is a basic implementation - in practice, you'd use NLP or a skills database
        common_skills = [
            'Python', 'Java', 'JavaScript', 'C++', 'C#', 'SQL', 'HTML', 'CSS',
            'React', 'Angular', 'Vue', 'Node.js', 'Django', 'Flask', 'Spring',
            'AWS', 'Azure', 'GCP', 'Docker', 'Kubernetes', 'Git', 'Linux',
            'Machine Learning', 'Data Science', 'AI', 'Deep Learning',
            'Project Management', 'Agile', 'Scrum', 'Leadership', 'Communication'
        ]
        
        found_skills = []
        text_upper = text.upper()
        
        for skill in common_skills:
            if skill.upper() in text_upper:
                found_skills.append(skill)
        
        return found_skills
    
    def _extract_education(self, text: str) -> list:
        """Extract education information"""
        education = []
        
        # Degree patterns
        degree_patterns = [
            r'(?i)(bachelor|b\.?s\.?|b\.?a\.?|bs|ba)',
            r'(?i)(master|m\.?s\.?|m\.?a\.?|ms|ma|mba)',
            r'(?i)(phd|ph\.?d\.?|doctorate|doctoral)',
            r'(?i)(associate|a\.?s\.?|as)'
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
            r'(?i)(engineer|developer|manager|analyst|director|consultant|specialist)',
            r'(?i)(software|senior|junior|lead|principal|staff)'
        ]
        
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if len(line) > 10 and len(line) < 100:  # Reasonable length for job titles
                for pattern in job_patterns:
                    if re.search(pattern, line):
                        experience.append(line)
                        break
        
        return experience