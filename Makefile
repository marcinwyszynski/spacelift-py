.DEFAULT_GOAL := generate

generate:
	rm -rf ./generated && ariadne-codegen
