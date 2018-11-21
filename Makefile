PROJECT=bojs

all: test

parser : \
	$(PROJECT)/parser/js_parser.py \
	$(PROJECT)/parser/js_model.py


$(PROJECT)/parser/js_parser.py \
$(PROJECT)/parser/js_model.py: $(PROJECT)/parser/grammars/js.ebnf
	python -u -Om tatsu $<  \
		-o $@ \
		-G $(PROJECT)/parser/js_model.py


test: parser
	pytest -v


clean_parser:
	rm -rf $(PROJECT)/parser/js_parser.py
	rm -rf $(PROJECT)/parser/js_model.py


clean:
	find -name "__pycache__" | xargs rm -rf
	find -name "*.pyc" | xargs rm -f
	find -name "*.pyd" | xargs rm -f
	find -name "*.pyo" | xargs rm -f
	find -name "*.orig" | xargs rm -f
	rm -rf tatsu.egg-info
	rm -rf dist
	rm -rf build
