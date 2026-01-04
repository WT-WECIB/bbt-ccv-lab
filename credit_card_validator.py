import importlib.util
import sys
from pathlib import Path

pyc = Path(__file__).with_suffix(".pyc")
spec = importlib.util.spec_from_file_location("credit_card_validator", pyc)
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)

credit_card_validator = module.credit_card_validator
