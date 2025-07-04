import os
import json
from typing import Dict, List, Any, Optional
from datetime import datetime
from pathlib import Path

from ai_providers import get_ai_provider
from document_parser import ResumeParser
from config import get_config

class CareerAgent:
    """AI-powered career assistance agent"""
    
    def __init__(self, provider_name: Optional[str] = None):
        self.ai_provider = get_ai_provider(provider_name)
        self.resume_parser = ResumeParser()
        self.config = get_config()
        self.resume_data = None
        
        # Ensure output directory exists
        os.makedirs(self.config.output_dir, exist_ok=True)
    
    def load_resume(self, file_path: Optional[str] = None) -> Dict[str, Any]:
        """Load and parse resume"""
        resume_path = file_path or self.config.resume_path
        
        if not os.path.exists(resume_path):
            raise FileNotFoundError(f"Resume file not found: {resume_path}")
        
        print(f"📄 Parsing resume: {resume_path}")
        self.resume_data = self.resume_parser.parse_resume(resume_path)
        
        return self.resume_data
    
    def analyze_resume(self, detailed: bool = True) -> str:
        """Analyze resume and provide feedback"""
        if not self.resume_data:
            self.load_resume()
        
        analysis_prompt = self._create_resume_analysis_prompt(detailed)
        
        messages = [
            {"role": "system", "content": "You are an expert career consultant and resume reviewer with deep knowledge of hiring practices across industries."},
            {"role": "user", "content": analysis_prompt}
        ]
        
        return self.ai_provider.generate_response(messages)
    
    def get_career_advice(self, query: str, context: Optional[str] = None) -> str:
        """Get personalized career advice"""
        if not self.resume_data:
            self.load_resume()
        
        advice_prompt = self._create_career_advice_prompt(query, context)
        
        messages = [
            {"role": "system", "content": "You are a senior career counselor with expertise in various industries. Provide practical, actionable advice tailored to the individual's background."},
            {"role": "user", "content": advice_prompt}
        ]
        
        return self.ai_provider.generate_response(messages)
    
    def optimize_resume_for_job(self, job_description: str) -> str:
        """Optimize resume for a specific job"""
        if not self.resume_data:
            self.load_resume()
        
        optimization_prompt = self._create_optimization_prompt(job_description)
        
        messages = [
            {"role": "system", "content": "You are an expert resume writer who specializes in tailoring resumes for specific job opportunities. Focus on highlighting relevant skills and experiences."},
            {"role": "user", "content": optimization_prompt}
        ]
        
        return self.ai_provider.generate_response(messages)
    
    def generate_cover_letter(self, job_description: str, company_name: str, additional_info: Optional[str] = None) -> str:
        """Generate a tailored cover letter"""
        if not self.resume_data:
            self.load_resume()
        
        cover_letter_prompt = self._create_cover_letter_prompt(job_description, company_name, additional_info)
        
        messages = [
            {"role": "system", "content": "You are an expert at writing compelling cover letters that showcase candidates' qualifications and enthusiasm for specific roles."},
            {"role": "user", "content": cover_letter_prompt}
        ]
        
        return self.ai_provider.generate_response(messages)
    
    def prepare_interview_questions(self, job_description: str, interview_type: str = "general") -> str:
        """Generate likely interview questions and answers"""
        if not self.resume_data:
            self.load_resume()
        
        interview_prompt = self._create_interview_prep_prompt(job_description, interview_type)
        
        messages = [
            {"role": "system", "content": "You are an experienced hiring manager and interview coach. Provide realistic interview questions and strategic answer guidance."},
            {"role": "user", "content": interview_prompt}
        ]
        
        return self.ai_provider.generate_response(messages)
    
    def suggest_skill_improvements(self, target_role: Optional[str] = None) -> str:
        """Suggest skills to develop"""
        if not self.resume_data:
            self.load_resume()
        
        skills_prompt = self._create_skills_improvement_prompt(target_role)
        
        messages = [
            {"role": "system", "content": "You are a career development expert who understands current market trends and skill demands across industries."},
            {"role": "user", "content": skills_prompt}
        ]
        
        return self.ai_provider.generate_response(messages)
    
    def save_output(self, content: str, filename: str) -> str:
        """Save output to file"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = os.path.join(self.config.output_dir, f"{timestamp}_{filename}")
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return output_path
    
    def _create_resume_analysis_prompt(self, detailed: bool) -> str:
        """Create prompt for resume analysis"""
        analysis_level = "detailed" if detailed else "summary"
        
        return f"""
Please provide a {analysis_level} analysis of this resume:

RESUME CONTENT:
{self.resume_data['raw_text']}

EXTRACTED INFORMATION:
Contact Info: {json.dumps(self.resume_data['contact_info'], indent=2)}
Skills: {', '.join(self.resume_data['skills'])}
Education: {self.resume_data['education']}
Experience: {self.resume_data['experience']}

Please analyze:
1. Overall structure and formatting
2. Content quality and relevance
3. Skills and qualifications presentation
4. Experience descriptions and impact
5. Areas for improvement
6. Strengths to highlight
7. ATS (Applicant Tracking System) optimization
8. Industry-specific recommendations

Provide actionable feedback and specific suggestions for improvement.
"""
    
    def _create_career_advice_prompt(self, query: str, context: Optional[str]) -> str:
        """Create prompt for career advice"""
        context_section = f"\nADDITIONAL CONTEXT: {context}" if context else ""
        
        return f"""
Based on this resume and career background, please provide advice for the following query:

QUERY: {query}

RESUME SUMMARY:
Skills: {', '.join(self.resume_data['skills'])}
Education: {self.resume_data['education']}
Experience: {self.resume_data['experience']}
{context_section}

Please provide:
1. Specific, actionable advice
2. Potential career paths or opportunities
3. Steps to achieve the goal
4. Resources or next actions to consider
5. Timeline considerations if applicable

Make the advice practical and tailored to their background.
"""
    
    def _create_optimization_prompt(self, job_description: str) -> str:
        """Create prompt for resume optimization"""
        return f"""
Please help optimize this resume for the following job opportunity:

JOB DESCRIPTION:
{job_description}

CURRENT RESUME:
{self.resume_data['raw_text']}

EXTRACTED SKILLS: {', '.join(self.resume_data['skills'])}

Please provide:
1. Key skills/keywords to emphasize from the job description
2. Specific resume sections to modify
3. Suggested rewording for better alignment
4. Additional skills or experiences to highlight
5. Content to add, modify, or remove
6. ATS optimization suggestions

Focus on making the resume more relevant while maintaining truthfulness.
"""
    
    def _create_cover_letter_prompt(self, job_description: str, company_name: str, additional_info: Optional[str]) -> str:
        """Create prompt for cover letter generation"""
        additional_section = f"\nADDITIONAL INFORMATION: {additional_info}" if additional_info else ""
        
        return f"""
Write a compelling cover letter for this job application:

COMPANY: {company_name}

JOB DESCRIPTION:
{job_description}

CANDIDATE BACKGROUND:
Skills: {', '.join(self.resume_data['skills'])}
Education: {self.resume_data['education']}
Experience: {self.resume_data['experience']}
Contact: {self.resume_data['contact_info']}
{additional_section}

Please create a cover letter that:
1. Addresses the specific role and company
2. Highlights relevant qualifications
3. Shows enthusiasm and cultural fit
4. Includes specific examples when possible
5. Has a professional yet engaging tone
6. Is appropriately formatted and length (3-4 paragraphs)

Make it compelling and personalized.
"""
    
    def _create_interview_prep_prompt(self, job_description: str, interview_type: str) -> str:
        """Create prompt for interview preparation"""
        return f"""
Help prepare for a {interview_type} interview for this position:

JOB DESCRIPTION:
{job_description}

CANDIDATE BACKGROUND:
Skills: {', '.join(self.resume_data['skills'])}
Education: {self.resume_data['education']}
Experience: {self.resume_data['experience']}

Please provide:
1. 10-15 likely interview questions specific to this role
2. Strategic answer frameworks for each question
3. Key points to emphasize from their background
4. Questions they should ask the interviewer
5. Potential weaknesses to address proactively
6. Examples/stories they should prepare
7. Technical questions if applicable

Focus on both behavioral and technical aspects relevant to the role.
"""
    
    def _create_skills_improvement_prompt(self, target_role: Optional[str]) -> str:
        """Create prompt for skills improvement suggestions"""
        target_section = f"TARGET ROLE: {target_role}" if target_role else "GENERAL CAREER GROWTH"
        
        return f"""
Suggest skill development priorities for career advancement:

{target_section}

CURRENT SKILLS: {', '.join(self.resume_data['skills'])}
CURRENT BACKGROUND:
Education: {self.resume_data['education']}
Experience: {self.resume_data['experience']}

Please provide:
1. Top 5 skills to develop or strengthen
2. Learning resources and methods for each skill
3. Timeline for skill development
4. How to demonstrate these skills
5. Market demand and career impact
6. Complementary skills to consider
7. Certification or formal training recommendations

Consider current market trends and future industry direction.
"""