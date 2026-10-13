#!/bin/bash

# BINF6310
# Module 04 Assignment - Task III
# By Spencer Elliott

# 1.
echo "This is the first line." > source.txt
echo "This is the second line." >> source.txt

# 2.
cat < source.txt > copy.txt
cat copy.txt

# 3.
echo "This is the third line." >> copy.txt

# 4.
cat copy.txt

# 5.
ls /fake/directory 2> error.txt

# 6.
date >> dates.log

# 7.
cat dates.log

# 8.
ls > files.txt

# 9.
cat > message.txt << END
This is a custom message.
Please press Ctrl+D to finish.
END

# 10.
cat message.txt

# 11.
wc -l < files.txt > line_count.txt

# 12.
cat line_count.txt

# 13.
rm copy.txt error.txt dates.log files.txt message.txt line_count.txt
