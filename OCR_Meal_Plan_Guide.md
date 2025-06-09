# Image OCR Text Extraction Guide

This guide shows how to extract text from meal plan images (or any images with text) on macOS and convert them into organized markdown meal plans.

## Prerequisites

- macOS (for built-in OCR capabilities)
- Terminal access
- Python 3 (usually pre-installed on macOS)

## Files Created in This Process

1. `extract_with_vision.py` - Python script using macOS Vision framework
2. `Week_X/extracted_meal_plans_week_x.txt` - Raw OCR output
3. `Week_X_Meal_Plan.md` - Final formatted meal plan

## Step-by-Step Process

### Step 1: Organize Your Images

1. Create a folder for your meal plan week (e.g., `Week_2/`, `Week_3/`, etc.)
2. Inside each week folder, create an `Images/` subfolder
3. Name your images consistently in the Images folder:
   - `Monday.png`
   - `Tuesday.png`
   - `Wednesday.png`
   - `Thursday.png`
   - `Friday.png`
   - `Saturday.png`
   - `Sunday.png`

Example structure:
```
Week_2/
  Images/
    Monday.png
    Tuesday.png
    ...
Week_3/
  Images/
    Monday.png
    Tuesday.png
    ...
```

### Step 2: Extract Text Using OCR

```bash
# Run the Python OCR script from the project root
python3 extract_with_vision.py Week_2

# For other weeks
python3 extract_with_vision.py Week_3

# With custom output location
python3 extract_with_vision.py Week_2 --output custom_output.txt
```

### Step 3: Review Extracted Text

1. Open `Week_X/extracted_meal_plans_week_x.txt`
2. Review the OCR results
3. Note any errors or misread text that need manual correction

### Step 4: Create Formatted Meal Plan

1. Create a new markdown file: `Week_X_Meal_Plan.md`
2. Use the table format with days as columns and meals as rows:

```markdown
# Week X Meal Plan

## Daily Meal Plan

| Meal | Monday | Tuesday | Wednesday | Thursday | Friday | Saturday | Sunday |
|------|--------|---------|-----------|----------|--------|----------|--------|
| **Breakfast** | [Meal] | [Meal] | [Meal] | [Meal] | [Meal] | [Meal] | [Meal] |
| **Morning Snack** | [Snack] | [Snack] | [Snack] | [Snack] | [Snack] | [Snack] | [Snack] |
| **Lunch** | [Meal] | [Meal] | [Meal] | [Meal] | [Meal] | [Meal] | [Meal] |
| **Afternoon Snack** | [Snack] | [Snack] | [Snack] | [Snack] | [Snack] | [Snack] | [Snack] |
| **Dinner** | [Meal] | [Meal] | [Meal] | [Meal] | [Meal] | [Meal] | [Meal] |
| **Late Evening Snack** | [Snack] | [Snack] | [Snack] | [Snack] | [Snack] | [Snack] | [Snack] |
```

## Usage Examples

### For Week 3:
```bash
# Create the week folder and images subfolder
mkdir -p Week_3/Images
# Add your images to Week_3/Images/

# Extract text
python3 extract_with_vision.py Week_3
```

### For Week 4:
```bash
# Create the week folder and images subfolder
mkdir -p Week_4/Images
# Add your images to Week_4/Images/

# Extract text
python3 extract_with_vision.py Week_4
```

## Common OCR Issues and Solutions

### Text Not Recognized
- Ensure images are high resolution
- Check that text is clearly visible
- Try adjusting image brightness/contrast

### Garbled Text
- Review the `extracted_meal_plans.txt` file
- Manually correct obvious errors
- Some symbols (€, special characters) may appear as artifacts

### Missing Images
- Verify all 7 day images are present
- Check file naming convention matches exactly
- Ensure images are in PNG format

## Alternative OCR Methods

If the automated scripts don't work:

1. **Manual Live Text (macOS)**:
   - Open images in Preview
   - Use Live Text to select and copy text
   - Paste into a text file

2. **Online OCR Tools**:
   - Upload images to Google Drive
   - Right-click → "Open with Google Docs"
   - Copy extracted text

3. **Tesseract OCR** (if installed):
   ```bash
   brew install tesseract
   tesseract image.png output.txt
   ```

## File Organization Tips

```
BFT Challenge/
│── extract_with_vision.py
├── Week_1/
│   ├── Images/
│   │   ├── Monday.png
│   │   ├── Tuesday.png
│   │   └── ...
│   └── extracted_meal_plans_week_1.txt
├── Week_2/
│   ├── Images/
│   │   ├── Monday.png
│   │   ├── Tuesday.png
│   │   └── ...
│   └── extracted_meal_plans_week_2.txt
├── Week_1_Meal_Plan.md
├── Week_2_Meal_Plan.md
└── OCR_Meal_Plan_Guide.md
```

## Troubleshooting

### Script Permissions
```bash
# No longer needed - Python script handles everything
```

### Python Issues
```bash
# Install required packages if needed
pip3 install pyobjc-framework-Vision pyobjc-framework-Quartz
```

### Path Issues
- Make sure to run the script from the project root directory
- The script automatically looks for `Week_X/Images/` folders
- Output files are saved to `Week_X/extracted_meal_plans_week_x.txt`

---

## Quick Reference Commands

```bash
# Create new week structure
mkdir -p Week_3/Images

# Extract text from images
python3 extract_with_vision.py Week_3

# Extract with custom output
python3 extract_with_vision.py Week_3 --output custom_name.txt

# Get help
python3 extract_with_vision.py --help
```

This process can be repeated for any week or any set of images containing text that you want to extract and organize!
