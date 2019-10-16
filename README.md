# SenseHatPatterns
Just some funky lights for the Sense HAT. The project consists of a collection of stand-alone pattern scripts, triggered by a control script. Automated deployment to the raspberry is included.

## Instructions for new patterns
New patterns are to be added as python scripts in the sensehat folder. They need a continuous naming schmeme (unique numbers without gaps) to be recognized correctly.

## Deployment instructions
The project can easily be deployed to a raspberry from your windows machine using the deployment script. Everything required is an internet connection.
The command syntax is as follows:
	
	.\deploy_to_raspi.bat <hostname> <username> <password>
	
All files will be deployed automatically; if there is already an instance of the project running, it will be terminated an its files removed, the Sense HAT will be reset and the new version will be started. Warning: Any local changes on the Pi will be lost in the process.

## Putty / Pscp / Plink license note:


    PuTTY is copyright 1997-2019 Simon Tatham.

    Portions copyright Robert de Bath, Joris van Rantwijk, Delian Delchev, Andreas Schultz, Jeroen Massar, Wez Furlong, Nicolas Barry, Justin Bradford, Ben Harris, Malcolm Smith, Ahmad Khalifa, Markus Kuhn, Colin Watson, Christopher Staite, Lorenz Diener, Christian Brabandt, Jeff Smith, Pavel Kryukov, Maxim Kuznetsov, Svyatoslav Kuzmich, Nico Williams, Viktor Dukhovni, and CORE SDI S.A.

    Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
