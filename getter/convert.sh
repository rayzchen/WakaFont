#!/bin/sh

cd "$1"
for f in * ; do
	convert "$f" -alpha extract -negate pnm:- | potrace - -s -o "$2/$f.svg"
done
