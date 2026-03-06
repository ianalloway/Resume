#!/usr/bin/env python3
"""
Career Agent - Main Entry Point

This is the main entry point for the Career Agent application.
You can run this directly or use the CLI interface.
"""

import sys
from cli import cli

if __name__ == '__main__':
    try:
        cli()
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
