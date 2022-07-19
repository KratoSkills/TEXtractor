# TEXtractor

### Model description
- This is a Machine Learning model which extracts text from images, pdf and documents.
- Developed using Keras in Python 3, this program uses Convolutional Neural Network for Optical Character Recognition (OCR).

### Dataset
- [NIST Special Database 19](https://www.nist.gov/srd/nist-special-database-19)
- [EMNIST (Extended MNIST)](https://www.kaggle.com/datasets/crawford/emnist)

### Model Accuracy
- Training: 88.53%
- Testing: 87.04%

### Extra toolkits
- A python script, "TEXtractor - eXtract.py", to use the TEXtractor for easy extraction of text from images, pdf and documents will be released in future.
- Any contribution for building "TEXtractor - eXtract.py" or to improve the model are welcome.

### Prerequisites
- Tested on [Python 3](https://www.python.org/) >= 3.9.12
- Keras for Python 3: `pip3 install keras`
- Numpy: `pip3 install numpy`
- Sklearn (Optional): `pip3 install sklearn`

### Usage
1. Install the prerequisite tools.
2. Download the [dataset source files](https://github.com/KratoSkills/TEXtractor/releases/download/TEXtractor/emnist_source_files.rar).
3. Run "TEXtractor - Build.py" using the specified version of Python 3 to train your own TEXtractor
    OR
   use pretrained TEXtractor, "[TEXtractor - Model](https://github.com/KratoSkills/TEXtractor/releases/download/TEXtractor/TEXtractor.-.Model.h5)".
4. You can check TEXTractor's Accuracy on test dataset and also few pre-plotted predictions in "TEXtractor - Tester.ipynb"
5. Done! Use the model as pleased following the Guidelines of Apache License 2.0

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
