build:
	python3 -m coffeehouse_dltc --train-model langdetect

background_build:
	screen -dm bash -c 'python3 -m coffeehouse_dltc --train-model langdetect'

generate_data:
	python3 generate_data.py

test:
	python3 -m coffeehouse_dltc --test-model langdetect_build

clean:
	@for f in $(shell ls langdetect/); do \
		echo "Processing $${f}" && sort -u "langdetect/$${f}" > "langdetect/$${f}.clean" && rm "langdetect/$${f}" && mv "langdetect/$${f}.clean" "langdetect/$${f}"; \
	done