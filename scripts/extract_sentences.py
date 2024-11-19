import pandas as pd
import argparse
import sys

def extract_sentences(input_file, output_file, condition_value="commentary"):
    """
    Reads a TSV file, extracts 'textid' and 'text' columns,
    renames them to 'sentid' and 'sentence', and writes to a new TSV file.

    :param input_file: Path to the input TSV file.
    :param output_file: Path to the output TSV file.
    """
    try:
        # Read the TSV file
        df = pd.read_csv(input_file, sep='\t', dtype=str)
        print(f"Successfully read the input file: {input_file}")

        # Check if required columns exist
        required_columns = {'textid', 'text'}
        missing_columns = required_columns - set(df.columns)
        if missing_columns:
            print(f"Error: Missing columns in the input file: {missing_columns}", file=sys.stderr)
            sys.exit(1)

        # Extract 'textid' and 'text' columns
        extracted_df = df[['textid', 'text', 'label']].copy()
        print("Extracted 'textid' and 'text' columns.")

        # Rename the columns
        extracted_df.rename(columns={'textid': 'textid', 'text': 'text', 'label':'target'}, inplace=True)
        extracted_df['condition'] = condition_value
        print("Renamed columns to 'sentid' and 'sentence'.")

        # Write the updated DataFrame to a new TSV file with only the two columns
        extracted_df.to_csv(output_file, sep='\t', index=False)
        print(f"Successfully wrote the extracted data to: {output_file}")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.", file=sys.stderr)
        sys.exit(1)
    except pd.errors.EmptyDataError:
        print(f"Error: The file '{input_file}' is empty.", file=sys.stderr)
        sys.exit(1)
    except pd.errors.ParserError as e:
        print(f"Error parsing the file '{input_file}': {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Extract 'textid' and 'text' columns from a TSV file, rename them, and save to a new TSV file.")
    parser.add_argument('input_file', help='Path to the input TSV file.')
    parser.add_argument('output_file', help='Path to the output TSV file.')

    args = parser.parse_args()

    # Call the function with provided arguments
    extract_sentences(args.input_file, args.output_file)

if __name__ == "__main__":
    main()
