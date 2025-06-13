from typing import List, Dict
from pathlib import Path
import contextlib, io, sys, logging

from mcp.server.fastmcp import FastMCP
from ultralytics import YOLO

mcp = FastMCP("Object-Detection Service")

buf = io.StringIO()
with contextlib.redirect_stdout(sys.stderr), contextlib.redirect_stderr(sys.stderr):
    logging.getLogger("ultralytics").setLevel(logging.WARNING)   
    model = YOLO("yolov8n.pt")


@mcp.tool()
def detect_objects(files: List[str]) -> Dict[str, List[str]]:
    """
    Получить список объектов на каждой картинке.

    Args:
        files: список путей к изображениям (jpg/png/…).

    Returns:
        { путь_к_файлу: [класс1, класс2, …] }
        Классы без повторов, отсортированы по алфавиту.
    """
    results: Dict[str, List[str]] = {}

    for path in files:
        img_path = Path(path)
        if not img_path.exists():
            results[str(path)] = ["<file not found>"]
            continue

        det = model(img_path, verbose=False)[0]      
        classes = {model.names[int(c)] for c in det.boxes.cls.tolist()}
        results[str(path)] = sorted(classes)

    return results

if __name__ == "__main__":
    mcp.run()      
