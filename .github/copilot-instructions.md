# RPG-BUGS Copilot Instructions

## Project Overview
Educational repository containing intentionally buggy Python code for classroom exercises. The goal is teaching students to identify and fix common programming mistakes in RPG-themed code samples.

## Repository Structure
- `bugs/` - Contains buggy Python scripts (e.g., `bug01.py`): variable declarations, type handling, string formatting
- Each file demonstrates common Python mistakes in an RPG context (hero names, levels, health points, etc.)

## Purpose & Workflow
- **Student Task**: Analyze buggy code, identify issues, and fix them
- **Expected Issues**: Variable type mismatches, string formatting errors, incorrect operations
- **Language**: Portuguese comments for classroom instruction

## Key Patterns to Follow

### Bug Types Covered
1. **Variable Type Handling** - Mixing types (e.g., int/float operations)
2. **String Formatting** - f-strings usage and variable interpolation
3. **Basic Data Types** - Strings, floats, integers in RPG context

### File Naming Convention
- `bug0X.py` - Sequential bug examples for progressive difficulty
- Each file is self-contained with Portuguese documentation

### Code Style
- Portuguese variable names and comments for educational context
- RPG terminology: `herói` (hero), `vida` (health), `nível` (level)
- Descriptive comments explaining what should work

## AI Agent Guidance
When helping students or creating new bugs:
1. **Preserve educational intent** - Keep bugs deliberate and identifiable
2. **Add comments** - Document what should happen vs. what's broken
3. **Use RPG theme** - Maintain consistency with hero/combat terminology
4. **Sequential progression** - Each bug builds on previous concepts

## Development
No special build or test commands. Files run directly:
```bash
python bugs/bug0X.py
```

For new bug files, follow the existing pattern and add Portuguese comments explaining the issue.
