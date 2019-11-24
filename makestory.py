import argparse
from pandocwrapper import PandocWrapper

# Only do something if the file is being run directly
if __name__ == "__main__":
    cli = argparse.ArgumentParser()

    cli.add_argument("outfile", help="Name of the output file")

    cli.parse_args()

    pandoc = PandocWrapper()

    pandoc.convert(cli.outfile)
