# Copyright 2017 Division of Medical Image Computing, German Cancer Research Center (DKFZ)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from __future__ import print_function
from __future__ import absolute_import

import unittest
from batchgenerators.augmentations import color_augmentations
from batchgenerators.augmentations import crop_and_pad_augmentations
from batchgenerators.augmentations import noise_augmentations
from batchgenerators.augmentations import resample_augmentations
from batchgenerators.augmentations import spatial_transformations
from batchgenerators.augmentations import utils

class TestSanity(unittest.TestCase):

    def test_sanity(self):
        self.assertTrue(3 == 3, "Sanity test failed")


if __name__ == '__main__':
    unittest.main()