#!/usr/bin/env python3
"""
Download and prepare FOMC transcripts for sentiment analysis.

- Source: Miguel Acosta, "FOMC Communications Data"
  https://www.acostamiguel.com/data/fomc_data.html
"""

import argparse
import logging
import pathlib
import sys

import requests
import pandas as pd

TRANSCRIPTS_URL = "https://www.acostamiguel.com/data/FOMC/transcripts.xlsx"


def download_file(url: str, dest: pathlib.Path, force: bool = False) -> pathlib.Path:
    """Download file with simple resume logic (skip if exists unless --force)."""
    dest = pathlib.Path(dest)
    if dest.exists() and not force:
        logging.info(
            "File %s already exists; skipping download. Use --force to re-download.",
            dest,
        )
        return dest

    dest.parent.mkdir(parents=True, exist_ok=True)
    logging.info("Downloading %s -> %s", url, dest)

    with requests.get(url, stream=True, timeout=60) as r:
        r.raise_for_status()
        tmp = dest.with_suffix(dest.suffix + ".part")
        with open(tmp, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        tmp.replace(dest)

    logging.info("Finished download.")
    return dest


def split_meetings_to_txt(df: pd.DataFrame, out_dir: pathlib.Path) -> None:
    """Group utterances by meeting date and write one text file per meeting."""
    out_dir = pathlib.Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    # Choose a date column and normalize to datetime (handles raw YYYYMMDD ints).
    date_col = "meeting_date" if "meeting_date" in df.columns else "date"
    if date_col not in df.columns:
        raise KeyError("Expected a 'date' or 'meeting_date' column in the transcript data.")

    dates = df[date_col]
    if pd.api.types.is_integer_dtype(dates):
        df["meeting_date"] = pd.to_datetime(dates.astype(str), format="%Y%m%d")
    else:
        df["meeting_date"] = pd.to_datetime(dates)

    # Ensure we have ordering columns for reproducible text output.
    sort_cols = [c for c in ["sequence", "n_utterance"] if c in df.columns]

    for date, g in df.groupby("meeting_date"):
        date_str = pd.to_datetime(date).strftime("%Y-%m-%d")
        g_sorted = g.sort_values(sort_cols)

        text = "\n\n".join(g_sorted["text"].astype(str))

        out_path = out_dir / f"meeting_{date_str}.txt"
        out_path.write_text(text, encoding="utf-8")
        logging.info("Wrote %s (%d utterances)", out_path.name, len(g_sorted))


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Download and preprocess FOMC transcripts for sentiment analysis."
    )
    parser.add_argument(
        "--out-dir",
        default="fomc_data",
        help="Root output directory (default: %(default)s)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Force re-download of source files even if they exist.",
    )
    parser.add_argument(
        "--xlsx",
        help="Use an existing transcripts.xlsx instead of downloading.",
    )
    parser.add_argument(
        "--meetings-dir",
        default="meetings_txt_all",
        help="Subdirectory under processed/ for per-meeting text files (default: %(default)s).",
    )

    args = parser.parse_args(argv)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )

    out_root = pathlib.Path(args.out_dir)
    raw_dir = out_root / "raw"
    processed_dir = out_root / "processed"

    # 1. Download (or reuse) the transcripts Excel
    if args.xlsx:
        xlsx_path = pathlib.Path(args.xlsx)
        if not xlsx_path.exists():
            raise FileNotFoundError(f"Provided --xlsx path does not exist: {xlsx_path}")
        logging.info("Using existing transcripts file at %s", xlsx_path)
    else:
        xlsx_path = download_file(
            TRANSCRIPTS_URL,
            raw_dir / "fomc_transcripts.xlsx",
            force=args.force,
        )

    # 2. Read into pandas and save a CSV version
    logging.info("Reading %s", xlsx_path)
    df = pd.read_excel(xlsx_path)

    tables_dir = processed_dir / "tables"
    tables_dir.mkdir(parents=True, exist_ok=True)

    csv_path = tables_dir / "fomc_transcripts.csv"
    df.to_csv(csv_path, index=False)
    logging.info("Saved full transcripts table to %s", csv_path)

    # 3. Write one text file per meeting
    meetings_txt_dir = processed_dir / args.meetings_dir
    split_meetings_to_txt(df, meetings_txt_dir)

    logging.info("All done. Meeting-level text lives in %s", meetings_txt_dir)


if __name__ == "__main__":
    main(sys.argv[1:])
