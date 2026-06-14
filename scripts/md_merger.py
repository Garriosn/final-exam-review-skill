import os
import sys

def merge_markdowns(input_dir, output_filepath):
    """
    Merges all Markdown (.md) files in the input_dir into a single Markdown file.
    
    Args:
        input_dir (str): Directory containing .md files to merge.
        output_filepath (str): The path for the merged output .md file.
    """
    import re
    def natural_keys(text):
        return [int(c) if c.isdigit() else c for c in re.split(r'(\d+)', text)]
        
    md_files = [f for f in os.listdir(input_dir) if f.endswith('.md')]
    md_files.sort(key=natural_keys)  # Sort naturally so 10.md comes after 2.md
    
    if not md_files:
        print(f"No Markdown files found in {input_dir} to merge.")
        return False
        
    merged_content = []
    for md_file in md_files:
        full_path = os.path.join(input_dir, md_file)
        try:
            with open(full_path, "r", encoding="utf-8") as f:
                content = f.read()
                # Add a separator between files for clarity
                merged_content.append(f"<!-- Source: {md_file} -->\n")
                merged_content.append(content)
                merged_content.append("\n\n---\n\n")
            print(f"Appended: {md_file}")
        except Exception as e:
            print(f"Failed to append {md_file}: {e}")
            
    try:
        # Create output directory if it doesn't exist
        os.makedirs(os.path.dirname(output_filepath), exist_ok=True)
        with open(output_filepath, "w", encoding="utf-8") as output_file:
            output_file.write("".join(merged_content))
        print(f"Successfully created merged Markdown at: {output_filepath}")
        return True
    except Exception as e:
        print(f"Failed to save merged Markdown: {e}")
        return False

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Merge multiple Markdown files into one.")
    parser.add_argument("--input-dir", required=True, help="Directory containing .md files.")
    parser.add_argument("--output", required=True, help="Output merged .md file path.")
    args = parser.parse_args()
    
    merge_markdowns(args.input_dir, args.output)
