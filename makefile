build:
	python -m generate_font
	python -m scripts.banner
	python -m scripts.specimen_pdf
	python -m scripts.specimen_png

install-mac:
	cp -r fonts/otf/NordwandMono-*.otf ~/Library/Fonts
