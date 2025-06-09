#!/usr/bin/env python3
"""
Extract text from meal plan images using macOS Vision framework
Requires macOS 10.15+ and Python with pyobjc

Usage:
    python3 extract_with_vision.py <week_folder>
    python3 extract_with_vision.py Week_2
    python3 extract_with_vision.py Week_3
"""

import os
import sys
import argparse
from pathlib import Path

try:
    import Vision
    import Quartz
    from Foundation import NSURL
    from Cocoa import NSImage
except ImportError:
    print("PyObjC not available. Installing...")
    os.system("pip3 install pyobjc-framework-Vision pyobjc-framework-Quartz")
    try:
        import Vision
        import Quartz
        from Foundation import NSURL
        from Cocoa import NSImage
    except ImportError:
        print("Could not import Vision framework. Falling back to alternative method.")
        sys.exit(1)

def extract_text_from_image(image_path):
    """Extract text from image using macOS Vision framework"""
    try:
        # Create URL from file path
        url = NSURL.fileURLWithPath_(str(image_path))
        
        # Create CGImageSource
        image_source = Quartz.CGImageSourceCreateWithURL(url, None)
        if not image_source:
            return f"Could not load image: {image_path}"
        
        # Get CGImage
        image = Quartz.CGImageSourceCreateImageAtIndex(image_source, 0, None)
        if not image:
            return f"Could not create image from: {image_path}"
        
        # Create Vision request
        request = Vision.VNRecognizeTextRequest.alloc().init()
        request.setRecognitionLevel_(Vision.VNRequestTextRecognitionLevelAccurate)
        
        # Create request handler
        handler = Vision.VNImageRequestHandler.alloc().initWithCGImage_options_(image, {})
        
        # Perform request
        success = handler.performRequests_error_([request], None)
        if not success:
            return f"OCR failed for: {image_path}"
        
        # Extract text from results
        results = request.results()
        if not results:
            return f"No text found in: {image_path}"
        
        text_lines = []
        for observation in results:
            text_lines.append(observation.topCandidates_(1)[0].string())
        
        return "\n".join(text_lines)
        
    except Exception as e:
        return f"Error processing {image_path}: {str(e)}"

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Extract text from meal plan images using macOS Vision framework')
    parser.add_argument('week_folder', help='Week folder name (e.g., Week_2, Week_3)')
    parser.add_argument('--output', '-o', help='Output file path (optional)')
    
    args = parser.parse_args()
    
    # Get the current script directory
    script_dir = Path(__file__).parent.absolute()
    
    # Construct paths
    week_dir = script_dir / args.week_folder / 'Images'
    
    # Default output file name based on week folder
    if args.output:
        output_file = Path(args.output)
    else:
        output_file = script_dir / args.week_folder / f"extracted_meal_plans_{args.week_folder.lower()}.txt"
    
    # Validate week directory exists
    if not week_dir.exists():
        print(f"Error: Week directory '{week_dir}' does not exist!")
        print(f"Available directories:")
        for item in script_dir.iterdir():
            if item.is_dir() and item.name.startswith('Week_'):
                print(f"  - {item.name}")
        sys.exit(1)
    
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    print(f"Processing images from: {week_dir}")
    print(f"Output will be saved to: {output_file}")
    
    with open(output_file, 'w') as f:
        f.write(f"Extracted Meal Plans from {args.week_folder} Images\n")
        f.write("=" * 50 + "\n\n")
        
        for day in days:
            image_path = week_dir / f"{day}.png"
            
            if image_path.exists():
                print(f"Processing {day}...")
                f.write(f"=== {day} ===\n")
                
                text = extract_text_from_image(image_path)
                f.write(f"{text}\n\n")
                f.write("-" * 20 + "\n\n")
            else:
                print(f"Image not found: {image_path}")
                f.write(f"=== {day} ===\n")
                f.write(f"Image not found: {day}.png\n\n")
                f.write("-" * 20 + "\n\n")
    
    print(f"Extraction complete! Results saved to: {output_file}")

if __name__ == "__main__":
    main()
