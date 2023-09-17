import re
import argparse

def remove_comments(input_file, output_file):
    with open(input_file, 'r') as f:
        code = f.read()

    # Regular expression to match and remove multi-line comments
    code = re.sub(r'(\'\'\'(.*?)\'\'\'|\"\"\"(.*?)\"\"\")', '', code, flags=re.DOTALL)

    # Regular expression to match and remove single-line comments
    code = re.sub(r'#.*', '', code)

    # Remove consecutive newlines
    code = re.sub(r'\n{2,}', '\n', code)

    with open(output_file, 'w') as f:
        f.write(code)

def main():
    parser = argparse.ArgumentParser(description="Remove comments and consecutive newlines from a Python code file.")
    parser.add_argument("input_file", help="Path to the input Python code file")
    parser.add_argument("output_file", help="Path to the output file without comments and consecutive newlines")
    args = parser.parse_args()

    remove_comments(args.input_file, args.output_file)
    print(f"Comments and consecutive newlines removed and saved to {args.output_file}")

if __name__ == "__main__":
    main()
