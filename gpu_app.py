from openvino.runtime import Core

def build_argparser():
    """Input Arguments"""
    parser = ArgumentParser()
    parser.add_argument(
        "-d",
        "--device",
        help="Specify the target infer device to; CPU, GPU, MYRIAD, or HDDL."
        "(CPU by default).",
        default="CPU",
        type=str,
    )

def main():
    """EntryPoint for the program."""
    args = build_argparser().parse_args()

    # Create OpenVINO™ Runtime Core
    core = Core()

    # Compile the model optimized for Thorugput, can be toggled for Latency bu changing config value
    compiled_model = core.compile_model(
        model=args.model,
        device_name=args.device,
        config={"PERFORMANCE_HINT": "THROUGHPUT"},
    )
    # Your code here
