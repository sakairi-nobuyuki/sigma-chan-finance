# config: utf-8

from typing import List
import numpy as np
import dataclasses


@dataclasses.dataclass
class AnnotationDataClass:
    source: List[np.ndarray]
    annotated: List[np.ndarray]

    