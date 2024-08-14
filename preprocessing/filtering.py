# /**
#  * Use Case Cardiology HiGHmed Data Anonymisation
#  * Copyright (C) 2023 - Berlin Institute of Health
#  * <p>
#  * Use of this software is govered by the Business Source License included in the LICENSE.md file.
#  * Change Date: 14.08.2028, Change License: Academic Free License v3.0
#  * On the date above, in accordance with the Business Source License, use of this software will be governed by the
#  * open source license AFL v3.0 or as specified in the LICENSE.md file.
#  *
#  * Unless required by applicable law or agreed to in writing, software
#  * distributed under the License is distributed on an "AS IS" BASIS,
#  * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  * See the License for the specific language governing permissions and
#  * limitations under the License.
#  */


#!/usr/bin/env python3
"""Preprocess UCC data by plausibility"""
from argparse import ArgumentParser

import pandas as pd

from evaluation.local_utils import MEDICAL_SCORE, FEATURE_SETS


def select_score_subsample(full_dataset_cleaned: pd.DataFrame,
                           medical_score: MEDICAL_SCORE) -> pd.DataFrame:
    match medical_score:
        case MEDICAL_SCORE.BIOHF:
            return filter_for_biohf(full_dataset_cleaned)
        case MEDICAL_SCORE.MAGGIC:
            return filter_for_maggic(full_dataset_cleaned)
    return None


def filter_for_biohf(dataset: pd.DataFrame):
    required_columns = FEATURE_SETS[MEDICAL_SCORE.BIOHF]["all"]
    return dataset.dropna(subset=required_columns)


def filter_for_maggic(dataset: pd.DataFrame):
    required_columns = FEATURE_SETS[MEDICAL_SCORE.MAGGIC]["all"]
    return dataset.dropna(subset=required_columns)
