TEXFILE=presentation-web

all: presentation-web.pdf

$(TEXFILE).pdf: $(TEXFILE).tex
	# Initial run
	pdflatex -shell-escape --synctex=1 -interaction=nonstopmode $(TEXFILE)

	# Recompile if instructed
	@if(grep "Rerun" $(TEXFILE).log > /dev/null);\
	then \
		pdflatex -shell-escape --synctex=1 -interaction=nonstopmode $(TEXFILE); \
	fi

