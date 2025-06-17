from cli import parse_commands
from src.core import load_csv, run_pipeline, format_result


def main():
    cli_args = parse_commands()
    data = load_csv(cli_args["file_path"])
    processed_data = run_pipeline(data, cli_args["commands"])
    format_result(processed_data)


if __name__ == "__main__":
    main()
