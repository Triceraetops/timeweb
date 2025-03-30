setup:
	python3 -m venv venv
	. venv/bin/activate && pip install -r requirements.txt

clean:
	rm -rf venv
	##rm -r __pycache__

test:
	. venv/bin/activate && pytest

run:
	. venv/bin/activate && python app.py

