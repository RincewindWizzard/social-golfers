pdf:
	cd src; pdflatex Ausarbeitung.tex; mv Ausarbeitung.pdf ../build/
view: pdf
	evince ./build/Ausarbeitung.pdf

daemon:
	while true; do inotifywait -e CLOSE src/*.tex src/*/*.tex; make pdf; done;

clean:
	(rm src/*.log; rm src/*.aux; rm bin/*; ) 2> /dev/null || true
