import argparse
from exercises.pushup_eval import PushupEvaluator
from pipeline.video_pipeline import VideoPipeline 

def main():
    parser = argparse.ArgumentParser(description="Fitness Pose Estimation Pipeline")

    parser.add_argument(
        "--model",
        type=str,
        required=True,
        help="Path to model file (.pt or .engine)"
    )
    parser.add_argument(
        "--source",
        type=str,
        required=True,
        help="Source: video path, RTSP URL, webcam index (int), or image path"
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Path to save output video (optional)"
    )
    parser.add_argument(
        "--evaluator",
        type=str,
        default="pushup",
        choices=["pushup"],  
        help="Which evaluator to use"
    )

    args = parser.parse_args()

    if args.evaluator == "pushup":
        evaluator = PushupEvaluator()
    else:
        raise ValueError(f"Unsupported evaluator: {args.evaluator}")

    pipeline = VideoPipeline(
        model_path=args.model,
        evaluator=evaluator,
        source=args.source,
        output_path=args.output
    )

    pipeline.run()

if __name__ == "__main__":
    main()