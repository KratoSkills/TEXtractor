# TEXtractor

### Model description
- This is a Machine Learning model which extracts text from images, pdf and documents.
- Developed using Keras in Python 3, this program uses Convolutional Neural Network for Optical Character Recognition (OCR).

### Dataset
- [NIST Special Database 19](https://www.nist.gov/srd/nist-special-database-19)
- [EMNIST (Extended MNIST)](https://www.kaggle.com/datasets/crawford/emnist)

### Extra toolkits
- A python script to use the TEXtractor.

### Prerequisites
- Tested on [Python 3](https://www.python.org/) >= 3.9.12
- [Tesseract](https://github.com/tesseract-ocr/tessdoc) for Python 3 (pytesseract): `pip3 install pytesseract`
- Keras for Python 3: `pip3 install keras`

### Usage
1. Install the prerequisite tools.
2. Download the [dataset source files](https://anonfiles.com/PeP2Vay7y5/emnist_source_files_rar).
3. Run "TEXtractor - Build.py" using the specified version of Python 3 to train your own TEXtractor
    OR
   use prebuild TEXtractor, "[TEXtractor - Model.h5](https://anonfiles.com/vb71V1y5y3/TEXtractor_-_Model_h5)".
4. Once TEXTractor is build, use it to extract text from images using "TEXtractor - eXtract.py"

### References
- https://towardsdatascience.com/a-comprehensive-guide-to-convolutional-neural-networks-the-eli5-way-3bd2b1164a53
- https://thesai.org/Publications/ViewPaper?Volume=12&Issue=1&Code=IJACSA&SerialNo=25
- https://towardsdatascience.com/train-a-custom-tesseract-ocr-model-as-an-alternative-to-google-vision-ocr-for-reading-childrens-db8ba41571c8

### Copyright disclaimer
Copyright 2022 KratoSkills, kr4T0X, krX, Himanshu Yadav

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
