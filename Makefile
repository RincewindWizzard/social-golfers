pdf:
	cd src; pdflatex Ausarbeitung.tex; mv Ausarbeitung.pdf ../build/
view: pdf
	evince ./bin/Ausarbeitung.pdf

clean:
	(rm src/*.log; rm src/*.aux; rm bin/*; ) 2> /dev/null || true
