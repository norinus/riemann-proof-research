import subprocess
from pathlib import Path

def check_candidate(path: Path, timeout=120):
    """Preliminary compiler gate only; not an axiom or statement audit."""
    result = subprocess.run(["lake", "env", "lean", "-DwarningAsError=true", str(path)],
                            capture_output=True, text=True, timeout=timeout)
    return {"compiled": result.returncode == 0, "output": result.stdout + result.stderr,
            "accepted_as_proof": False}
