#!/usr/bin/env bash

typeset -i i END
let i=1 END=59
pandoc *.md >GG.html
while ((i<=END)); do
    echo $i
    pandoc $i/*.md >$i/GG.html
    let i++
done
