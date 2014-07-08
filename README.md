PyRattus
========
This is an open and free tool for creating application to windows, linux and mac.
I started this project to learn python and create an application tool like "quickly".


# Get Source

We need python2.7 and gtk2 packages to install them run the follwoing command: `sudo apt-get install python2.7 python-gtk2`.
If we are using MS Windows we can download and install from [https://www.python.org/download/releases/2.7/](https://www.python.org/download/releases/2.7/).
After installation we can checkout `svn co https://github.com/nv8h/PyRattus` or clone `git clone https://github.com/nv8h/PyRattus.git` the source.

# Create Windows with Glade

If we want create windows with graphic interface, we can install glade. In Ubuntu the following command will install the needed packages `sudo apt-get install glade`. If we are using MS Windows we can download and install from [http://sourceforge.net/projects/gladewin32/](http://sourceforge.net/projects/gladewin32/).
After installation we should create a directory for windows in base/data folder to have a clear directory structure. After that we can access the glade files with the following path: `rat.registry.getValue("path")["data"] + "/your-directory-name/your-glade-file-name.glade"`.

We can use GtkBuilder or rat.applicaton.bgtk class. In the rat.application.bgtk we can set params and glade filename in the initParams function and we can connect element's events with functions in iniElements like the following example.

    class your-app-name(rat.application.bgtk):
        def initParams(self):
            self.params['filename'] = rat.registry.getValue("path")["data"] + "/your-directory-name/your-glade-file-name.glade"
            return
            
        def initElements(self):
            self.__builder__.get_object("MainWindow").show_all()
            self.__builder__.get_object("MainWindow").connect('destroy', self.on_MainWindow_destroy)
            self.__builder__.get_object("btnHelloWorld").connect('clicked', self.on_btnHelloWorld_clicked)
            return
        
        def on_btnHelloWorld_clicked(self, widget):
            self.quit()
            return
            
        def on_MainWindow_destroy(self, widget, data=None):
            self.quit()
            return

# License

Copyright (c) 2014 Istvan Schoffhauzer

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

[Source](http://opensource.org/licenses/MIT)
