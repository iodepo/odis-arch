.DEFAULT_GOAL := production
   
production:
	cat gleanerconfig_prefix.yaml production-sources.yaml | sed '/^[[:space:]]*#/d' > ./gleanerio/gleanerconfig_production.yaml

dev:
	cat gleanerconfig_prefix.yaml dev-sources.yaml | sed '/^[[:space:]]*#/d' > ./gleanerio/gleanerconfig_dev.yaml
