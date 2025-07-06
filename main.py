#!/usr/bin/env python3
"""
Career Agent - Main Entry Point

This is the main entry point for the Career Agent application.
You can run this directly or use the CLI interface.
"""

import sys
import os
from pathlib import Path

# Add current directory to Python path
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

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