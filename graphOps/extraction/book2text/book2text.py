import os
import shutil

def find_and_copy_markdown_files(input_dirs, output_dir):
    for input_dir in input_dirs:
        for root, _, files in os.walk(input_dir):
            for file in files:
                if file.endswith('.md'):
                    source_path = os.path.join(root, file)
                    relative_path = os.path.relpath(source_path, input_dir)
                    new_name = os.path.join(output_dir, relative_path.replace(os.path.sep, '_'))
                    shutil.copy(source_path, new_name)

if __name__ == "__main__":
    input_dirs = ["/home/fils/src/Projects/OIH/odis-arch/bookRev1"]  # Replace with your input directories
    output_dir = "./output_md"  # Replace with your output directory

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    find_and_copy_markdown_files(input_dirs, output_dir)
