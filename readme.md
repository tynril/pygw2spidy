Python Bindings to the Guild Wars 2 Spidy API
=============================================

This small Python module provides easy-to-use bindings to the Guild Wars 2 Spidy API.

What is Guild Wars 2 Spidy?
---------------------------

[Guild Wars 2 Spidy](http://www.gw2spidy.com) is a fan-made website that allows browsing the Black Lion Trading Post, which is the trading market of the Guild Wars 2 game. Its [API](https://github.com/rubensayshi/gw2spidy/wiki/API-v0.9) allow to programatically access this data. Note that the data being accessed is the one fetched by Gw2Spidy, and not directly the one on ArenaNet's servers.

How to use it?
--------------

Simply put the `gw2spidy.py` module somewhere in your project, and import it with `from gw2spidy import Gw2Spidy`. You can then use the static methods of the `Gw2Spidy` class.

License
-------

This module is provided under the [MIT Open Source License](http://opensource.org/licenses/MIT). Meaning you're free to use it for anything as long as you keep my name and the copyright notice in the module file. Also, if the use of this module triggers a worldwide war, I'm not responsible.

    Copyright (c) 2012 Samuel Loretan (tynril at gmail dot com)
    
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
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.