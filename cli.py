#!/usr/bin/env python3
import click
import os
import sys
from typing import Optional
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.table import Table
from rich.prompt import Prompt

from career_agent import CareerAgent
from config import get_config

console = Console()

@click.group()
@click.option('--provider', type=click.Choice(['openai', 'anthropic']), help='AI provider to use')
@click.option('--config-file', help='Path to configuration file')
@click.pass_context
def cli(ctx, provider, config_file):
    """🚀 Career Agent - Your AI-powered career assistant"""
    ctx.ensure_object(dict)
    ctx.obj['provider'] = provider
    ctx.obj['config_file'] = config_file

@cli.command()
@click.option('--resume-path', help='Path to resume file')
@click.option('--detailed/--summary', default=True, help='Detailed or summary analysis')
@click.option('--save', is_flag=True, help='Save analysis to file')
@click.pass_context
def analyze(ctx, resume_path, detailed, save):
    """📊 Analyze your resume and get improvement suggestions"""
    try:
        agent = CareerAgent(ctx.obj['provider'])
        
        if resume_path:
            agent.load_resume(resume_path)
        else:
            agent.load_resume()
        
        with console.status("[bold green]Analyzing resume..."):
            analysis = agent.analyze_resume(detailed=detailed)
        
        console.print(Panel(
            Markdown(analysis),
            title="📊 Resume Analysis",
            border_style="blue"
        ))
        
        if save:
            output_path = agent.save_output(analysis, "resume_analysis.md")
            console.print(f"💾 Analysis saved to: {output_path}")
            
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {str(e)}")

@cli.command()
@click.argument('query')
@click.option('--context', help='Additional context for the advice')
@click.option('--save', is_flag=True, help='Save advice to file')
@click.pass_context
def advice(ctx, query, context, save):
    """💡 Get personalized career advice"""
    try:
        agent = CareerAgent(ctx.obj['provider'])
        
        with console.status("[bold green]Generating career advice..."):
            advice_text = agent.get_career_advice(query, context)
        
        console.print(Panel(
            Markdown(advice_text),
            title="💡 Career Advice",
            border_style="green"
        ))
        
        if save:
            output_path = agent.save_output(advice_text, "career_advice.md")
            console.print(f"💾 Advice saved to: {output_path}")
            
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {str(e)}")

@cli.command()
@click.option('--job-file', help='Path to file containing job description')
@click.option('--save', is_flag=True, help='Save optimized resume to file')
@click.pass_context
def optimize(ctx, job_file, save):
    """🎯 Optimize your resume for a specific job"""
    try:
        if job_file and os.path.exists(job_file):
            with open(job_file, 'r', encoding='utf-8') as f:
                job_description = f.read()
        else:
            console.print("📝 Please paste the job description (press Ctrl+D when done):")
            job_description = sys.stdin.read()
        
        if not job_description.strip():
            console.print("[bold red]Error:[/bold red] No job description provided")
            return
        
        agent = CareerAgent(ctx.obj['provider'])
        
        with console.status("[bold green]Optimizing resume..."):
            optimization = agent.optimize_resume_for_job(job_description)
        
        console.print(Panel(
            Markdown(optimization),
            title="🎯 Resume Optimization",
            border_style="yellow"
        ))
        
        if save:
            output_path = agent.save_output(optimization, "resume_optimization.md")
            console.print(f"💾 Optimization saved to: {output_path}")
            
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {str(e)}")

@cli.command()
@click.option('--job-file', help='Path to file containing job description')
@click.option('--company', prompt=True, help='Company name')
@click.option('--additional-info', help='Additional information to include')
@click.option('--save', is_flag=True, help='Save cover letter to file')
@click.pass_context
def cover_letter(ctx, job_file, company, additional_info, save):
    """✉️ Generate a tailored cover letter"""
    try:
        if job_file and os.path.exists(job_file):
            with open(job_file, 'r', encoding='utf-8') as f:
                job_description = f.read()
        else:
            console.print("📝 Please paste the job description (press Ctrl+D when done):")
            job_description = sys.stdin.read()
        
        if not job_description.strip():
            console.print("[bold red]Error:[/bold red] No job description provided")
            return
        
        agent = CareerAgent(ctx.obj['provider'])
        
        with console.status("[bold green]Generating cover letter..."):
            letter = agent.generate_cover_letter(job_description, company, additional_info)
        
        console.print(Panel(
            Markdown(letter),
            title="✉️ Cover Letter",
            border_style="cyan"
        ))
        
        if save:
            output_path = agent.save_output(letter, f"cover_letter_{company.replace(' ', '_')}.md")
            console.print(f"💾 Cover letter saved to: {output_path}")
            
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {str(e)}")

@cli.command()
@click.option('--job-file', help='Path to file containing job description')
@click.option('--type', 'interview_type', default='general', 
              type=click.Choice(['general', 'technical', 'behavioral', 'panel']),
              help='Type of interview')
@click.option('--save', is_flag=True, help='Save interview prep to file')
@click.pass_context
def interview(ctx, job_file, interview_type, save):
    """🎤 Prepare for job interviews"""
    try:
        if job_file and os.path.exists(job_file):
            with open(job_file, 'r', encoding='utf-8') as f:
                job_description = f.read()
        else:
            console.print("📝 Please paste the job description (press Ctrl+D when done):")
            job_description = sys.stdin.read()
        
        if not job_description.strip():
            console.print("[bold red]Error:[/bold red] No job description provided")
            return
        
        agent = CareerAgent(ctx.obj['provider'])
        
        with console.status("[bold green]Preparing interview questions..."):
            prep = agent.prepare_interview_questions(job_description, interview_type)
        
        console.print(Panel(
            Markdown(prep),
            title="🎤 Interview Preparation",
            border_style="magenta"
        ))
        
        if save:
            output_path = agent.save_output(prep, f"interview_prep_{interview_type}.md")
            console.print(f"💾 Interview prep saved to: {output_path}")
            
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {str(e)}")

@cli.command()
@click.option('--target-role', help='Target role or career direction')
@click.option('--save', is_flag=True, help='Save skills suggestions to file')
@click.pass_context
def skills(ctx, target_role, save):
    """📚 Get skill development suggestions"""
    try:
        agent = CareerAgent(ctx.obj['provider'])
        
        with console.status("[bold green]Analyzing skill development opportunities..."):
            suggestions = agent.suggest_skill_improvements(target_role)
        
        console.print(Panel(
            Markdown(suggestions),
            title="📚 Skill Development Suggestions",
            border_style="yellow"
        ))
        
        if save:
            output_path = agent.save_output(suggestions, "skill_suggestions.md")
            console.print(f"💾 Suggestions saved to: {output_path}")
            
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {str(e)}")

@cli.command()
@click.pass_context
def interactive(ctx):
    """🔄 Interactive mode for comprehensive career assistance"""
    console.print(Panel(
        "Welcome to Career Agent Interactive Mode!\n"
        "I can help you with resume analysis, career advice, job applications, and more.",
        title="🚀 Career Agent",
        border_style="blue"
    ))
    
    try:
        agent = CareerAgent(ctx.obj['provider'])
        
        while True:
            console.print("\n" + "="*50)
            
            table = Table(title="Available Commands")
            table.add_column("Option", style="cyan")
            table.add_column("Description", style="white")
            
            table.add_row("1", "Analyze Resume")
            table.add_row("2", "Get Career Advice")
            table.add_row("3", "Optimize Resume for Job")
            table.add_row("4", "Generate Cover Letter")
            table.add_row("5", "Interview Preparation")
            table.add_row("6", "Skill Development")
            table.add_row("q", "Quit")
            
            console.print(table)
            
            choice = Prompt.ask("\nWhat would you like to do?", choices=["1", "2", "3", "4", "5", "6", "q"])
            
            if choice == "q":
                console.print("👋 Goodbye! Good luck with your career journey!")
                break
            elif choice == "1":
                _interactive_analyze(agent)
            elif choice == "2":
                _interactive_advice(agent)
            elif choice == "3":
                _interactive_optimize(agent)
            elif choice == "4":
                _interactive_cover_letter(agent)
            elif choice == "5":
                _interactive_interview(agent)
            elif choice == "6":
                _interactive_skills(agent)
                
    except KeyboardInterrupt:
        console.print("\n👋 Goodbye!")
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {str(e)}")

def _interactive_analyze(agent):
    detailed = Prompt.ask("Detailed analysis?", choices=["y", "n"], default="y") == "y"
    
    with console.status("[bold green]Analyzing resume..."):
        analysis = agent.analyze_resume(detailed=detailed)
    
    console.print(Panel(Markdown(analysis), title="📊 Resume Analysis", border_style="blue"))
    
    if Prompt.ask("Save to file?", choices=["y", "n"], default="n") == "y":
        output_path = agent.save_output(analysis, "resume_analysis.md")
        console.print(f"💾 Saved to: {output_path}")

def _interactive_advice(agent):
    query = Prompt.ask("What career advice do you need?")
    context = Prompt.ask("Any additional context? (optional)", default="")
    
    with console.status("[bold green]Generating advice..."):
        advice_text = agent.get_career_advice(query, context if context else None)
    
    console.print(Panel(Markdown(advice_text), title="💡 Career Advice", border_style="green"))
    
    if Prompt.ask("Save to file?", choices=["y", "n"], default="n") == "y":
        output_path = agent.save_output(advice_text, "career_advice.md")
        console.print(f"💾 Saved to: {output_path}")

def _interactive_optimize(agent):
    console.print("📝 Please paste the job description (press Enter twice when done):")
    lines = []
    empty_count = 0
    while empty_count < 2:
        line = input()
        if line.strip() == "":
            empty_count += 1
        else:
            empty_count = 0
        lines.append(line)
    
    job_description = "\n".join(lines).strip()
    
    if not job_description:
        console.print("[bold red]No job description provided[/bold red]")
        return
    
    with console.status("[bold green]Optimizing resume..."):
        optimization = agent.optimize_resume_for_job(job_description)
    
    console.print(Panel(Markdown(optimization), title="🎯 Resume Optimization", border_style="yellow"))
    
    if Prompt.ask("Save to file?", choices=["y", "n"], default="n") == "y":
        output_path = agent.save_output(optimization, "resume_optimization.md")
        console.print(f"💾 Saved to: {output_path}")

def _interactive_cover_letter(agent):
    company = Prompt.ask("Company name")
    console.print("📝 Please paste the job description (press Enter twice when done):")
    lines = []
    empty_count = 0
    while empty_count < 2:
        line = input()
        if line.strip() == "":
            empty_count += 1
        else:
            empty_count = 0
        lines.append(line)
    
    job_description = "\n".join(lines).strip()
    additional_info = Prompt.ask("Any additional info to include? (optional)", default="")
    
    with console.status("[bold green]Generating cover letter..."):
        letter = agent.generate_cover_letter(job_description, company, additional_info if additional_info else None)
    
    console.print(Panel(Markdown(letter), title="✉️ Cover Letter", border_style="cyan"))
    
    if Prompt.ask("Save to file?", choices=["y", "n"], default="n") == "y":
        output_path = agent.save_output(letter, f"cover_letter_{company.replace(' ', '_')}.md")
        console.print(f"💾 Saved to: {output_path}")

def _interactive_interview(agent):
    interview_type = Prompt.ask("Interview type", choices=["general", "technical", "behavioral", "panel"], default="general")
    console.print("📝 Please paste the job description (press Enter twice when done):")
    lines = []
    empty_count = 0
    while empty_count < 2:
        line = input()
        if line.strip() == "":
            empty_count += 1
        else:
            empty_count = 0
        lines.append(line)
    
    job_description = "\n".join(lines).strip()
    
    with console.status("[bold green]Preparing interview questions..."):
        prep = agent.prepare_interview_questions(job_description, interview_type)
    
    console.print(Panel(Markdown(prep), title="🎤 Interview Preparation", border_style="magenta"))
    
    if Prompt.ask("Save to file?", choices=["y", "n"], default="n") == "y":
        output_path = agent.save_output(prep, f"interview_prep_{interview_type}.md")
        console.print(f"💾 Saved to: {output_path}")

def _interactive_skills(agent):
    target_role = Prompt.ask("Target role or career direction (optional)", default="")
    
    with console.status("[bold green]Analyzing skill development opportunities..."):
        suggestions = agent.suggest_skill_improvements(target_role if target_role else None)
    
    console.print(Panel(Markdown(suggestions), title="📚 Skill Development", border_style="yellow"))
    
    if Prompt.ask("Save to file?", choices=["y", "n"], default="n") == "y":
        output_path = agent.save_output(suggestions, "skill_suggestions.md")
        console.print(f"💾 Saved to: {output_path}")

if __name__ == '__main__':
    cli()