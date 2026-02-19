# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |

## Reporting a Vulnerability

If you discover a security vulnerability, please send an email to ianalloway43@gmail.com

Please include:
- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Any suggested fixes (optional)

## Security Best Practices

When using this application:

1. **API Keys**: Never commit API keys to version control
2. **Environment Variables**: Use `.env` files (already in `.gitignore`)
3. **Data Privacy**: Resume data may contain sensitive personal information - handle accordingly
4. **PDF Processing**: Be cautious when processing resumes from untrusted sources

## Dependencies

We regularly update dependencies to patch security vulnerabilities. Run `npm audit` to check for known vulnerabilities.

## Compliance

This tool helps users create better resumes. Users are responsible for:
- Accuracy of resume content
- Not including false information
- Respecting ATS (Applicant Tracking System) guidelines
