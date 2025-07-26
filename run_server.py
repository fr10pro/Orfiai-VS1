#!/usr/bin/env python3
"""
StreamHub Server Startup Script

This script ensures the correct directory structure and starts the server.
"""

import os
import sys
import subprocess
from pathlib import Path

def setup_directories():
    """Create necessary directories if they don't exist"""
    directories = [
        "templates",
        "static",
        "static/banners"
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"✓ Directory {directory}/ ready")

def check_files():
    """Check if all required files exist"""
    required_files = [
        "main.py",
        "models.py", 
        "database.py",
        "requirements.txt"
    ]
    
    missing_files = []
    for file in required_files:
        if not Path(file).exists():
            missing_files.append(file)
    
    if missing_files:
        print("❌ Missing required files:")
        for file in missing_files:
            print(f"   - {file}")
        print("\nPlease ensure all files are in the current directory.")
        return False
    
    print("✓ All required files present")
    return True

def check_templates():
    """Check if template files exist"""
    template_files = [
        "templates/base.html",
        "templates/index.html",
        "templates/watch.html", 
        "templates/admin.html",
        "templates/edit.html"
    ]
    
    missing_templates = []
    for template in template_files:
        if not Path(template).exists():
            missing_templates.append(template)
    
    if missing_templates:
        print("❌ Missing template files:")
        for template in missing_templates:
            print(f"   - {template}")
        print("\nPlease ensure all template files are in the templates/ directory.")
        return False
    
    print("✓ All template files present")
    return True

def install_dependencies():
    """Install required dependencies"""
    try:
        print("📦 Installing dependencies...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✓ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False

def start_server():
    """Start the FastAPI server"""
    try:
        print("🚀 Starting StreamHub server...")
        print("📍 Server will be available at: http://localhost:8000")
        print("🔧 Admin panel at: http://localhost:8000/admin")
        print("📚 API docs at: http://localhost:8000/docs")
        print("\n" + "="*50)
        print("Press Ctrl+C to stop the server")
        print("="*50 + "\n")
        
        # Start the server
        subprocess.run([
            sys.executable, "-m", "uvicorn", 
            "main:app", 
            "--reload",
            "--host", "0.0.0.0",
            "--port", "8000"
        ])
    except KeyboardInterrupt:
        print("\n👋 Server stopped by user")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to start server: {e}")

def main():
    """Main function to set up and run the server"""
    print("🎬 StreamHub - Video Streaming Platform")
    print("="*40)
    
    # Setup directories
    setup_directories()
    
    # Check for required files
    if not check_files():
        sys.exit(1)
    
    # Check for template files
    if not check_templates():
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        sys.exit(1)
    
    # Start the server
    start_server()

if __name__ == "__main__":
    main()
