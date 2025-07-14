import argparse

def main():
    parser = argparse.ArgumentParser(description="Simple CLI for PharmacoRoute")
    parser.add_argument('--vcf', type=str, help='Path to VCF file')
    args = parser.parse_args()

    print(f"VCF file path received: {args.vcf}")

if _name_ == "_main_":
    main()
