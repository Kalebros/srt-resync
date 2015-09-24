# srt-resync
Re-synchronize your SRT subtitles

## USAGE

> srt-resync *ORIGIN.srt* *DESTINY.srt* *time*

- **ORIGIN.srt**: File to be re-synchronized
- **DESTINY.srt**: New file, re-synchronized
- **time**: Amount of time, specified in seconds and using the float format, we want to re-sync; it can be a positive or negative value (just add *+* or *-* before)

### Examples:

> srt-resync my_favorite_episode_subtitles.srt resynchronized_subtitles.srt +4.5

> srt-resync boring_episode_subtitles.srt resynchronized_boring_subtitles.srt -5.67 

## License
The MIT License (MIT)

Copyright (c) 2015

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
