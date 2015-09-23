iq_suite
============

![barion](https://raw.githubusercontent.com/xaratustrah/iq_suite/master/screenshot.png)

Collection of code for working with IQ Time data with numpy. While the GUI program offers a limited graphical way to view data, the advanced usage allows direct programing using the class file and tools within own scrips or iPython Notebook sessions.


#### IQData class
This class covers all required parameters to handle time domain IQ data and their representation in frequency domain. Cuts, slices etc. are also available.

#### iqtools
Is a collection that uses the IQData class as main data type but additionally offers tools for plotting and accessing the data. Stand alone operation is also possible using
command line arguments.

#### iqgui
This is a GUI written using the Qt5 bindings for quick showing of the spectrogram plots for visual analysis or inspection.

**Building under windows**

Building iqgui under windows has been tested using a minimal python installation under Win7 64 bit:

Python 3.4.0 and PyQt5.5.0 both x64 versions, directly from their respective official websites. Following packages were installed from [Ch. Gohlke](http://www.lfd.uci.edu/~gohlke/pythonlibs/)'s website: 

matplotlib-1.5.0rc1-cp34-none-win_amd64
numpy-1.10.0b1+mkl-cp34-none-win_amd64.whl
scipy-0.16.0-cp34-none-win_amd64.whl

Following packages where installed using **pip**:

cycler (0.9.0)
pip (1.5.4)
py2exe (0.9.2.2)
pyparsing (2.0.3)
python-dateutil (2.4.2)
pytz (2015.4)
setuptools (2.1)
six (1.9.0)

