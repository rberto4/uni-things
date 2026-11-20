#!/bin/bash
# Compila la guida: richiede tectonic (brew install tectonic)
cd "$(dirname "$0")/src" && tectonic main.tex && cp main.pdf ../Guida_RTLC.pdf && echo "Creato Guida_RTLC.pdf"
