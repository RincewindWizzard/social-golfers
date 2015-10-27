bin/Ausarbeitung.pdf:
	cd src; pdflatex Ausarbeitung.tex; mv Ausarbeitung.pdf ../bin/
view: bin/Ausarbeitung.pdf
	evince ./bin/Ausarbeitung.pdf

clean:
	(rm src/*.log; rm src/*.aux) 2> /dev/null || true
