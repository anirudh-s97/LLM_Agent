# Intelligent File Management & Task Automation Agent

## Overview

This enterprise-grade application implements an intelligent agent powered by Google's Gemini-2.0-flash-exp model to automate file management workflows and execute scheduled operations based on natural language instructions. The system provides a comprehensive solution for file organization, media compression, and task automation, significantly reducing manual overhead for routine file management tasks.

## Core Capabilities

### Automated File Organization

The agent implements a sophisticated file management system with the following capabilities:

- **Recursive Directory Scanning**: Traverses specified directory structures to identify and catalog all files
- **Advanced Type Detection**: Employs both extension-based and content-based analysis to accurately identify file types
- **Intelligent Categorization**: Applies classification algorithms to sort files into appropriate directory structures
- **Metadata Preservation**: Maintains file metadata during organization processes
- **Configurable Organization Schemes**: Supports custom organization rules and directory structures

### Media Compression Services

The system integrates with optimization services to reduce storage requirements while maintaining content quality:

- **PDF Compression Pipeline**: 
  - Implements size reduction algorithms specifically tailored for PDF documents
  - Maintains document structure, hyperlinks, and searchability
  - Configurable compression levels based on quality requirements
  - Batch processing support for multiple documents

- **Image Optimization Engine**: 
  - Specialized compression for PNG and JPG formats
  - Intelligent quality-size balancing algorithms
  - Preservation of image metadata
  - Support for batch processing with progress tracking

### Task Automation Framework

The system includes a robust task execution engine that:

- **Parses Natural Language Instructions**: Processes human-readable task descriptions from a `todo.txt` file
- **Implements Email Communication**: Sends contextual reminders and information via configurable email services
- **Manages Calendar Operations**: Creates, modifies, and shares calendar invitations with specified recipients
- **Provides Financial Data Monitoring**: Retrieves stock information on scheduled intervals
- **Supports Extensible Task Types**: Architecture allows for easy addition of new task types

## Technical Architecture

```
├── file_compression/                # Compression module (root level)
│   ├── __init__.py                 # Module initialization
│   ├── image_compression.py        # Image-specific compression algorithms
│   └── pdf_compression.py          # PDF-specific compression algorithms
│
├── notebooks/                      # Development and experimentation
│   └── [Jupyter notebooks]         # Analysis and testing notebooks
│
├── root_data/                      # Data storage directory
│   └── [Data files]                # Processed and raw data files
│
├── src/                            # Primary source code
│   ├── execute_to_do_tasks/        # Task execution module
│   │   ├── __init__.py             # Module initialization
│   │   ├── run_to_do_tasks.py      # Task execution orchestration
│   │   └── [Task implementations]  # Individual task type handlers
│   │
│   ├── file_compression/           # Compression implementation
│   │   ├── __init__.py             # Module initialization
│   │   ├── image_compression.py    # Image optimization implementation
│   │   └── pdf_compression.py      # PDF optimization implementation
│   │
│   ├── file_organizer/             # File organization module
│   │   ├── __init__.py             # Module initialization
│   │   ├── organize_files.py       # Core organization logic
│   │   ├── validate_and_scan_folder.py # Directory validation and scanning
│   │   └── [Organization utilities] # Supporting utilities
│   │
│   └── llm_engine/                 # LLM integration framework
│       ├── __init__.py             # Module initialization
│       ├── gemini_agent.py         # Gemini API integration
│       ├── llm_utilities.py        # LLM operation utilities
│       ├── scheduler.py            # Scheduling implementation
│       └── [LLM components]        # Additional LLM functionality
│
├── .env                            # Environment configuration
├── .gitignore                      # Version control exclusions
├── invite.ics                      # Calendar invite template
├── llm_agent_pi.py                 # Agent initialization interface
├── README.md                       # Project documentation
├── requirements.txt                # Dependency specifications
├── run_agent.py                    # Main execution entry point
├── schedule_agent.py               # Scheduling control interface
└── utility_functions.py            # Shared utility functions
```

## Installation Guide

### System Requirements

Before beginning installation, ensure your system meets the following requirements:

- **Operating System**: Windows 10/11, macOS 10.14+, or Linux (Ubuntu 20.04+, Debian 10+, CentOS 8+)
- **Python**: Version 3.8 or higher (3.9+ recommended)
- **CPU**: Dual-core processor (quad-core recommended for batch operations)
- **RAM**: 1GB minimum (2GB+ recommended)
- **Disk Space**: 500MB for application, additional space for processed files
- **Network**: Internet connection for API services, SMTP access for email capabilities
- **Dependencies**: pip, venv or conda for environment management

### Step 1: Set Up Python Environment

First, ensure you have Python 3.8+ installed on your system:

```bash
python --version
# or
python3 --version
```

If Python is not installed or is an older version, download and install the latest version from [python.org](https://www.python.org/downloads/) or use your system's package manager.

### Step 2: Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/intelligent-file-agent.git
cd intelligent-file-agent
```

### Step 3: Create a Virtual Environment

Create a virtual environment to isolate the project dependencies:

#### Using venv (Python's built-in solution):

```bash
# On Linux/macOS
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

#### Using conda (alternative approach):

```bash
conda create -n file-agent python=3.9
conda activate file-agent
```

### Step 4: Install Dependencies

Install all required packages:

```bash
pip install -r requirements.txt
```

This will install all necessary dependencies, including:

- Google API client libraries for Gemini integration
- Pillow for image processing
- PyPDF2 for PDF manipulation
- Requests for API communication
- Schedule for task scheduling
- python-dotenv for environment management
- Other supporting libraries

### Step 5: Set Up API Access

To use the Gemini AI capabilities:

1. Create a Google Cloud Platform account if you don't have one
2. Create a new project in the Google Cloud Console
3. Enable the Gemini API for your project
4. Create an API key with appropriate permissions
5. Note the API key for configuration in the next step

### Step 6: Configure Environment Variables

Create a `.env` file in the project root directory with the following configuration parameters:

```
# API Configuration
GOOGLE_API_KEY=your_gemini_api_key_here

# Email Configuration (for notifications and reminders)
EMAIL_ADDRESS=your_email@example.com
EMAIL_PASSWORD=your_app_specific_password
SMTP_SERVER=smtp.example.com
SMTP_PORT=587

# File System Configuration
DEFAULT_SCAN_PATH=/path/to/default/directory
ORGANIZED_FILES_BASE=/path/to/organized/files

# Task Configuration
TODO_FILE_PATH=/path/to/todo.txt
DEFAULT_REMINDER_LEAD_TIME=24  # hours

# Logging Configuration
LOG_LEVEL=INFO  # DEBUG, INFO, WARNING, ERROR, CRITICAL
LOG_FILE=/path/to/log/file.log
```

Notes on email configuration:
- For Gmail, use an App Password rather than your account password
- For Office 365, you may need to configure appropriate security settings
- For other providers, check their documentation for SMTP settings

### Step 7: Create Required Directories

Ensure all necessary directories exist:

```bash
# Create log directory
mkdir -p logs

# Create default directories for organized files
mkdir -p organized_files/{Documents,Images,Audio,Video,Archives,Other}

# Create directory for saving compressed files
mkdir -p compressed_files/{PDFs,Images}
```

### Step 8: Verify Installation

Run the verification script to confirm proper installation:

```bash
python verify_installation.py
```

This script will:
- Check all dependencies are correctly installed
- Verify API key validity and access
- Test SMTP configuration
- Confirm directory permissions
- Report any issues that need resolution

### Step 9: Install Additional Components (Optional)

For enhanced functionality, you may want to install additional components:

#### PDF Processing Extensions

For better PDF handling capabilities:
```bash
pip install pymupdf ocrmypdf
```

#### Enhanced Image Processing

For additional image optimization capabilities:
```bash
pip install opencv-python-headless
```

#### Database Integration (Optional)

For logging and tracking file operations:
```bash
pip install sqlalchemy
```

### Step 10: Set Up Scheduled Execution (Optional)

For automated execution, set up the agent to run on a schedule:

#### On Linux/macOS (using cron):

```bash
# Open crontab
crontab -e

# Add entry to run daily at 9 AM
0 9 * * * cd /path/to/intelligent-file-agent && /path/to/venv/bin/python run_agent.py
```

#### On Windows (using Task Scheduler):

1. Open Task Scheduler
2. Create a new Basic Task
3. Set trigger to Daily at your preferred time
4. Set action to "Start a program"
5. Program/script: `C:\path\to\venv\Scripts\python.exe`
6. Arguments: `C:\path\to\intelligent-file-agent\run_agent.py`
7. Start in: `C:\path\to\intelligent-file-agent`

### Troubleshooting Installation

If you encounter issues during installation:

1. **Dependency Conflicts**:
   ```bash
   pip install -r requirements.txt --upgrade --force-reinstall
   ```

2. **Permission Issues**:
   - Ensure you have write access to all directories specified in configuration
   - On Linux/macOS, you may need to use `sudo` for global installations

3. **API Connection Failures**:
   - Verify your API key is correct
   - Check network connectivity and firewall settings
   - Confirm API service is enabled in Google Cloud Console

4. **Python Version Issues**:
   If you receive compatibility errors:
   ```bash
   # Install a specific Python version using pyenv
   pyenv install 3.9.7
   pyenv local 3.9.7
   # Then recreate your virtual environment
   ```

## Implementation Details

### File Organization Implementation

The file organization system implements a multi-stage pipeline:

1. **Directory Scanning**: The system traverses the target directory structure recursively, building a comprehensive file inventory.

2. **File Analysis**: Each file undergoes a two-phase analysis:
   - Extension-based classification (primary)
   - Content-based analysis for ambiguous files (secondary)

3. **Organization Execution**: Files are moved to destination directories based on their determined types, with conflict resolution for duplicate filenames.

4. **Verification**: Post-organization verification ensures all files were properly categorized and validates the integrity of moved files.

Key components:
- `validate_and_scan_folder.py`: Handles directory validation and recursive scanning
- `organize_files.py`: Implements the core organization logic and categorization algorithms

### Compression Service Architecture

The compression services are implemented as separate modules for different file types:

#### PDF Compression (`pdf_compression.py`)

- Utilizes optimized libraries for PDF processing
- Implements multiple compression strategies:
  - Image downsampling with configurable resolution thresholds
  - Font subsetting and optimization
  - Content structure preservation
  - Optional OCR for image-based PDFs

#### Image Compression (`image_compression.py`)

- Employs specialized algorithms for JPG and PNG formats
- Implements intelligent quality/size trade-off calculations
- Preserves essential metadata during compression
- Provides progress tracking for batch operations

### LLM Integration Framework

The system leverages Google's Gemini-2.0-flash-exp for intelligent processing:

- **Natural Language Understanding**: Parses unstructured text in `todo.txt` to extract actionable instructions
- **Task Classification**: Categorizes instructions into appropriate task types
- **Parameter Extraction**: Identifies key parameters from natural language descriptions
- **Content Generation**: Creates appropriate email content and calendar descriptions

Components:
- `gemini_agent.py`: Handles communication with the Gemini API
- `llm_utilities.py`: Provides supporting functions for LLM operations
- `scheduler.py`: Implements scheduling logic for periodic tasks

### Task Automation Implementation

The task automation framework processes instructions from `todo.txt` and executes corresponding actions:

1. **Parsing**: Extracts task descriptions, parameters, and scheduling information
2. **Scheduling**: Creates appropriate execution schedules based on timing parameters
3. **Execution**: Performs the specified tasks at scheduled times
4. **Notification**: Provides confirmation and status updates as appropriate

Supported task types include:
- Email reminders with customizable content and scheduling
- Calendar event creation and sharing
- Financial data retrieval and reporting
- File system operations with scheduling

## Configuration Setup

1. Create a `.env` file with the following parameters:
   ```
   # API Configuration
   GOOGLE_API_KEY=your_gemini_api_key
   
   # Email Configuration
   EMAIL_ADDRESS=your_notification_email@example.com
   EMAIL_PASSWORD=your_app_specific_password
   SMTP_SERVER=smtp.example.com
   SMTP_PORT=587
   
   # File System Configuration
   DEFAULT_SCAN_PATH=/path/to/default/directory
   ORGANIZED_FILES_BASE=/path/to/organized/files
   
   # Task Configuration
   TODO_FILE_PATH=/path/to/todo.txt
   DEFAULT_REMINDER_LEAD_TIME=24  # hours
   
   # Logging Configuration
   LOG_LEVEL=INFO  # DEBUG, INFO, WARNING, ERROR, CRITICAL
   LOG_FILE=/path/to/log/file.log
   ```

2. Configure API access:
   - Obtain a Google API key with access to Gemini-2.0-flash-exp
   - Enable necessary API services in the Google Cloud Console
   - Set appropriate quotas for your expected usage

3. Configure email services:
   - For Gmail, generate an App Password rather than using your account password
   - Ensure SMTP settings are correct for your email provider
   - Test email functionality before deploying

## Usage Guide

### Basic Operation

Run the agent with default configuration:
```bash
python run_agent.py
```

### Custom Configuration

Specify custom paths and configurations:
```bash
python run_agent.py --scan_path /path/to/files --todo_file /path/to/custom_todo.txt --output_dir /path/to/output
```

### Scheduled Operation

Configure the agent to run on a schedule:
```bash
python schedule_agent.py --interval daily --time "18:00" --config /path/to/config.json
```

Available scheduling options:
- `--interval`: hourly, daily, weekly, monthly
- `--time`: 24-hour format time (HH:MM)
- `--day`: Day of week for weekly schedules (Monday, Tuesday, etc.)
- `--date`: Day of month for monthly schedules (1-31)

### Component-Specific Usage

#### File Organization Only

```bash
python -c "from src.file_organizer.organize_files import organize; organize('/path/to/directory', output_dir='/path/to/output')"
```

#### PDF Compression Only

```bash
python -c "from src.file_compression.pdf_compression import compress_pdfs; compress_pdfs('/path/to/pdfs', quality='medium')"
```

#### Image Compression Only

```bash
python -c "from src.file_compression.image_compression import compress_images; compress_images('/path/to/images', quality=85)"
```

## Task Instruction Format

The system processes instructions from a `todo.txt` file using natural language processing. The following formats are supported:

### Email Reminders

```
Remind me to "Complete quarterly tax filing" via email on "2025-03-15 14:00"
Remind me to "Submit expense report" via email on "2025-03-10" with priority "high"
Send weekly reminder to "Update project timeline" every "Monday" at "09:00"
```

### Calendar Management

```
Add a calendar invite for "Team Strategy Meeting" on "2025-03-20 13:00" and share it with "team@company.com"
Schedule "Client Presentation" on "2025-04-05 11:00-12:30" and invite "client@example.com, manager@company.com"
Create recurring meeting "Weekly Status Update" every "Friday" at "16:00" until "2025-06-30"
```

### Financial Data Monitoring

```
Share the stock price for NVIDIA every day at 5 PM via email with me
Send weekly summary of "AAPL, MSFT, GOOGL" stock performance every "Friday" at "17:00"
Alert me if "TSLA" drops below "$150" or rises above "$250"
```

### File Management

```
Scan and organize folder "Downloads" weekly
Compress all PDFs in "Documents/Reports" every "Monday" at "01:00"
Delete files older than "30 days" in "Temporary" folder weekly
```

## Error Handling and Logging

The system implements comprehensive error handling and logging:

- Detailed logs are maintained in the configured log file
- Critical errors trigger email notifications to the administrator
- Failed operations are retried according to configurable policies
- Transaction logs allow for audit and recovery

Log levels can be configured in the `.env` file:
- `DEBUG`: Detailed debugging information
- `INFO`: Confirmation of expected operation
- `WARNING`: Indication of potential issues
- `ERROR`: Error conditions preventing specific operations
- `CRITICAL`: Critical conditions requiring immediate attention

## Security Considerations

The system implements several security measures:

- API keys and credentials are stored in the `.env` file and not committed to version control
- Email authentication uses app-specific passwords rather than primary credentials
- All external API calls use secure connections (HTTPS)
- File access is limited to specified directories
- Input validation is performed on all user-provided parameters

## Performance Optimization

For optimal performance, consider the following guidelines:

- **File Organization**: Performance scales with file count; consider batch processing for large directories
- **Compression**: CPU-intensive operations; adjust batch sizes based on available resources
- **Task Scheduling**: Distribute resource-intensive tasks to minimize overlap
- **API Usage**: Be mindful of API rate limits for external services

## Extending the System

The modular architecture allows for straightforward extension:

1. **Adding New Task Types**:
   - Create a new task handler in the `execute_to_do_tasks` directory
   - Implement the task execution logic
   - Register the task type in the task parser

2. **Supporting New File Types**:
   - Add detection logic to the file organizer
   - Create appropriate category handlers
   - Implement any specialized processing required

3. **Integrating Additional Services**:
   - Create appropriate service connectors
   - Implement authentication and communication logic
   - Register the service with the task execution framework

## Troubleshooting

Common issues and their resolutions:

1. **API Connection Failures**:
   - Verify API keys in `.env` file
   - Check network connectivity
   - Confirm API service status
   - Review API quotas and limits

2. **Email Delivery Issues**:
   - Verify SMTP settings
   - Check email credentials
   - Confirm firewall allows SMTP traffic
   - Review email service security settings

3. **File Access Errors**:
   - Verify directory permissions
   - Check for file locks from other applications
   - Confirm sufficient disk space
   - Validate path configurations

## Contributing

We welcome contributions to enhance the system's capabilities:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-capability`)
3. Implement and test your changes
4. Ensure all tests pass and code meets quality standards
5. Submit a pull request with detailed description of changes

Please refer to our contribution guidelines for code style, testing requirements, and review processes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- Google AI for the Gemini model capabilities
- Contributors and maintainers of the open-source libraries utilized
- The Python community for their ongoing support and resources