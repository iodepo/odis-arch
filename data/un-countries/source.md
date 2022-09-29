# Source

- UN SDG API : https://unstats.un.org/SDGAPI/swagger/#/

- GeoArea endpoint: https://unstats.un.org/SDGAPI/swagger/#!/GeoArea/V1SdgGeoAreaListGet

- command to generate JSON file of countries:

```
curl -X GET --header 'Accept: application/json' 'https://unstats.un.org/SDGAPI/v1/sdg/GeoArea/List'

```