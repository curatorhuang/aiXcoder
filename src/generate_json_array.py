import sys
import json

def read_file_to_json_array(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file]
        return lines
    except FileNotFoundError:
        return f"Error: The file '{filename}' does not exist."
    except Exception as e:
        return f"Error: {str(e)}"

def write_json_to_file(data, output_filename):
    try:
        with open(output_filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        return f"JSON output has been written to {output_filename}"
    except Exception as e:
        return f"Error writing to file: {str(e)}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py input_filename [output_filename]")
    else:
        input_filename = sys.argv[1]
        output_filename = sys.argv[2] if len(sys.argv) > 2 else None
        json_data = read_file_to_json_array(input_filename)
        if isinstance(json_data, list):
            if output_filename:
                result = write_json_to_file(json_data, output_filename)
                print(result)
            else:
                print(json.dumps(json_data, ensure_ascii=False, indent=4))
        else:
            print(json_data)
