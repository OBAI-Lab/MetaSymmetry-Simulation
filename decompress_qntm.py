import gzip
import json
import os

def decompress_qntm(input_file_path, output_file_path):
    """
    Decompress a .qntm file assumed to be gzipped JSON.
    Args:
        input_file_path (str): Path to the input .qntm file.
        output_file_path (str): Path where the decompressed .json will be saved.
    """
    if not os.path.exists(input_file_path):
        print("❌ Error: Input file does not exist.")
        return

    try:
        with gzip.open(input_file_path, "rt", encoding="utf-8") as infile:
            data = json.load(infile)

        with open(output_file_path, "w", encoding="utf-8") as outfile:
            json.dump(data, outfile, indent=2)

        print(f"✅ Decompression successful. Output saved to: {output_file_path}")

    except Exception as e:
        print(f"❌ Decompression failed: {e}")

# ==== Example usage ====
if __name__ == "__main__":
    print("🔓 QNTM Decompression Tool")
    input_path = input("Enter path to your .qntm file: ").strip()
    output_path = input("Enter desired output .json file name: ").strip()

    decompress_qntm(input_path, output_path)
